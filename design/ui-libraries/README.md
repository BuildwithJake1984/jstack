# UI libraries catalog

Curated links and markdown digests for UI component libraries and design inspiration. Not executable recipes—for skills, see [`../README.md`](../README.md#skills). Tool references live in [`../tools/README.md`](../tools/README.md).

## How to add an entry

1. Copy [`../templates/reference-template/`](../templates/reference-template/) to a new kebab-case folder under `ui-libraries/` (e.g. `ui-libraries/footer-pattern-notes/`).
2. Fill frontmatter and body in `README.md`.
3. For `kind: media-set`, add or update sibling `media.md` (URLs only—no image or video binaries in git).
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
| `kind` | `reference`, `media-set`, `link-digest` | `media-set` requires sibling `media.md` |
| `status` | `inbox`, `curated`, `deprecated` | Only `curated` entries belong in agent context by default |
| `tags` | string array | Discovery filters (e.g. `seo`, `aeo`, `ui`, `footer`, `intake`) |
| `sources` | url + label pairs | Canonical links this entry summarizes or cites |

## Media-set pattern

For `kind: media-set`, keep `README.md` as the index and put URL rows in `media.md`:

```markdown
| url | type | alt | when-to-use |
| --- | --- | --- | --- |
| https://example.com/photo.jpg | image | ... | ... |
| https://example.com/demo.mp4 | video | ... | ... |
```

Each row: `url`, `type` (`image` | `video`), `alt`, `when-to-use`. URLs only—no binaries in git.

## Catalog

| Folder | Title | Kind | Status | Tags |
| --- | --- | --- | --- | --- |
| [`book-of-shapes/`](book-of-shapes/README.md) | Book of Shapes — generative SVG patterns | reference | curated | design, shapes, svg, patterns, generative, backgrounds, free, commercial |
| [`playgrnd/`](playgrnd/README.md) | Playgrnd — browser-based generative design tools | reference | curated | design, generative, patterns, posters, backgrounds, textures, browser, privacy, free |
| [`specialized-galleries/`](specialized-galleries/README.md) | Specialized web and brand design inspiration galleries | link-digest | curated | ui, design, inspiration, gallery, sections, bento, hero, navigation, footer, 404, saas, social |
| [`kage/`](kage/README.md) | Kage — real-product interface inspiration and agent prompts | reference | curated | ui, design, inspiration, components, prompts, agents, gallery, free |
| [`quiver-ai/`](quiver-ai/README.md) | QuiverAI — structured AI-generated SVGs | reference | curated | design, ai, svg, vector, logos, icons, illustrations, animation, mcp, api, paid |
| [`typeface-fyi/`](typeface-fyi/README.md) | Typeface.fyi — visual typeface discovery | reference | curated | design, typography, fonts, inspiration, discovery, licensing |
| [`uisfx/`](uisfx/README.md) | UI SFX — semantic interface sound library | reference | curated | design, audio, sound, ui, accessibility, typescript, mit, cc0, free |
| [`dialkit/`](dialkit/README.md) | DialKit — live interface tuning controls | reference | curated | ui, development, controls, animation, tuning, react, solid, svelte, vue, javascript, mit, free |
| [`liquid-glass/`](liquid-glass/README.md) | Liquid Glass — refractive glass for the web | reference | curated | ui, effects, glass, react, refraction, accessibility, mit, free |
| [`md-resources/`](md-resources/README.md) | DESIGN.md generators, catalogs, and UI references | link-digest | curated | design, design-md, design-systems, agents, inspiration, mcp, ui-reference |
| [`aicss/`](aicss/README.md) | AICSS — UI components for AI agents | reference | curated | ui, components, ai, agents, chat, react, vue, svelte, shadcn |
| [`annnimate/`](annnimate/README.md) | Annnimate — GSAP motion components | reference | curated | ui, animation, motion, gsap, react, vue |
| [`astryx/`](astryx/README.md) | Astryx — Meta-grown agent-ready design system | reference | curated | ui, components, design-system, react, stylex, themes, templates, cli, mcp, mit, free |
| [`beautiful-ui/`](beautiful-ui/README.md) | Beautiful UI — AI-native interface primitives | reference | curated | ui, components, ai, agents, react, mit, free |
| [`bencho/`](bencho/README.md) | Bencho — interactive UI blocks | reference | curated | ui, components, interactions, react, mit, free |
| [`bestdesignsonx/`](bestdesignsonx/README.md) | Best Designs On X | reference | curated | ui, design, inspiration, gallery, x, instagram, dribbble, behance, fonts, app-icons |
| [`beui-pro/`](beui-pro/README.md) | beUI Pro — premium motion components | reference | curated | ui, components, motion, react, nextjs, tailwind, paid |
| [`reverseui/`](reverseui/README.md) | ReverseUI - premium animated UI components; animated site reference | reference | curated | ui, components, react, motion, animation, paid |
| [`components/`](components/README.md) | UI Components — catalog | reference | curated | ui, components, catalog |
| [`cue/`](cue/README.md) | Cue — curated component references and AI prompts | reference | curated | ui, components, inspiration, prompts, react, motion, free, paid |
| [`evil-buttons/`](evil-buttons/README.md) | Evil Buttons — animated shadcn button components | reference | curated | ui, components, buttons, react, shadcn, motion, apache, free |
| [`feralui/`](feralui/README.md) | FeralUI — playful physics-driven React experiments | reference | curated | ui, components, react, typescript, physics, animation, interaction, free, mit |
| [`halaska/`](halaska/README.md) | UI by Halaska — AI product UI kit | reference | curated | ui, components, ai, agents, react, shadcn, mit, free |
| [`keyline-icons/`](keyline-icons/README.md) | Keyline Icons | reference | curated | ui, icons, shadcn, svg, react, mit |
| [`kobra/`](kobra/README.md) | Kobra — React component system | reference | curated | ui, components, react, shadcn, figma, mcp, free, paid |
| [`libraries-dev/`](libraries-dev/README.md) | Libraries.dev — UI effects for AI agents | reference | curated | ui, components, effects, react, agents, mit, free, paid |
| [`openui/`](openui/README.md) | OpenUI — open standard for generative interfaces | reference | curated | ui, generative-ui, agents, streaming, react, vue, svelte, react-native, mcp, mit, free |
| [`page-mascot/`](page-mascot/README.md) | Page Mascot — cursor-aware interactive character | reference | curated | ui, mascot, character, animation, sprite-sheet, react, interaction, mit, free |
| [`xiod/`](xiod/README.md) | XiodUI — versioned React component library | reference | curated | ui, components, react, tailwind, base-ui, accessibility, theming, animation, source-available, free |
| [`vibeprompts/`](vibeprompts/README.md) | VibePrompt — UI prompt and Tailwind snippet library | reference | curated | ui, prompts, tailwind, layouts, ai, vibe-coding, free |
| [`shadcncraft/`](shadcncraft/README.md) | ShadcnCraft — production-ready shadcn blocks and Figma kit | reference | curated | ui, components, blocks, shadcn, react, figma, mcp, agents, free, paid |
| [`shadcn/`](shadcn/README.md) | shadcn/ui — primary component foundation | reference | curated | ui, components, shadcn, react, tailwind, primary |
| [`spectrum/`](spectrum/README.md) | Spectrum UI — components and MCP registry | reference | curated | ui, components, react, tailwind, shadcn, mcp, agents |

**UI and design detail folders:** [`shadcn/`](shadcn/README.md) (primary), [`shadcncraft/`](shadcncraft/README.md), [`aicss/`](aicss/README.md) (AI-specific), [`astryx/`](astryx/README.md), [`spectrum/`](spectrum/README.md) (components + MCP), [`beautiful-ui/`](beautiful-ui/README.md), [`bencho/`](bencho/README.md), [`bestdesignsonx/`](bestdesignsonx/README.md), [`beui-pro/`](beui-pro/README.md), [`reverseui/`](reverseui/README.md), [`cue/`](cue/README.md), [`dialkit/`](dialkit/README.md), [`evil-buttons/`](evil-buttons/README.md), [`feralui/`](feralui/README.md), [`halaska/`](halaska/README.md), [`kobra/`](kobra/README.md), [`libraries-dev/`](libraries-dev/README.md), [`liquid-glass/`](liquid-glass/README.md), [`amicro/`](amicro/README.md), [`annnimate/`](annnimate/README.md), [`kinetics/`](kinetics/README.md), [`jakubkrehel-skills/`](jakubkrehel-skills/README.md), [`keyline-icons/`](keyline-icons/README.md), [`openui/`](openui/README.md), [`page-mascot/`](page-mascot/README.md), [`xiod/`](xiod/README.md), [`vibeprompts/`](vibeprompts/README.md), [`book-of-shapes/`](book-of-shapes/README.md), [`playgrnd/`](playgrnd/README.md), [`quiver-ai/`](quiver-ai/README.md), [`kage/`](kage/README.md), [`typeface-fyi/`](typeface-fyi/README.md), [`uisfx/`](uisfx/README.md), [`specialized-galleries/`](specialized-galleries/README.md), [`md-resources/`](md-resources/README.md)



Contributions: open a pull request that adds a folder from [`../templates/reference-template/`](../templates/reference-template/) plus a catalog row; entries are merged after maintainer review.


