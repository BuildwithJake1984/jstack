
---
type: tool
title: Cursor — AI editor and cloud agents
purpose: Jake's primary IDE for agentic coding, MCP, and shipping from the repo.
status: curated
tags: [tools, ai-agents, cursor, ide, agents, mcp, cloud-agents]
sources:
  - url: https://cursor.com/
    label: Cursor
  - url: https://docs.cursor.com/
    label: Cursor documentation
---

# Cursor — AI editor and cloud agents

## When to use

- Setting up agentic coding workflows (rules, skills, MCP, Cloud Agents).
- Choosing when Cursor fits versus terminal-only agents or other IDEs.
- Tracking Cursor product and docs changes that affect daily development.

## What it is

[Cursor](https://cursor.com/) is an **AI-native code editor** built on the VS Code foundation: inline and chat **agents**, codebase indexing, extensions, and team features. Documentation at [docs.cursor.com](https://docs.cursor.com/) covers installation, models, MCP, Background/Cloud Agents, and enterprise settings.

## What it can do

### Agent chat and inline edits

Cursor agents read repository context, propose multi-file edits, run terminal commands (with user approval settings), and iterate on errors. Jake uses this as the main loop for shipping [Next.js](../../development/tools/nextjs.md) features.

### Codebase indexing and context

The editor indexes the workspace so prompts reference relevant files without manually @-mentioning every path. `.cursor/rules`, `AGENTS.md`, and skills extend behavior per project.

### Model Context Protocol (MCP)

Cursor supports **MCP servers** so agents call external tools—[Paper](../../design/tools/paper.md), [Mobbin](../../design/tools/mobbin.md), [Supabase](../../development/tools/supabase.md), and others—inside the same session. Configure servers in Cursor settings per docs.

### Cloud / background agents

Cursor documents **Cloud Agents** (naming may evolve) for running longer tasks off the laptop with repository integration—useful for parallel PRs and automation; confirm current product names in docs.

### VS Code compatibility

Extensions and keybindings from the VS Code ecosystem largely work, lowering migration friction from stock VS Code.

## How it fits Jake's stack

**Primary IDE** for writing code, running agents, and opening PRs on [GitHub](../../development/tools/github.md). Models from [Claude](claude.md), [OpenAI](openai.md), and others are selectable per Cursor’s model settings; deploy targets remain [Vercel](../../development/tools/vercel.md) and related infra docs in [`development/tools/`](../../development/tools/README.md).

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [cursor.com](https://cursor.com/) changelog/blog, [docs.cursor.com](https://docs.cursor.com/) updates, and [@cursor on X](https://x.com/cursor). Link [this file](cursor.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://cursor.com/](https://cursor.com/) — product overview
- [https://docs.cursor.com/](https://docs.cursor.com/) — documentation (agents, MCP, cloud features)
