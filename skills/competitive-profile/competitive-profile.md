---
type: skill
title: Competitive Profile
trigger: /build competitive-profile
created: 2026-04-14
updated: 2026-04-22
---

## Purpose

Build a deep competitive profile comparing a named competitor against your product. This is a pre-battlecard research artifact — more comprehensive than a competitive brief, less action-compressed than a battle card. It establishes the intel foundation that informs both.

Intended audience: PMM, product, sales leadership. Not designed for direct rep use in live deals — distill into a battle card for that purpose.

**Standalone skill** — no wiki or external files required. Bring your own intel; all guidance is embedded here.

---

## Inputs

**Required:**
- **Competitor**: Company or product name, or URL (competitor's main website or specific product page)
- **Your product**: Product name, or URL (your product page or marketing site)

**Optional (but improves output significantly):**
- **Master messaging document** for your product — paste or reference a file if one exists
- **Existing competitive intel** — prior research docs, saved notes, vendor sheets, G2 reviews, lost deal notes
- **Known deal context** — specific segments, deal types, or competitive scenarios to emphasize

---

## Process

### Step 1 — Resolve your product positioning

1. **If a messaging doc is provided:** extract positioning statement, ICP, value props, and key differentiators
2. **If no messaging doc is provided:** prompt the user: "I don't have a master messaging document for [product]. You can paste one, point me to a file, provide a URL, or I can approximate from training data. Which would you prefer?"
   - If a URL is provided: fetch it; extract positioning claims, feature descriptions, and target audience signals; note this is an approximation
   - If a doc is provided: treat as authoritative

### Step 2 — Resolve competitor intelligence

Pull from sources in this priority order:

1. **User-provided intel** — any docs, notes, or files the user brings in; treat as authoritative
2. **Competitor URL** — if provided, fetch it; extract positioning, capabilities, buyer profile, pricing signals, GTM motion
3. **Training data** — if no URL or user intel is available; flag all claims: `[training data — verify before use]`

**Source confidence labeling** — use consistently throughout the output:
- `[user-provided]` — intel the user supplied directly
- `[fetched]` — pulled from a URL in this session
- `[training data — verify before use]` — from Claude's training; may be outdated on pricing, features, company facts

### Step 3 — Build the comparative analysis

Work through each section of `template.md`:

1. **Quick verdict** — one paragraph; who wins in what context; no spin
2. **Competitor snapshot** — factual overview; company stage, funding, products, buyer, GTM
3. **Their positioning** — how they describe themselves; category play; key claims; messaging patterns
4. **Capability comparison** — feature/capability table, 6–10 dimensions; honest on both sides
5. **Buyer profile comparison** — who buys them and why; who buys you and why; where profiles overlap and diverge
6. **Where they win** — specific deal types, buyer profiles, scenarios; be honest or the doc is useless
7. **Where you win** — specific deal types, buyer profiles, scenarios; tied to ICP and positioning
8. **Their vulnerabilities** — weaknesses with evidence; distinguish between real gaps and positioning spin
9. **Their narrative against you** — what they say about you; known FUD and attacks; what they coach buyers to ask
10. **Your counter-narrative** — reframes and responses; tied to positioning, not just feature rebuttals
11. **Research gaps** — what's unknown; what would materially change the analysis if answered

### Step 4 — Output

1. Apply `template.md` as the output structure
2. *(If using the full codex: append to `log.md` and offer to create/update a competitor entity page)*

---

## Key Rules

- **Honesty over confidence.** A competitive profile that claims universal superiority is useless and destroys PMM credibility with sales. Document where the competitor genuinely wins.
- **Source everything.** Label every claim: user-provided, fetched, or training data. Training data may be wrong on pricing, features, or company facts.
- **Gaps are content.** An explicit research gap is more valuable than a hallucinated answer. Flag it, don't fill it.
- **Your positioning is the anchor.** Every section should be evaluated relative to your product's actual positioning and ICP. If no messaging doc exists, say so — the profile will be weaker.

---

## Artifact Chain

This skill sits in a deliberate sequence:

```
Master messaging doc → Competitive profile → Competitive brief → Battle card
(your foundation)      (deep research)        (summary)           (rep-ready)
```

Use the messaging-framework skill first if no messaging doc exists. Use the battle-card skill after this profile to produce the sales-ready distillation.

---

## Example Usage

```
/build competitive-profile
Competitor: ServiceNow
Your product: https://yourcompany.com/product/workflow
```

```
/build competitive-profile
Competitor: https://www.servicenow.com/products/platform.html
Your product: Acme Workflow Suite
Messaging doc: [paste or reference file]
Existing intel: [paste any competitive notes]
```
