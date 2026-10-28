# UI libraries catalog

Curated links and markdown digests for UI component libraries and design inspiration. Not executable recipes—for skills, see [`../../business-workflows/design/README.md`](../../business-workflows/design/README.md#skills). Tool references live in [`../tools/design/README.md`](../tools/design/README.md).

## How to add an entry

1. Add a new kebab-case markdown file under `ui-libraries/` (e.g. `ui-libraries/footer-pattern-notes.md`) using the reference frontmatter in [CONVENTIONS.md](../../CONVENTIONS.md#reference-ui-libraries-link-outs) or the contract below.
2. Fill frontmatter and body in that file.
3. For `kind: media-set`, add a `## Media` section in the same file with URL rows (no image or video binaries in git).
4. Set `status: inbox` until reviewed; move to `curated` when ready for agent use.
5. Add a row to the catalog table below.

## Frontmatter contract

```yaml
---
title: ...
kind: reference | media-set | link-digest
status: inbox | curated | deprecated
tags: [seo, aeo, ui, ...]
sources:
  - url: https://...
    label: ...
---
```

| Field | Values | Notes |
| --- | --- | --- |
| `title` | string | Human-readable entry name |
| `kind` | `reference`, `media-set`, `link-digest` | `media-set` uses a `## Media` section in the same file |
| `status` | `inbox`, `curated`, `deprecated` | Only `curated` entries belong in agent context by default |
| `tags` | string array | Discovery filters (e.g. `seo`, `aeo`, `ui`, `footer`, `intake`) |
| `sources` | url + label pairs | Canonical links this entry summarizes or cites |

## Media-set pattern

For `kind: media-set`, put URL rows in a `## Media` section in the entry file:

```markdown
| url | type | alt | when-to-use |
| --- | --- | --- | --- |
| https://example.com/photo.jpg | image | ... | ... |
| https://example.com/demo.mp4 | video | ... | ... |
```

Each row: `url`, `type` (`image` | `video`), `alt`, `when-to-use`. URLs only—no binaries in git.

## Catalog

| File | Title | Kind | Status | Tags |
| --- | --- | --- | --- | --- |
| [`book-of-shapes/`](book-of-shapes.md) | Book of Shapes — generative SVG patterns | reference | curated | design, shapes, svg, patterns, generative, backgrounds, free, commercial |
| [`playgrnd/`](playgrnd.md) | Playgrnd — browser-based generative design tools | reference | curated | design, generative, patterns, posters, backgrounds, textures, browser, privacy, free |
| [`specialized-galleries/`](specialized-galleries.md) | Specialized web and brand design inspiration galleries | link-digest | curated | ui, design, inspiration, gallery, sections, bento, hero, navigation, footer, 404, saas, social |
| [`kage/`](kage.md) | Kage — real-product interface inspiration and agent prompts | reference | curated | ui, design, inspiration, components, prompts, agents, gallery, free |
| [`quiver-ai/`](quiver-ai.md) | QuiverAI — structured AI-generated SVGs | reference | curated | design, ai, svg, vector, logos, icons, illustrations, animation, mcp, api, paid |
| [`typeface-fyi/`](typeface-fyi.md) | Typeface.fyi — visual typeface discovery | reference | curated | design, typography, fonts, inspiration, discovery, licensing |
| [`uisfx/`](uisfx.md) | UI SFX — semantic interface sound library | reference | curated | design, audio, sound, ui, accessibility, typescript, mit, cc0, free |
| [`dialkit/`](dialkit.md) | DialKit — live interface tuning controls | reference | curated | ui, development, controls, animation, tuning, react, solid, svelte, vue, javascript, mit, free |
| [`liquid-glass/`](liquid-glass.md) | Liquid Glass — refractive glass for the web | reference | curated | ui, effects, glass, react, refraction, accessibility, mit, free |
| [`md-resources/`](md-resources.md) | DESIGN.md generators, catalogs, and UI references | link-digest | curated | design, design-md, design-systems, agents, inspiration, mcp, ui-reference |
| [`aicss/`](aicss.md) | AICSS — UI components for AI agents | reference | curated | ui, components, ai, agents, chat, react, vue, svelte, shadcn |
| [`annnimate/`](annnimate.md) | Annnimate — GSAP motion components | reference | curated | ui, animation, motion, gsap, react, vue |
| [`astryx/`](astryx.md) | Astryx — Meta-grown agent-ready design system | reference | curated | ui, components, design-system, react, stylex, themes, templates, cli, mcp, mit, free |
| [`beautiful-ui/`](beautiful-ui.md) | Beautiful UI — AI-native interface primitives | reference | curated | ui, components, ai, agents, react, mit, free |
| [`bencho/`](bencho.md) | Bencho — interactive UI blocks | reference | curated | ui, components, interactions, react, mit, free |
| [`bestdesignsonx/`](bestdesignsonx.md) | Best Designs On X | reference | curated | ui, design, inspiration, gallery, x, instagram, dribbble, behance, fonts, app-icons |
| [`beui-pro/`](beui-pro.md) | beUI Pro — premium motion components | reference | curated | ui, components, motion, react, nextjs, tailwind, paid |
| [`reverseui/`](reverseui.md) | ReverseUI - premium animated UI components; animated site reference | reference | curated | ui, components, react, motion, animation, paid |
| [`scrolltide/`](scrolltide.md) | Scrolltide — cinematic scroll templates and AI prompts | reference | curated | ui, components, templates, prompts, scroll, motion, shaders, 3d, ai, paid |
| [`components/`](components.md) | UI Components — catalog | reference | curated | ui, components, catalog |
| [`cue/`](cue.md) | Cue — curated component references and AI prompts | reference | curated | ui, components, inspiration, prompts, react, motion, free, paid |
| [`evil-buttons/`](evil-buttons.md) | Evil Buttons — animated shadcn button components | reference | curated | ui, components, buttons, react, shadcn, motion, apache, free |
| [`feralui/`](feralui.md) | FeralUI — playful physics-driven React experiments | reference | curated | ui, components, react, typescript, physics, animation, interaction, free, mit |
| [`halaska/`](halaska.md) | UI by Halaska — AI product UI kit | reference | curated | ui, components, ai, agents, react, shadcn, mit, free |
| [`keyline-icons/`](keyline-icons.md) | Keyline Icons | reference | curated | ui, icons, shadcn, svg, react, mit |
| [`kobra/`](kobra.md) | Kobra — React component system | reference | curated | ui, components, react, shadcn, figma, mcp, free, paid |
| [`libraries-dev/`](libraries-dev.md) | Libraries.dev — UI effects for AI agents | reference | curated | ui, components, effects, react, agents, mit, free, paid |
| [`openui/`](openui.md) | OpenUI — open standard for generative interfaces | reference | curated | ui, generative-ui, agents, streaming, react, vue, svelte, react-native, mcp, mit, free |
| [`page-mascot/`](page-mascot.md) | Page Mascot — cursor-aware interactive character | reference | curated | ui, mascot, character, animation, sprite-sheet, react, interaction, mit, free |
| [`xiod/`](xiod.md) | XiodUI — versioned React component library | reference | curated | ui, components, react, tailwind, base-ui, accessibility, theming, animation, source-available, free |
| [`vibeprompts/`](vibeprompts.md) | VibePrompt — UI prompt and Tailwind snippet library | reference | curated | ui, prompts, tailwind, layouts, ai, vibe-coding, free |
| [`shadcncraft/`](shadcncraft.md) | ShadcnCraft — production-ready shadcn blocks and Figma kit | reference | curated | ui, components, blocks, shadcn, react, figma, mcp, agents, free, paid |
| [`shadcn/`](shadcn.md) | shadcn/ui — primary component foundation | reference | curated | ui, components, shadcn, react, tailwind, primary |
| [`spectrum/`](spectrum.md) | Spectrum UI — components and MCP registry | reference | curated | ui, components, react, tailwind, shadcn, mcp, agents |

**UI and design detail entries:** [`shadcn/`](shadcn.md) (primary), [`shadcncraft/`](shadcncraft.md), [`aicss/`](aicss.md) (AI-specific), [`astryx/`](astryx.md), [`spectrum/`](spectrum.md) (components + MCP), [`beautiful-ui/`](beautiful-ui.md), [`bencho/`](bencho.md), [`bestdesignsonx/`](bestdesignsonx.md), [`beui-pro/`](beui-pro.md), [`reverseui/`](reverseui.md), [`scrolltide/`](scrolltide.md), [`cue/`](cue.md), [`dialkit/`](dialkit.md), [`evil-buttons/`](evil-buttons.md), [`feralui/`](feralui.md), [`halaska/`](halaska.md), [`kobra/`](kobra.md), [`libraries-dev/`](libraries-dev.md), [`liquid-glass/`](liquid-glass.md), [`amicro/`](amicro.md), [`annnimate/`](annnimate.md), [`kinetics/`](kinetics.md), [`jakubkrehel-skills/`](jakubkrehel-skills.md), [`keyline-icons/`](keyline-icons.md), [`openui/`](openui.md), [`page-mascot/`](page-mascot.md), [`xiod/`](xiod.md), [`vibeprompts/`](vibeprompts.md), [`book-of-shapes/`](book-of-shapes.md), [`playgrnd/`](playgrnd.md), [`quiver-ai/`](quiver-ai.md), [`kage/`](kage.md), [`typeface-fyi/`](typeface-fyi.md), [`uisfx/`](uisfx.md), [`specialized-galleries/`](specialized-galleries.md), [`md-resources/`](md-resources.md)



Contributions: open a pull request that adds a reference `.md` file plus a catalog row; entries are merged after maintainer review.


