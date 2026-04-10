---
type: skill
title: Sales Battle Card
trigger: /build battle-card
created: 2026-04-10
updated: 2026-04-10
---

## Purpose

Generate a one-page sales battle card for a named competitor. Designed for reps to use in live deals. Synthesizes competitive brief and messaging framework into a scannable, actionable format.

## Inputs

- **Competitor name**: The competitor this card is for

## Process

1. Read `wiki/hot.md` for session context
2. Read `wiki/entities/[competitor-name].md` for known competitive intel
3. Run (or read output of) `skills/competitive-brief.md` for this competitor
4. Read `wiki/concepts/` for relevant positioning and messaging concepts
5. Pull messaging pillars from any existing messaging framework (or run `skills/messaging-framework.md` first)
6. Use `templates/battle-card-template.md` as the output structure
7. If an example exists in `examples/`, use it as a quality reference
8. Append to `log.md`

## Output Format

See [[battle-card-template]].

- Win themes: 3 reasons we beat this competitor
- Landmines: Questions to ask that expose competitor weaknesses
- Trap questions: Questions the competitor will ask, and how to respond
- Proof points: Customer evidence or metrics that back up win themes
- One-line summary: A single sentence a rep can use to reframe the competitive conversation

## Example Usage

```
/build battle-card
Competitor: ServiceNow
```
