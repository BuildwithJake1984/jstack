---
type: reference
title: Liquid Glass — refractive glass for the web
purpose: MIT headless refractive glass lens for React.
status: curated
tags: [ui, effects, glass, react, refraction, canvas, accessibility, mit, free]
sources:
  - url: https://glass.samasante.com/
    label: Liquid Glass demos and documentation
  - url: https://github.com/samasante/liquid-glass
    label: Source repository and license
---

# Liquid Glass — refractive glass for the web

## When to use

- Use as a focused accent where refraction materially supports the design. It fits the project's atmospheric and object-like interface direction, especially for floating navigation, control trays, planet labels, and compact CTA surfaces.

Listed in the [UI Components catalog](components.md).

A headless React lens that creates refractive, frosted-glass surfaces over the live page rather than relying on a flat backdrop blur. It is useful for premium navigation, floating controls, compact overlays, and experimental interface objects.

## Access and licensing

**Free and open source under MIT.** The project advertises zero runtime dependencies and cross-browser rendering.


## Cautions

- Test performance on mobile hardware and lower-powered devices.
- Provide a simpler fallback for unsupported rendering paths and reduced-motion or reduced-transparency preferences.
- Maintain text contrast while the background changes beneath the lens.
- Do not apply the effect to every surface; the visual hierarchy depends on restraint.
