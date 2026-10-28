
---
type: tool
title: ElevenLabs — AI voice and audio
purpose: Synthetic voice, dubbing, and audio for marketing and product content.
status: curated
tags: [tools, marketing, elevenlabs, voice, audio, ai, tts]
sources:
  - url: https://elevenlabs.io/
    label: ElevenLabs
  - url: https://elevenlabs.io/docs
    label: ElevenLabs documentation
---

# ElevenLabs — AI voice and audio

## When to use

- **Voiceovers**, dubbing, or character audio for ads, demos, and social clips.
- Evaluating ElevenLabs APIs versus local tools such as [VoiceStudio](../design/voicestudio.md).
- Checking voice licensing and disclosure before publishing synthetic speech.

## What it is

[ElevenLabs](https://elevenlabs.io/) provides **AI voice synthesis**, dubbing, and audio APIs for creators and developers. Documentation: [elevenlabs.io/docs](https://elevenlabs.io/docs).

## What it can do

### Text-to-speech and voice design

Generate speech from text with selectable **voices**; design new voices from prompts or samples where the product and license allow (see ElevenLabs **Voice Design** docs).

### Voice cloning (policy-bound)

**Instant Voice Cloning** and related features require consent and prohibited-use policies published by ElevenLabs—read current terms before cloning real speakers.

### Dubbing and multilingual audio

**Dubbing** workflows translate and re-voice video audio tracks—useful for adapting campaign creative across locales.

### API and SDK access

HTTP **API** endpoints and official SDKs integrate with automation pipelines (export from Higgsfield/Canva timelines, assemble in edit tools). API keys stay server-side when called from [Next.js](../development/nextjs.md) backends.

### Projects and studio UI

The web **Projects** UI supports non-developer iteration; developers pair UI exports with API calls for scale.

## How it fits Jake's stack

**Marketing and content audio** in JStack—hosted voice for campaigns and explainers—cataloged in [`marketing/tools/`](README.md) even though the tech is AI. Not a substitute for in-app conversational models ([Claude](../ai-agents/claude.md), etc.). Disclose synthetic voice in ads; confirm commercial rights per voice license.

## News and insights

**Not** in the weekly [News & Insights](../../../insights/news-and-insights/README.md) vendor sweep. Link [this file](elevenlabs.md) when mentioning ElevenLabs elsewhere. Follow [elevenlabs.io/blog](https://elevenlabs.io/blog) (when published), [docs](https://elevenlabs.io/docs) updates, and [@elevenlabs on X](https://x.com/elevenlabs).

## Sources

Pages checked for this reference (2026-10-22):

- [https://elevenlabs.io/](https://elevenlabs.io/) — product overview
- [https://elevenlabs.io/docs](https://elevenlabs.io/docs) — API, voice design, dubbing, policies
