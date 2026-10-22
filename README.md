# AI Skills

A public library of agent skills and reference notes, organized by category. Skills are executable instructions an AI coding or design agent can load on demand; references are curated research notes (libraries, tools, patterns) that skills and agents can consult.

## Categories

| Folder | What's in it |
| --- | --- |
| [`ai-agents/lessons/`](ai-agents/lessons/README.md) | Lessons on building AI-powered product features |
| [`updates/`](updates/README.md) | Monthly index of new lessons and published material |
| [`ui-ux-design/`](ui-ux-design/README.md) | UI polish skill plus a reference library of component kits, design tools and UI patterns |
| [`development/`](development/README.md) | Coming soon |
| [`content-creation/`](content-creation/README.md) | Coming soon |
| [`relationship-management/`](relationship-management/README.md) | Coming soon |
| [`lead-generation/`](lead-generation/README.md) | Coming soon |

More categories will be added over time.

## Skills

| Skill | Category | When to load |
| --- | --- | --- |
| [`make-interfaces-feel-better`](ui-ux-design/skills/make-interfaces-feel-better/SKILL.md) | UI/UX Design | Building or reviewing UI polish |

## How agents should use this repo

1. Open the category `README.md` that matches the task. Don't load the whole library.
2. Load only the one skill that fits. Read its `SKILL.md` first, then open the detail files it links to only when needed.
3. Use `references/` for research: picking a component library, finding inspiration, checking licenses. References are notes, not instructions.
4. Your project's own `AGENTS.md`, design system and component inventory always win over anything here.

To use a skill in a project, link or copy its folder (for example into `.claude/skills/` or `.cursor/skills/`), ideally pinned to a commit of this repo.

## Contributing

Open a pull request. New references start from [`ui-ux-design/references/_template/`](ui-ux-design/references/_template/) and get a row in the category catalog. Skills should follow the [skills audit standard](ui-ux-design/references/astra-skills-standard/README.md).

## Credits

- `make-interfaces-feel-better` is adapted from [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) (MIT, © 2026 Jakub Krehel). See its [NOTICE](ui-ux-design/skills/make-interfaces-feel-better/NOTICE.md).
- Third-party libraries and tools in `references/` belong to their respective owners; check each one's license before use.

## License

[MIT](LICENSE)
