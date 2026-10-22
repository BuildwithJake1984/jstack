
---
title: Keyline Icons
kind: reference
status: curated
tags: [ui, icons, shadcn, svg, react, mit]
sources:
  - url: https://keylineicons.com/
    label: Keyline Icons site
  - url: https://keylineicons.com/install
    label: Install guide
  - url: https://github.com/keyline-icons/keyline-icons
    label: GitHub (MIT)
---

Listed in [UI Components catalog](../components/) under Icons.

# Keyline Icons

Free **MIT** icon set built for **shadcn/ui**: **585** drawings on one **24×24** grid with **2px** keylines. Each icon can ship as stroke / duotone / fill and rounded / sharp (~2,994 SVG files). Commercial and client use allowed; no subscription.

## When to use

- Choosing or reviewing icons for client sites or product UI when a consistent shadcn-aligned set is wanted.
- Prefer copy-one SVG/JSX from the browser for a few icons; `@keyline-icons/react` or CLI when you need many.
- Also on Iconify as `keyline-icons` (Vue/Svelte/etc.).

## How to load

| Path | Notes |
| --- | --- |
| Browser copy | [keylineicons.com](https://keylineicons.com/) — SVG or JSX, no install |
| React package | `npm i @keyline-icons/react` (`/duotone`, `/fill` entry points) |
| CLI one-off | `npx @keyline-icons/cli add <name>` |
| Repo SVGs | [github.com/keyline-icons/keyline-icons](https://github.com/keyline-icons/keyline-icons) `icons/` |

## Notes

- **Reference only** — do not register as an agent skill.
- Colors via `currentColor`; matches shadcn `size-4` defaults.
- The project's AGENTS.md or component inventory wins (e.g. if it names Lucide as the default); use Keyline when the default lacks a fit or a shadcn-aligned look is intentional.
- Figma plugin / community listing available; set is AI-crafted but MIT-licensed for product use.


