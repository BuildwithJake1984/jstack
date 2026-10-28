
---
type: tool
title: Screenshot to Code — visual frontend reconstruction
purpose: Generate a first-pass front-end from screenshots, mockups, or Figma exports.
status: curated
tags: [tools, ai, code, screenshots, figma, frontend, react, vue, tailwind, mit, free, paid]
sources:
  - url: https://screenshottocode.com/
    label: Hosted Screenshot to Code product
  - url: https://github.com/abi/screenshot-to-code
    label: Open-source repository
---

# Screenshot to Code — visual frontend reconstruction

## When to use

- Bootstrapping layout or component structure from an approved visual reference.
- Prototyping migration or rebuild studies from screenshots or short recordings.

Listed in the [UI Components catalog](../../ui-libraries/components.md).

## What it is

[Screenshot to Code](https://screenshottocode.com/) is an AI tool (with an [MIT-licensed open-source project](https://github.com/abi/screenshot-to-code)) that turns **screenshots, mockups, Figma inputs, text prompts, and short screen recordings** into front-end code. The README documents output stacks such as **HTML + Tailwind/CSS**, **React + Tailwind**, **Vue + Tailwind**, **Bootstrap**, and **Ionic + Tailwind**.

## What it can do

### Image and mockup to code

Upload a static screenshot or mockup and receive generated markup and styles as a **starting layout**. The model infers structure and visual hierarchy from pixels; you still own semantics, accessibility, and production quality.

### Figma and recording inputs

The project README describes using **Figma** exports and **short recordings** as additional inputs beyond still images, which helps when motion or multi-state UI is part of the reference (within the limits of what the model can see).

### Self-hosted open source

Clone and run the **MIT** project locally or on your infrastructure. You supply model API keys, optional image services, and hosting; there is no vendor lock-in for the core app, but operational cost shifts to you.

### Hosted credits product

The [hosted product](https://screenshottocode.com/) sells monthly **credits** for managed runs. Pricing and credit counts change—confirm at checkout before relying on quoted tiers in older notes.

## How it fits Jake's stack

A **rapid prototyping** utility—not a substitute for [Paper](paper.md), [Figma](figma.md), or the production design system in [Next.js](../development/nextjs.md) repos. Use it to explore layout ideas from approved references, then rewrite into real components, tokens, tests, and accessible markup. Do not upload confidential or third-party designs without rights.

## News and insights

**Not** in the weekly [News & Insights](../../../insights/news-and-insights/README.md) vendor sweep. If you mention it elsewhere in JStack, link [this file](screenshot-to-code.md). Follow [screenshottocode.com](https://screenshottocode.com/) and [GitHub releases](https://github.com/abi/screenshot-to-code/releases) for the open-source project.

## Sources

Pages checked for this reference (2026-10-22):

- [https://screenshottocode.com/](https://screenshottocode.com/) — hosted product and pricing
- [https://github.com/abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) — README (inputs, stacks, MIT license)
