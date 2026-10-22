---
type: reference
title: Jakub Krehel — interface agent skills
purpose: Upstream better-* agent skills for interface polish and review.
status: curated
tags: [ui, design, typography, accessibility, layout, colors, writing]
sources:
  - url: https://skills.sh/jakubkrehel/skills
    label: skills.sh listing (jakubf.skills)
  - url: https://github.com/jakubkrehel/skills
    label: GitHub jakubkrehel/skills
  - url: https://jakubf.dev/
    label: Author site
  - url: https://interfaces.dev/
    label: Interfaces magazine
---

# Jakub Krehel — interface agent skills

## When to use

- UI polish or interface review beyond the local make-interfaces quick reference. Load this entry, then fetch specific upstream skill docs from [GitHub](https://github.com/jakubkrehel/skills) on demand.

Listed in [UI Components catalog](../components/).

Open-source agent skill suite for polished product UI: `better-ui`, `better-typography`, `better-colors`, `better-accessibility`, `better-layout`, `better-writing`, `better-interface` (orchestrator), plus verb skills `interface-review`, `variant`, `break`, `explain-interface`.

## Install upstream (humans experimenting)

```bash
npx skills add jakubkrehel/skills
```

**Not** the default. We curate; we don't bulk-register.

## Overlap with local work

The design catalog entry is [`skills/make-interfaces-feel-better.md`](../../skills/make-interfaces-feel-better.md) (points at upstream [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) / [jakubf.dev article](https://jakubf.dev/)). Load that skill for UI polish and interface review. This reference covers the broader `better-*` suite and when to pull domain depth (colors, a11y, writing, layout) without registering every `better-*` into the catalog.

## Astra rule

Prefer one thin local router that points here over copying all 16 `SKILL.md` files into a project's `skills/` folder.

## Security review (2026-09-05)

Reviewed upstream commit `267330e1adfc66a718fb65fa6918c1f06d0a689e`. **Verdict:** pass-with-notes for reference use.

- Documentation-only (no scripts/executables in the reviewed tree).
- `explain-interface` documents unpinned `npx chrome-devtools-mcp@latest` and may curl user URLs — treat as agent capability risk if that skill is ever invoked, not as malware in-repo.
- `break` / `variant` write local temp harnesses when user-invoked.

**Policy:** reference-only by default; do not bulk-register; re-check on upstream bumps.
