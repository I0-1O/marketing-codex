---
type: skill
title: "Master Messaging Document"
trigger: /build messaging-framework
created: 2026-04-10
updated: 2026-04-13
---

## Purpose

Build a complete master messaging document: positioning statement, ICP and persona definitions, per-audience value propositions, pillar-based messaging architecture, objection handling, and proof points. Output is the single source of truth that feeds every downstream deliverable — decks, battle cards, one-pagers, talk tracks, email campaigns.

Load [[pmm-writing-voice]] alongside this skill. All copy output must pass its editing checklist.

See [[master-messaging-document]], [[problem-first-messaging]], and [[benefit-ladder]] for the frameworks this skill operationalizes.

---

## Inputs

Gather these before starting. The quality of the output is bounded by the quality of what you bring in.

- **Product name and scope**: official product name; is this doc product-level (full value story) or theme-level (one value area in depth)?
- **Target persona(s)**: 2–4 audiences, each defined by job title, company type, and key responsibilities — not vague categories
- **Customer problems**: what are buyers frustrated by, blocked by, or worried about? Verbatim customer language preferred over product-team paraphrases
- **Key differentiators**: 3–5 capabilities that are meaningfully distinct from alternatives
- **Competitive context**: named competitors or status-quo alternatives (manual process, internal builds, do nothing) — at least one per persona
- **Proof points**: customer outcomes with metrics, analyst quotes, or market data — even rough numbers beat vague claims
- **"Why now"**: what market shift, regulation, or business pressure makes this urgent today? If a buyer could wait six months and nothing would change, the messaging lacks urgency.

If customer language, win/loss data, or sales feedback are available, load them. They produce better pain points than any internal brainstorm.

---

## Process

1. Read `wiki/hot.md` for session context
2. Load [[pmm-writing-voice]] — all copy written in this session follows those rules
3. Search `wiki/entities/` for existing pages on the product, personas, and named competitors
4. Search `wiki/concepts/` for relevant positioning frameworks ([[problem-first-messaging]], [[benefit-ladder]], [[master-messaging-document]])
5. **Decide scope**: product-level doc (full value story across all pillars) or theme-level doc (one value area in depth, references product-level doc)
6. **Build the positioning statement** — see structure below; draft it first, because everything else flows from it
7. **Define ICP and personas** — company size, geography, industry, problem sets; then per-persona: job title, primary concern, what they'd do instead
8. **Write per-audience value propositions** — one per persona; apply the benefit ladder: write direct effect, ask "so what?" once, use that answer
9. **Build the pillar framework** — three pillars, each named for a customer problem cluster (not a product capability); for each pillar, work through: pain points → use cases → features & differentiators → value proposition → outcomes
10. **Write pillar-level messaging** — short (25 words) and long (100 words) for each pillar; these get used when writing about one pillar in isolation
11. **Write top-level messaging** — short (25 words) and long (100 words) that spans all pillars; leads with the buyer's problem, second person, no features
12. **Draft objection handling** — anticipate the 3 most likely objections; write each as the buyer would say it, then respond in full sentences; acknowledge the valid part before addressing it
13. **Assemble proof points** — organized by pillar; note when a proof point supports multiple pillars; flag any that are older than 12 months for refresh
14. Use `templates/messaging-framework-template.md` as the output structure
15. Append to `log.md`

---

## Positioning Statement Structure

> **For [persona] who [problem or situation], [product] is the [category] that [key benefit]. Unlike [alternative], [product] [key differentiator].**

All five elements must be present. The statement doesn't have to use this exact syntax, but it must be specific enough that a competitor couldn't claim it, name or imply the alternative, and lead with the situation before the product.

**Weak:** "Acme is an AI platform that helps engineering teams work faster and more efficiently."

**Strong:** "Acme is the workflow automation platform built for ops teams that need to deploy on their own infrastructure — so automation projects don't get blocked by security review before they start."

---

## Pillar Construction Rules

Name each pillar for the **customer problem it solves**, not the product capability that solves it.

- "Data Sovereignty" ✓ — customer problem
- "On-Premises Deployment" ✗ — product capability

Inside each pillar, sequence matters. It mirrors how a good sales conversation flows:

1. **Pain points** — written in the customer's voice, not the product team's. Test: does this sound like a customer describing their day?
2. **Use cases** — where and when customers encounter this pain; specific contexts (industry, process, system), not generic ones
3. **Features & differentiators** — what the product does; note what makes each feature different from how competitors solve the same problem
4. **Value proposition** — business outcome one tier up from the direct effect; apply [[benefit-ladder]]
5. **Outcomes** — tangible, measurable results a buyer could verify after implementation

Three pillars. Two is thin. Four dilutes. The one-sentence test: can you describe the entire positioning in three sentences — one per pillar — without mentioning a single feature? If not, the architecture has drifted into the weeds.

---

## Competitive Framing Rules

Be specific. "Unlike other tools, we are more autonomous" is not competitive positioning.

**Weak:** "Unlike other platforms, Acme is easier to use."
**Strong:** "Salesforce requires a certified admin to build most workflows. Acme's form-based builder is owned by ops teams — no IT queue."

If your company sells in multiple categories (cloud and on-prem, for example): attack specific trade-offs, not entire categories. Broad attacks on a category you also sell undercut your own portfolio.

---

## Common Mistakes to Avoid

- **Benefits stated as features**: every pillar's value prop should survive the "so what?" test
- **Product-voice pain points**: if the pain point sounds like it came from a product roadmap, rewrite it in customer language
- **Every pillar about the product**: at least one pillar should name a business outcome (cost predictability, risk reduction, speed) not a product capability area
- **Missing "why now"**: if urgency isn't in the doc, reps will improvise it — usually badly
- **Proof points without dates**: analyst data and metrics decay; cite sources and dates so anyone downstream can verify or refresh
- **Finished artifact thinking**: a messaging doc is a living reference. Set a review cadence when you ship it — quarterly with PM and sales is a reasonable minimum

---

## Output Format

See [[messaging-framework-template]].

---

## Example Usage

```
/build messaging-framework
Product: Acme Workflow Automation
Scope: product-level
Personas: VP of Operations (buyer), IT Director (technical approver), Process Analyst (champion)
Differentiators: no-code builder, real-time process visibility, native ERP integrations, on-prem deployment
Competitive context: ServiceNow (enterprise), homegrown scripts (status quo), Monday.com (SMB crossover)
Why now: new data residency requirements in EU effective Q3
```
