// The official Figma runtime is loaded from its origin, not vendored.
const runtimeUrl = 'https://mcp.figma.com/mcp/html-to-design/capture.js';
const button = document.querySelector('#copy');
const status = document.querySelector('#status');
const design = document.querySelector('#design');
const diagnostics = document.querySelector('#diagnostics');
const originalLabel = button.textContent;
const messages = {
  ready: status.dataset.ready || 'Ready. Copy captures the design only, without this toolbar.',
  copying: status.dataset.copying || 'Figma is preparing layers. Keep this tab focused.',
  copied: status.dataset.copied || 'Copied by Figma. Paste directly onto a Figma Design canvas: Cmd+V / Ctrl+V.',
  session: status.dataset.session || 'Capture session closed. Follow the confirmation shown by Figma.',
  failed: status.dataset.failed || 'Capture failed: ',
  retry: button.dataset.retry || 'Retry',
};
let ready = false;
let sessionActive = false;
let copied = false;
let runtimePromise = null;

// This observed verbose signal is version-dependent. Figma's own toolbar is
// authoritative; no timer or mere button click is treated as successful copy.
const originalLog = console.log.bind(console);
console.log = (...args) => {
  originalLog(...args);
  const line = args.filter(value => typeof value === 'string').join(' ');
  if (!sessionActive || !line.includes('[Figma Capture]')) return;
  diagnostics.textContent = (diagnostics.textContent + line + '\n').slice(-8000);
  if (line.includes('Success! Capture copied to clipboard.')) {
    copied = true;
    status.textContent = messages.copied;
  }
};
function timeout(promise, label) {
  let timer;
  return Promise.race([promise, new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(label + ' timed out. Check the connection and retry.')), 25000);
  })]).finally(() => clearTimeout(timer));
}
async function loadRuntime() {
  if (window.figma?.captureForDesign) return;
  if (!runtimePromise) runtimePromise = new Promise((resolve, reject) => {
    const script = document.createElement('script');
    script.src = runtimeUrl;
    script.onload = () => window.figma?.captureForDesign ? resolve() : reject(new Error('The official capture API is unavailable.'));
    script.onerror = () => reject(new Error('Cannot load the official Figma capture runtime.'));
    document.head.append(script);
  });
  try { await timeout(runtimePromise, 'Figma runtime'); }
  catch (error) { runtimePromise = null; throw error; }
}
async function prepare() {
  button.disabled = true;
  try {
    const response = await timeout(fetch('./fragment.html'), 'Design loading');
    if (!response.ok) throw new Error('Cannot load fragment.html: HTTP ' + response.status);
    design.innerHTML = await response.text();
    if (design.querySelectorAll('[data-figma-board]').length !== 1) throw new Error('Expected one data-figma-board root.');
    for (const axis of ['width', 'height']) {
      const value = Number(design.dataset['board' + axis[0].toUpperCase() + axis.slice(1)]);
      if (!Number.isFinite(value) || value <= 0) throw new Error('Set the approved artboard dimensions.');
      design.style.setProperty('--board-' + axis, value + 'px');
    }
    await timeout(document.fonts.ready, 'Fonts');
    await timeout(Promise.all([...design.querySelectorAll('img')].map(image => image.decode())), 'Images');
    await loadRuntime();
    ready = true;
    status.textContent = messages.ready;
    button.textContent = originalLabel;
  } catch (error) {
    ready = false;
    status.textContent = messages.failed + error.message;
    button.textContent = messages.retry;
  } finally { button.disabled = false; }
}
button.addEventListener('click', async () => {
  if (!ready) { await prepare(); return; }
  if (sessionActive) return;
  sessionActive = true;
  copied = false;
  button.disabled = true;
  diagnostics.textContent = '';
  status.textContent = messages.copying;
  try {
    // The promise completes when Figma's capture toolbar closes, not at copy.
    const result = await window.figma.captureForDesign({ selector: '[data-figma-board]', verbose: true });
    if (result?.success === false) throw new Error(result.error || 'Capture cancelled.');
    status.textContent = copied ? messages.copied : messages.session;
  } catch (error) {
    status.textContent = messages.failed + error.message;
  } finally {
    sessionActive = false;
    button.disabled = false;
  }
});
void prepare();
