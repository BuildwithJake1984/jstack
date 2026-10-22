
---
name: make-interfaces-feel-better
description: When building or reviewing UI polish: components, animations, hover/focus states, shadows, borders, typography, icons, or micro-interactions.
---

# Make interfaces feel better

Design-engineering principles for polished UI. Apply when building or reviewing components, motion, surfaces, and micro-interactions. Express fixes in the project's existing styling system (Tailwind, CSS, or established CSS-in-JS)—never introduce a second one.

Before reviewing, slow motion to 10% in the browser Animations panel and walk every state: hover, focus, active, loading, empty.

## Core principles

1. **Concentric border radius** — outer = inner + padding.
2. **Optical over geometric alignment** — adjust asymmetric icons and buttons visually.
3. **Shadows for elevation, borders for structure** — layered transparent shadows for depth; borders for dividers and state.
4. **Interruptible animations** — CSS transitions for interactive state; keyframes for one-shot sequences.
5. **Split and stagger enter animations** — ~100ms stagger for infrequent staged entrances only.
6. **Subtle exit animations** — small fixed translateY, ease-out, softer than enters.
7. **Contextual icon animations** — opacity/scale/blur cross-fade; spring bounce 0.
8. **Font smoothing** — `-webkit-font-smoothing: antialiased` on macOS root.
9. **Tabular numbers** — `font-variant-numeric: tabular-nums` for dynamic values.
10. **Text wrapping** — `text-wrap: balance` on headings; `pretty` on body.
11. **Image outlines** — 1px pure black/white low-opacity outline, not tinted neutrals.
12. **Scale on press** — `scale(0.96)` on click; never below 0.95.
13. **Skip animation on page load** — `initial={false}` on AnimatePresence.
14. **Never `transition: all`** — specify exact properties.
15. **`will-change` sparingly** — only transform/opacity/filter when stutter observed.
16. **Minimum hit area** — 44×44px touch, 40×40px dense desktop.
17. **Match icon stroke to text weight** — 1.5px regular, 2px semibold.
18. **One SVG, recolored per state** — `currentColor`; outline default, fill active.
19. **Motion restraint** — no custom animation on high-frequency interactions.

## Detail files

| File | When to load |
| --- | --- |
| [typography.md](typography.md) | Text wrapping, font smoothing, tabular numbers |
| [surfaces.md](surfaces.md) | Border radius, optical alignment, shadows, image outlines, hit areas |
| [animations.md](animations.md) | Interruptible motion, enter/exit, icon animations, scale on press, motion restraint |
| [icons.md](icons.md) | Stroke weight, `currentColor` states, outline vs fill, sizing, RTL |
| [performance.md](performance.md) | Transition specificity, `will-change`, GPU compositing |

## Review modes

| Mode | Scope | Cap |
| --- | --- | --- |
| `quick` (default when unspecified) | Primary path; HIGH/MEDIUM only | 5 findings |
| `full` | All five detail files across requested scope | 15 findings |

Group findings by principle with Severity, Location, Before, After, Why. End with verification steps and a verdict: Block / Needs changes / Approve.

## Reference

Upstream: [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better). Broader `better-*` suite: [`ui-libraries/jakubkrehel-skills/`](../../ui-libraries/jakubkrehel-skills/README.md).


