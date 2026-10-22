
---
title: Paper — connected canvas for design and agents
kind: reference
status: curated
tags: [tools, design, ui, agents, mcp, html, css, canvas, handoff]
sources:
  - url: https://paper.design/
    label: Paper
  - url: https://paper.design/docs/mcp
    label: Paper MCP documentation
---

# Paper — connected canvas for design and agents

[Paper](https://paper.design/) is a connected design canvas for teams shipping with agents. It positions design, code, agents, and data on a single space built on web standards so work can move between canvas and implementation without a separate translation layer.

Paper describes its canvas as **HTML/CSS-based**, which helps agents reason about layout and export designs toward real front-end code. The **Paper MCP server** lets compatible agents read and write open design files—for example generating layouts, pulling real content into frames, or turning a selected frame into code. Paper Desktop runs the MCP server in the background and supports one-click or manual setup for agents such as Cursor, Claude, Codex, VS Code, and others (see the [MCP docs](https://paper.design/docs/mcp)).

Product messaging also highlights syncing **design tokens and styles** between a codebase and the canvas, connecting external data sources into layers, and agent-assisted tasks such as responsive variants and consistency checks—while keeping the human on creative decisions.

## Capabilities

- **Canvas design** for apps, websites, and product screens on a web-technology foundation.
- **Agent connectivity** via MCP so IDEs and CLI agents can read and write the open file.
- **Design–code loop** — Paper emphasizes exporting and iterating in code because the canvas maps to HTML/CSS.
- **Real content** — workflows to pull data from connected tools (for example CMS or databases) into designs, and to push copy updates back toward code.
- **Tokens and themes** — documentation covers using tokens to style designs (see Paper docs).
- **Desktop app** — Paper Desktop unlocks the connected workflow and MCP/CLI integration described in official docs.

## Access and pricing

Paper offers web and desktop experiences; **verify current plans and pricing on [paper.design](https://paper.design/)** before recommending a purchase. MCP setup requires Paper Desktop for the supported agent workflows in the official documentation.

## Use notes

Jake uses Paper as his **primary UI/UX tool for mapping website and app screens**. His AI agents connect through Paper MCP and design directly on the platform. Because output is grounded in **HTML/CSS**, handoff to front-end development tends to stay closer to what ships in the browser. Paper also lets him be **more hands-on** when he wants to—he can work **directly on the canvas** instead of only delegating to agents.

Treat Paper files as the source of truth for exploratory UI work in this stack; pair with your repo’s components, tokens, and accessibility standards before production merge.

## Jake's take

<!-- Jake's input goes here -->
