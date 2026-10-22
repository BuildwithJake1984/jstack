
---
title: DESIGN.md generators, catalogs, and UI references
kind: link-digest
status: curated
tags: [design, design-md, design-systems, agents, inspiration, mcp, ui-reference]
sources:
  - url: https://www.typeui.sh/
    label: TypeUI
  - url: https://designmd.me/
    label: DesignMD
  - url: https://www.designmd.supply/
    label: DESIGN.md Supply
  - url: https://styles.refero.design/
    label: Refero Styles
  - url: https://collectui.com/
    label: CollectUI
  - url: https://designmd-store.com/
    label: Design.md Store
  - url: https://www.niblet.com/
    label: Niblet
  - url: https://open-design.ai/
    label: OpenDesign
  - url: https://www.aura.build/
    label: Aura
  - url: https://neuform.ai/
    label: Neuform
  - url: https://design-md.hyperbrowser.ai/
    label: Hyperbrowser DESIGNMD
---

# DESIGN.md generators, catalogs, and UI references

A curated starting point for giving AI coding agents stronger visual direction. Some entries generate or distribute structured `DESIGN.md` files; others provide real interface references that help people and agents study proven patterns.

A `DESIGN.md` file is portable design context: colors, typography, spacing, radii, components, interaction guidance, and other visual rules expressed in Markdown so coding agents can apply them consistently.

## Directory

| Resource | Type | Description | Access notes |
| --- | --- | --- | --- |
| [TypeUI](https://www.typeui.sh/) | Agent design layer + MCP | Gives Codex and other coding agents curated design skills, UI and animation prompts, brand kits, reusable design systems, and UI/UX audits through MCP. It also offers a separate privacy-focused website analytics product. | **Paid:** Creative is currently $30/month; commercial and client work allowed. |
| [DesignMD](https://designmd.me/) | Website-to-DESIGN.md generator | Crawls a public website and extracts its design system into a structured `DESIGN.md`, with optional live HTML preview and one-click Figma import. It can also compare two extracted design systems. | **Credit-based:** 4 free credits initially; generation starts at 4 credits. One-time credit packs begin at $5 and do not expire. |
| [OpenDesign](https://open-design.ai/) | Local AI design workspace | Connects Codex and other local coding agents to a complete design workflow for prototypes, websites, dashboards, slides, images, and HTML video. It supports portable `DESIGN.md` systems, templates, skills, local files, and Figma exports. | **Free and open source:** Apache-2.0; runs locally with BYOK, so model-provider usage costs remain separate. |
| [Aura](https://www.aura.build/) | AI website builder + DESIGN.md library | Creates landing pages from prompts and templates, converts live pages or references into reusable `DESIGN.md` systems, and applies those systems across generated pages. Its catalog currently includes thousands of templates and reusable design directions. | **Freemium:** free account/start; advanced generation, private libraries, hosting, CMS, and exports may require a paid plan. |
| [Neuform](https://neuform.ai/) | HTML template generator + living DESIGN.md | Generates visually ambitious landing pages and app sections, exposes reusable design-system notes and `DESIGN.md` source, and lets builders remix templates into new outputs with motion, WebGL, and Three.js-oriented directions. | **Freemium:** public templates are free to browse; private generation and source/export capacity are paid-tier features. |
| [Hyperbrowser DESIGNMD](https://design-md.hyperbrowser.ai/) | Lightweight website-to-DESIGN.md extractor | Paste a website URL to extract colors, typography, spacing, components, and design tokens into Google’s open `DESIGN.md` format. Results are stored in the local browser rather than uploaded to a separate DESIGNMD account. | **API-key based:** requires a Hyperbrowser API key; Hyperbrowser offers a free credit allowance and usage-based paid capacity. |
| [DESIGN.md Supply](https://www.designmd.supply/) | Generated style-guide catalog | Uses public-domain website data, screenshots, live markup, and Context.dev to produce Google-style `DESIGN.md` documents for well-known brands. Useful for quickly studying how recognizable visual systems are expressed for an agent. | **Free/open-source entry point** according to the site; verify each generated reference before production use. |
| [Refero Styles](https://styles.refero.design/) | DESIGN.md example library | Searchable beta catalog of 2,000+ AI-readable design systems derived from leading product websites. Each entry exposes colors, typography, spacing, components, and agent-ready design context. | **Free to browse**; Refero connection features may have separate account or plan requirements. |
| [CollectUI](https://collectui.com/) | Daily UI inspiration gallery | Human-facing stream of curated websites and interfaces, useful for discovering layouts, interaction patterns, component treatments, and visual directions before translating them into original project work. | **Free to browse**; inspiration only. |
| [Design.md Store](https://designmd-store.com/) | Ready-made DESIGN.md marketplace | Library of downloadable, production-oriented `DESIGN.md` files organized by product category and recognizable brand style, with live previews and supporting articles about using design context with coding agents. | **Free tier + Pro:** 51+ files are currently advertised as free; optional Pro subscription exists. |
| [Niblet](https://www.niblet.com/) | Real-product UI reference library + MCP | Searchable collection of 65,000+ real mobile and web screens organized by apps, journeys, packs, and interface elements. Coding agents can access the same references through its API or remote MCP; a self-hosted edition is Apache-2.0 licensed. | **Free to browse**; agent connection and hosting options vary. |

## Best use by task

| Need | Start with |
| --- | --- |
| Extract the visual system from a specific live website | DesignMD, Hyperbrowser DESIGNMD, Aura |
| Browse ready-made agent-readable design systems | Refero Styles, Design.md Store, DESIGN.md Supply |
| Give Codex reusable design skills and prompts through MCP | TypeUI |
| Run a local, open-source design workspace around Codex | OpenDesign |
| Generate and remix a polished landing page from a living design system | Aura, Neuform |
| Ground a new screen in real shipped product patterns | Niblet |
| Explore broad visual ideas manually | CollectUI |
| Compare two websites’ design-system decisions | DesignMD |

## Usage guidance

- Treat extracted or brand-inspired files as references, not permission to impersonate a brand or copy its protected assets.
- Validate generated tokens against the live source before treating them as exact.
- Adapt patterns to the target product’s own brand, accessibility requirements, content, and user workflows.
- Prefer one coherent project-level `DESIGN.md` over combining several unrelated brand systems.
- Record the source and retrieval date when a generated design file becomes part of a client or the project project.


