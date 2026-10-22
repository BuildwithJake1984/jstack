
---
title: Astra skills audit standard
kind: reference
status: curated
tags: [skills, astra, standards]
sources:
  - url: https://x.com/pvncher/status/2095991462416490862
    label: Eric Provencher — Rethinking skills and prompts for GPT-6 Astra
---

# Astra skills audit standard

A governing checklist for operator skills, always-on agent instructions (`AGENTS.md`), and agent profiles. Do not invent article text—read the source link above.

## Nine-point checklist

1. **Descriptions** — as short as possible; clear WHEN; no pick-me; no overlapping triggers
2. **Skill count** — fewer is better; catalog pressure truncates descriptions
3. **Progressive disclosure** — root `SKILL.md` is a minimal router; detail in supporting docs loaded on demand
4. **Specificity** — drop elaborate itineraries that overconstrain; keep durable principles and true constraints
5. **Multi-model** — don't overfit to one model
6. **Always-on (`AGENTS.md`)** — every line must earn its place on every task
7. **Testing / verification** — no redundant always-run-all-tests
8. **Decision boundaries** — ask-first only for real risk; avoid premature stops
9. **Persistence / completion** — define done; don't force early review stops unless needed

## How agents should use skills

1. Read the skill index for the relevant category (e.g. [`../../README.md`](../../README.md))—do not load the whole library.
2. Load **only** the one skill that matches the current task.
3. Follow progressive disclosure: the skill router first, then its linked `docs/` or reference files on demand.
4. If auditing or changing skills, check them against the nine points above.

## Gate

Maintainer review audits every skill add or change against these nine points. No merge without a pass—or an explicit maintainer exception.


