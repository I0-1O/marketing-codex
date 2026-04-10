---
type: skill
title: Messaging Framework
trigger: /build messaging-framework
created: 2026-04-10
updated: 2026-04-10
---

## Purpose

Build a structured messaging framework for a product or feature — positioning statement, value pillars, proof points, and objection handling. Output is ready to share with sales, demand gen, or use as input for other deliverables (battle cards, one-pagers, content briefs).

## Inputs

- **Product name**: The product or feature being positioned
- **Target persona**: Primary buyer or user (title, role, company type)
- **Key differentiators**: 3–5 things that make this product distinct
- **Competitive context**: Main alternatives buyers consider (named competitors or categories)

## Process

1. Read `wiki/hot.md` for session context
2. Search `wiki/entities/` for any existing pages on the product, persona, or named competitors
3. Search `wiki/concepts/` for relevant frameworks (e.g., [[positioning]], [[jobs-to-be-done]], [[value-pillar]])
4. Construct positioning statement using the format: *For [persona] who [need/problem], [product] is the [category] that [key benefit]. Unlike [alternative], [product] [key differentiator].*
5. Identify 3 value pillars — each pillar should be a business outcome, not a feature
6. For each pillar: 2–3 proof points (quantified where possible), 1 key objection + response
7. Use `templates/messaging-framework-template.md` as the output structure
8. If an example exists in `examples/`, use it as a quality reference

## Output Format

See [[messaging-framework-template]].

- Positioning statement (1–2 sentences)
- Value pillar 1: name, description, proof points, objection + response
- Value pillar 2: name, description, proof points, objection + response
- Value pillar 3: name, description, proof points, objection + response

## Example Usage

```
/build messaging-framework
Product: Acme Workflow Automation
Persona: VP of Operations at a 500–5000 employee manufacturing company
Differentiators: no-code, real-time process visibility, native ERP integrations
Competitive context: ServiceNow, homegrown scripts, manual handoffs
```
