
---
type: tool
title: Figma — collaborative design and design systems
purpose: Build and maintain design systems, variables, and dev-ready UI specs.
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

## When to use

- Setting up or extending a design system, token library, or component library.
- Advanced product UI work that needs variables, variants, and Dev Mode handoff.
- Aligning design foundations before Paper or code implementation.

## What it is

[Figma](https://www.figma.com/) is a **collaborative interface design** product for apps, websites, and design systems. Figma separates **design** workflows from **build/dev** tooling (including **Dev Mode**) and publishes guidance for **design systems** at [figma.com/design-systems](https://www.figma.com/design-systems/).

## What it can do

### UI design and prototyping

Figma Design supports frames, components, variants, auto layout, and prototyping for product and marketing UI. Teams co-edit in shared files with comments and version history (see Figma product pages).

### Design systems, components, and libraries

Figma’s design-systems material describes **reusable components**, **styles**, **libraries**, and **slots** for flexible instances. **Published libraries** let teams share foundations across files and projects so product UI stays consistent.

### Variables and tokens

**Variables** store structured values (color, typography, spacing, and related modes such as light/dark). When variables change, linked designs update—supporting token-tier thinking that maps to CSS or Tailwind in code ([design systems](https://www.figma.com/design-systems/)).

### Dev Mode

[Dev Mode](https://www.figma.com/dev-mode/) is a developer-focused view to **inspect** components and properties, **compare** design changes, attach **dev resources** (for example GitHub, Jira, Storybook), and use inspection aids such as focus views and component playgrounds. Availability depends on plan and org settings.

### Design–code and agent connections

Figma documents **Code Connect** (mapping design components to code), a **Figma MCP server** for bringing design context into IDEs and agents, and variable **code syntax** in Dev Mode. Agent and MCP features require confirming current plan, admin, and product documentation before relying on them in production workflows.

## How it fits Jake's stack

Jake uses Figma for **design systems**, **token libraries** (colors, typography), and **more advanced design** work where deep components, variables, and systems tooling matter. Those foundations feed [Paper](paper.md) and front-end code; keep variable naming documented so agents and developers map tiers consistently to theme files in [Next.js](../development/nextjs.md) repos.

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [figma.com](https://www.figma.com/) (blog and product updates), [Dev Mode](https://www.figma.com/dev-mode/) and help-center release notes, and [@figma on X](https://x.com/figma). Link [this file](figma.md) when an issue mentions Figma.

## Sources

Pages checked for this reference (2026-10-22):

- [https://www.figma.com/](https://www.figma.com/) — product positioning, design vs build tools
- [https://www.figma.com/design-systems/](https://www.figma.com/design-systems/) — components, tokens, variables, libraries, Code Connect, MCP
- [https://www.figma.com/dev-mode/](https://www.figma.com/dev-mode/) — inspection, compare, dev resources, MCP, Code Connect
