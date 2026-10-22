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

More categories will be added over time.

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

Open a pull request. Follow [CONVENTIONS.md](CONVENTIONS.md) for lessons, tools, and skills. New UI library or tool references start from [`design/templates/reference-template/`](design/templates/reference-template/) and get a row in the matching catalog. Skills should follow the [skills audit standard](design/templates/astra-skills-standard/README.md).

## Credits

- `make-interfaces-feel-better` is from [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) (MIT, © 2026 Jakub Krehel). Catalog entry: [`design/skills/make-interfaces-feel-better.md`](design/skills/make-interfaces-feel-better.md).
- Third-party libraries and tools in `design/ui-libraries/` and `design/tools/` belong to their respective owners; check each one's license before use.

## License

[MIT](LICENSE)
