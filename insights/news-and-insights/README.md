# News & Insights

Weekly digests of product news, releases, and platform changes from the tools and AI labs that matter to JStack. Each issue is written in our voice: we **repurpose, never copy**—rewrite every item, explain why it matters, and link the original source.

This folder is **separate from** [`updates/`](../../updates/README.md), which remains the consolidated changelog of **JStack itself** (new lessons, skills, tools, and other material published in this repo).

## File naming

One markdown file per calendar week:

`insights/news-and-insights/YYYY-MM-DD-news-and-insights.md`

The date in the filename is the **Monday** that starts that week (ISO week, local convention: use the Monday date even when the article is published later in the week).

Examples:

- `insights/news-and-insights/2026-10-26-news-and-insights.md` — week of Monday 26 October 2026

The article **H1** uses a slash date and the section title, for example:

`# 2026/10/26 News & Insights`

(`title` in frontmatter should match that heading.)

## Cadence

- **One article per week**, covering the prior seven days (or the window agreed for that issue).
- Open a **draft pull request** when the weekly issue is ready for review.
- **Jake reviews every News & Insights PR.** These PRs are **never auto-merged** and stay **draft** until he explicitly approves and marks ready for merge.
- After merge, set frontmatter `status: published` (or merge only when already `published`, per reviewer direction).

## Content rules

1. **Repurpose, never copy** — Do not paste vendor copy, release notes, or posts. Summarize each item in our words.
2. **Why it matters** — Every item should make clear what changed and why a JStack reader should care.
3. **Source link** — Each item ends with a link to the primary official announcement or doc (see body template in [CONVENTIONS.md](../../CONVENTIONS.md)).
4. **Related JStack** — Tie items to relevant lessons, tools, or skills in this repo when they exist.
5. **JStack tool links** — Every mention of a tool that has a JStack tool file must link to that file with a relative path (for example [`../../libraries/tools/ai-agents/claude.md`](../../libraries/tools/ai-agents/claude.md), [`../../libraries/tools/development/vercel.md`](../../libraries/tools/development/vercel.md), [`../../libraries/tools/design/figma.md`](../../libraries/tools/design/figma.md)), including tools **outside** the weekly sweep below.

Follow the `news-insights` template in [CONVENTIONS.md](../../CONVENTIONS.md) for frontmatter and body structure.

## Sources we follow

The weekly sweep covers **only** the vendors in the tables below (major labs, shipping stack, and core design tools). Official sites and X accounts are the primary channels; add verified RSS/Atom URLs in the feeds section when confirmed.

**Out of scope for the weekly sweep** (still cataloged in JStack—link to their tool files if you mention them elsewhere):

- [`screenshot-to-code.md`](../../libraries/tools/design/screenshot-to-code.md), [`shotbase.md`](../../libraries/tools/design/shotbase.md), [`voicestudio.md`](../../libraries/tools/design/voicestudio.md) — utilities, not major platform vendors.
- [`libraries/tools/marketing/`](../../libraries/tools/marketing/README.md) — marketing creative tools (for example Higgsfield, ElevenLabs).

### AI agents (`libraries/tools/ai-agents/`)

| JStack file | Follow for news |
| --- | --- |
| [Claude / Anthropic](../../libraries/tools/ai-agents/claude.md) | anthropic.com, docs.anthropic.com; X: [@Anthropic](https://x.com/Anthropic), [@Claude](https://x.com/Claude) |
| [OpenAI](../../libraries/tools/ai-agents/openai.md) | openai.com, platform.openai.com/docs; X: [@OpenAI](https://x.com/OpenAI) |
| [xAI / Grok](../../libraries/tools/ai-agents/xai.md) | x.ai, docs.x.ai; X: [@xai](https://x.com/xai), [@grok](https://x.com/grok) |
| [Google / Gemini](../../libraries/tools/ai-agents/google.md) | ai.google, gemini.google.com, ai.google.dev; X: [@GoogleDeepMind](https://x.com/GoogleDeepMind), [@GeminiApp](https://x.com/GeminiApp) |
| [Meta / Meta AI / Muse](../../libraries/tools/ai-agents/meta-muse.md) | ai.meta.com, meta.ai; X: [@MetaAI](https://x.com/MetaAI) |
| [Cursor](../../libraries/tools/ai-agents/cursor.md) | cursor.com, docs.cursor.com; X: [@cursor](https://x.com/cursor) |

### Development (`libraries/tools/development/`)

| JStack file | Follow for news |
| --- | --- |
| [Supabase](../../libraries/tools/development/supabase.md) | supabase.com, supabase.com/docs; X: [@supabase](https://x.com/supabase) |
| [Railway](../../libraries/tools/development/railway.md) | railway.com, docs.railway.com; X: [@Railway](https://x.com/Railway) |
| [Vercel](../../libraries/tools/development/vercel.md) | vercel.com, vercel.com/docs; X: [@vercel](https://x.com/vercel) |
| [Next.js](../../libraries/tools/development/nextjs.md) | nextjs.org, nextjs.org/docs; X: [@nextjs](https://x.com/nextjs) |
| [GitHub](../../libraries/tools/development/github.md) | github.com, docs.github.com; X: [@github](https://x.com/github) |
| [Resend](../../libraries/tools/development/resend.md) | resend.com, resend.com/docs; X: [@resend](https://x.com/resend) |

### Design (`libraries/tools/design/`)

| JStack file | Follow for news |
| --- | --- |
| [Paper](../../libraries/tools/design/paper.md) | paper.design; X: [@paper](https://x.com/paper) |
| [Figma](../../libraries/tools/design/figma.md) | figma.com; X: [@figma](https://x.com/figma) |
| [Mobbin](../../libraries/tools/design/mobbin.md) | mobbin.com; X: [@mobbin](https://x.com/mobbin) |
| [Canva](../../libraries/tools/design/canva.md) | canva.com; X: [@canva](https://x.com/canva) |

### Analysts and commentators

For **tool comparisons and analysis** (not official vendor announcements). Cadence is a guide for the weekly sweep—not a hard rule.

**Weekly**

| Name | X | Focus |
| --- | --- | --- |
| Matt Wolfe | [@mreflow](https://x.com/mreflow) | Tool comparisons |
| Theo | [@theo](https://x.com/theo) | Next.js, Vercel, and AI coding |
| Matthew Berman | [@MatthewBerman](https://x.com/MatthewBerman) | AI labs and agents |
| Alex Volkov (ThursdAI) | [@altryne](https://x.com/altryne) | Weekly AI news show |
| Ray Fernando | [@RayFernando1337](https://x.com/RayFernando1337) | Hands-on model testing |

**Occasional**

| Name | X | Focus |
| --- | --- | --- |
| swyx | [@swyx](https://x.com/swyx) | AI engineering |
| Jake (Railway founder; not neutral) | [@JustJake](https://x.com/JustJake) | Railway updates |
| shadcn | [@shadcn](https://x.com/shadcn) | Design and front end |
| Lee Robinson | [@leerob](https://x.com/leerob) | Agent explainers |
| Riley Brown | [@rileybrown](https://x.com/rileybrown) | Vibe-coding and agent tools |

When their takes appear in a weekly issue:

- **Credit by name** (for example “Matthew Berman argues…”).
- Label the item as **analysis**, not official news.
- **Verify against the official source** (vendor blog, changelog, or docs) before stating anything as fact; use analyst posts for framing or comparison only when the primary source checks out.

Optional body section: **What the analysts are saying** (see [CONVENTIONS.md](../../CONVENTIONS.md) news-insights template).

Add a row when a new tool joins the **sweep** list in one of these folders. Do not invent feed URLs—update the verified feeds section below when confirmed.

## Verified feeds and check pages

### RSS / Atom (verified)

| Feed | URL |
| --- | --- |
| OpenAI news | https://openai.com/news/rss.xml |
| GitHub releases — `anthropics/claude-code` | https://github.com/anthropics/claude-code/releases.atom |
| GitHub releases — `anthropics/anthropic-sdk-python` | https://github.com/anthropics/anthropic-sdk-python/releases.atom |
| GitHub releases — `openai/codex` | https://github.com/openai/codex/releases.atom |
| GitHub releases — `openai/openai-python` | https://github.com/openai/openai-python/releases.atom |
| GitHub releases — `xai-org/xai-sdk-python` | https://github.com/xai-org/xai-sdk-python/releases.atom |

### Unofficial community mirrors (use with judgment; label as unofficial in the article when cited)

Hosted at https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/:

- `feed_anthropic_news.xml`
- `feed_anthropic_engineering.xml`
- `feed_xainews.xml`

### Change-checked pages (no feed; poll or manual review)

| Source | URL |
| --- | --- |
| Claude release notes | https://docs.claude.com/en/release-notes/overview |
| OpenAI platform changelog | https://platform.openai.com/docs/changelog |
| xAI release notes | https://docs.x.ai/docs/release-notes |

### Feed TBD

Official RSS/Atom URLs are **not listed** for: Anthropic (primary site), Cursor, Google, Meta, Supabase, Railway, Paper, Next.js, Vercel, GitHub (beyond per-repo release atoms above), Resend, and Figma. Add rows only after a feed is verified—do not invent URLs.

## Index

Weekly issues appear in this folder as they are published. Newest files sort by Monday date in the filename.
