
---
title: Page Mascot — cursor-aware interactive character
kind: reference
status: curated
tags: [ui, mascot, character, animation, sprite-sheet, react, interaction, mit, free]
sources:
  - url: https://koboyo.com/page-mascot
    label: Page Mascot demo
  - url: https://github.com/nilbuild/page-mascot
    label: Page Mascot source and documentation
---

# Page Mascot

Page Mascot is a lightweight interactive-character component by Kamran Ahmed. A mascot watches the pointer, changes its gaze as the cursor moves, and briefly reacts when clicked or “poked.”

This is a strong candidate for a brand character system: each site area could have its own character while sharing the same interaction engine.

## Classification

- **Price:** Free.
- **License:** MIT.
- **Commercial use:** Allowed under the MIT license.
- **Package:** `page-mascot` on npm.
- **Framework usage:** The documented component API is React-oriented.
- **Source:** [nilbuild/page-mascot](https://github.com/nilbuild/page-mascot).

## How it works

Each character is represented by two aligned 3×3 sprite sheets:

1. **Direction sheet:** nine head or eye directions selected from the pointer angle.
2. **Reaction sheet:** nine expressions shown temporarily after interaction.

The component uses a dead zone so the character’s gaze settles when the pointer is close. Clicking triggers a brief squash/reaction state.

The documented props are deliberately small:

- `directions`: path to the directional sprite sheet.
- `reactions`: path to the expression sprite sheet.
- `size`: square display size, defaulting to 140 pixels.
- `label`: accessible name for screen readers.
- `className`: project styling hook.

Pointer tracking turns off on devices without a fine pointer, and the click squash respects `prefers-reduced-motion`.

## Concept direction

The mascot should be an original brand character, not one of the demo animals.

A particularly strong direction would be a small alien astronaut who:

- follows the visitor’s cursor with its eyes or helmet,
- blinks and subtly breathes while idle,
- reacts when poked,
- looks toward the currently hovered planet or navigation target,
- changes tools, patches, helmet details, or expressions by site section,
- occasionally performs a rare surprise reaction without interrupting navigation.

Possible character roles could map to site sections:

- **Builder:** carries tools and represents commercial products.
- **Inventor:** creates internal tools and experiments.
- **Curator:** collects libraries, references, and inspiration.

## Art direction

Page Mascot’s generation workflow supports color, ink, sketch, riso, paper, and pixel treatments. For a retro-futurist brand, explore:

- clean retro-futurist color illustration,
- slightly dimensional helmet glass,
- a restrained navy, cream, electric blue, and warm accent palette,
- bold silhouette that stays recognizable around 120–160 pixels,
- facial features readable inside a small helmet,
- consistent proportions across every direction and reaction.

## Adoption guidance

- Start with one mascot in one high-value location before distributing characters across the entire site.
- Keep it decorative and optional; it must not block navigation, copy, forms, or mobile content.
- Preserve the package’s reduced-motion and coarse-pointer behavior.
- Give the mascot a meaningful screen-reader label, or hide it from assistive technology when purely decorative.
- Optimize sprite sheets and reserve fixed layout space to avoid loading shifts.
- Generate and own original character artwork rather than shipping the repository’s example mascot sheets.
- Pin and review the npm package before production adoption.

## Potential first placement

The best first experiment is an immersive homepage. Position one alien or astronaut beside the primary navigation universe and have its gaze follow the pointer toward the planets. A click reaction could acknowledge planet selection before the transition begins.

This preserves the character’s surprise-and-delight value without turning it into constant decoration throughout every page.


