# Hot — Session Context Cache

> Rolling context cache. Stays under ~500 words. Updated at the end of each session.
> Not a full history — just enough to orient the next session.

---

## Last Updated: 2026-04-12

### What Was Built This Session

**Vault scaffolding decisions:**
- Added `articles/` folder for Brian's own writing — full text lives here, wiki holds synopsis + wikilinks back to article file
- Updated `CLAUDE.md`: articles/ in vault structure, article frontmatter schema (`published: false`, `url:`), `origin: self` field on concept pages, updated `/ingest` to branch on own article vs. external source
- Ingested Corey Haines' marketingskills GitHub repo as external reference source

**Four articles ingested (all Brian Rieb, unpublished):**
1. `writing-for-humans-killing-ai-voice` → concepts: `ai-voice-tells-in-marketing-copy`, `marketing-voice-and-pov`
2. `benefit-ladder-copy-lands-one-tier-too-low` → concept: `benefit-ladder`
3. `slides-dont-talk` → concepts: `presentation-as-story`, `leave-behind-fallacy`
4. `technical-thinkers-guide-to-messaging` → concepts: `master-messaging-document`, `problem-first-messaging`

### Current Wiki State

**8 concepts** (6 origin: self), **13 entities**, **5 sources**, **4 articles**

**Brian's PMM philosophy, as it emerges across the wiki:**
- Start with the customer's problem (`problem-first-messaging`)
- Climb to the business outcome (`benefit-ladder`)
- Build a three-pillar architecture around it (`master-messaging-document`)
- Present it as a story, not a document (`presentation-as-story`)
- Write it with a human voice and a point of view (`marketing-voice-and-pov`)

### Key Entities Created
- `brian-rieb` — vault owner, technical/PM background, writing + messaging + presentation philosophy documented
- `april-dunford`, `clayton-christensen`, `matthew-dixon-brent-adamson` — referenced frameworks
- `garr-reynolds`, `edward-tufte`, `nancy-duarte`, `barbara-minto` — presentation references
- `mailchimp`, `37signals`, `slack` — brand voice / positioning case studies

### Next Session Priorities (anticipated)
- Potentially more articles to ingest
- Start building skills that leverage the wiki (value prop writer, messaging doc builder, deck reviewer)
- Consider building a template for the master messaging document
