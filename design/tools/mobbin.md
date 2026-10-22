
---
type: tool
title: Mobbin — real-product UI and UX research library
purpose: Find how shipped apps handle screens, flows, and sections before you design.
status: curated
tags: [tools, design, ux, research, patterns, flows, mcp, inspiration]
sources:
  - url: https://mobbin.com/
    label: Mobbin
  - url: https://mobbin.com/index.md
    label: Mobbin product overview (machine-readable)
  - url: https://mobbin.com/mcp.md
    label: Mobbin MCP guide
  - url: https://mobbin.com/pricing.md
    label: Mobbin pricing (machine-readable)
---

# Mobbin — real-product UI and UX research library

## When to use

- Researching UX patterns from real shipped products (not mock concepts).
- Having an agent search screens, flows, or site sections via Mobbin MCP.
- Comparing multiple products before locking a layout or flow.

[Mobbin](https://mobbin.com/) is a **searchable library of real mobile apps, web apps, and websites**. Mobbin’s own overview states that designers, developers, and agents use it to see how **shipped products** handle screens, UI patterns, website sections, and **multi-step user flows** (for example onboarding, checkout, account setup, and subscription).

Mobbin publishes that **new content is added weekly** and that references can be **saved to collections** and **copied into Figma on eligible plans**.

## Capabilities

- **Screen research** — Individual mobile and web UI states (login, paywalls, empty states, navigation, forms, and similar).
- **Flow research** — Ordered multi-step journeys where sequence matters.
- **Website sections** — Heroes, pricing, testimonials, navigation, footers, and related composition patterns.
- **Search scope** — Mobbin describes search across apps, sites, screen text, patterns, and UI elements ([product overview](https://mobbin.com/index.md)).
- **Mobbin MCP** — On **Pro, Team, and Enterprise** plans, compatible AI tools can search in natural language and return screen images and links. Endpoint: `https://api.mobbin.com/mcp` (Streamable HTTP; **OAuth** sign-in on first connect). Documented read-only tools: **`search_screens`**, **`search_flows`**, **`search_sections`** ([MCP guide](https://mobbin.com/mcp.md)). Published rate limit: **60 requests per 60 seconds per user** (see MCP guide).
- **REST API** — **Team and Enterprise** plans; bearer API keys scoped to a workspace ([API quick start](https://docs.mobbin.com/api/quickstart)).

Use Mobbin as **evidence of what real products ship**, not proof that a pattern improved a metric. Compare multiple examples, keep source links, and adapt to your brand, system, and accessibility requirements (Mobbin’s agent guidance aligns with this).

## Access and pricing

Mobbin offers **Free, Pro, Team, and Enterprise** tiers. Highlights from [Mobbin pricing](https://mobbin.com/pricing.md) — **confirm on [mobbin.com/pricing](https://mobbin.com/pricing) before purchase** (plans and prices change):

| Plan | Highlights |
| --- | --- |
| Free | Limited library access; **MCP not included** |
| Pro | Full library, flows, search; **MCP included** (individual) |
| Team | Collaboration, shared collections; **REST API included**; MCP included |
| Enterprise | Advanced security/administration; MCP and API included |

Free browsing is available at [mobbin.com/explore](https://mobbin.com/explore) with limited access; paid plans unlock the full library, search, flows, animations, and related features per Mobbin’s overview.

## Where it fits in Jake's stack and JStack

Jake uses Mobbin to **research UX/UI best practices** from real products. When building screen designs, he often has an AI agent **reference Mobbin through MCP** to compare patterns before committing to a layout.

Preserve product names and Mobbin URLs when citing examples in specs or PRs so others can inspect the source.

## Official links

- [Mobbin](https://mobbin.com/)
- [Mobbin on X](https://x.com/mobbin)

## News & Insights

Weekly external coverage: [`news-and-insights/README.md`](../../news-and-insights/README.md). When an issue mentions Mobbin, link to [this file](mobbin.md).

## Related

- [Figma](figma.md) — systems and specs after you pick patterns
- [Paper](paper.md) — canvas exploration with agents and MCP
- [Design tokens in a design system](../lessons/design-tokens.md) — keep research aligned with your token tiers

## Jake's take

<!-- Jake's input goes here -->

## Sources

Pages checked for this reference (2026-10-22):

- [https://mobbin.com/](https://mobbin.com/) — positioning and entry points
- [https://mobbin.com/index.md](https://mobbin.com/index.md) — research types, weekly updates, Figma copy, plans summary, MCP/API pointers
- [https://mobbin.com/mcp.md](https://mobbin.com/mcp.md) — MCP endpoint, OAuth, tools, rate limits, evidence limitations, client setup links
- [https://mobbin.com/pricing.md](https://mobbin.com/pricing.md) — plan capabilities (MCP, API, library access)
- [https://docs.mobbin.com/api/quickstart](https://docs.mobbin.com/api/quickstart) — REST API availability (linked from Mobbin overview)
