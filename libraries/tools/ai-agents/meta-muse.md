
---
type: tool
title: Meta — Meta AI and Muse
purpose: Meta's open and product AI stack, including Meta AI experiences and Muse research.
status: curated
tags: [tools, ai-agents, meta, meta-ai, muse, llama, open-models]
sources:
  - url: https://ai.meta.com/
    label: Meta AI research
  - url: https://www.meta.ai/
    label: Meta AI app
  - url: https://llama.meta.com/
    label: Llama
---

# Meta — Meta AI and Muse

## When to use

- Evaluating **Meta AI** assistant experiences or **Llama** open models for self-hosted stacks.
- Tracking Meta research (including **Muse** generative work) when architecture or media pipelines are affected.
- Comparing open-weights options with API-first labs.

## What it is

[Meta AI](https://ai.meta.com/) is Meta’s research and product organization for AI. **[Llama](https://llama.meta.com/)** is Meta’s open model family with downloadable weights and license terms. The **[Meta AI](https://www.meta.ai/)** app provides a consumer assistant across Meta surfaces. **Muse** refers to Meta-published generative research (for example text-to-image Muse models described on Meta AI research channels)—confirm current product names on official pages before integration.

## What it can do

### Llama models

Meta releases **Llama** checkpoints with documented licenses for research and commercial use subject to terms on [llama.meta.com](https://llama.meta.com/). Teams can fine-tune or host on their own GPUs—useful when data residency or cost favors self-hosting over [OpenAI](openai.md)-style APIs.

### Meta AI assistant

The Meta AI app answers questions, generates images where enabled, and integrates with Meta apps per Meta’s product pages. Distribution reach differs from developer APIs—treat it as a product surface, not a drop-in replacement for Claude/OpenAI in custom apps.

### Research models (Muse and related)

Meta AI research blogs document models such as **Muse** for high-quality image generation and other modalities. Research artifacts may not map 1:1 to shipping APIs—read each release for availability and license constraints.

### PyTorch and open ecosystem

Much of Meta’s stack builds on **PyTorch** and open tooling, influencing how Llama weights are served (vLLM, Ollama, etc.) in self-hosted deployments.

## How it fits Jake's stack

A **secondary frontier and open-model source** when Llama weights or Meta distribution matter; not Jake’s default for [Cursor](cursor.md)-driven app development unless a project explicitly targets Meta’s stack. Marketing creative may use separate tools in [`marketing/tools/`](../marketing/README.md).

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [ai.meta.com](https://ai.meta.com/) blog/research, [llama.meta.com](https://llama.meta.com/) releases, [meta.ai](https://www.meta.ai/) product updates, and [@MetaAI](https://x.com/MetaAI). Link [this file](meta-muse.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://ai.meta.com/](https://ai.meta.com/) — research and blog
- [https://llama.meta.com/](https://llama.meta.com/) — Llama models and license
- [https://www.meta.ai/](https://www.meta.ai/) — Meta AI assistant product
