
---
type: tool
title: Claude — Anthropic models, apps, and APIs
purpose: Primary frontier-model family for reasoning, coding agents, and product AI features.
status: curated
tags: [tools, ai-agents, anthropic, claude, api, agents, mcp]
sources:
  - url: https://www.anthropic.com/
    label: Anthropic
  - url: https://docs.anthropic.com/
    label: Claude documentation
  - url: https://docs.claude.com/en/release-notes/overview
    label: Claude release notes
---

# Claude — Anthropic models, apps, and APIs

## When to use

- Choosing or integrating Anthropic models (Claude) for agents, chat, or batch workflows.
- Comparing Claude capabilities, context windows, and tool/MCP support against other frontier labs.
- Tracking Claude Code, SDK, and platform release notes for JStack agent setups.

## What it is

[Anthropic](https://www.anthropic.com/) builds the **Claude** model family for safe, capable AI assistants. Developers integrate through the **Claude API** and SDKs documented at [docs.anthropic.com](https://docs.anthropic.com/); consumers use Claude apps; **Claude Code** targets agentic software work. Product changes are summarized in [Claude release notes](https://docs.claude.com/en/release-notes/overview).

## What it can do

### Messages API and models

The API exposes **messages**-style chat with multiple Claude model tiers (names, context windows, and pricing change over time—see current [models documentation](https://docs.anthropic.com/en/docs/about-claude/models)). Use it for assistants, extraction, classification, and multi-step prompts in application backends.

### Tool use and computer use

Anthropic documents **tool use** so Claude can call developer-defined functions, and **computer use** (where enabled) for UI automation scenarios. These patterns underpin coding agents and product copilots that must act on structured tools rather than text alone.

### Vision and document inputs

Many Claude models accept **images** and structured content blocks in API requests, supporting UI critique, diagram understanding, and document Q&A when your product sends permitted media.

### Claude Code and developer tooling

**Claude Code** (and related CLI/IDE integrations Anthropic ships) targets **repository-aware coding agents**—edits, tests, and reviews grounded in project context. Pair with [Cursor](cursor.md) or terminal workflows depending on task.

### Prompting and safety documentation

Anthropic publishes **prompt engineering** guides, **system prompt** patterns, and **usage policies** so teams can design reliable assistants and stay within acceptable-use rules.

## How it fits Jake's stack

A **default frontier lab** for reasoning, long-context tasks, and agent backends alongside [OpenAI](openai.md) and [xAI](xai.md). Jake routes daily coding through [Cursor](cursor.md) and Claude-powered agents; product features on [Next.js](../development/nextjs.md) + [Supabase](../development/supabase.md) call the API where needed. UI exploration often happens in [Paper](../design/paper.md) with MCP-connected agents.

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [anthropic.com/news](https://www.anthropic.com/news), [Claude release notes](https://docs.claude.com/en/release-notes/overview), [docs.anthropic.com](https://docs.anthropic.com/) updates, GitHub release feeds for `anthropics/*` repos listed in the news README, [@Anthropic](https://x.com/Anthropic) and [@Claude](https://x.com/Claude) on X. Link [this file](claude.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://www.anthropic.com/](https://www.anthropic.com/) — company and products
- [https://docs.anthropic.com/](https://docs.anthropic.com/) — API, models, tool use
- [https://docs.claude.com/en/release-notes/overview](https://docs.claude.com/en/release-notes/overview) — release notes
