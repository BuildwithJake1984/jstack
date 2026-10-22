
---
type: tool
title: Google — Gemini and Google AI
purpose: Google's Gemini models, AI Studio, and cloud AI surfaces for apps and agents.
status: curated
tags: [tools, ai-agents, google, gemini, ai-studio, api]
sources:
  - url: https://ai.google/
    label: Google AI
  - url: https://ai.google.dev/
    label: Google AI for Developers
  - url: https://gemini.google.com/
    label: Gemini
---

# Google — Gemini and Google AI

## When to use

- Building with **Gemini** via AI Studio, the Gemini API, or Google Cloud AI products.
- Comparing Google's multimodal and long-context offerings with other frontier labs.
- Tracking Google AI announcements that affect product choices.

## What it is

[Google AI](https://ai.google/) is Google’s umbrella for AI products and research. **Gemini** is the multimodal model family for consumers ([gemini.google.com](https://gemini.google.com/)) and developers ([ai.google.dev](https://ai.google.dev/)). Research and model advances often surface through **Google DeepMind** channels.

## What it can do

### Gemini API and AI Studio

[Google AI Studio](https://aistudio.google.com/) (see current ai.google.dev links) provides a browser environment to prototype prompts and export code. The **Gemini API** documents authentication, model IDs, streaming, safety settings, and multimodal inputs (text, images, audio, video—per model capability pages).

### Multimodal reasoning

Gemini models support **mixed modalities** in a single conversation when the chosen model tier allows it—useful for UI screenshots, document Q&A, and media-heavy assistants.

### Grounding and tools (product-dependent)

Google documents **grounding** with Google Search or private data, **function calling**, and **code execution** features on select models and Cloud products. Confirm enabled APIs and regions in Cloud console before architecture sign-off.

### Vertex AI (Google Cloud)

Teams on **Google Cloud** deploy Gemini and related models through **Vertex AI** with enterprise IAM, logging, and data residency controls—separate from the consumer Gemini app but sharing model families per Google Cloud docs.

## How it fits Jake's stack

A **frontier lab option** when Gemini pricing, modality, or Google Cloud alignment wins over [Claude](claude.md) or [OpenAI](openai.md). Jake’s default shipping path remains [Vercel](../../development/tools/vercel.md) + [Next.js](../../development/tools/nextjs.md); integrate Gemini where the API fits product requirements.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [ai.google](https://ai.google/), [ai.google.dev](https://ai.google.dev/) release/blog posts, [Google DeepMind](https://deepmind.google/) announcements, [@GoogleDeepMind](https://x.com/GoogleDeepMind) and [@GeminiApp](https://x.com/GeminiApp). Link [this file](google.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://ai.google/](https://ai.google/) — Google AI hub
- [https://ai.google.dev/](https://ai.google.dev/) — Gemini API and AI Studio documentation
- [https://gemini.google.com/](https://gemini.google.com/) — consumer Gemini
