---
type: reference
title: DialKit — live interface tuning controls
purpose: Live dev controls for tuning interface values and animation timing.
status: curated
tags: [ui, development, controls, animation, tuning, react, solid, svelte, vue, javascript, mit, free]
sources:
  - url: https://dialkit.dev/
    label: DialKit documentation and demos
---

# DialKit — live interface tuning controls

## When to use

- Use during design engineering to tune spacing, radii, color, shadows, spring behavior, easing, and multi-step animation timing without repeatedly editing source values. The editor is hidden in production by default.

Listed in the [UI Components catalog](../components/).

A developer-facing control panel for tuning interface values and animation timing in real time. It supports React, Solid, Svelte, Vue, and plain JavaScript, with sliders, toggles, text, selects, color and image controls, two-axis pads, spring and easing editors, actions, folders, presets, and a timeline.

## Access and licensing

**Free and open source under MIT.** Install the package and any required animation adapter through the project package manager.


## Cautions

- Treat it as a development tool, not a customer-facing control surface.
- Copy finalized values back into production code and remove temporary bindings when appropriate.
- Verify framework compatibility, bundle impact, keyboard behavior, and reduced-motion outcomes.
- Avoid exposing internal development controls in production unless the product explicitly requires them.
