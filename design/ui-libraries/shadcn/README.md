
---
title: shadcn/ui — primary component foundation
kind: reference
status: curated
tags: [ui, components, shadcn, react, tailwind, radix, primary]
sources:
  - url: https://ui.shadcn.com/
    label: shadcn/ui
  - url: https://ui.shadcn.com/docs
    label: Docs
  - url: https://ui.shadcn.com/docs/components
    label: Components
  - url: https://reactnativereusables.com/
    label: React Native Reusables (mobile port)
---

Listed in [UI Components catalog](../components/) under **Primary**.

# shadcn/ui — primary component foundation

**Primary** place for UI components across your projects (web first). Composable, accessible React components with Tailwind + Radix primitives. Copy-into-repo ownership model (`npx shadcn@latest add …`) — not a black-box npm UI kit.

## When to use

- Default starting point for new web UI (client sites and product apps) before Amicro, Kinetics, or one-off patterns.
- Prefer existing project components / brand tokens when they already cover the need; otherwise reach for shadcn patterns and adapt.
- Pair with [Keyline Icons](../keyline-icons/) when an icon set is needed (built for shadcn defaults).
- Pair with [`skills/make-interfaces-feel-better`](../../skills/make-interfaces-feel-better/) for polish after structure is in place.

## Mobile (Expo / React Native)

Upstream shadcn/ui is **web (React DOM + Radix)**. For product mobile / Expo, use a shadcn-*shaped* port rather than importing web components:

| Option | Notes |
| --- | --- |
| [React Native Reusables](https://reactnativereusables.com/) | Closest shadcn ownership model on NativeWind — preferred when matching web shadcn |
| gluestack-ui | Universal web+native copy-paste; different API surface |

Do not treat ui.shadcn.com demos as drop-in RN code.

## How to load

1. Browse [ui.shadcn.com/docs/components](https://ui.shadcn.com/docs/components).
2. Add via CLI into the app’s component path (or copy the source).
3. Restyle with project tokens (brand / client tokens) — keep ownership of the files.

## Notes

- **Reference + primary default** — not registered as a operator skill; the catalog marks it primary so agents open here first.
- MIT / open copy-paste; respect project AGENTS and approved screen inventory before inventing new surfaces.
- The project's AGENTS.md or component inventory wins over this reference when they conflict.


