# JStack write-up conventions

Lessons, tools, skills, and reference notes share one shape so humans and agents can scan them quickly.

## Structure

1. **YAML frontmatter** (required keys below).
2. **`#` title** — matches `title` in frontmatter.
3. **`## When to use`** — a few bullets: when to open this file.
4. **Body** — the lesson, tool notes, or skill instructions.

Optional sections (tools): extra subsections under `## What it can do` when needed; `## Sources` is required when citing vendor pages.

## Catalog layout

Choose a top-level section by the reader's outcome or the content's role before choosing a technology subcategory:

| Section | What belongs here |
| --- | --- |
| [`personal-workflows/`](personal-workflows/README.md) | Guidance for personal outcomes and everyday life |
| [`business-workflows/`](business-workflows/README.md) | Guidance for business outcomes, including the existing product-design skill catalog |
| [`libraries/`](libraries/README.md) | Reusable tools, UI references, templates, and guides |
| [`insights/`](insights/README.md) | Lessons, thoughts, observations, and the existing external-news digest |
| [`updates/`](updates/README.md) | Monthly updates about J-Stack itself |

**One markdown file per standalone catalog item** — no per-item subfolders. Each catalog keeps a single `README.md` index linking to sibling `.md` files with a one-line purpose. Real workflow projects and vendored skill packages are the exceptions described below.

| Area | Item path | Index |
| --- | --- | --- |
| Lessons | `insights/<area>/<slug>.md` | `insights/<area>/README.md` |
| AI agent tools | `libraries/tools/ai-agents/<name>.md` | `libraries/tools/ai-agents/README.md` |
| Development tools | `libraries/tools/development/<name>.md` | `libraries/tools/development/README.md` |
| Marketing tools | `libraries/tools/marketing/<name>.md` | `libraries/tools/marketing/README.md` |
| Design tools | `libraries/tools/design/<name>.md` | `libraries/tools/design/README.md` |
| UI libraries | `libraries/ui-libraries/<name>.md` | `libraries/ui-libraries/README.md` |
| Design skills | `business-workflows/design/skills/<name>.md` | `business-workflows/design/README.md` |
| Other outcome skills | `<workflow-section>/<outcome>/skills/<name>.md` | outcome or skills `README.md` |
| Vendored skills | `<workflow-section>/<outcome>/skills/<name>/SKILL.md` | outcome or skills `README.md` |
| Templates | `libraries/templates/<area>/<name>.md` | `libraries/templates/<area>/README.md` |
| Guides | `libraries/guides/<name>.md` | `libraries/guides/README.md` |

`<workflow-section>` means `personal-workflows` or `business-workflows`. Existing subject areas are `ai-agents`, `design`, `development`, and `marketing`; retain these useful groupings below the outcome/content sections. When the best outcome is unclear, retain the resource, explain the provisional placement, and cross-link it rather than discarding it or inventing a workflow.

For `kind: media-set` references, put URL tables in a `## Media` section inside the same file (not a sibling `media.md`).

Use lowercase-hyphen names for new content folders and ordinary Markdown filenames. Keep conventional `README.md` indexes, upstream `SKILL.md` filenames, and root documents such as `GETTING_STARTED.md`, `TERMS.md`, and `CONVENTIONS.md`. Monthly updates use the deliberate exception `YYYY_MM_update.md` (for example `2026_11_update.md`). Preserve infrastructure and code filenames.

## Category by use, not tech

Within the five sections, group content by what the reader is trying to do, not the vendor's technical label:

- **Marketing** — campaigns, creative production, ads, email copy, growth, and GTM tooling (including AI video/voice tools used for marketing).
- **AI agents** — frontier models, coding agents, and product AI features in the application.
- **Development** — runtime infrastructure: data, hosting, frameworks, git, transactional email APIs, and shipping.
- **Design** — product UI, design systems, and design research tools.

Example: an AI voice API used for **ads and promos** belongs in `libraries/tools/marketing/`; the same vendor's **in-app assistant API** could belong in `libraries/tools/ai-agents/`. A guide to achieving a particular business result belongs under `business-workflows/` and links to the reusable tool reference. Personal outcomes belong under `personal-workflows/` even when they use the same tools.

## Workflows

Use **per-project subfolders** for real workflow projects under `personal-workflows/` or `business-workflows/`. Start a project with its `README.md` and supporting Markdown, then list it from the relevant section index. The retained [project-playbook index](business-workflows/project-playbooks/README.md) has no published projects yet. Do not commit empty placeholder project folders or present examples as completed workflows.

Standalone catalog entries remain flat in their catalog folders. A vendored skill may retain its own router and supporting files as described in [Skill — vendored](#skill--vendored).

## Read-only guidance and consent

J-Stack is a read-only guide, not an automation engine. Reading an entry, following a link, or finding a relevant skill does not install or activate it, grant account access, or authorize any action. Explain the resource and offer a walkthrough; separately obtain the user's authorization before any supported account change, installation, message, or other action. The host's permissions and the user's project instructions still apply.

Start with [Getting Started](GETTING_STARTED.md). Keep terms consent separate from account-connection consent and optional monthly-check scheduling consent. [TERMS.md](TERMS.md) is a **draft for legal review**; its setup consent wording is a preview pending legal review and owner approval, not a claim of enforceability or a replacement for the repository and third-party licenses. Do not activate integrations, scheduling, question delivery, or telemetry merely because a reader opened the guide.

The monthly [update conventions](updates/README.md) define stable entry IDs. The [relevance-check guide](libraries/guides/monthly-relevance-check.md) explains entry-level deduplication and matching against the full catalog; this repository does not implement a scheduler or private delivery ledger.

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

**News & Insights** (`type: news-insights` in `insights/news-and-insights/`): `title`, `date`, `week_of`, `status` (`draft` \| `published`), `tags`, `purpose`, and `sources` (non-empty list of URLs) are required. See the [News & Insights template](#news--insights-template) below.

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

### Tool

Tool entries use `libraries/tools/<area>/<name>.md`.

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

Where to follow releases (blog, changelog, docs, GitHub releases, X) and link to [`insights/news-and-insights/README.md`](../../../insights/news-and-insights/README.md). State whether the tool is in the weekly sweep.

## Sources

Pages checked for this reference (YYYY-MM-DD):

- https://example.com/ — what you verified
```

### Skill — outcome catalog

Use one Markdown file per skill catalog entry under the relevant outcome, such as `business-workflows/design/skills/<name>.md`. A catalog entry points to the executable skill (upstream repo or a vendored `SKILL.md` elsewhere in this repo); it is not activation or authorization to run that skill. Keep link-out entries flat rather than nesting a folder for each entry.

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

### Skill — vendored

When a skill's full instructions live in this repo (no external source), keep the router `SKILL.md` and detail files under `<workflow-section>/<outcome>/skills/<name>/`. Link to the router from the relevant catalog entry. Preserve upstream package layout, attribution, and license requirements; do not install or execute the package as part of reading the catalog.

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

### News & Insights template

Path: `insights/news-and-insights/YYYY-MM-DD-news-and-insights.md`.

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

- [Build AI Features as a Graph, Not One Giant Prompt](../ai-agents/build-ai-features-as-a-graph.md) — explain why it is relevant

When you name a stack tool that has a JStack tool file, **link the tool name** to that file (relative path), for example [Claude](../../libraries/tools/ai-agents/claude.md) or [Supabase](../../libraries/tools/development/supabase.md)—do not mention the tool as plain text only.

## What the analysts are saying (optional)

Use when [analysts and commentators](README.md#analysts-and-commentators) add useful comparison or context on a story already anchored to an official source.

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

- `insights/<area>/*.md`, where `<area>` is `ai-agents`, `design`, `development`, or `marketing` (except each `README.md`)
- `libraries/tools/<area>/*.md`, for those same four areas (except each `README.md`)
- `libraries/ui-libraries/*.md` (except `README.md`)
- `personal-workflows/**/skills/*.md` and `business-workflows/**/skills/*.md` (except each `README.md`)
- `personal-workflows/**/skills/*/SKILL.md` and `business-workflows/**/skills/*/SKILL.md`
- `libraries/templates/<area>/**/*.md`, for those same four areas (top-level catalog `README.md` excluded; YAML parse when frontmatter is present)
- `updates/*.md` (except `updates/README.md`; YAML parse when frontmatter is present)
- `insights/news-and-insights/*.md` (except `README.md`)

Frontmatter must be valid YAML (`yaml.safe_load`); schema rules apply to lessons, tools, skills, references, and news-insights articles. Navigation indexes and plain setup/guidance documents do not need catalog frontmatter. Existing Markdown lint, offline relative-link, secret-scanning, and allowed-file checks remain in place.
