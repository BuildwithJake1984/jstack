
---
title: Figma — collaborative design and design systems
kind: reference
status: curated
tags: [tools, design, design-system, variables, tokens, components, collaboration, dev-mode]
sources:
  - url: https://www.figma.com/
    label: Figma
  - url: https://www.figma.com/design-systems/
    label: Figma design systems
  - url: https://www.figma.com/dev-mode/
    label: Figma Dev Mode
---

# Figma — collaborative design and design systems

[Figma](https://www.figma.com/) markets a **collaborative canvas** for turning ideas into apps, websites, and products, with separate emphasis on **design tools** and **build/dev tools** that extend toward production. Figma also promotes an in-product **agent** for tasks such as adding motion, documenting design systems, and implementing feedback (see Figma homepage).

For **design systems**, Figma describes reusable **components**, **tokens**, and **libraries** as a shared foundation; **variables** for values such as color and typography that can switch across contexts (for example light and dark mode) and update linked designs when values change; and **slots** for flexible component instances without breaking the system ([design systems](https://www.figma.com/design-systems/)).

## Capabilities

- **UI design and prototyping** — Core Figma Design workflows for product and marketing UI (Figma homepage).
- **Published libraries** — Share components, styles, and variables across files and teams (design-systems page).
- **Variables** — Reusable structured values; design-systems and Dev Mode docs describe using variables for implementation-oriented handoff.
- **Dev Mode** — Dedicated developer view to **inspect** components, properties, and layer data; **compare changes** over time; link **dev resources** (for example GitHub, Jira, Storybook); and use features such as **focus view** and component playgrounds ([Dev Mode](https://www.figma.com/dev-mode/)).
- **Design–code connections (as marketed by Figma)** — **Code Connect** to map design components to production components; **Figma MCP server** to bring design context into IDEs/agents; **code syntax on variables** in Dev Mode inspection; optional **write to canvas** from agents (all described on Dev Mode / design-systems pages—confirm plan and admin settings).
- **Consistency tooling** — Design-systems page describes finding and fixing inconsistencies against libraries and using system context in Figma Make.

## Access and pricing

Figma sells multiple products and seat types (for example Design and Dev). **Verify current plans and pricing at [figma.com](https://www.figma.com/)** before recommending a subscription. Dev Mode, MCP, and Code Connect availability can depend on plan and organization settings.

## Use notes

Jake uses Figma especially for **setting up a design system** and a **token library** for colors and typography—foundations that downstream tools (including Paper and code) can align to. He reaches for it when he is doing **more advanced design** work that benefits from deep component, variable, and systems tooling.

When tokens live in Figma variables, keep naming and tiers documented so agents and developers map them consistently to CSS custom properties or Tailwind theme extensions.

## Jake's take

<!-- Jake's input goes here -->

## Sources

Pages checked for this reference (2026-10-22):

- [https://www.figma.com/](https://www.figma.com/) — product positioning, design vs build tools, agent features
- [https://www.figma.com/design-systems/](https://www.figma.com/design-systems/) — components, tokens, variables, slots, libraries, Code Connect, MCP, Figma Make, Dev Mode handoff
- [https://www.figma.com/dev-mode/](https://www.figma.com/dev-mode/) — Dev Mode inspection, MCP, Code Connect, variables in Dev Mode, statuses, compare changes, code-to-canvas
