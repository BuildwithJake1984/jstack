# AI Skills

A public library of agent skills and reference notes, organized by category. Skills are executable instructions an AI coding or design agent can load on demand; references are curated research notes (libraries, tools, patterns) that skills and agents can consult.

## Categories

| Folder | What's in it |
| --- | --- |
| [`ai-agents/`](ai-agents/lessons/README.md) | Lessons, skills, tools, and templates for building AI-powered product features |
| [`design/`](design/README.md) | UI polish skill plus UI library link-outs, design tools, and templates |
| [`development/`](development/README.md) | Lessons, skills, tools, and templates for building and shipping software (coming soon) |
| [`workflows/`](workflows/README.md) | Project workflow playbooks (one subfolder per project) |
| [`updates/`](updates/README.md) | Monthly index of new lessons and published material |
| [`news-and-insights/`](news-and-insights/README.md) | Weekly digest of external product news (AI labs and stack tools), separate from JStack changelogs |

More categories will be added over time.

## Core stack

Canonical JStack tool files for Jake's AI labs, shipping infrastructure, and design/build tools. Use these paths when linking from [News & Insights](news-and-insights/README.md) or lessons.

| Area | Tools |
| --- | --- |
| **AI frontier labs** | [Claude](ai-agents/tools/claude.md) · [OpenAI](ai-agents/tools/openai.md) · [xAI / Grok](ai-agents/tools/xai.md) · [Google / Gemini](ai-agents/tools/google.md) · [Meta / Muse](ai-agents/tools/meta-muse.md) |
| **Infrastructure** | [Supabase](development/tools/supabase.md) · [Railway](development/tools/railway.md) · [Vercel](development/tools/vercel.md) · [Next.js](development/tools/nextjs.md) · [GitHub](development/tools/github.md) |
| **Design and build** | [Paper](design/tools/paper.md) · [Figma](design/tools/figma.md) · [Mobbin](design/tools/mobbin.md) · [Canva](design/tools/canva.md) · [Screenshot to Code](design/tools/screenshot-to-code.md) · [Shotbase](design/tools/shotbase.md) · [VoiceStudio](design/tools/voicestudio.md) |

Full catalogs: [`ai-agents/tools/`](ai-agents/tools/README.md), [`development/tools/`](development/tools/README.md), [`design/tools/`](design/tools/README.md).

## Skills

| Skill | Category | When to load |
| --- | --- | --- |
| [`make-interfaces-feel-better`](design/skills/make-interfaces-feel-better.md) | Design | Building or reviewing UI polish |

## How agents should use this repo

1. Open the category `README.md` that matches the task. Don't load the whole library.
2. Load only the one skill that fits. Open its catalog entry under `design/skills/`, then follow **Skill source** to the upstream or vendored `SKILL.md` and any detail files it links to.
3. Use `design/ui-libraries/` and `design/tools/` for research: picking a component library, finding inspiration, checking licenses. References are notes, not instructions.
4. Your project's own `AGENTS.md`, design system and component inventory always win over anything here.

To use a skill in a project, link or copy from the **Skill source** URL (for example into `.claude/skills/` or `.cursor/skills/`), ideally pinned to a commit of the upstream repo or this repo.

## Contributing

Open a pull request. Follow [CONVENTIONS.md](CONVENTIONS.md) for lessons, tools, skills, and reference frontmatter. New UI library or tool references use the reference layout in CONVENTIONS and get a row in the matching catalog. Skills should meet the [skills audit standard](CONVENTIONS.md#skills-audit-standard).

## Credits

- `make-interfaces-feel-better` is from [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) (MIT, © 2026 Jakub Krehel). Catalog entry: [`design/skills/make-interfaces-feel-better.md`](design/skills/make-interfaces-feel-better.md).
- Third-party libraries and tools in `design/ui-libraries/` and `design/tools/` belong to their respective owners; check each one's license before use.

## License

[MIT](LICENSE)
