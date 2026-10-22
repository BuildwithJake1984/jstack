# News & Insights

Weekly digests of product news, releases, and platform changes from the tools and AI labs that matter to JStack. Each issue is written in our voice: we **repurpose, never copy**—rewrite every item, explain why it matters, and link the original source.

This folder is **separate from** [`updates/`](../updates/README.md), which remains the consolidated changelog of **JStack itself** (new lessons, skills, tools, and other material published in this repo).

## File naming

One markdown file per calendar week:

`news-and-insights/YYYY-MM-DD-news-and-insights.md`

The date in the filename is the **Monday** that starts that week (ISO week, local convention: use the Monday date even when the article is published later in the week).

Examples:

- `news-and-insights/2026-10-26-news-and-insights.md` — week of Monday 26 October 2026

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
3. **Source link** — Each item ends with a link to the primary official announcement or doc (see body template in [CONVENTIONS.md](../CONVENTIONS.md)).
4. **Related JStack** — Tie items to relevant lessons, tools, or skills in this repo when they exist.

Follow the `news-insights` template in [CONVENTIONS.md](../CONVENTIONS.md) for frontmatter and body structure.

## Sources we watch

Track both **official sites / feeds** and **X (Twitter) accounts** where teams ship news. Include any tool added to JStack later (new rows in `design/tools/`, integrations, etc.) using the same rules: official channels first; add feeds to this README when verified.

### AI frontier labs

| Source | Notes |
| --- | --- |
| Anthropic / Claude | Website, blog, docs; X: [@Anthropic](https://x.com/Anthropic), [@Claude](https://x.com/Claude) |
| OpenAI | Website, blog, platform docs; X: [@OpenAI](https://x.com/OpenAI) |
| xAI / Grok, Grok Bot | Website, docs; X: [@xai](https://x.com/xai), [@grok](https://x.com/grok) |
| Google (Gemini, AI studio, cloud AI) | Google AI blog and product pages; X: Google / DeepMind accounts as relevant |
| Meta (incl. Muse) | AI blog and product news; X: Meta AI accounts as relevant |

### Platform and stack (JStack catalog and peers)

| Source | Notes |
| --- | --- |
| Supabase | Blog, changelog, docs; X: [@supabase](https://x.com/supabase) |
| Railway | Blog, changelog; X: [@Railway](https://x.com/Railway) |
| Paper | Product updates; X as listed on official site |
| Next.js | Blog, releases; X: [@nextjs](https://x.com/nextjs) |
| Vercel | Blog, changelog; X: [@vercel](https://x.com/vercel) |
| GitHub | Changelog, blog; X: [@github](https://x.com/github) |
| Resend | Blog, changelog; X: [@resend](https://x.com/resend) |
| Figma | Blog, release notes; X: [@figma](https://x.com/figma) |

Add new JStack tools here when they land in the repo (feed URL: **TBD** until verified).

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

Official RSS/Atom URLs are **not listed** for: Anthropic (primary site), Google, Meta, Supabase, Railway, Paper, Next.js, Vercel, GitHub (beyond per-repo release atoms above), Resend, and Figma. Add rows here only after a feed is verified—do not invent URLs.

## Index

Weekly issues appear in this folder as they are published. Newest files sort by Monday date in the filename.
