# Hot — Session Context Cache

> Rolling context cache. Stays under ~500 words. Updated at the end of each session.
> Not a full history — just enough to orient the next session.

---

## Last Updated: 2026-05-12

### What Was Built This Session

**Drafted + ingested a new Brian article: "Your Homepage Is Written for Nobody"**

Co-drafted via back-and-forth using the new `about_me.xml` writing profile (`C:\Users\brieb\Downloads\about_me.xml`). Article lives at `articles/your-homepage-is-written-for-nobody.md`. ~720 words. Voice anchors deployed: `Look,` opener, conjunction starts, one ALL CAPS (NONE), one ellipsis ("Your teams"...), two parenthetical asides, no em dashes (caught and stripped after Brian flagged 8 in v1), no buzzwords, no TL;DR.

**New pages (2):**
- `wiki/sources/your-homepage-is-written-for-nobody.md` — synopsis; links to full article
- `wiki/concepts/safe-middle-copy.md` — the failure mode named in the piece; origin: self

**Updated (4 cross-links):**
- `wiki/entities/brian-rieb.md` — added Homepage / GTM Copy Philosophy section; new source link
- `wiki/concepts/benefit-ladder.md` — cross-linked to safe-middle (tier vs. reader)
- `wiki/concepts/marketing-voice-and-pov.md` — cross-linked (exclusion failure at audience layer)
- `wiki/concepts/master-messaging-document.md` — cross-linked (downstream symptom)

---

### Core Argument (Brian, new article)

Most SaaS homepages are vague because marketing writes for **nobody**. The page has two readers — the **user** (practitioner who will live in the product) and the **buyer** (exec who signs) — and hedging both produces sentences the buyer cannot disagree with and the user cannot picture. "Safe-middle copy." Then the approval cycle finishes the job: every reviewer adds a hedge until the headline only asserts the company exists.

Fix: the homepage is not a billboard — it's the first stop on a multi-stop trip. Hero for the buyer (outcome + mechanism). Next section for the user (the specific motion inside the product). Both find their evidence on the same page in the order they care about it.

Test: if your competitor could swap their logo onto your homepage and ship it, the page is written for nobody.

---

### Process Note for Next Session

Brian provided a new writing-style profile XML. First-pass draft missed several anchors (em dashes leaked in, acronyms not spelled out, no signature `Look,` opener, no parenthetical asides). Second-pass audit against the full profile caught and fixed. **Pattern to remember:** when working from a voice profile, do a full pass against `hard_refusals`, `phrase_bank avoid`, and `signature_tells` before declaring a draft done — those are the lists that catch the small voice violations.

---

### Current Wiki State

**15 concepts** (7 origin: self) | **18 entities** | **12 sources** | **5 articles**

**Skills (10):** unchanged this session.

---

### Next Session Priorities

- Consider building a `/build voice-file` skill (Hassid 100-question interview)
- Build gold-standard example output for `competitive-profile`
- Run `/lint` for a full vault health check
- Tool name-drops from Hassid (Wispr Flow, Cowork, Obsidian) — decide if any deserve entity pages
