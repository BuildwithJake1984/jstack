# JStack write-up conventions

Lessons, tools, skills, and reference notes share one shape so humans and agents can scan them quickly.

## Structure

1. **YAML frontmatter** (required keys below).
2. **`#` title** — matches `title` in frontmatter.
3. **`## When to use`** — a few bullets: when to open this file.
4. **Body** — the lesson, tool notes, or skill instructions.

Optional sections (tools): `## Capabilities`, `## Access and pricing`, `## Use notes`, `## Jake's take`, `## Sources`.

## Frontmatter

| Key | Lessons | Tools | Skills | References (ui-libraries) |
| --- | --- | --- | --- | --- |
| `type` | `lesson` | `tool` | `skill` | `reference` (follow-up for link-outs) |
| `title` | required | required | — | required |
| `purpose` | required (one line) | required | required | follow-up |
| `tags` | required list | required list | required list | follow-up |
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

### Skill (`SKILL.md`)

```markdown
---
type: skill
name: skill-folder-name
description: Short loader line (when to invoke this skill).
tags: [design, ui]
purpose: One line on the outcome this skill helps you produce.
---

# Skill display name

## When to use

- Building or reviewing …

(rest of skill content unchanged)
```

### Reference (ui-libraries link-outs)

Existing folders under `design/ui-libraries/` still use the older frontmatter shape. **Follow-up:** migrate them to `type: reference` and add `purpose` + `## When to use` in a dedicated pass.

## CI

Pull requests must satisfy the frontmatter job for:

- `*/lessons/*.md` (except `README.md`)
- `design/tools/*/README.md` (not the catalog `design/tools/README.md`)
- `**/skills/**/SKILL.md`
