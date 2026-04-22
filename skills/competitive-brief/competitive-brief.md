---
type: skill
title: Competitive Brief
trigger: /build competitive-brief
created: 2026-04-10
updated: 2026-04-22
---

## Purpose

Build a concise competitive brief on a named competitor — 2–3 pages, written for sales, PMM, and product audiences. Synthesizes research into a scannable reference. Not the research artifact (that's the competitive profile) and not the rep tool (that's the battle card). It's the digestible middle layer.

**Standalone skill** — no wiki or external files required. Bring your own intel; all guidance is embedded here.

---

## Inputs

- **Competitor**: Company or product name
- **Your product**: Name or context — used to frame differentiation
- **Optional**: Existing competitive profile for this competitor (paste or reference)
- **Optional**: Specific deal type, segment, or use case to focus on
- **Optional**: Buyer voice — win/loss notes, G2 reviews, rep debrief intel (see Buyer Voice section below)

---

## Buyer Voice

Buyer voice is the language buyers actually use when comparing vendors — sourced from call recordings, win/loss interviews, G2 or Gartner Peer Insights reviews, rep debriefs, and lost deal notes. It's the highest-signal source for weaknesses and objection patterns because it reflects what real buyers said, not what marketing inferred.

If you have any buyer voice material (even a handful of G2 quotes or rep debrief notes), bring it in. It makes talk tracks and weakness sourcing significantly more credible. If you don't, the brief will still work — but note which claims are inferred vs. evidenced.

**Where to find buyer voice:**
- G2.com or Gartner Peer Insights — search competitor name, filter by reviews mentioning your company or switching
- Win/loss interview recordings or transcripts
- CRM notes from closed-lost opportunities
- Sales team debrief sessions (ask: "what did the buyer say when they chose them over us?")

---

## Process

### Step 0 — Check for a competitive profile

If the user provides a competitive profile for this competitor, use it as the research base — don't re-derive what's already been synthesized. Note the profile date and flag if it's more than 90 days old.

### Step 1 — Gather intel

Pull from sources in this priority order:

1. **Existing competitive profile** — if provided, start here
2. **User-provided intel** — any notes, docs, or files the user brings in
3. **Buyer voice** — if win/loss data, G2 reviews, or rep debrief notes are available, use the language buyers use when comparing; this is the most credible sourcing for weaknesses and objection patterns
4. **Competitor website** — fetch if a URL is available or can be inferred
5. **Training data** — last resort; always flag claims sourced this way as `[unverified — confirm before use]`

Validate all specific claims — pricing, feature specifics, customer names — before including them. Training data hallucinates on these. If unverified, include the claim and flag it.

### Step 2 — Frame against your positioning

Pull your positioning from a provided messaging framework (or ask for it if not available). Every differentiation claim should be anchored to a specific buyer pain — not a feature comparison in the abstract.

### Step 3 — Build the brief

Use `template.md` in this folder as the output structure. Fill each section:

1. **Competitor overview** — factual, 1–2 paragraphs; company stage, products, buyers, GTM
2. **Their positioning** — quoted from their site where possible; name their category play
3. **Strengths** — what they genuinely do well; accuracy here builds rep trust in the whole document
4. **Weaknesses** — sourced only; attribute each to a source
5. **Our differentiation** — specific deal types and buyer scenarios where you win; tied to ICP, not generic
6. **Talk track** — 3–5 sentences in buyer language; a rep should be able to say this verbatim
7. **Research gaps** — explicit unknowns; flag them rather than filling with inference

### Step 4 — Output

1. Apply `template.md`
2. *(If using the full codex: append to `log.md` and flag any new intel that should update a competitor entity page)*

---

## Key Rules

- Honest on strengths. A brief that overstates your advantage trains reps to distrust the whole document.
- Source every weakness. "They're slow to implement" needs to come from somewhere real — G2, a rep debrief, a lost deal.
- Gaps are content. Write them down explicitly. An acknowledged unknown is more useful than a confident inference.
- Buyer language in the talk track. If the talk track sounds like your website, rewrite it.

---

## Artifact Chain

```
Competitive profile → Competitive brief → Battle card
(full research)        (digestible summary)  (rep-ready)
```

Use the competitive-profile skill first if no profile exists. Distill this brief into the battle-card skill for the one-page rep tool.

---

## Example Usage

```
/build competitive-brief
Competitor: ServiceNow
Your product: Acme Workflow Suite
Focus: Mid-market IT automation deals
```
