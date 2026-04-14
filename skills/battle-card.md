---
type: skill
title: Sales Battle Card
trigger: /build battle-card
created: 2026-04-10
updated: 2026-04-14
---

## Purpose

Generate a one-page sales battle card for a named competitor. For reps in active competitive deals — scannable in 60 seconds, usable in a live conversation. Everything that doesn't serve that purpose gets cut.

## Inputs

- **Competitor**: The competitor this card is for
- **Your product**: Name or context
- **Optional**: Specific deal type or segment to optimize for

## Process

### Step 1 — Pull research base

In priority order:

1. **Competitive profile** (`skills/competitive-profile.md` output for this competitor) — preferred; use if it exists
2. **Competitive brief** — use if no profile exists
3. **Wiki entity** — `wiki/entities/[competitor].md`
4. **Buyer voice** — win/loss notes, G2 reviews, rep call intel; extract objection triggers and exact buyer vocabulary (see [[buyer-voice-intelligence]]); this is the highest-signal source for talk tracks and objection pairs
5. **Competitor website** — fetch if needed to verify positioning claims

Flag any claim sourced from training data as `[unverified]`. Pricing numbers and specific feature claims are the highest-risk hallucination targets — never include without confirmation.

### Step 2 — Pull your positioning

Read any existing messaging framework for your product. Extract:
- Win themes tied to this competitor specifically (not generic positioning)
- ICP profile for deals where you beat this competitor
- Proof points relevant to this competitive scenario

If no messaging doc exists, ask for it or note the gap in the card.

### Step 3 — Identify topics to avoid

This is a step most battle cards skip. For this competitor specifically: what framings, comparisons, or product angles play into their narrative? What do reps instinctively say that hands the competitor an advantage? Document these explicitly — they're as important as what to say.

Sources: rep debrief intel, lost deal patterns, competitor's own attack lines from Step 1.

### Step 4 — Assemble the card

Use `templates/battle-card-template.md`. One page. Every section must be usable in a live deal — if a rep can't act on it in the moment, cut it.

Sections:
1. **Win themes** — 3 reasons; outcome-first, not feature-first
2. **Landmines** — questions that expose competitor vulnerabilities; specific, not rhetorical
3. **Trap questions** — what the competitor coaches buyers to ask; with ready responses
4. **Topics to avoid** — framings that favor their narrative; what not to say
5. **Proof points** — customer evidence; specific beats general
6. **One-liner** — a single sentence that reframes the competitive conversation
7. **Know your enemy** — honest side-by-side on strengths, weaknesses, best-fit buyer

### Step 5 — Output and logging

1. Apply `templates/battle-card-template.md`
2. Append to `log.md`: `build: battle-card → [Competitor]`
3. Note the update date on the card — stale battle cards lose rep trust fast

## Update Cadence

Don't update on a fixed quarterly schedule. Update on trigger events:

- Competitor announces a new product or major feature
- You see a pattern of losses to this competitor (3+ in a quarter is a signal)
- Competitor changes pricing or packaging
- You win a competitive displacement — learn from what worked
- Your own product ships something that changes the comparison

Trigger-based cadence keeps cards current when it matters, without the overhead of refreshing cards that haven't changed. See the competitive execution tutorial for Claude Code scheduling options.

## Key Rules

- One page. If it doesn't fit, you haven't prioritized — cut, don't expand.
- Outcome-first win themes. "Faster deployment" is a feature. "Teams go live in 2 weeks instead of 6 months" is an outcome.
- Real buyer language in talk tracks. Mine call recordings and G2 reviews, not your website.
- Honest on weaknesses. Reps know when a card is propaganda. Credibility > coverage.

## Artifact Chain

```
Competitive profile → Competitive brief → Battle card
(full research)        (PMM/leadership)    (rep-ready, one page)
```

## Example Usage

```
/build battle-card
Competitor: ServiceNow
Your product: Acme Workflow Suite
```
