# J-Stack

A free, read-only guide to workflows, reusable resources, and ideas for bringing AI into your life and business. Start with an outcome you care about; use the catalog to find relevant guidance and decide what to try.

## Start J-Stack

**[Start J-Stack — Getting Started](GETTING_STARTED.md)**

Read the guide yourself, or ask your assistant to walk through it with you. Opening this link does not install anything, execute skills or scripts, connect accounts, sync data, or schedule updates. J-Stack is guidance, not an automation engine or permission to act. Any actions need your separate authorization in the host you choose.

## Find your starting point

| Section | What you will find |
| --- | --- |
| [Personal Workflows](personal-workflows/README.md) | Guidance organized around personal outcomes; no personal playbooks are published yet |
| [Business Workflows](business-workflows/README.md) | Outcome-focused business and product work, including the existing interface-polish skill reference |
| [Libraries](libraries/README.md) | Reusable tool notes, UI libraries, templates, and J-Stack guidance |
| [Insights](insights/README.md) | Lessons, thoughts, observations, and the existing external-news reference collection |
| [Updates](updates/README.md) | Monthly author updates, with stable entry IDs for optional check-ins |

The older technology categories remain useful as subcategories, not the top-level navigation. See the [migration map](insights/repository-reorganization.md) for every existing file's new location and the choices still open for owner review.

## Find what is relevant to you

Tell your assistant what you want to achieve, or let it use only the relevant context that is actually available and permitted. It should scan the **whole catalog**, then read promising resources closely and explain a few useful matches. No match is a valid result. A walkthrough is an offer, not an instruction to execute a workflow.

Monthly suggestions are optional and depend on a scheduler provided by your host and your explicit consent. See the [monthly relevance-check guide](libraries/guides/monthly-relevance-check.md). J-Stack does not implement a scheduler, telemetry, or background account access.

## Existing catalog

The catalog below is preserved from the earlier AI Skills library. Skills can contain executable instructions, but reading or recommending one here does not activate it. Vendor notes are existing research, not a promise of current availability or integration with J-Stack; verify capabilities, prices, and licenses before use.

## Core stack

Canonical JStack tool files for Jake's AI labs, shipping infrastructure, and design/build tools. Use these paths when linking from [News & Insights](insights/news-and-insights/README.md) or lessons.

| Area | Tools |
| --- | --- |
| **AI agents** | [Claude](libraries/tools/ai-agents/claude.md) · [OpenAI](libraries/tools/ai-agents/openai.md) · [xAI / Grok](libraries/tools/ai-agents/xai.md) · [Google / Gemini](libraries/tools/ai-agents/google.md) · [Meta / Muse](libraries/tools/ai-agents/meta-muse.md) · [Cursor](libraries/tools/ai-agents/cursor.md) |
| **Development** | [Supabase](libraries/tools/development/supabase.md) · [Railway](libraries/tools/development/railway.md) · [Vercel](libraries/tools/development/vercel.md) · [Next.js](libraries/tools/development/nextjs.md) · [GitHub](libraries/tools/development/github.md) · [Resend](libraries/tools/development/resend.md) |
| **Design** (weekly news sweep) | [Paper](libraries/tools/design/paper.md) · [Figma](libraries/tools/design/figma.md) · [Mobbin](libraries/tools/design/mobbin.md) · [Canva](libraries/tools/design/canva.md) |
| **Design** (other references) | [Screenshot to Code](libraries/tools/design/screenshot-to-code.md) · [Shotbase](libraries/tools/design/shotbase.md) · [VoiceStudio](libraries/tools/design/voicestudio.md) |
| **Marketing** | [Higgsfield](libraries/tools/marketing/higgsfield.md) · [ElevenLabs](libraries/tools/marketing/elevenlabs.md) |

Full catalogs: [`libraries/tools/ai-agents/`](libraries/tools/ai-agents/README.md), [`libraries/tools/development/`](libraries/tools/development/README.md), [`libraries/tools/design/`](libraries/tools/design/README.md), [`libraries/tools/marketing/`](libraries/tools/marketing/README.md). Weekly [News & Insights](insights/news-and-insights/README.md) sweep scope is narrower—see **Sources we follow** there.

## Skills

| Skill | Category | When useful |
| --- | --- | --- |
| [`make-interfaces-feel-better`](business-workflows/design/skills/make-interfaces-feel-better.md) | Design | Building or reviewing UI polish |

## How to use skill references

1. Scan the section indexes to find useful candidates; for a monthly relevance check, consider all five sections rather than only new entries.
2. Read the relevant catalog entry. Follow its **Skill source** only when you want to inspect that source, not to execute it automatically.
3. Use `libraries/ui-libraries/` and `libraries/tools/` for research: picking a component library, finding inspiration, and checking licenses. References are notes, not action authorization.
4. Your project's own `AGENTS.md`, design system, and component inventory take precedence over imported guidance, subject to the host's rules and your permissions.

If you separately choose to use a skill in a project, link or copy from its **Skill source** URL (for example into `.claude/skills/` or `.cursor/skills/`), ideally pinned to a commit. This is a manual, separately authorized choice—not something the Start J-Stack link does.

## Questions and responsible use

[Questions are brought to Jake for consideration, and selected answers are shared in future updates.](libraries/guides/questions.md) The dedicated inbox is **pending configuration and verification**; no submission service or individual reply is promised.

Read the [responsible-use guidance](GETTING_STARTED.md#2-use-the-guidance-responsibly) and [Terms of Use draft](TERMS.md). The terms and guided consent flow are **drafts for legal and owner review**, not a claim that approved terms are already in force. Account access, monthly scheduling, and any action each require separate consent. Existing MIT and third-party licenses remain unchanged.

## Contributing

Open a pull request. Follow [CONVENTIONS.md](CONVENTIONS.md) for lessons, tools, skills, and reference frontmatter. New UI library or tool references use the reference layout in CONVENTIONS and get a row in the matching catalog. Skills should meet the [skills audit standard](CONVENTIONS.md#skills-audit-standard).

## Credits

- `make-interfaces-feel-better` is from [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) (MIT, © 2026 Jakub Krehel). Catalog entry: [`business-workflows/design/skills/make-interfaces-feel-better.md`](business-workflows/design/skills/make-interfaces-feel-better.md).
- Third-party libraries and tools in `libraries/ui-libraries/` and `libraries/tools/design/` belong to their respective owners; check each one's license before use.

## License

[MIT](LICENSE)
