
---
type: tool
title: Paper — connected canvas for design and agents
purpose: Map product UI on an HTML/CSS canvas with agents and cleaner code handoff.
status: curated
tags: [tools, design, ui, agents, mcp, html, css, canvas, handoff]
sources:
  - url: https://paper.design/
    label: Paper marketing site
  - url: https://paper.design/docs/mcp
    label: Paper MCP documentation
---

# Paper — connected canvas for design and agents

## When to use

- Mapping website or app screens before implementation.
- Connecting Cursor or other agents to a design file via Paper MCP.
- Syncing tokens or real content between code and canvas.

[Paper](https://paper.design/) describes itself as **the connected canvas for teams shipping with agents**: a single design space built on **web standards** where teams, agents, code, and data can stay aligned. Paper Desktop extends that workflow by connecting visual work to apps, agents, and repos through **MCP**.

Paper’s site emphasizes a **design-to-code loop**: an **HTML/CSS canvas** so designs map to code, agents that can **sync design tokens, styles, and components** between a **codebase and the canvas**, and workflows to **pull real content or data** (files, CMS, databases, APIs) into layers and **push copy updates back toward code**. It also positions agents for repetitive work such as **responsive layouts**, style variations, and consistency checks while the designer keeps creative control.

## Capabilities

- **Canvas on web technology** — Paper markets an HTML/CSS-based canvas so layout work stays close to how sites and apps are built.
- **Paper Desktop** — Desktop app that unlocks the connected workflow and MCP setup described in official docs.
- **Paper MCP server** — Agents can **read and write** open Paper files: generate layouts, pull real content, or turn a selected frame into code ([MCP docs](https://paper.design/docs/mcp)). Setup is centered on Paper Desktop (install/open Desktop, then connect agents via the in-app MCP panel or documented manual config). Supported agents listed in docs include **Cursor**, Claude / Claude Code, Codex, VS Code, GitHub Copilot, OpenCode, Antigravity, and others.
- **Agent connection options** — Docs describe **stdio via the Paper CLI** (`paper mcp`) for many agents, plus legacy **localhost HTTP** MCP while a file is open; Cursor can use the marketplace plugin or `/add-plugin paper-desktop`.
- **Documented MCP workflows** — Official guides cover **syncing tokens/styles from Figma** (Figma MCP + Paper MCP together), **pulling content from Notion** into frames, and **building sites from selected frames** (docs recommend flex layouts/containers for better code generation).
- **Tokens** — Paper documents **tokens and themes** for styling designs (see Paper docs index at [paper.design/docs](https://paper.design/docs)).

## Access and pricing

Paper offers web and desktop experiences. **Verify current plans and pricing on [paper.design](https://paper.design/)** before recommending a purchase. MCP workflows in the official documentation assume **Paper Desktop** is installed and updated.

## Use notes

Jake uses Paper as his **primary UI/UX tool for mapping website and app screens**. His AI agents connect through Paper MCP and design directly on the platform. Because output is grounded in **HTML/CSS**, handoff to front-end development tends to stay closer to what ships in the browser. Paper also lets him be **more hands-on** when he wants to—he can work **directly on the canvas** instead of only delegating to agents.

Treat Paper files as the source of truth for exploratory UI work in this stack; pair with your repo’s components, tokens, and accessibility standards before production merge.

## Related

- [Figma](figma.md) — design systems, variables, and Dev Mode handoff
- [Mobbin](mobbin.md) — real-product UI and UX pattern research
- [Design tokens in a design system](../lessons/design-tokens.md) — shared naming between Figma, Paper, and code

## Jake's take

<!-- Jake's input goes here -->

## Sources

Pages checked for this reference (2026-10-22):

- [https://paper.design/](https://paper.design/) — product positioning, HTML/CSS canvas, token/style sync with code, real data workflows, agent-assisted layout work
- [https://paper.design/docs/mcp](https://paper.design/docs/mcp) — MCP read/write behavior, Desktop requirement, supported agents, Figma/Notion/code workflows, CLI vs HTTP transport
- [https://paper.design/docs](https://paper.design/docs) — docs index (tokens/themes, MCP, and related guides)
