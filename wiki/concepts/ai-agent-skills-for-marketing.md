---
type: concept
title: "AI Agent Skills for Marketing"
created: "2026-04-12"
updated: "2026-04-12"
tags: [ai-agents, skills, workflows, claude-code, marketing-ops]
related: []
---

# AI Agent Skills for Marketing

## Definition

A pattern for packaging marketing knowledge and workflows as structured markdown files ("skills") that AI coding agents (Claude Code, Cursor, Windsurf, etc.) load as context. Each skill file defines the purpose, inputs, steps, and output format for a specific marketing task — enabling repeatable, high-quality AI-assisted execution.

## Why It Matters

- **Consistency**: A shared `product-marketing-context` skill anchors all other skills to your product, audience, and positioning — eliminating drift across tasks
- **Reusability**: Skills are version-controlled, portable, and shareable across teams or projects
- **Agent-agnostic**: Plain markdown works with any AI coding agent, not just one vendor
- **Specialization**: Each skill encodes expert-level workflow steps, not just prompts — the agent knows *how* to do the task, not just what to produce

## How It Works

1. A foundational `product-marketing-context` skill is created with core product/ICP/positioning info
2. Task-specific skills (e.g., `seo-audit`, `email-sequence`) reference the context skill first
3. The AI agent loads the relevant skill(s) and executes the defined workflow
4. Output follows the format defined in the skill file

## Skill Categories (from [[marketingskills-coreyhaines31]])

- **Conversion Optimization** — CRO for pages, signups, onboarding, forms, popups, paywalls
- **Content & Copy** — copywriting, editing, cold email, email sequences, social
- **SEO & Discovery** — on-page SEO, AI SEO, programmatic SEO, site architecture, schema
- **Paid & Distribution** — paid ads, ad creative
- **Measurement & Testing** — analytics tracking, A/B test setup
- **Retention** — churn prevention
- **Growth Engineering** — free tool strategy, referral programs
- **Strategy & Monetization** — marketing ideas, psychology, launch strategy, pricing
- **Sales & RevOps** — RevOps, sales enablement

## Examples

- This vault uses the same pattern: skills in `skills/`, templates in `templates/`, examples in `examples/`
- [[marketingskills-coreyhaines31]] — reference implementation by [[corey-haines]]

## Related Concepts

- [[pmm-ai-workflow-architecture]] — system-level AI setup for PMMs using Claude products; Skills layer is the Claude equivalent of this markdown pattern
