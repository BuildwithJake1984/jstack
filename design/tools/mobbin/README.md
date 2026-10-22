
---
title: Mobbin — real-product UI and UX research library
kind: reference
status: curated
tags: [tools, design, ux, research, patterns, flows, mcp, inspiration]
sources:
  - url: https://mobbin.com/
    label: Mobbin
  - url: https://mobbin.com/mcp.md
    label: Mobbin MCP guide
  - url: https://mobbin.com/pricing.md
    label: Mobbin pricing (machine-readable)
---

# Mobbin — real-product UI and UX research library

[Mobbin](https://mobbin.com/) is a searchable library of **real mobile apps, web apps, and websites**. Designers, developers, and agents use it to study how shipped products handle individual screens, UI patterns, website sections, and **multi-step flows** (onboarding, checkout, account setup, subscriptions, and similar).

Research spans named products and categories. Mobbin states that **new content is added weekly**. On eligible plans, references can be saved to collections and copied into Figma.

## Capabilities

- **Screens** — search mobile and web UI states (login, paywalls, empty states, navigation, forms, and more).
- **Flows** — ordered, multi-step journeys where sequence matters.
- **Website sections** — heroes, pricing, testimonials, navigation, footers, and related layout patterns.
- **Mobbin MCP** — compatible AI tools search the library in natural language and can return screen images and links to Mobbin pages. Endpoint: `https://api.mobbin.com/mcp` (OAuth; documented tools include `search_screens`, `search_flows`, and `search_sections`). See the [MCP guide](https://mobbin.com/mcp.md).
- **REST API** — available on Team and Enterprise plans for programmatic search (see [Mobbin API docs](https://docs.mobbin.com/api/quickstart)).

Use Mobbin as **evidence of what shipped products do**, not proof that a pattern improved a metric. Compare multiple examples and adapt to your brand, system, and accessibility requirements.

## Access and pricing

Mobbin publishes **Free, Pro, Team, and Enterprise** tiers. As summarized in [Mobbin pricing](https://mobbin.com/pricing.md) (verify freshness on the canonical pricing page):

| Plan | Highlights |
| --- | --- |
| Free | Limited library access; MCP not included |
| Pro | Full library, flows, search; **MCP included** for individuals |
| Team | Collaboration, shared collections; **REST API** included |
| Enterprise | Advanced security and administration; MCP and API included |

MCP access requires **Pro, Team, or Enterprise**. Confirm current prices and features at [mobbin.com/pricing](https://mobbin.com/pricing) before purchase.

## Use notes

Jake uses Mobbin to **research UX/UI best practices** from real products. When building screen designs, he often has an AI agent **reference Mobbin through MCP** to compare patterns before committing to a layout.

Preserve product names and Mobbin URLs when citing examples in specs or PRs so others can inspect the source.

## Jake's take

<!-- Jake's input goes here -->
