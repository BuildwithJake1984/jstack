# JStack write-up conventions

Lessons, tools, skills, and reference notes share one shape so humans and agents can scan them quickly.

## Structure

1. **YAML frontmatter** (required keys below).
2. **`#` title** — matches `title` in frontmatter.
3. **`## When to use`** — a few bullets: when to open this file.
4. **Body** — the lesson, tool notes, or skill instructions.

Optional sections (tools): extra subsections under `## What it can do` when needed; `## Sources` is required when citing vendor pages.

## Catalog layout

**One markdown file per catalog item** — no per-item subfolders. Each category folder keeps a single `README.md` index that links to sibling `.md` files with a one-line purpose.

| Area | Item path | Index |
| --- | --- | --- |
| Lessons | `*/lessons/<slug>.md` | `*/lessons/README.md` |
| AI agent tools | `ai-agents/tools/<name>.md` | `ai-agents/tools/README.md` |
| Development tools | `development/tools/<name>.md` | `development/tools/README.md` |
| Marketing tools | `marketing/tools/<name>.md` | `marketing/tools/README.md` |
| Design tools | `design/tools/<name>.md` | `design/tools/README.md` |
| UI libraries | `design/ui-libraries/<name>.md` | `design/ui-libraries/README.md` |
| Design skills | `design/skills/<name>.md` | _(listed in `design/README.md`)_ |
| Vendored skills | `ai-agents/skills/<name>/SKILL.md`, `development/skills/<name>/SKILL.md` | category `skills/README.md` |

For `kind: media-set` references, put URL tables in a `## Media` section inside the same file (not a sibling `media.md`).

## Category by use, not tech

Pick the **top-level category folder** from what the reader is trying to do, not from the vendor's technical label.

- **Marketing** (`marketing/`) — campaigns, creative production, ads, email copy, growth, and GTM tooling (including AI video/voice tools used for marketing).
- **AI agents** (`ai-agents/`) — frontier models, coding agents, and product AI features in the application.
- **Development** (`development/`) — runtime infrastructure: data, hosting, frameworks, git, transactional email APIs, and shipping.
- **Design** (`design/`) — product UI, design systems, and design research tools.

Example: an AI voice API used for **ads and promos** → `marketing/tools/`; the same vendor's **in-app assistant API** would still be documented under `ai-agents/` or product code, not marketing.

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

**News & Insights** (`type: news-insights` in `news-and-insights/`): `title`, `date`, `week_of`, `status` (`draft` \| `published`), `tags`, `purpose`, and `sources` (non-empty list of URLs) are required. See the [News & Insights template](#news--insights-news-and-insightsyyyy-mm-dd-news-and-insightsmd) below.

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

### Tool (`design/tools/<name>.md`, `ai-agents/tools/<name>.md`, `development/tools/<name>.md`, `marketing/tools/<name>.md`)

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

## What it is

One or two paragraphs grounded in official product/docs pages.

## What it can do

### Feature area one

Short paragraph on what it does and how it helps—not a one-liner bullet list.

### Feature area two

…

## How it fits Jake's stack

How Jake uses the tool with sibling JStack links where relevant.

## News and insights

Where to follow releases (blog, changelog, docs, GitHub releases, X) and link to [`news-and-insights/README.md`](../news-and-insights/README.md). State whether the tool is in the weekly sweep.

## Sources

Pages checked for this reference (YYYY-MM-DD):

- https://example.com/ — what you verified
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

### News & Insights (`news-and-insights/YYYY-MM-DD-news-and-insights.md`)

Weekly external news digest (not the JStack changelog—see [`updates/`](updates/README.md)). Filename date is that week's **Monday**. Heading format: `# YYYY/MM/DD News & Insights` (slashes in the H1; `title` in frontmatter matches).

```markdown
---
type: news-insights
title: YYYY/MM/DD News & Insights
date: YYYY-MM-DD
week_of: YYYY-MM-DD
status: draft
tags: [news, weekly]
purpose: One line on what this week's digest covers.
sources:
  - https://example.com/official-announcement
---

# YYYY/MM/DD News & Insights

Short intro: what week this covers and the themes in this issue.

## Company — short update title

### What is the update?

…

### Who does it affect?

…

### How could it affect you?

…

**Source:** [Official announcement](https://example.com/official-announcement)

## Related JStack lessons and tools

- [Lesson or tool title](../path/to/item.md) — why it is relevant

When you name a stack tool that has a JStack tool file, **link the tool name** to that file (relative path), for example [Claude](../ai-agents/tools/claude.md) or [Supabase](../development/tools/supabase.md)—do not mention the tool as plain text only.

## What the analysts are saying (optional)

Use when [analysts and commentators](../news-and-insights/README.md#analysts-and-commentators) add useful comparison or context on a story already anchored to an official source.

- Credit each person **by name**; label content as **analysis**, not vendor news.
- Do not state facts unless they are **checked against the official announcement** (blog, changelog, docs, or release page) cited in the item’s **Source** link.
- Link to the analyst’s post on X when you reference their view (for example [Matthew Berman on X](https://x.com/MatthewBerman)).

…
```

Use `status: draft` until Jake approves the PR; set `status: published` when the issue is live. `week_of` must match the Monday in the filename. `sources` in frontmatter is the list of primary URLs cited in the issue (official announcements, docs, or release pages).

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
- `ai-agents/tools/*.md` (not `ai-agents/tools/README.md`)
- `development/tools/*.md` (not `development/tools/README.md`)
- `marketing/tools/*.md` (not `marketing/tools/README.md`)
- `design/ui-libraries/*.md` (not the catalog `design/ui-libraries/README.md`)
- `design/skills/*.md` (not `design/skills/README.md`)
- `ai-agents/skills/**/SKILL.md` and `development/skills/**/SKILL.md`
- `*/templates/**/*.md` (catalog `*/templates/README.md` excluded; YAML parse when frontmatter is present)
- `updates/*.md` (except `updates/README.md`; YAML parse when frontmatter is present)
- `news-and-insights/*.md` (except `news-and-insights/README.md`)

Frontmatter must be valid YAML (`yaml.safe_load`); schema rules apply to lessons, tools, skills, references, and news-insights articles.
