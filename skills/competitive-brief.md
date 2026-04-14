---
type: skill
title: Competitive Brief
trigger: /build competitive-brief
created: 2026-04-10
updated: 2026-04-14
---

## Purpose

Build a concise competitive brief on a named competitor — 2–3 pages, written for sales, PMM, and product audiences. Synthesizes research into a scannable reference. Not the research artifact (that's [[competitive-profile]]) and not the rep tool (that's [[battle-card]]). It's the digestible middle layer.

## Inputs

- **Competitor**: Company or product name
- **Your product**: Name or context — used to frame differentiation
- **Optional**: Specific deal type, segment, or use case to focus on

## Process

### Step 0 — Check for a competitive profile

Look for `wiki/entities/[competitor].md` and any existing competitive profile output for this competitor. If a competitive profile exists, use it as the research base — don't re-derive what's already been synthesized. Note the profile date and flag if it's more than 90 days old.

### Step 1 — Gather intel

Pull from sources in this priority order:

1. **Existing competitive profile** — if available, start here
2. **Wiki entity page** — `wiki/entities/[competitor].md`
3. **Previously ingested sources** — check `wiki/sources/` for any competitive sources on this competitor
4. **Buyer voice** — if win/loss data, G2 reviews, or rep debrief notes are available, pull the language buyers use when comparing; this is the most credible sourcing for weaknesses and objection patterns (see [[buyer-voice-intelligence]])
5. **Competitor website** — fetch if a URL is available or can be inferred
6. **Training data** — last resort; always flag claims sourced this way as unverified

Validate all specific claims — pricing, feature specifics, customer names — before including them. Training data hallucinates on these. If unverified, include the claim and flag it: `[unverified — confirm before use]`.

### Step 2 — Frame against your positioning

Pull your positioning from the messaging framework (or ask for it if not available). Every differentiation claim in the brief should be anchored to a specific buyer pain — not a feature comparison in the abstract.

### Step 3 — Build the brief

Use `templates/competitive-brief-template.md` as the output structure. Fill each section:

1. **Competitor overview** — factual, 1–2 paragraphs; company stage, products, buyers, GTM
2. **Their positioning** — quoted from their site where possible; name their category play
3. **Strengths** — what they genuinely do well; accuracy here builds rep trust in the whole document
4. **Weaknesses** — sourced only; attribute each to a source
5. **Our differentiation** — specific deal types and buyer scenarios where you win; tied to ICP, not generic
6. **Talk track** — 3–5 sentences in buyer language; a rep should be able to say this verbatim
7. **Research gaps** — explicit unknowns; flag them rather than filling with inference

### Step 4 — Output and logging

1. Apply `templates/competitive-brief-template.md`
2. Append to `log.md`: `build: competitive-brief → [Competitor]`
3. If new intel surfaced that should update the competitor entity, flag it

## Key Rules

- Honest on strengths. A brief that overstates your advantage trains reps to distrust the whole document.
- Source every weakness. "They're slow to implement" needs to come from somewhere real — G2, a rep debrief, a lost deal.
- Gaps are content. Write them down explicitly. An acknowledged unknown is more useful than a confident inference.
- Buyer language in the talk track. If the talk track sounds like your website, rewrite it.

## Artifact Chain

```
Competitive profile → Competitive brief → Battle card
(full research)        (digestible summary)  (rep-ready)
```

Run `skills/competitive-profile.md` first if no profile exists. Distill this brief into `skills/battle-card.md` for the one-page rep tool.

## Example Usage

```
/build competitive-brief
Competitor: ServiceNow
Your product: Acme Workflow Suite
Focus: Mid-market IT automation deals
```
