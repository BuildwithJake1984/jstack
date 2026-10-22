
---
type: tool
title: OpenAI — models, API, and Codex
purpose: Frontier models and APIs for chat, reasoning, embeddings, and coding agents.
status: curated
tags: [tools, ai-agents, openai, api, gpt, codex, agents]
sources:
  - url: https://openai.com/
    label: OpenAI
  - url: https://platform.openai.com/docs
    label: OpenAI Platform documentation
  - url: https://platform.openai.com/docs/changelog
    label: OpenAI platform changelog
  - url: https://openai.com/news/rss.xml
    label: OpenAI news RSS
---

# OpenAI — models, API, and Codex

## When to use

- Integrating OpenAI models via the Platform API or evaluating new model tiers.
- Following Codex, SDK, and platform changelog items that affect agent workflows.
- Comparing OpenAI tooling with other frontier labs in the stack.

## What it is

[OpenAI](https://openai.com/) researches and ships frontier models (GPT family and successors) for developers and consumers. The **OpenAI Platform** at [platform.openai.com/docs](https://platform.openai.com/docs) documents REST APIs, SDKs, billing, and the [platform changelog](https://platform.openai.com/docs/changelog). News releases publish to [openai.com/news](https://openai.com/news) with RSS at [openai.com/news/rss.xml](https://openai.com/news/rss.xml).

## What it can do

### Chat Completions and Responses API

Platform docs describe **chat**-style model calls for assistants, tools, and structured outputs. Newer **Responses**-style APIs (see current docs) unify tool calling, reasoning, and multimodal inputs depending on model—confirm the recommended API for your SDK version.

### Embeddings and moderation

**Embeddings** endpoints support semantic search and RAG pipelines in [Supabase](../../development/tools/supabase.md) or custom vector stores. **Moderation** endpoints help screen user-generated content before display or storage.

### Images, audio, and realtime (product-dependent)

OpenAI documents **image generation**, **speech**, and **realtime** APIs on the Platform for products that need multimodal I/O. Availability, models, and pricing vary—read the current model pages before designing features.

### Codex and coding agents

**Codex** and related coding products target **software engineering agents** integrated with IDEs and Git hosts. Track `openai/codex` GitHub releases when Jake’s agent stack includes OpenAI coding tools alongside [Cursor](cursor.md).

### Batch and scale features

The Platform documents **batch** processing, rate limits, and organization controls for production workloads on [Vercel](../../development/tools/vercel.md) or [Railway](../../development/tools/railway.md) backends.

## How it fits Jake's stack

OpenAI is a **core frontier option** when a specific model, embedding, or Codex workflow fits better than [Claude](claude.md) or [Grok](xai.md). Jake uses it for APIs, experiments, and multi-model fallbacks; app code lives in GitHub-backed [Next.js](../../development/tools/nextjs.md) repos with lessons in [`ai-agents/lessons/`](../lessons/README.md) for graph-style AI features.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [openai.com/news](https://openai.com/news) (RSS), [platform changelog](https://platform.openai.com/docs/changelog), [platform docs](https://platform.openai.com/docs), GitHub releases for `openai/*` SDK repos, and [@OpenAI](https://x.com/OpenAI). Link [this file](openai.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://openai.com/](https://openai.com/) — product and research news
- [https://platform.openai.com/docs](https://platform.openai.com/docs) — API reference and guides
- [https://platform.openai.com/docs/changelog](https://platform.openai.com/docs/changelog) — platform changelog
