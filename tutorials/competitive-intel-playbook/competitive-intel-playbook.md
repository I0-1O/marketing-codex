---
type: tutorial
title: "Competitive Intel Playbook"
subtitle: "What to build, in what order, and how to keep it current"
created: 2026-04-14
updated: 2026-04-14
---

# Competitive Intel Playbook

A practical guide to building and maintaining a competitive intelligence system in this vault. Four artifacts, a clear build order, update cadences, and Claude Code scheduling options.

---

## The Four Artifacts

Most competitive programs produce too much or too little. Too much: sprawling research documents no one reads. Too little: a Confluence page that's two years stale. The right answer is four distinct artifacts at different depths, for different audiences, updated at different frequencies.

| Artifact | Audience | Depth | Length | Built from |
|---|---|---|---|---|
| [[master-messaging-document]] | PMM, product, exec | Foundational | Long | Research, positioning sessions |
| [[competitive-profile]] | PMM, product, leadership | Deep research | 8–12 pages | Messaging doc + competitor research |
| Competitive brief | Sales, PMM, product | Digestible summary | 2–3 pages | Competitive profile |
| [[battle-card]] | Sales reps | Action-compressed | 1 page | Competitive brief + buyer voice |

Each artifact has a specific job. Conflating them produces documents that are too long for reps and too shallow for PMM. Build the right thing for the right audience.

---

## The Build Chain

Order matters. Each artifact depends on the one before it.

```
Master messaging doc
        │
        ▼
Competitive profile        ← competitor research anchored to YOUR positioning
        │
        ▼
Competitive brief          ← summary distilled for a broader audience
        │
        ▼
Battle card                ← rep-ready, one page, buyer language
```

**Why it flows this way:**

Competitive analysis without your own positioning is just a Wikipedia entry on the competitor. The messaging doc establishes your ICP, your differentiators, and the specific buyer pain you solve. That foundation is what makes a competitive profile useful — it frames every competitor finding relative to where you actually win and lose, not just in the abstract.

The brief distills the profile for people who need the summary, not the research. The battle card distills the brief into something a rep can use in 60 seconds.

Skip steps and you pay for it: profiles without a messaging anchor drift into "they have feature X, we have feature Y." Battle cards without research behind them are guesses. Briefs without a profile source have no way to know what's known vs. inferred.

---

## Step 1: Master Messaging Document

**Skill:** `skills/messaging-framework.md`
**Template:** `templates/messaging-framework-template.md`
**Trigger:** `/build messaging-framework`

### What it is

Your positioning foundation. Not a competitive document — it's about you. But it's the prerequisite for everything competitive because it defines:

- Who your ICP actually is (not aspirationally — actually)
- The specific pain you solve, in buyer language
- Your three messaging pillars and why they're structured around problems, not features
- Where you win and why — the honest version

### When to build it

Before any competitive work. If you're starting a competitive profile and you don't have a messaging doc, the profile skill will prompt you — you can approximate from your website, but the output will be weaker. Build the messaging doc first.

### What you need

- Access to customer research, win/loss data, or rep call intel
- A clear view of your ICP — the companies and buyers where you win most reliably
- A "why now" — what's driving urgency for buyers today

### Build time

3–6 hours for a first draft. Expect iteration. The first version will be wrong in some section; that's fine — it's a living document.

---

## Step 2: Competitive Profile

**Skill:** `skills/competitive-profile.md`
**Template:** `templates/competitive-profile-template.md`
**Trigger:** `/build competitive-profile`

### What it is

The deep research artifact. Everything you know about one competitor, framed against your own positioning. 11 sections:

1. Quick verdict
2. Competitor snapshot
3. Their positioning
4. Capability comparison
5. Buyer profile comparison
6. Where they win
7. Where you win
8. Their vulnerabilities
9. Their narrative against you
10. Your counter-narrative
11. Research gaps

The "their narrative against you" and "topics to avoid" sections are what elevate this beyond a standard competitive analysis. Most competitive docs document the competitor. This one also documents how the competitor is actively working against you — what they say about you, what they coach buyers to ask, and what conversational framings play into their hands.

### When to build it

- When you're launching into a market where a specific competitor is consistently showing up in deals
- When you've lost 3+ deals to the same competitor in a quarter
- Before a major product launch where competitive displacement is part of the GTM motion
- When you're building a battle card and realize you don't have the research foundation

### What you need

- Your master messaging doc (or the profile skill will prompt you)
- Competitor name or URL
- Access to buyer voice sources if available (G2 reviews, call recordings, rep debrief notes)

### Build time

30–60 minutes with AI assistance. More if competitor intel requires manual verification.

---

## Step 3: Competitive Brief

**Skill:** `skills/competitive-brief.md`
**Template:** `templates/competitive-brief-template.md`
**Trigger:** `/build competitive-brief`

### What it is

The digestible middle layer — 2–3 pages, readable in 5 minutes. Written for sales, product, and leadership audiences who need accurate intel but don't need the full research depth. Seven sections:

1. Competitor overview
2. Their positioning
3. Strengths
4. Weaknesses (sourced)
5. Our differentiation
6. Talk track
7. Research gaps

The talk track is the most important section. It should be in buyer language — not your website copy. If it sounds like your homepage, rewrite it until a rep can say it in a normal conversation without sounding like they're reading from something.

### When to build it

After the competitive profile exists. Use the profile as source material. The brief is also useful as a standalone when you need something fast and the full profile isn't warranted — for a new competitor you're just starting to see in deals, a brief first is reasonable.

### What you need

- Competitive profile (or wiki entity + research as fallback)
- Your messaging doc positioning and ICP

### Build time

15–20 minutes.

---

## Step 4: Battle Card

**Skill:** `skills/battle-card.md`
**Template:** `templates/battle-card-template.md`
**Trigger:** `/build battle-card`

### What it is

One page. For reps in active deals. Scannable in 60 seconds.

Seven sections, in order of how a rep needs them in a conversation:

1. **Win themes** — outcome-first, not feature-first
2. **Landmines** — questions that surface competitor weaknesses
3. **Trap questions** — what the competitor coaches buyers to ask, with ready responses
4. **Topics to avoid** — framings that play into their narrative; what not to say
5. **Proof points** — specific customer evidence
6. **One-liner** — a single sentence to reframe the conversation
7. **Know your enemy** — honest side-by-side

"Topics to avoid" is the section most battle cards skip and most reps need. For a given competitor, there are always 2–3 angles where instinctive rep behavior hands the competitor an advantage. Making those explicit is as valuable as the positive guidance.

### When to build it

After the brief (or profile) exists. The battle card is a distillation — if you build it without research backing it, it's guesswork dressed up as enablement.

### What you need

- Competitive brief or profile as the research base
- Buyer voice intel for the talk track and objection pairs (G2 reviews, call recording excerpts, rep debrief notes)

### Build time

15–20 minutes.

---

## Research Sources and Buyer Voice

The quality of competitive intel is constrained by the quality of sources. In rough priority order:

| Source | What it's good for | Reliability |
|---|---|---|
| Win/loss interviews | Why deals go the way they go; buyer decision logic | Highest |
| Sales call recordings | Objection triggers; exact buyer vocabulary; what competitor says about you | High |
| Rep debrief notes | Pattern spotting across deals; what's working and what isn't | High |
| G2 / review platforms | Buyer-written weaknesses; authentic buyer vocabulary at scale | Medium-high |
| Competitor website | Their positioning claims; what they want buyers to believe | Medium (it's marketing) |
| Press releases / news | Product announcements; funding; partnership moves | Medium |
| LinkedIn / job postings | GTM motion shifts; where they're investing | Low-medium |
| Training data / AI | Quick synthesis; directionally useful | Low — always verify |

**On buyer voice:** The single highest-leverage improvement to most competitive programs is using buyer language instead of marketing language. What buyers say when they're comparing vendors — the exact words, the specific concerns — is available in call recordings and G2 reviews. Mine it. Objection-rebuttal pairs built from actual buyer language are materially more effective than pairs written from product knowledge. See [[buyer-voice-intelligence]].

**On AI-generated competitive intel:** Useful for synthesis and structure. Unreliable for specifics — pricing, feature claims, customer names, and company facts are the highest hallucination risk. Always validate before publishing anything a rep will use in a deal.

---

## Update Cadences

### Don't use a fixed quarterly schedule

Quarterly updates mean your battle card is stale the week after a competitor ships a major release. They also mean you're updating cards that haven't changed when you could be focused on something else.

Use trigger-based cadence instead:

| Trigger | What to update |
|---|---|
| Competitor announces a major product or feature | Competitive profile, competitive brief, battle card |
| 3+ losses to the same competitor in a quarter | Battle card first; investigate gaps; update profile if findings are significant |
| Competitor changes pricing or packaging | Competitive profile (capabilities section), battle card (proof points, one-liner) |
| You win a competitive displacement | Update profile with what worked; update battle card win themes with specifics |
| Competitor gets acquired or raises a significant round | Update entity page; flag positioning implications in profile |
| New G2 reviews surface a recurring theme | Update weaknesses in brief and battle card; add to buyer voice section of profile |
| Your product ships something that changes the comparison | Update capability comparison in profile; update win themes in battle card |

### Suggested minimum cadence

Even with trigger-based updates, set a floor:

| Artifact | Minimum review cadence |
|---|---|
| Master messaging doc | Semi-annual (or after major positioning shifts) |
| Competitive profile | Quarterly per priority competitor |
| Competitive brief | Quarterly per priority competitor (derive from profile) |
| Battle card | Quarterly per priority competitor |

---

## Automating with Claude Code

You can schedule Claude Code runs to handle parts of the competitive intelligence refresh cycle automatically. These work best for detection and drafting — not for publishing without human review.

### What's practical to automate

**Competitor monitoring:** Schedule a weekly web fetch of a competitor's site and diff against the last captured version. Flag changes for human review.

**G2 review ingestion:** Schedule a periodic fetch of a competitor's G2 page; extract new review themes; flag for ingestion into the vault.

**Competitive brief refresh reminder:** On a quarterly schedule, run a check on the `wiki/entities/` pages for your priority competitors; surface pages that haven't been updated in 90+ days; prompt you to run a competitive profile update.

**Post-loss debrief trigger:** After logging a loss in the vault, automatically queue a competitive profile update for that competitor.

### Setting up a schedule

Use the `/schedule` skill or the Claude Code scheduling tools to create recurring triggers. Example:

```
/schedule
Task: Check competitor entity pages for staleness
Frequency: Every 90 days
Action: Run /lint focused on wiki/entities/ pages tagged [competitive]; 
        surface any page not updated in 90+ days; prompt for profile refresh
```

```
/schedule
Task: Competitive brief quarterly refresh
Frequency: First Monday of each quarter
Action: For each priority competitor in wiki/entities/, 
        check last-updated date; if > 60 days, flag for /build competitive-brief
```

### What still needs a human

- Validating AI-generated intel before it goes into a published artifact
- Win/loss interviews — no substitute for the conversation
- Deciding when a competitive shift is material enough to warrant a full profile update
- The judgment calls in the talk track and counter-narrative sections

Automation handles the detection and the reminder. PMM handles the decision and the voice.

---

## Putting It Together: A First-Time Setup

If you're building a competitive program from scratch for a new product or market:

**Week 1:** Build the master messaging document. Without it, everything else is unanchored.

**Week 2:** Pick your top 2–3 competitors by deal frequency. Run a competitive profile on each.

**Week 3:** Distill each profile into a competitive brief. Run these by a rep or two for gut-check — does the talk track sound like something they'd actually say?

**Week 4:** Build battle cards from the briefs. Distribute. Set up trigger-based update reminders.

**Ongoing:** Feed the machine. Every win/loss conversation, every G2 review, every rep debrief is an input. Ingest what's signal, ignore the rest.

---

## Related Skills and Templates

| What | Where |
|---|---|
| Build messaging foundation | `skills/messaging-framework.md` |
| Deep competitor research | `skills/competitive-profile.md` |
| Digestible competitive summary | `skills/competitive-brief.md` |
| Rep-ready one-pager | `skills/battle-card.md` |
| Schedule recurring tasks | `/schedule` skill |
| Mine buyer language | [[buyer-voice-intelligence]] |

---

*This tutorial describes the generic competitive intel workflow. For company-specific competitors, use the `company/` fork structure described in `CLAUDE.md`.*
