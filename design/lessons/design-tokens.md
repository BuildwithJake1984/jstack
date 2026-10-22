---
type: lesson
title: Design Tokens in a Design System
slug: design-tokens
date: 2026-10-22
tags: [design, design-system, tokens, figma, css, tailwind, theming]
purpose: Define and tier tokens so design tools and code share one naming system.
status: published
---

# Design Tokens in a Design System

## When to use

- Starting or refactoring a design system for color, type, spacing, or radius.
- Preparing Figma variables, Paper tokens, or Tailwind/CSS custom properties to match.
- Debugging inconsistent UI or planning dark mode and theming.

Hard-coded hex values and one-off spacing in components feel fast until you ship dark mode, rebrand, or a second product surface. **Design tokens** are the shared vocabulary that keeps visual decisions consistent from Figma or Paper through to CSS and Tailwind.

## What design tokens are

A **design token** is a named, reusable design decision: a color, font size, spacing step, border radius, shadow, or motion duration. Tokens store the *value* (or reference to another token) and a *name* the whole team agrees on.

Tokens are not the same as raw CSS in every file, and they are not the same as a single Figma paint style without a naming system. They are the **contract** between design tools and code.

## Why they matter

### Consistency

When every button uses `color.action.primary` instead of `#2563eb`, marketing pages, settings screens, and agent-generated UI pull from the same source. Reviews get easier because “wrong blue” becomes a token mismatch, not a subjective argument.

### Theming and dark mode

Semantic tokens (for example `surface.default` and `text.primary`) can swap values per theme while component code keeps referencing the same names. Light and dark become data changes, not a wholesale component rewrite.

### Design-to-dev handoff

Developers should not re-measure padding from a screenshot. Tokens export as **CSS custom properties**, **Tailwind theme keys**, or platform-specific resources so implementation matches the system file.

### Scaling products and teams

As libraries grow, tokens let you add a brand variant, density mode, or new platform by updating tiers—not by searching the repo for `#1a1a1a`.

## Token tiers

Most mature systems use layered tokens:

| Tier | Also called | Role | Example |
| --- | --- | --- | --- |
| **Primitive / global** | Core, foundation | Raw palette and scales | `blue.500`, `space.4`, `font.size.16` |
| **Semantic / alias** | Decision, role | Meaning in UI | `color.text.primary`, `color.border.subtle` |
| **Component** | Composite | Slot on a specific component | `button.primary.background`, `input.focus.ring` |

**Rule of thumb:** components reference semantic tokens; semantic tokens reference primitives. Avoid components pointing straight at `blue.500` unless it is intentional.

## Naming conventions

Pick one scheme and document it:

- **Category–property–variant:** `color-bg-surface-raised`, `font-size-body-md`
- **Dot notation:** `color.text.primary`, `space.stack.md` (common in code export)
- **Scale indices:** `spacing.1` … `spacing.8` mapped to a rem table

Whatever you choose, be consistent across Figma variables, Paper tokens, and code. Prefer **stable semantic names** over literal names like `gray-700-text` that break when the palette shifts.

## Examples by category

### Color

```text
primitive: color.blue.600     → #2563eb
semantic:  color.action.primary → {color.blue.600}
semantic:  color.text.primary   → {color.neutral.900}
component: button.primary.bg     → {color.action.primary}
```

### Typography

```text
font.family.sans   → "Inter", system-ui, sans-serif
font.size.body.md  → 1rem
font.lineheight.body.md → 1.5
font.weight.heading → 600
```

### Spacing and radius

```text
space.1 → 0.25rem
space.4 → 1rem
radius.sm → 0.25rem
radius.lg → 0.75rem
```

Document the **spacing scale** (linear, geometric, or hybrid) so agents do not invent `13px` gaps.

## From Figma or Paper into code

### Figma variables

See also: [Figma tool reference](../tools/figma.md).

Define primitives and semantics as **variables** and publish them through your library. Dev Mode and export tooling (plus team integrations such as MCP or Code Connect, where you use them) should read the same names developers implement.

Typical CSS output:

```css
:root {
  --color-text-primary: #111827;
  --color-surface-default: #ffffff;
  --space-4: 1rem;
}
```

### Paper

See also: [Paper tool reference](../tools/paper.md).

Paper documents **tokens and themes** on canvas and supports syncing token/style context with code via agent workflows. Treat Paper as another consumer of the same semantic names you maintain in Figma or in the repo.

### Tailwind

Map tokens in `tailwind.config` theme extension:

```js
theme: {
  extend: {
    colors: {
      surface: {
        DEFAULT: "var(--color-surface-default)",
        raised: "var(--color-surface-raised)",
      },
    },
    spacing: {
      4: "var(--space-4)",
    },
  },
},
```

Prefer **CSS variables as the bridge** so runtime theming does not require rebuilding Tailwind for every brand switch.

## Common mistakes

- **Skipping semantics** — components bind to primitives; rebranding breaks everything.
- **Duplicate names** — `primary` means blue in one file and brand green in another.
- **Unbounded scales** — forty spacing steps nobody can remember.
- **One-off tokens** — a new token for every PR instead of extending the scale.
- **Tool drift** — Figma, Paper, and CSS use different names for the same role.
- **No dark-mode plan** — only light values defined at the semantic layer.

## Starter checklist

1. Audit existing colors, type, spacing, and radius; cluster into primitives.
2. Define semantic tokens for text, surfaces, borders, and actions.
3. Document naming rules in one page (link from `design/lessons/` and your repo `AGENTS.md`).
4. Publish Figma variables (or Paper tokens) and match names in CSS/Tailwind.
5. Refactor one vertical slice (for example buttons + forms) to prove the pipeline.
6. Add a theme switch (light/dark) by swapping semantic values only.
7. Schedule a quarterly token review when brand or density requirements change.

## Jake's take

<!-- Jake's input goes here -->
