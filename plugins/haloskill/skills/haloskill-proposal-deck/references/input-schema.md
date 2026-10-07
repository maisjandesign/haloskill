# Proposal intake

Extract these fields from the user's prompt, files, notes, or prior context. Do not demand every optional field. Ask a concise question only when the missing answer would materially change the commercial offer or story.

```yaml
proposal:
  language: "en | uk | ru | other"
  client_name: "required for final delivery"
  project_name: "required for final delivery"
  proposal_date: "default to current date"
  validity_until: "optional"
  prepared_by: "optional"
  primary_contact: "optional"

decision:
  audience: "decision-makers and stakeholders"
  desired_next_action: "approve | choose option | book workshop | sign | other"
  client_context: "current situation and why now"
  desired_outcomes: []
  success_measures: []

scope:
  services: []
  phases:
    - name: ""
      objective: ""
      activities: []
      deliverables: []
      client_inputs: []
      duration: ""
  exclusions: []
  dependencies: []
  revision_rounds: "optional"

commercials:
  currency: "required if prices are shown"
  pricing_model: "fixed | range | retainer | time-and-materials | options"
  options: []
  taxes: "included | excluded | not supplied"
  payment_schedule: "optional"
  expenses: "optional"

proof:
  case_studies: []
  verified_metrics: []
  testimonials: []
  source_urls: []

delivery:
  start_window: "optional"
  target_deadline: "optional"
  review_cadence: "optional"
  team_members: []
  legal_terms: []
  call_to_action: "optional"

assets:
  client_logo: "optional path"
  project_images: []
  brand_guidelines: "optional path or URL"
  previous_proposal: "optional path"
```

## Minimum viable brief

Before final delivery, know at least:

- client and project names;
- the outcome being proposed;
- included scope and deliverables;
- timeline basis or an explicit “to be confirmed”;
- whether pricing should appear and, if yes, the exact figures and currency;
- the action the client should take next.

If the user requests a first draft and some fields are missing, proceed with bracketed placeholders. Do not disguise assumptions as facts.

