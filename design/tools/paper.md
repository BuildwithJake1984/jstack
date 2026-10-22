
---
type: tool
title: Paper — connected canvas for design and agents
purpose: Map product UI on an HTML/CSS canvas with agents and cleaner code handoff.
status: curated
tags: [tools, design, ui, agents, mcp, html, css, canvas, handoff]
sources:
  - url: https://paper.design/
    label: Paper marketing site
  - url: https://paper.design/docs
    label: Paper documentation
  - url: https://paper.design/docs/mcp
    label: Paper MCP documentation
---

# Paper — connected canvas for design and agents

## When to use

- Mapping website or app screens before implementation.
- Connecting Cursor or other agents to a design file via Paper MCP.
- Syncing tokens or real content between code and canvas.

## What it is

[Paper](https://paper.design/) is a **connected canvas** for teams that ship with agents: a design space built on **web standards** where visual work, code, and data can stay aligned. [Paper Desktop](https://paper.design/) extends that workflow with local files and agent connections through the **Model Context Protocol (MCP)** described in [Paper’s MCP docs](https://paper.design/docs/mcp).

## What it can do

### HTML/CSS canvas

Paper’s canvas is grounded in **HTML and CSS**, so layouts map closely to how sites and apps are built in production. That reduces translation loss when moving from exploration to front-end implementation compared with purely abstract drawing models.

### Paper Desktop and MCP

With **Paper Desktop** installed, agents can **read and write** open Paper files—generate layouts, apply styles, or export selected frames toward code. Official docs list supported clients (including **Cursor**, Claude / Claude Code, Codex, VS Code, GitHub Copilot, and others) and setup via the in-app MCP panel, **`paper mcp` CLI** (stdio), or documented HTTP transport while a file is open.

### Design–code sync

Paper documents workflows to **sync design tokens, styles, and components** between a **codebase and the canvas**, and to **pull real content** from files, CMS, databases, or APIs into layers. Copy and structure updates can flow back toward code so the canvas does not drift from what ships.

### Documented cross-tool workflows

Official guides cover combining **Figma MCP with Paper MCP** to bring tokens or styles from Figma, **Notion** content into frames, and **building sites from selected frames** (docs recommend flex layouts and containers for stronger code generation).

### Tokens and themes

Paper documents **tokens and themes** for consistent styling on the canvas ([docs index](https://paper.design/docs)), which pairs with Jake’s Figma token libraries and code-side theme files.

## How it fits Jake's stack

Jake uses Paper as his **primary UI/UX tool for mapping website and app screens**. Agents connect through **Paper MCP** and can design directly in the file; because output is **HTML/CSS**, handoff to [Next.js](../../development/tools/nextjs.md) development stays closer to the browser. He also works **hands-on on the canvas** when he wants direct control instead of delegating everything to agents. Paper complements [Figma](figma.md) (systems and tokens) and [Mobbin](mobbin.md) (pattern research). Verify plans on [paper.design](https://paper.design/) before purchase; MCP flows in docs assume an up-to-date Desktop app.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [paper.design](https://paper.design/), [Paper docs](https://paper.design/docs) (including MCP and release-related pages), and [@paper on X](https://x.com/paper). Link [this file](paper.md) when an issue mentions Paper.

## Sources

Pages checked for this reference (2026-10-22):

- [https://paper.design/](https://paper.design/) — product positioning, HTML/CSS canvas, agent and data workflows
- [https://paper.design/docs](https://paper.design/docs) — documentation index (tokens, themes, MCP)
- [https://paper.design/docs/mcp](https://paper.design/docs/mcp) — MCP setup, supported agents, Figma/Notion/code workflows, CLI vs HTTP
