# JStack write-up conventions

Lessons, tools, skills, and reference notes share one shape so humans and agents can scan them quickly.

## Structure

1. **YAML frontmatter** (required keys below).
2. **`#` title** — matches `title` in frontmatter.
3. **`## When to use`** — a few bullets: when to open this file.
4. **Body** — the lesson, tool notes, or skill instructions.

Optional sections (tools): `## Capabilities`, `## Access and pricing`, `## Use notes`, `## Jake's take`, `## Sources`.

## Catalog layout

**One markdown file per catalog item** — no per-item subfolders. Each category folder keeps a single `README.md` index that links to sibling `.md` files with a one-line purpose.

| Area | Item path | Index |
| --- | --- | --- |
| Lessons | `*/lessons/<slug>.md` | `*/lessons/README.md` |
| Design tools | `design/tools/<name>.md` | `design/tools/README.md` |
| UI libraries | `design/ui-libraries/<name>.md` | `design/ui-libraries/README.md` |
| Design skills | `design/skills/<name>.md` | _(listed in `design/README.md`)_ |
| Vendored skills | `ai-agents/skills/<name>/SKILL.md`, `development/skills/<name>/SKILL.md` | category `skills/README.md` |

For `kind: media-set` references, put URL tables in a `## Media` section inside the same file (not a sibling `media.md`).

## Workflows

`workflows/` is the **only** section that uses **per-project subfolders** (`workflows/<project-name>/`). Everything in the catalog table above stays flat. Add a workflow subfolder when a real project is ready—start with `README.md` inside it—and list it from [`workflows/README.md`](workflows/README.md). Do not commit empty placeholder project folders.

## Frontmatter

| Key | Lessons | Tools | Skills | References (ui-libraries) |
| --- | --- | --- | --- | --- |
| `type` | `lesson` | `tool` | `skill` | `reference` |
| `title` | required | required | — | required |
| `purpose` | required (one line) | required | required | required (one line) |
| `tags` | required list | required list | required list | required list |
| `slug` | required | — | — | — |
| `date` | required | — | — | — |
| `status` | required (`published` for lessons) | optional (`curated`, etc.) | — | optional |
| `name` | — | — | required (skill id) | — |
| `description` | — | — | required (loader summary) | — |

Keep any other keys already in use (`sources`, `kind`, etc.) unless `type` replaces them.

## Templates

### Lesson

```markdown
---
type: lesson
title: Your Lesson Title
slug: your-lesson-slug
date: YYYY-MM-DD
tags: [category, topic]
purpose: One line on what the reader will learn or decide.
status: published
---

# Your Lesson Title

## When to use

- You are …
- You need to …

## First section

Content…
```

### Tool (`design/tools/<name>.md`)

```markdown
---
type: tool
title: Tool Name — short subtitle
status: curated
tags: [tools, …]
purpose: One line on what this tool is for in your stack.
sources:
  - url: https://example.com/
    label: Official site
---

# Tool Name — short subtitle

## When to use

- Choosing or comparing …
- Setting up …

## Capabilities

…
```

### Skill — design catalog (`design/skills/<name>.md`)

One markdown file per skill under `design/skills/`. It is a catalog entry that points at the executable skill (upstream repo or a vendored `SKILL.md` elsewhere in this repo). Do not nest a skill folder under `design/skills/`.

```markdown
---
type: skill
name: skill-id
description: Short loader line (when to invoke this skill).
tags: [design, ui]
purpose: One line on the outcome this skill helps you produce.
---

# Skill display name

## When to use

- Building or reviewing …

Short summary of what the skill covers.

## Skill source

Link to the upstream or vendored skill (for example `SKILL.md` on GitHub).
```

### Skill — vendored (`<category>/skills/<name>/SKILL.md`)

When a skill's full instructions live in this repo (no external source), keep the router `SKILL.md` and detail files under `ai-agents/skills/` or `development/skills/` and link to that path from the design catalog file when applicable.

### Reference (ui-libraries link-outs)

```markdown
---
type: reference
title: Resource Name — short subtitle
purpose: One line on what this reference summarizes or links to.
status: curated
tags: [ui, …]
sources:
  - url: https://example.com/
    label: Official site
---

# Resource Name — short subtitle

## When to use

- Choosing or comparing …
- …

(body unchanged from prior digest)
```

## Skills audit standard

Governing checklist for operator skills, always-on agent instructions (`AGENTS.md`), and agent profiles. Read [Eric Provencher — Rethinking skills and prompts for GPT-6 Astra](https://x.com/pvncher/status/2095991462416490862) for context; do not invent article text.

1. **Descriptions** — as short as possible; clear WHEN; no pick-me; no overlapping triggers
2. **Skill count** — fewer is better; catalog pressure truncates descriptions
3. **Progressive disclosure** — root `SKILL.md` is a minimal router; detail in supporting docs loaded on demand
4. **Specificity** — drop elaborate itineraries that overconstrain; keep durable principles and true constraints
5. **Multi-model** — don't overfit to one model
6. **Always-on (`AGENTS.md`)** — every line must earn its place on every task
7. **Testing / verification** — no redundant always-run-all-tests
8. **Decision boundaries** — ask-first only for real risk; avoid premature stops
9. **Persistence / completion** — define done; don't force early review stops unless needed

Maintainer review audits every skill add or change against these nine points before merge (or records an explicit exception).

## CI

Pull requests must satisfy the frontmatter job for:

- `*/lessons/*.md` (except `README.md`)
- `design/tools/*.md` (not the catalog `design/tools/README.md`)
- `design/ui-libraries/*.md` (not the catalog `design/ui-libraries/README.md`)
- `design/skills/*.md` (not `design/skills/README.md`)
- `ai-agents/skills/**/SKILL.md` and `development/skills/**/SKILL.md`
- `*/templates/**/*.md` (catalog `*/templates/README.md` excluded; YAML parse when frontmatter is present)
- `updates/*.md` (except `updates/README.md`; YAML parse when frontmatter is present)

Frontmatter must be valid YAML (`yaml.safe_load`); schema rules apply to lessons, tools, skills, and references.
