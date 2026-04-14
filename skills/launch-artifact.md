---
type: skill
title: "Launch Artifact / GTM Campaign Brief"
trigger: /build launch-artifact
created: 2026-04-14
updated: 2026-04-14
---

## Purpose

Build a complete GTM campaign brief (launch artifact): strategic rationale, audience sequencing, per-stage channel strategy, messaging by funnel stage, content plan, execution timeline, and success metrics. Output is the master document that aligns marketing, sales, and leadership on how a campaign will run — from first awareness impression through closed deal.

Load [[pmm-writing-voice]] alongside this skill. All copy output must pass its editing checklist.

See [[master-messaging-document]], [[problem-first-messaging]], and [[benefit-ladder]] for the messaging frameworks this skill draws on.

If a messaging framework for this product or campaign theme doesn't already exist, run `/build messaging-framework` first — the launch artifact depends on it.

---

## Inputs

Gather these before starting. If a messaging framework exists, many of these are already answered — reference it rather than rebuilding from scratch.

- **Campaign name / theme**: the overarching headline or campaign concept (e.g., "Control Without Compromise")
- **Campaign type**: new logo, pipeline acceleration, competitive displacement, expansion, product launch, feature launch
- **Product or product line**: what is being launched or promoted
- **Launch tier**: determines execution scope (Tier 1 = full integrated campaign; Tier 2 = partial; Tier 3 = sales-led with limited marketing)
- **ICP and personas**: company size, geography, industry, problem sets; named personas with job titles and primary concerns
- **Positioning and messaging**: reference an existing messaging framework if available; otherwise provide: positioning statement, top-level short and long message, three pillars with pain → use case → differentiator → value prop → outcome
- **Compelling events**: what triggers a buyer to act now? Regulatory change, cost pressure, architecture requirement, competitive threat, internal catalyst?
- **Competitive context**: named competitors; which alternatives buyers consider; how this campaign addresses head-to-head decisions
- **Target timeline**: campaign start date, launch date, duration
- **Available resources**: teams involved (demand gen, content, SDR, field, partners); budget level; assets already in production
- **Success metrics**: what does this campaign need to move? Leads, pipeline, deals closed, awareness?

---

## Process

1. Read `wiki/hot.md` for session context
2. Load [[pmm-writing-voice]] — all copy written in this session follows those rules
3. Check `wiki/entities/` for existing pages on the product, target accounts, named competitors
4. Check `wiki/sources/` and `wiki/concepts/` for any existing messaging framework or prior campaign brief for this product
5. **State the campaign objective** — one sentence: what does winning look like, for whom, by when? "Generate X qualified opportunities in [segment] in [timeframe]" beats "increase awareness"
6. **Define market context** — 3–5 market facts with sources and dates that make this campaign credible and urgent; stat first, conclusion after
7. **Identify compelling events** — specific triggers that cause a buyer to start evaluating now; regulatory, architectural, cost, competitive, or internal catalyst; named events beat vague "urgency"
8. **Confirm ICP** — company size, geography, industry, and problem profile specific enough to drive list targeting and channel decisions
9. **Sequence the audience** — decide who you're reaching first and why (see Audience Sequencing framework below); write the rationale, don't assume it
10. **Define personas** — for each: job title, primary motivation, what they'd do if this product didn't exist, what objection they raise most often
11. **Write internal positioning** — how does this campaign's product or theme fit within the broader portfolio? What does it solve that adjacent products don't? Written for internal alignment — directness over polish
12. **Write external messaging** — short (25 words) and long (100 words); apply [[problem-first-messaging]]: lead with the buyer's situation, not the product; apply [[benefit-ladder]]: land at business outcome, not direct effect
13. **Map channels by funnel stage** using the ORB framework (see below); fill the Channel/Funnel Matrix; state the rationale for each choice
14. **Write the message for each funnel stage** — Awareness, Consideration, Decision; the message should visibly change as buyers move down; see Messaging Shift section
15. **Build the content plan** — one asset per channel/stage intersection that matters; scope to what's actually executable in the campaign window; note owner and due date
16. **Set the execution timeline** — directional milestones, not a project plan; key gates: asset readiness, campaign launch, SDR activation, first review
17. **Define success metrics** — one primary metric per funnel stage; distinguish leading indicators (CTR, demo requests) from lagging indicators (pipeline, closed-won)
18. **State what you're NOT doing and why** — at least one explicit deprioritization; this shows real tradeoffs were made and prevents scope creep
19. Use `templates/launch-artifact-template.md` as the output structure
20. Append to `log.md`

---

## Audience Sequencing

Choose a strategy — don't default to "all audiences at once." State the reason.

| Strategy | When to use | Trade-off |
|---|---|---|
| **Fastest path to proof** | Early in a campaign, limited resources; target who will say yes fastest | Optimizes for speed; may miss highest-value accounts |
| **Highest-value first** | Strategic accounts where deal size justifies slower conversion | Slower to revenue; needs strong top-down message |
| **Bottom-up adoption** | Product with practitioner usage model; let user adoption create pull | Requires time; fails if economic buyer controls budget tightly |
| **Top-down** | Complex enterprise sale; executive interest drives org-level evaluation | Needs executive-ready message and AE capacity |

For most enterprise B2B new logo campaigns: start with the technical champion or mid-level decision maker (feels the pain, has budget influence, can run a POC), support with practitioner awareness, convert with the economic buyer once momentum exists.

Whatever you choose, write it down and say why.

---

## Channel Strategy — ORB Framework

For each channel, answer: who reaches it? What funnel stage does it serve? What's the job? Why this over alternatives?

**ORB: Owned → Rented → Borrowed**

- **Owned**: channels you control entirely — website, email list, SDR sequences, in-product messaging, internal sales content
- **Rented**: channels you pay for or participate in under someone else's rules — LinkedIn paid, Google Ads, G2 listings, conference sponsorships
- **Borrowed**: reach you earn through others' audiences — PR/earned media, analyst coverage, partner co-marketing, customer references, community posts

Lead with owned. Supplement with rented. Pursue borrowed where credibility is the constraint — especially in enterprise and regulated industries where buyers validate through analysts, peers, and press before they trust a vendor.

### Channel Quick Reference

| Channel | ORB | Best for | Stage |
|---|---|---|---|
| SDR outreach | Owned | Targeted account activation | Consideration |
| Email (house list) | Owned | Warm audience nurture | Consideration |
| Website / landing page | Owned | Research and conversion | Consideration, Decision |
| Sales battle cards / enablement content | Owned | In-deal support | Decision |
| LinkedIn paid | Rented | Title-targeted reach by company size | Awareness, Consideration |
| Google Search (SEM) | Rented | Active intent capture | Consideration |
| G2 / review sites | Rented | Social proof, peer validation | Consideration, Decision |
| Webinar / live demo | Rented/Owned | Active consideration, "show don't tell" | Consideration |
| Conference sponsorship | Rented | In-person ICP density | Awareness |
| PR / earned media | Borrowed | Broad awareness, third-party credibility | Awareness |
| Analyst coverage (Gartner, Forrester) | Borrowed | Influence on enterprise shortlist | Awareness, Decision |
| Community (HN, Reddit, Slack, Dev.to) | Borrowed | Practitioner credibility | Awareness |
| Partner co-marketing | Borrowed | Reach adjacent audiences | Awareness, Consideration |
| Customer references | Borrowed | Final objection removal | Decision |
| POC / pilot program | Owned | Technical validation | Decision |

Three channels per funnel stage is enough for most campaigns. Don't plan what you can't execute.

---

## Messaging Shift Across the Funnel

The message must visibly change as buyers move from awareness to decision. Using the same pitch at every stage is the most common campaign execution failure.

| Stage | Message focus | Tone | What to avoid |
|---|---|---|---|
| Awareness | The problem exists and is worth solving | Provocative, creates recognition | Selling too early; feature lists; claiming uniqueness before you've earned credibility |
| Consideration | Why this product, why now, why not the alternatives | Specific, credibility-building | Vague claims; no proof; features without outcomes |
| Decision | Why this is safe, smart, and worth the risk | Reassuring, evidence-based | Overselling; ignoring real concerns; generic ROI theater |

**Example (same product, three stages):**

- **Awareness**: "Your procurement team is manually routing approvals that should take minutes. That backlog is costing you more than you know."
- **Consideration**: "[Product] connects to your existing ERP, routes approvals based on your policy rules, and escalates exceptions without email chains. Here's how [customer] cut approval cycle time by 60%."
- **Decision**: "Your IT team will ask about SSO, data residency, and rollback. Here are the answers. [Product] is live in [customer] environments on your exact stack."

Apply [[benefit-ladder]] at every stage: awareness messages name the business-level problem, not just the symptom; consideration messages show business outcomes, not just capabilities; decision messages name the risk of inaction alongside the value of action.

---

## Launch Phases (for product launches)

For product launches (vs. ongoing campaigns), a phased release model lets you build proof before going broad:

1. **Internal** — team alignment, sales enablement, SDR training; no external communication
2. **Alpha / limited access** — controlled early access; gathering proof, refining messaging; NDA or invite-only
3. **Beta / early access** — broader but bounded; building references and case studies; be explicit about beta status in communications
4. **GA / launch** — full market motion; all channels active; PR and analyst outreach released
5. **Post-launch** — sustained pipeline motion; optimization based on what worked; case study production from early customers

Most campaigns don't use all five phases. Skip what doesn't apply.

---

## What Makes a Strong Launch Artifact

- Every channel decision has a stated rationale — not just "we'll do LinkedIn" but why LinkedIn over alternatives for this audience at this stage
- Audience sequencing is explained, not assumed
- The message visibly evolves across funnel stages — you can point to the difference
- At least one "we deprioritized X because..." — explicit choices signal real tradeoffs were made
- Timeline is directional, not exhaustive — this is not a project plan
- Content plan contains only what can actually be executed in the campaign window
- Success metrics are specific enough to evaluate when the campaign ends

---

## Common Mistakes to Avoid

- **Leading with product, not problem** — awareness content that pitches before establishing the problem loses the audience before they know they should care
- **Treating all personas identically** — the CFO message and the IT Director message are not the same sentence said twice
- **No compelling event** — a campaign without urgency relies on the buyer's own timing; name specific triggers
- **Channel list without rationale** — "we'll do LinkedIn, email, webinar, and a landing page" is not a channel strategy
- **Content planned, execution not staffed** — plans that exceed available headcount fail mid-campaign; scope to what's realistic
- **Vanity metrics as primary KPIs** — impressions and open rates are leading indicators, not proof that a campaign is working
- **Missing internal positioning** — when the portfolio is multi-product, skipping this creates mixed signals in the field

---

## Output Format

See [[launch-artifact-template]].

---

## Example Usage

```
/build launch-artifact
Campaign name: Control Without Compromise
Campaign type: New logo
Product: K2 enterprise automation
ICP: Enterprise (1,000+), regulated industries (Public Sector, FinServ, Manufacturing), global
Compelling events: Data residency regulations tightening (DORA, country-level sovereignty laws); cloud cost overruns blocking automation scale; AI vendor lock-in concerns as model deprecation accelerates
Competitive context: Microsoft Power Automate (cloud-only architecture), ServiceNow (proprietary AI)
Launch tier: Tier 2
Timeline: Q2 2026 start, 90-day execution window
Messaging framework: Reference K2 Master Messaging 2026 (existing internal doc)
```
