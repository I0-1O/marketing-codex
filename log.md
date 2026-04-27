# Log

Reverse-chronological activity log. Appended by `/ingest`, `/lint`, `/build`, and session end.

## 2026-04-27
- **ingested**: https://www.linkedin.com/posts/hattiethepmm_prompting-is-the-weakest-way-to-use-claude-share-7450096258104561664-YR_P/ + infographic → wiki/sources/hattie-pmm-claude-power-users.md
- **created**: wiki/entities/hattie-the-pmm.md — product marketing coach; Visible & Valued PMM Challenge; productmarketers.com
- **created**: wiki/concepts/pmm-ai-workflow-architecture.md — system-level Claude setup for PMMs; four leverage layers (Projects, Skills, Cowork, Connectors); power users build systems, not prompts
- **updated**: wiki/concepts/ai-agent-skills-for-marketing.md — added related link to pmm-ai-workflow-architecture
- **updated**: wiki/index.md — added source, entity, concept; added two previously unindexed tutorials (How to Build Your PMM Brain, Bootstrap)
- **session**: single ingest (Hattie the PMM); pmm-ai-workflow-architecture added as new concept (system layers beat prompting); vault at 13 concepts / 17 entities / 10 sources

## 2026-04-22
- **ingested**: https://marketingthatmatters.substack.com/p/marketing-that-matters-035-stop-turning → wiki/sources/stop-turning-antithesis-angus.md
- **created**: wiki/concepts/antithesis-positioning-pattern.md — "It's not X, it's Y" as AI tell and positioning shortcut; mechanism, why AI reaches for it, the fix
- **created**: wiki/entities/jeff-angus.md — author, Marketing That Matters newsletter
- **updated**: wiki/concepts/ai-voice-tells-in-marketing-copy.md — added 7th tell (antithesis construction), updated checklist, added sources and related concept links
- **updated**: wiki/index.md — added source, concept, entity; corrected ai-voice-tells entry to "seven patterns"
- **session**: single ingest (Angus); antithesis pattern catalogued as 7th AI voice tell; 3 new pages, 1 updated concept; vault at 12 concepts / 16 entities / 9 sources

## 2026-04-14
- **lint**: 1 dead link (hash anchor syntax in stop-building-ugly-slides.md:74) — fixed; 0 orphans; 0 frontmatter gaps
- **session**: built out full competitive intel system — 3 ingests, 3 concepts, 3 entities, 1 new skill (competitive-profile), 2 updated skills (competitive-brief, battle-card), 2 new templates, 1 tutorial (competitive-intel-playbook); registered slash commands in ~/.claude/commands/
- **skill**: updated skills/competitive-brief.md — added Step 0 (check for profile), buyer voice sourcing priority, claim validation, template reference, artifact chain; updated output format
- **skill**: updated skills/battle-card.md — added buyer voice sourcing, topics-to-avoid step, trigger-based update cadence, competitive-profile as preferred predecessor; updated output sections
- **template**: updated templates/battle-card-template.md — added Topics to Avoid section; tightened instructional language; added last-updated note
- **template**: created templates/competitive-brief-template.md — 7-section template: competitor overview, positioning, strengths, weaknesses (sourced), differentiation, talk track, research gaps
- **tutorial**: created tutorials/competitive-intel-playbook/competitive-intel-playbook.md — four-artifact system, build chain rationale, per-artifact guidance, research source priority table, trigger-based update cadence, Claude Code scheduling examples
- **updated**: wiki/index.md — added competitive-intel-playbook tutorial
- **skill**: created skills/competitive-profile.md — deep pre-battlecard research artifact; competitor + your product inputs; resolves or approximates master messaging doc; 11-section output; artifact chain: messaging doc → competitive profile → competitive brief → battle card
- **template**: created templates/competitive-profile-template.md — 11 sections: quick verdict, competitor snapshot, positioning, capability comparison, buyer profile comparison, where they win, where you win, vulnerabilities, their narrative against you, counter-narrative, research gaps
- **updated**: wiki/index.md — added competitive-profile skill
- **ingested**: https://medium.com/@tdoherty_96508/the-30-minute-battlecard-58fe3a74b1da → wiki/sources/30-minute-battlecard-doherty.md
- **created**: wiki/concepts/buyer-voice-intelligence.md — mining call recordings for authentic buyer language; four intelligence categories; sources and limitations
- **created**: wiki/entities/thomas-e-doherty.md — PMM author, AI-accelerated GTM, three-phase battlecard methodology
- **created**: wiki/entities/g2.md — B2B review platform; PMM use cases for competitive research and buyer vocabulary
- **updated**: wiki/concepts/battle-card.md — added continuous intelligence framing, Doherty example
- **updated**: wiki/concepts/objection-handling.md — added buyer voice as sourcing method
- **updated**: wiki/index.md — added source, concept, 2 entities
- **ingested**: https://www.momentum.io/prompts/competitive-research-battlecard-creation → wiki/sources/competitive-research-battlecard-creation-momentum.md
- **updated**: wiki/entities/momentum.md — added Salesforce acquisition note, second source link
- **updated**: wiki/concepts/battle-card.md — added v2 prompt to Examples section
- **updated**: wiki/index.md — added second source entry
- **ingested**: https://www.momentum.io/prompts/competitor-research-battlecard → wiki/sources/competitor-research-battlecard-momentum.md
- **created**: wiki/entities/momentum.md — Salesforce-native AI sales platform, prompt library source
- **created**: wiki/concepts/battle-card.md — one-page sales reference; battle card vs. competitive brief distinction
- **created**: wiki/concepts/objection-handling.md — anticipating/structuring buyer resistance rebuttals; upstream of battle cards
- **updated**: wiki/index.md — added source, 2 concepts, 1 entity
- **skill**: created skills/launch-artifact.md — GTM campaign brief builder; synthesized from SKILL_launch_artifact.md (funnel model, audience sequencing, messaging shift, channel rationale), K2 GTM Brief (doc structure: objective, market context, compelling events, ICP, personas, internal/external positioning, messaging pillars, channel matrix, content plan, timeline, metrics, appendices), Corey Haines launch-strategy (ORB channel framework, five-phase launch progression); generic/product-agnostic
- **template**: created templates/launch-artifact-template.md — full output format for launch-artifact skill; covers GTM strategy, ICP, personas, audience sequencing, positioning, funnel-stage messaging, ORB channel matrix, content plan, timeline, metrics, and three appendices (market evidence, product primer, objection handling)
- **updated**: wiki/index.md — added [[launch-artifact]] to Skills section

## 2026-04-13
- **updated**: tutorials/building your own codex/Bootstrap.md — added tutorials/ and articles/ to directory scaffold; added article frontmatter schema; updated all 8 skills descriptions; updated session management to reference /session-close; added /session-close slash command definition; added Bootstrap + README drift checks
- **updated**: skills/session-close.md — added items 8 (Bootstrap drift) and 9 (README drift) to checklist
- **created**: skills/session-close.md — end-of-session checklist skill; covers index sync, wikilinks, hot.md, log, raw folder; referenced from CLAUDE.md Session Management section
- **updated**: CLAUDE.md — Session Management section now references session-close skill
- **updated**: wiki/index.md — added session-close; added 4 previously missing skills (competitive-brief, analyst-prep, battle-card, content-brief)
- **updated**: skills/messaging-framework.md — major rewrite from SKILL_messaging_framework.md + Master_Messaging_Document_Guide.md; merged skill + guide into single process; removed Orion-specific references, time-constrained shortcuts section; added ICP section, "why now" input, pillar construction rules, common mistakes, competitive framing rules; linked [[pmm-writing-voice]], [[master-messaging-document]], [[problem-first-messaging]], [[benefit-ladder]]
- **updated**: templates/messaging-framework-template.md — major upgrade from Master_Messaging_Template.md; added ICP table, personas with "what they'd do instead" column, per-audience value props section, partner messaging section, proof points with sourcing notes; pillar structure now full pain→use cases→features→VP→outcomes sequence
- **created**: skills/pmm-writing-voice.md — ported from SKILL_writing_style.md; reformatted to skill schema; trimmed for modern LLMs; cross-referenced [[ai-voice-tells-in-marketing-copy]], [[marketing-voice-and-pov]], [[benefit-ladder]]; removed redundant before/after examples and competitive claims block; kept em dash rule, comma chain rule, banned word list, and editing checklist
- **updated**: wiki/index.md — added [[pmm-writing-voice]] to Skills section
- **created**: tutorials/stop-building-ugly-slides/stop-building-ugly-slides.md — primer linking to PPTX deck (Dropbox), cheat sheet PDF (Dropbox), and AI skill
- **created**: tutorials/stop-building-ugly-slides/cheat-sheet.md — vault-native cheat sheet with updated Dropbox links, wikilinked to skill and primer
- **created**: skills/slide-deck.md — slide deck builder skill; ported from external file with encoding fixes, schema frontmatter, genericized examples, added Inputs/Process/Example Usage sections
- **updated**: wiki/index.md — added Skills section; added [[slide-deck]] entry

## 2026-04-12 (session 2, misc 2)
- **updated**: CLAUDE.md — documented flat-until-needed skill organization convention; /build resolution order

## 2026-04-12 (session 2, misc)
- **updated**: README.md — added articles/ folder, raw/ vs articles/ distinction, corrected directory name (pmm-brain → marketing-codex), added article: git convention

## 2026-04-12 (session 2, ingest 5)
- **ingested**: articles/technical-thinkers-guide-to-messaging.md (Brian Rieb, own article)
- **created**: wiki/sources/technical-thinkers-guide-to-messaging.md
- **created**: wiki/concepts/master-messaging-document.md (origin: self)
- **created**: wiki/concepts/problem-first-messaging.md (origin: self)
- **updated**: wiki/entities/brian-rieb.md (added technical background, messaging philosophy section)
- **updated**: wiki/index.md

## 2026-04-12 (session 2, ingest 4)
- **ingested**: articles/slides-dont-talk.md (Brian Rieb, own article)
- **created**: wiki/sources/slides-dont-talk.md
- **created**: wiki/concepts/presentation-as-story.md (origin: self)
- **created**: wiki/concepts/leave-behind-fallacy.md (origin: self)
- **created**: wiki/entities/garr-reynolds.md
- **created**: wiki/entities/edward-tufte.md
- **created**: wiki/entities/nancy-duarte.md
- **created**: wiki/entities/barbara-minto.md
- **updated**: wiki/entities/brian-rieb.md (added presentation philosophy section)
- **updated**: wiki/index.md

## 2026-04-12 (session 2, ingest 3)
- **ingested**: articles/benefit-ladder-copy-lands-one-tier-too-low.md (Brian Rieb, own article)
- **created**: wiki/sources/benefit-ladder-copy-lands-one-tier-too-low.md
- **created**: wiki/concepts/benefit-ladder.md (origin: self)
- **created**: wiki/entities/april-dunford.md
- **created**: wiki/entities/clayton-christensen.md
- **created**: wiki/entities/matthew-dixon-brent-adamson.md
- **created**: wiki/entities/slack.md
- **updated**: wiki/entities/brian-rieb.md (added PMM frameworks section)
- **updated**: wiki/index.md

## 2026-04-12 (session 2, ingest 2)
- **ingested**: articles/writing-for-humans-killing-ai-voice.md (Brian Rieb, own article)
- **created**: wiki/sources/writing-for-humans-killing-ai-voice.md (synopsis; links to full article)
- **created**: wiki/entities/brian-rieb.md
- **created**: wiki/entities/mailchimp.md
- **created**: wiki/entities/37signals.md
- **created**: wiki/concepts/ai-voice-tells-in-marketing-copy.md (origin: self)
- **created**: wiki/concepts/marketing-voice-and-pov.md (origin: self)
- **updated**: wiki/index.md (added 6 new pages)

## 2026-04-12 (session 2)
- **updated**: CLAUDE.md — added articles/ folder, article frontmatter schema, origin field on concepts, updated /ingest to handle own articles vs external sources
- **created**: articles/ folder with _template.md

## 2026-04-12
- **ingested**: https://github.com/coreyhaines31/marketingskills → wiki/sources/marketingskills-coreyhaines31.md
- **created**: wiki/entities/corey-haines.md
- **created**: wiki/concepts/ai-agent-skills-for-marketing.md
- **updated**: wiki/index.md (added first 3 pages)

## 2026-04-10
- **session**: Vault scaffolded. Created directory structure, CLAUDE.md, index.md, hot.md, starter skills (messaging-framework, competitive-brief, analyst-prep, battle-card, content-brief), starter templates (battle-card, one-pager, messaging-framework), and .gitignore. Git initialized. No content ingested yet.
