---
type: skill
title: Competitive Profile
trigger: /build competitive-profile
created: 2026-04-14
updated: 2026-04-14
---

## Purpose

Build a deep competitive profile comparing a named competitor against your product. This is a pre-battlecard research artifact — more comprehensive than a competitive brief, less action-compressed than a battle card. It establishes the intel foundation that informs both.

Intended audience: PMM, product, sales leadership. Not designed for direct rep use in live deals — distill into a [[battle-card]] for that purpose.

## Inputs

**Required:**
- **Competitor**: Company or product name, or URL (competitor's main website or specific product page)
- **Your product**: Product name, or URL (your product page or marketing site)

**Optional (but improves output significantly):**
- **Master messaging document** for your product — if one exists in the vault or can be provided
- **Known deal context** — specific segments, deal types, or competitive scenarios to emphasize

## Process

### Step 1 — Resolve your product positioning

1. Check the vault for a master messaging document:
   - Look for any file in `wiki/` or output files matching the product name
   - Check `wiki/hot.md` for recently built messaging artifacts
2. **If a messaging doc is found:** load it; extract positioning statement, ICP, value props, and key differentiators
3. **If no messaging doc is found:**
   - Prompt the user: "I don't have a master messaging document for [product]. You can paste one, point me to a file, or I can approximate from your website. Which would you prefer?"
   - If the user provides a URL: fetch the product website; extract positioning claims, feature descriptions, and target audience signals; note that this is an approximation, not a sourced messaging doc
   - If the user provides a doc: treat it as authoritative and extract the same fields

### Step 2 — Resolve competitor intelligence

1. Check `wiki/entities/[competitor-name].md` for existing intel — use as base, note what's stale or missing
2. If a URL was provided: fetch it; extract positioning claims, product capabilities, target buyers, pricing signals, and GTM motion
3. If only a name was provided: note that research is limited to wiki intel + training data; flag for external verification
4. Check `wiki/sources/` for any previously ingested competitive sources on this competitor
5. Flag all claims sourced from training data vs. fetched/wiki-sourced — training data may be outdated

### Step 3 — Build the comparative analysis

Work through each section of the template:

1. **Quick verdict** — one paragraph; who wins in what context; no spin
2. **Competitor snapshot** — factual overview; company stage, funding, products, buyer, GTM
3. **Their positioning** — how they describe themselves; category plays; key claims; messaging patterns
4. **Capability comparison** — feature/capability table, 6–10 dimensions; honest on both sides
5. **Buyer profile comparison** — who buys them and why; who buys you and why; where profiles overlap and diverge
6. **Where they win** — specific deal types, buyer profiles, scenarios; be honest or the doc is useless
7. **Where you win** — specific deal types, buyer profiles, scenarios; tied to ICP and positioning
8. **Their vulnerabilities** — weaknesses with evidence; distinguish between real gaps and positioning spin
9. **Their narrative against you** — what they say about you; known FUD and attacks; what they coach buyers to ask
10. **Your counter-narrative** — reframes and responses; tied to positioning, not just feature rebuttals
11. **Research gaps** — what's unknown; what would materially change the analysis if answered; specific questions to investigate

### Step 4 — Output and logging

1. Apply `templates/competitive-profile-template.md` as the output structure
2. Append to `log.md`:
   - `build: competitive-profile → [Your Product] vs. [Competitor]`
3. If a new competitor entity was researched, offer to create or update `wiki/entities/[competitor].md`

## Key Rules

- **Honesty over confidence.** A competitive profile that claims universal superiority is useless and destroys PMM credibility with sales. Document where the competitor genuinely wins.
- **Source everything.** Distinguish between: wiki-sourced intel, fetched website content, and training data. Training data has a cutoff and may be wrong on pricing, features, or company facts.
- **Gaps are content.** An explicit research gap is more valuable than a hallucinated answer. Flag it, don't fill it.
- **Your positioning is the anchor.** Every section should be evaluated relative to your product's actual positioning and ICP — not just "us vs. them" in the abstract. If you don't have a messaging doc, the profile will be weaker. Say so.

## Artifact Chain

This skill sits in a deliberate sequence:

```
Master messaging doc → Competitive profile → Competitive brief → Battle card
(your foundation)      (deep research)        (summary)           (rep-ready)
```

Run `skills/messaging-framework.md` first if no messaging doc exists. Run `skills/battle-card.md` after this profile to produce the sales-ready distillation.

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
```
