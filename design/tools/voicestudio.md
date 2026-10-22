
---
type: tool
title: VoiceStudio — local AI voice production workspace
purpose: Clone, design, dub, and transcribe voice locally with optional API or MCP.
status: curated
tags: [tools, audio, voice, ai, local-first, voice-cloning, dubbing, transcription, audiobook, api, mcp, agpl]
sources:
  - url: https://voicestudio.sh/
    label: VoiceStudio
  - url: https://github.com/debpalash/VoiceStudio
    label: VoiceStudio GitHub
---

# VoiceStudio — local AI voice production workspace

## When to use

- Local voice cloning, dubbing, or transcription without sending audio to the cloud.
- Audiobook, multi-speaker story, or dictation workflows on your own machine.

## What it is

[VoiceStudio](https://voicestudio.sh/) is a **local-first** AI audio workspace published as **AGPL-3.0** open source on [GitHub](https://github.com/debpalash/VoiceStudio). It runs on macOS, Windows, Linux, WSL, or Docker and can expose an **OpenAI-compatible local API** and **MCP** connections per project documentation.

## What it can do

### Voice cloning and design

Create a voice from a **permitted reference recording** or design synthetic voices using controls such as age, accent, pitch, gender, emotion, and style described in the project README.

### Dubbing and video re-voice

Transcribe, translate, cast, synchronize, and **re-voice video** locally—useful for multilingual marketing drafts when cloud APIs are not desired.

### Long-form and multi-speaker audio

Produce **multi-character stories** and **chaptered audiobooks**, plus dictation and transcription workflows, with model management inside the app.

### Local API and MCP

Integrate other tools via the documented **local API** or **MCP** so agents or scripts can trigger generation on the same machine as the audio data.

## How it fits Jake's stack

A **local audio utility** for experiments, walkthrough narration, and transcription—not Jake’s primary marketing voice stack ([ElevenLabs](../../marketing/tools/elevenlabs.md) covers hosted campaign audio). Treat **AGPL-3.0** obligations seriously before embedding in proprietary client work; models and voices carry **separate licenses**—verify each before commercial use. Clone real voices only with permission; disclose synthetic speech where audiences could be misled.

## News and insights

**Not** in the weekly [News & Insights](../../news-and-insights/README.md) vendor sweep. Link [this file](voicestudio.md) if you mention VoiceStudio elsewhere. Follow [voicestudio.sh](https://voicestudio.sh/) and [GitHub releases](https://github.com/debpalash/VoiceStudio/releases).

## Sources

Pages checked for this reference (2026-10-22):

- [https://voicestudio.sh/](https://voicestudio.sh/) — product overview
- [https://github.com/debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) — README (capabilities, license, platforms, API/MCP)
