
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
    label: Mobbin product overview
  - url: https://mobbin.com/mcp.md
    label: Mobbin MCP guide
  - url: https://docs.mobbin.com/api/quickstart
    label: Mobbin API quick start
---

# Mobbin — real-product UI and UX research library

## When to use

- Researching UX patterns from real shipped products (not mock concepts).
- Having an agent search screens, flows, or site sections via Mobbin MCP.
- Comparing multiple products before locking a layout or flow.

## What it is

[Mobbin](https://mobbin.com/) is a **searchable library of real mobile apps, web apps, and websites**. Mobbin’s [product overview](https://mobbin.com/index.md) states that designers, developers, and agents use it to study how **shipped products** handle screens, UI patterns, website sections, and **multi-step flows** (onboarding, checkout, subscriptions, and similar). Mobbin publishes **weekly content updates** and supports **collections**; eligible plans can **copy references into Figma**.

## What it can do

### Screen research

Browse and search individual UI states—login, paywalls, empty states, navigation, forms, and comparable patterns—across a large catalog of production apps and sites.

### Flow research

Study **ordered multi-step journeys** where sequence matters (signup, purchase, activation). Flows complement single-screen research when you need to see how products connect steps.

### Website section research

Research marketing and product-site **sections** (heroes, pricing, testimonials, footers) as composition references separate from full app chrome.

### Search and collections

Mobbin describes search across apps, sites, on-screen text, patterns, and UI elements. Save references to **collections** for specs, critiques, or agent context ([overview](https://mobbin.com/index.md)).

### Mobbin MCP for agents

On **Pro, Team, and Enterprise** plans, compatible AI tools connect to `https://api.mobbin.com/mcp` (Streamable HTTP with **OAuth**). Documented read-only tools include **`search_screens`**, **`search_flows`**, and **`search_sections`** ([MCP guide](https://mobbin.com/mcp.md)). Published rate limit: **60 requests per 60 seconds per user**. Use results as **pattern evidence**, not proof of business outcomes.

### REST API (Team and Enterprise)

Team and Enterprise workspaces can use Mobbin’s **REST API** with bearer keys ([API quick start](https://docs.mobbin.com/api/quickstart)) for programmatic access outside MCP.

## How it fits Jake's stack

Jake uses Mobbin to **research UX/UI best practices** from real products. When designing screens, he often has agents **reference Mobbin through MCP** to compare patterns before committing to a layout—then implements direction in [Paper](paper.md) or [Figma](figma.md). Preserve product names and Mobbin URLs in specs so others can verify sources. Confirm current plans on [mobbin.com/pricing](https://mobbin.com/pricing); **MCP is not on the Free tier** per Mobbin’s pricing material.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [mobbin.com](https://mobbin.com/), Mobbin’s blog/changelog when published, [docs.mobbin.com](https://docs.mobbin.com/), and [@mobbin on X](https://x.com/mobbin). Link [this file](mobbin.md) when an issue mentions Mobbin.

## Sources

Pages checked for this reference (2026-10-22):

- [https://mobbin.com/](https://mobbin.com/) — positioning and entry points
- [https://mobbin.com/index.md](https://mobbin.com/index.md) — research types, updates, Figma copy, MCP/API pointers
- [https://mobbin.com/mcp.md](https://mobbin.com/mcp.md) — MCP endpoint, OAuth, tools, rate limits
- [https://docs.mobbin.com/api/quickstart](https://docs.mobbin.com/api/quickstart) — REST API
