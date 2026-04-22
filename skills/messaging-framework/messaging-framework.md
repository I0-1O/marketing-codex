---
type: skill
title: "Master Messaging Document"
trigger: /build messaging-framework
created: 2026-04-10
updated: 2026-04-22
---

## Purpose

Build a complete master messaging document: positioning statement, ICP and persona definitions, per-audience value propositions, pillar-based messaging architecture, objection handling, and proof points. Output is the single source of truth that feeds every downstream deliverable — decks, battle cards, one-pagers, talk tracks, email campaigns.

**Standalone skill** — no wiki or external files required. All frameworks are embedded here. If you have `pmm-writing-voice.md`, load it alongside this skill for copy review rules.

---

## Inputs

Gather these before starting. Output quality is bounded by input quality.

- **Product name and scope**: official product name; is this doc product-level (full value story) or theme-level (one value area in depth)?
- **Target persona(s)**: 2–4 audiences, each defined by job title, company type, and key responsibilities — not vague categories
- **Customer problems**: what are buyers frustrated by, blocked by, or worried about? Verbatim customer language preferred over product-team paraphrases
- **Key differentiators**: 3–5 capabilities meaningfully distinct from alternatives
- **Competitive context**: named competitors or status-quo alternatives (manual process, internal builds, do nothing) — at least one per persona
- **Proof points**: customer outcomes with metrics, analyst quotes, or market data — even rough numbers beat vague claims
- **"Why now"**: what market shift, regulation, or business pressure makes this urgent today? If a buyer could wait six months and nothing would change, the messaging lacks urgency.

If customer language, win/loss data, or sales feedback are available, bring them in. They produce better pain points than any internal brainstorm.

---

## Process

1. **Confirm scope**: product-level (full value story across all pillars) or theme-level (one value area, references a broader product-level doc)
2. **Load writing voice rules** (see Writing Voice section below) — all copy written in this session follows those rules
3. **Build the positioning statement** — draft it first; everything else flows from it (see Positioning Statement Structure below)
4. **Define ICP and personas** — company size, geography, industry, problem sets; then per-persona: job title, primary concern, what they'd do instead
5. **Write per-audience value propositions** — one per persona; apply the benefit ladder: write direct effect, ask "so what?" once, use that answer
6. **Build the pillar framework** — three pillars, each named for a customer problem cluster (not a product capability); for each pillar: pain points → use cases → features & differentiators → value proposition → outcomes
7. **Write pillar-level messaging** — short (25 words) and long (100 words) for each pillar
8. **Write top-level messaging** — short (25 words) and long (100 words) spanning all pillars; leads with buyer's problem, second person, no features
9. **Draft objection handling** — anticipate the 3 most likely objections; write each as the buyer would say it, then respond; acknowledge the valid part before addressing it
10. **Assemble proof points** — organized by pillar; flag any older than 12 months for refresh
11. Use `template.md` in this folder as the output structure
12. *(If using the full codex: append to `log.md`)*

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

Inside each pillar, sequence mirrors how a good sales conversation flows:

1. **Pain points** — written in the customer's voice. Test: does this sound like a customer describing their day?
2. **Use cases** — where and when customers encounter this pain; specific contexts (industry, process, system)
3. **Features & differentiators** — what the product does; what makes each feature different from how competitors solve the same problem
4. **Value proposition** — business outcome one tier up from the direct effect; apply the benefit ladder (see below)
5. **Outcomes** — tangible, measurable results a buyer could verify after implementation

Three pillars. Two is thin. Four dilutes. The one-sentence test: can you describe the entire positioning in three sentences — one per pillar — without mentioning a single feature? If not, the architecture has drifted into the weeds.

---

## Benefit Ladder

Every feature has a direct effect. That is not the benefit. The benefit is what the direct effect makes possible at the business level.

| Tier | What it is | Example |
|---|---|---|
| Feature | What the product does | "Drag-and-drop workflow builder" |
| Direct effect | The immediate result | "Non-technical users can build workflows without IT" |
| Business outcome | What that makes possible | "IT backlog shrinks; business teams ship faster" |

Apply "so what?" **once**. One level up is the sweet spot. Two levels up lands in platitudes ("achieve competitive advantage," "drive business growth").

---

## Problem-First Messaging

The product earns attention only after the problem earns recognition. Every top-level message and every pillar should open with the buyer's situation, not the product.

**Wrong order:** "Acme's no-code builder lets any ops team automate workflows without IT support."
**Right order:** "Most workflow automation projects stall in IT's backlog for months. Acme's no-code builder puts that work back in ops hands."

Both convey the same facts. The second one makes the reader feel the problem before meeting the solution.

---

## Competitive Framing Rules

Be specific. "Unlike other tools, we are more autonomous" is not competitive positioning.

**Weak:** "Unlike other platforms, Acme is easier to use."
**Strong:** "Salesforce requires a certified admin to build most workflows. Acme's form-based builder is owned by ops teams — no IT queue."

If your company sells in multiple categories (cloud and on-prem, for example): attack specific trade-offs, not entire categories.

---

## Writing Voice Rules

All copy produced by this skill must pass these checks:

- **No em dashes** — split into two sentences
- **One comma per sentence max** — more than one means split it
- **Bullets: 3 ideal, 5 ceiling** — no exceptions
- **Lead with the problem** — product earns attention after problem earns recognition
- **Use "you," not "organizations"** — forces specificity
- **Benefits must pass "so what?" once** — direct effect is not the benefit
- **No banned words**: Seamless, Robust, Leverage (verb), Harness, Empower, Unlock, Streamline, AI-powered, Accelerate, Next-generation, Best-in-class, World-class, Cutting-edge, Transformative, Game-changing, Holistic, Future-proof, Reimagine

---

## Common Mistakes

- **Benefits stated as features**: every pillar value prop should survive the "so what?" test
- **Product-voice pain points**: if the pain sounds like it came from a product roadmap, rewrite it in customer language
- **Every pillar about the product**: at least one pillar should name a business outcome, not a product capability area
- **Missing "why now"**: if urgency isn't in the doc, reps will improvise it — usually badly
- **Proof points without dates**: analyst data and metrics decay; cite sources and dates
- **Finished artifact thinking**: a messaging doc is a living reference. Set a review cadence — quarterly with PM and sales is a reasonable minimum

---

## Output Format

Use `template.md` in this folder.

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
