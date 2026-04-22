---
type: skill
title: Sales Battle Card
trigger: /build battle-card
created: 2026-04-10
updated: 2026-04-22
---

## Purpose

Generate a one-page sales battle card for a named competitor. For reps in active competitive deals — scannable in 60 seconds, usable in a live conversation. Everything that doesn't serve that purpose gets cut.

**Standalone skill** — no wiki or external files required. Bring your own intel; all guidance is embedded here.

---

## Inputs

- **Competitor**: The competitor this card is for
- **Your product**: Name or context
- **Optional**: Competitive profile or brief for this competitor (paste or reference)
- **Optional**: Win/loss notes, G2 reviews, or rep debrief intel (see Buyer Voice section below)
- **Optional**: Specific deal type or segment to optimize for

---

## Buyer Voice

Buyer voice is the language buyers actually use when comparing vendors — sourced from call recordings, win/loss interviews, G2 reviews, and rep debriefs. It is the highest-signal source for talk tracks and objection pairs because it reflects what real buyers said, not what marketing inferred.

If you have any buyer voice material, bring it in. It makes the card dramatically more credible with reps. If you don't have it, note which sections are inferred vs. evidenced — reps can tell the difference.

**Where to find buyer voice:**
- G2.com or Gartner Peer Insights — search competitor name, filter for reviews mentioning switching or comparison
- Win/loss interview recordings or transcripts
- CRM notes from closed-lost opportunities
- Rep debrief sessions: "What did the buyer say when they chose them over us?"

---

## Process

### Step 1 — Pull research base

In priority order:

1. **Competitive profile** — if provided by the user, use as primary research base
2. **Competitive brief** — use if no profile is available
3. **User-provided intel** — any notes, docs, or files the user brings in
4. **Buyer voice** — win/loss notes, G2 reviews, rep call intel; extract objection triggers and exact buyer vocabulary; highest-signal source for talk tracks
5. **Competitor website** — fetch if needed to verify positioning claims
6. **Training data** — last resort; flag any claim sourced this way as `[unverified]`

Pricing numbers and specific feature claims are the highest-risk hallucination targets — never include without confirmation.

### Step 2 — Pull your positioning

Read any provided messaging framework. Extract:
- Win themes tied to this competitor specifically (not generic positioning)
- ICP profile for deals where you beat this competitor
- Proof points relevant to this competitive scenario

If no messaging doc is available, ask for key differentiators and win themes, or note the gap on the card.

### Step 3 — Identify topics to avoid

This step is often skipped but is critical. For this competitor specifically: what framings, comparisons, or product angles play into their narrative? What do reps instinctively say that hands the competitor an advantage? Document these explicitly — they're as important as what to say.

Sources: rep debrief intel, lost deal patterns, competitor's known attack lines from Step 1.

### Step 4 — Assemble the card

Use `template.md` in this folder. One page. Every section must be usable in a live deal — if a rep can't act on it in the moment, cut it.

Sections:
1. **Win themes** — 3 reasons; outcome-first, not feature-first
2. **Landmines** — questions that expose competitor vulnerabilities; specific, not rhetorical
3. **Trap questions** — what the competitor coaches buyers to ask; with ready responses
4. **Topics to avoid** — framings that favor their narrative; what not to say
5. **Proof points** — customer evidence; specific beats general
6. **One-liner** — a single sentence that reframes the competitive conversation
7. **Know your enemy** — honest side-by-side on strengths, weaknesses, best-fit buyer

### Step 5 — Output

1. Apply `template.md`
2. Note the creation date on the card — stale cards lose rep trust fast
3. *(If using the full codex: append to `log.md`)*

---

## Update Cadence

Don't update on a fixed quarterly schedule. Update on trigger events:

- Competitor announces a new product or major feature
- Pattern of losses to this competitor (3+ in a quarter is a signal)
- Competitor changes pricing or packaging
- You win a competitive displacement — learn from what worked
- Your product ships something that changes the comparison

Trigger-based cadence keeps cards current when it matters, without the overhead of refreshing cards that haven't changed.

---

## Key Rules

- One page. If it doesn't fit, you haven't prioritized — cut, don't expand.
- Outcome-first win themes. "Faster deployment" is a feature. "Teams go live in 2 weeks instead of 6 months" is an outcome.
- Real buyer language in talk tracks. Mine call recordings and G2 reviews, not your website.
- Honest on weaknesses. Reps know when a card is propaganda. Credibility beats coverage.

---

## Artifact Chain

```
Competitive profile → Competitive brief → Battle card
(full research)        (PMM/leadership)    (rep-ready, one page)
```

---

## Example Usage

```
/build battle-card
Competitor: ServiceNow
Your product: Acme Workflow Suite
```

```
/build battle-card
Competitor: ServiceNow
Your product: Acme Workflow Suite
Competitive brief: [paste]
Buyer voice: [paste G2 reviews or win/loss notes]
```
