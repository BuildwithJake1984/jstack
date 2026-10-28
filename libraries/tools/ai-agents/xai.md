
---
type: tool
title: xAI — Grok models, API, and Grok Bot
purpose: xAI frontier models and Grok integrations for chat, agents, and X-native workflows.
status: curated
tags: [tools, ai-agents, xai, grok, api, agents]
sources:
  - url: https://x.ai/
    label: xAI
  - url: https://docs.x.ai/
    label: xAI documentation
  - url: https://docs.x.ai/docs/release-notes
    label: xAI release notes
---

# xAI — Grok models, API, and Grok Bot

## When to use

- Integrating **Grok** via the xAI API or Python SDK.
- Evaluating Grok for coding agents, research, or multi-model stacks.
- Tracking xAI release notes and Grok Bot product changes.

## What it is

[xAI](https://x.ai/) builds **Grok** and publishes developer documentation at [docs.x.ai](https://docs.x.ai/), including API guides, model lists, and [release notes](https://docs.x.ai/docs/release-notes). Grok also ships in consumer experiences such as **Grok Bot** on X.

## What it can do

### Chat Completions API

xAI documents a **chat completions**-style HTTP API compatible with common OpenAI-client patterns (base URL and model names per current docs). Use it for assistants, tool-augmented agents, and server-side features.

### Models and context

Model cards on docs.x.ai describe available **Grok** tiers, context limits, and pricing. Compare latency and quality against [Claude](claude.md) and [OpenAI](openai.md) before committing a user-facing default.

### SDKs and examples

The **`xai-org/xai-sdk-python`** repository (see GitHub releases in the news README) provides maintained Python access; other languages may use HTTP directly per API reference.

### Grok on X

Grok Bot exposes Grok inside **X** for conversational use and X-native context. Product behavior and availability change independently of the API—track xAI announcements when social workflows matter.

## How it fits Jake's stack

Part of Jake’s **multi-model frontier set**—useful when Grok’s speed, pricing, or X connectivity fits the task. Coding still flows through [Cursor](cursor.md); APIs integrate with the same [Next.js](../development/nextjs.md) / [Supabase](../development/supabase.md) backends as other labs.

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [x.ai](https://x.ai/), [docs.x.ai release notes](https://docs.x.ai/docs/release-notes), GitHub releases for `xai-org/xai-sdk-python`, [@xai](https://x.com/xai) and [@grok](https://x.com/grok). Link [this file](xai.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://x.ai/](https://x.ai/) — product positioning
- [https://docs.x.ai/](https://docs.x.ai/) — API and models
- [https://docs.x.ai/docs/release-notes](https://docs.x.ai/docs/release-notes) — release notes
