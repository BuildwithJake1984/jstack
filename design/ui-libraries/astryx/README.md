
---
title: Astryx — Meta-grown agent-ready design system
kind: reference
status: curated
tags: [ui, components, design-system, react, stylex, themes, templates, cli, mcp, mit, free]
sources:
  - url: https://astryx.atmeta.com/
    label: Astryx documentation
  - url: https://github.com/facebook/astryx
    label: Astryx source repository and license
---

# Astryx

Astryx is a free, open-source design system that grew inside Meta over eight years. It is designed for both people and coding agents, with accessible React components, brand-level theming, production-ready templates, CLI tooling, and MCP support.

## Classification

- **Price:** Free.
- **License:** MIT.
- **Commercial use:** Allowed under the MIT license; retain the copyright and license notice when required by the license.
- **Status:** Beta.
- **Source:** [facebook/astryx](https://github.com/facebook/astryx).

## What it includes

- 170+ accessible, themeable components according to the current documentation.
- React 19+ and TypeScript support.
- Seven ready-made themes plus CSS custom-property theming.
- Dark mode and built-in spacing conventions.
- Production-ready page templates and interaction patterns.
- CLI commands for scaffolding, browsing components and templates, generating themes, and agent-ready documentation.
- MCP integration for agent workflows.
- A `swizzle` path for ejecting component source into a project when deeper ownership is needed.

## Technical fit

Astryx authors its internal styles with StyleX, but consumers can override components with Tailwind, CSS Modules, or plain CSS. Basic installation does not require adopting a StyleX build plugin.

This makes Astryx useful when the project needs a broad, cohesive system rather than a single copy-paste effect. It is especially worth checking for dashboards, forms, tables, navigation, commerce flows, and other component-heavy products.

## Adoption notes

- Treat Astryx as a **supplemental** library; shadcn/ui remains the default starting point in this catalog.
- It requires React 19 or newer.
- Because Astryx is currently beta, verify component APIs and package versions before production adoption.
- Review generated or installed code for accessibility, bundle impact, styling conflicts, and fit with the target project's existing design language.
- Prefer selective adoption over mixing multiple complete design systems across the same interface.

## Quick links

- [Documentation and component browser](https://astryx.atmeta.com/)
- [GitHub repository](https://github.com/facebook/astryx)


