---
type: reference
title: UI SFX — semantic interface sound library
purpose: MIT/CC0 semantic interface sound library.
status: curated
tags: [design, audio, sound, ui, accessibility, typescript, mit, cc0, free]
sources:
  - url: https://uisfx.com/
    label: UI SFX browser and sound packs
  - url: https://github.com/romainsimon/uisfx
    label: Source, licenses, and implementation
---

# UI SFX — semantic interface sound library

## When to use

- Use for intentional confirmation, warning, progress, completion, navigation, and playful character interactions. It could support a brand mascot without requiring a custom sound system on day one.

Listed in the [UI Components catalog](../components/).

An open library of procedurally generated interface sounds organized around semantic product states and multiple sonic personalities. It is designed for web apps, mobile apps, SaaS, education, media, and games.

## Access and licensing

**Free and open source.** The TypeScript implementation is MIT licensed. The generated audio library and pack illustrations are dedicated to the public domain under CC0 1.0.


## Cautions

- Sound must enhance—not replace—visible or haptic feedback.
- Default conservatively; respect mute state, user preferences, and assistive contexts.
- Avoid sound on routine hover and scrolling actions.
- Test volume normalization, repeated events, latency, and overlapping playback.
