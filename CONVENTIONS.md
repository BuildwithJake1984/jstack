# JStack write-up conventions

Lessons, tools, skills, and reference notes share one shape so humans and agents can scan them quickly.

## Structure

1. **YAML frontmatter** (required keys below).
2. **`#` title** — matches `title` in frontmatter.
3. **`## When to use`** — a few bullets: when to open this file.
4. **Body** — the lesson, tool notes, or skill instructions.

Optional sections (tools): `## Capabilities`, `## Access and pricing`, `## Use notes`, `## Jake's take`, `## Sources`.

## Workflows

`workflows/` is the one section that uses **per-project subfolders** (`workflows/<project-name>/`). Lessons, tools, design skills, and ui-library references stay in the flat catalog paths described below; only workflow projects nest under their own folder. Add a subfolder when a real project is ready—start with `README.md` inside it—and list it from [`workflows/README.md`](workflows/README.md). Do not commit empty placeholder project folders.

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

### Tool (`design/tools/<name>/README.md`)

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
```

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

## CI

Pull requests must satisfy the frontmatter job for:

- `*/lessons/*.md` (except `README.md`)
- `design/tools/*/README.md` (not the catalog `design/tools/README.md`)
- `design/ui-libraries/*/README.md` (not the catalog `design/ui-libraries/README.md`)
- `design/skills/*.md` (not `design/skills/README.md`)
- `ai-agents/skills/**/SKILL.md` and `development/skills/**/SKILL.md`
- `*/templates/**/*.md` (catalog `*/templates/README.md` excluded; YAML parse when frontmatter is present)
- `updates/*.md` (except `updates/README.md`; YAML parse when frontmatter is present)

Frontmatter must be valid YAML (`yaml.safe_load`); schema rules apply to lessons, tools, skills, and references.
