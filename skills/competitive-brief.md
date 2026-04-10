---
type: skill
title: Competitive Brief
trigger: /build competitive-brief
created: 2026-04-10
updated: 2026-04-10
---

## Purpose

Build a competitive analysis brief on a named competitor. Useful for equipping sales, informing positioning, or preparing for a competitive deal. Synthesizes wiki knowledge and flags gaps that need research.

## Inputs

- **Competitor name**: The company or product being analyzed
- **Product category**: The market segment or use case in scope

## Process

1. Read `wiki/hot.md` for session context
2. Look up `wiki/entities/[competitor-name].md` — use any existing knowledge as the base
3. Look up `wiki/concepts/` for relevant concepts (e.g., [[competitive-positioning]], [[win-loss]])
4. Identify knowledge gaps — what's missing from the wiki that would improve the brief
5. Flag gaps explicitly in the output rather than hallucinating answers
6. Build the brief using the structure below
7. If a template exists in `templates/`, apply it
8. Append to `log.md`

## Output Format

- **Competitor overview**: What they do, who they sell to, go-to-market motion
- **Strengths**: What they genuinely do well (be honest — sales needs accurate intel)
- **Weaknesses**: Where they fall short, supported by evidence or customer feedback
- **Our differentiation**: Where we win and why — tied to specific buyer pain points
- **Talk track for sales**: 3–5 sentences a rep can use in a live conversation
- **Knowledge gaps**: What we don't know and should research

## Example Usage

```
/build competitive-brief
Competitor: ServiceNow
Category: Enterprise workflow automation
```
