# Repository reorganization

This proposal reorganizes J-Stack around outcomes without dropping the existing catalog. It is prepared for owner review; it does not activate linked skills, account connections, submissions, schedules, or draft terms.

## Starting point

The migration starts from `2446e2dff7a35a46db9b675f78422d9529cda0a0` on `main`. All **91 tracked source files** have a destination below: **83 move** and **8 retain their paths**. Every existing catalog item, frontmatter block, source attribution, and license notice is retained, with repository links repaired where needed. Navigation and layout instructions are updated to describe the new structure.

The root MIT `LICENSE` is unchanged. The workflow file, Markdown lint configuration, and offline link-check configuration are unchanged. Frontmatter validation retains all existing schema checks and covers the mapped locations; only discovery paths change, with equivalent coverage for future personal and business skills and marketing templates.

## Placement decisions

| Previous material | New home | Why |
| --- | --- | --- |
| Design/interface-polish skill and other skill indexes | `business-workflows/<area>/skills/` | Existing outcomes focus on products, interfaces, and business work. Skills are still references, not activated by reading. |
| Tools | `libraries/tools/<area>/` | Reusable resources, grouped by their established use (AI agents, design, development, or marketing). |
| UI library references | `libraries/ui-libraries/` | Reusable design and UI research, with all credits and source links retained. |
| Templates | `libraries/templates/<area>/` | Reusable templates and existing template indexes. |
| Lessons | `insights/<area>/` | Lessons and observations rather than executable workflows. |
| News & Insights | `insights/news-and-insights/` | External-news editorial guidance is distinct from the author's monthly J-Stack updates. |
| Unassigned project-playbook index | `business-workflows/project-playbooks/` | Retained provisionally, not interpreted as an existing business workflow. |
| Monthly update | `updates/2026_10_update.md` | Consistent monthly filename; author copy stays intact apart from repaired link destinations and entry-ID metadata. |

The original catalog contains no published personal workflow or project playbook. The new Personal Workflows index says so rather than inventing one. The interface-polish skill can also support personal projects; its business placement is a navigation choice for owner review, not a restriction. Empty legacy skill, lesson, and template indexes remain visible as unpublished areas, not advertised as complete workflows.

The existing monthly copy describes the layout when each entry was written. Those historical descriptions are intentionally not rewritten as if Jake authored new text. Current navigation is in the root README and section indexes.

## Review boundaries and open decisions

- **Questions inbox:** pending configuration and verification. No placeholder address is published and no submission service is activated.
- **Terms:** `TERMS.md` is a draft for legal and owner review; legal entity, jurisdictional details, final liability wording, effective date, and consent versioning remain unresolved. The setup consent flow is a preview until approved terms exist.
- **Host support:** no plugin, marketplace, Muse, scheduling, synchronization, or account-access capability is promised. Any future host implementation needs separate review and authorization.
- **Existing draft PR #18:** the unrelated external-news draft remains untouched. If this reorganization merges first, its owner will need to relocate that draft and repair its links to `insights/news-and-insights/` before merging it. This PR does not approve, merge, or rewrite that work.

## Complete file map

The old path column is historical. Use the linked new path to open the current file. Added onboarding, terms, section indexes, question guidance, relevance-check guidance, and this map supplement the preserved source files.

| Previous path | Current path | Treatment |
| --- | --- | --- |
| `README.md` | [README.md](../README.md) | Navigation and read-only guidance updated; core catalog and credits retained |
| `CONVENTIONS.md` | [CONVENTIONS.md](../CONVENTIONS.md) | Conventions updated for the new layout |
| `ai-agents/lessons/README.md` | [insights/ai-agents/README.md](../insights/ai-agents/README.md) | Moved |
| `.markdownlint.jsonc` | [.markdownlint.jsonc](../.markdownlint.jsonc) | Retained in place |
| `.github/scripts/validate_frontmatter.py` | [.github/scripts/validate_frontmatter.py](../.github/scripts/validate_frontmatter.py) | Discovery paths updated; schema checks preserved |
| `ai-agents/lessons/build-ai-features-as-a-graph.md` | [insights/ai-agents/build-ai-features-as-a-graph.md](../insights/ai-agents/build-ai-features-as-a-graph.md) | Moved |
| `.github/workflows/checks.yml` | [.github/workflows/checks.yml](../.github/workflows/checks.yml) | Retained in place |
| `LICENSE` | [LICENSE](../LICENSE) | Retained in place |
| `ai-agents/skills/README.md` | [business-workflows/ai-agents/skills/README.md](../business-workflows/ai-agents/skills/README.md) | Moved |
| `ai-agents/tools/claude.md` | [libraries/tools/ai-agents/claude.md](../libraries/tools/ai-agents/claude.md) | Moved |
| `ai-agents/templates/README.md` | [libraries/templates/ai-agents/README.md](../libraries/templates/ai-agents/README.md) | Moved |
| `ai-agents/tools/README.md` | [libraries/tools/ai-agents/README.md](../libraries/tools/ai-agents/README.md) | Moved |
| `ai-agents/tools/meta-muse.md` | [libraries/tools/ai-agents/meta-muse.md](../libraries/tools/ai-agents/meta-muse.md) | Moved |
| `ai-agents/tools/cursor.md` | [libraries/tools/ai-agents/cursor.md](../libraries/tools/ai-agents/cursor.md) | Moved |
| `ai-agents/tools/openai.md` | [libraries/tools/ai-agents/openai.md](../libraries/tools/ai-agents/openai.md) | Moved |
| `ai-agents/tools/google.md` | [libraries/tools/ai-agents/google.md](../libraries/tools/ai-agents/google.md) | Moved |
| `design/README.md` | [business-workflows/design/README.md](../business-workflows/design/README.md) | Moved |
| `design/lessons/design-tokens.md` | [insights/design/design-tokens.md](../insights/design/design-tokens.md) | Moved |
| `ai-agents/tools/xai.md` | [libraries/tools/ai-agents/xai.md](../libraries/tools/ai-agents/xai.md) | Moved |
| `design/lessons/README.md` | [insights/design/README.md](../insights/design/README.md) | Moved |
| `design/skills/make-interfaces-feel-better.md` | [business-workflows/design/skills/make-interfaces-feel-better.md](../business-workflows/design/skills/make-interfaces-feel-better.md) | Moved |
| `design/tools/canva.md` | [libraries/tools/design/canva.md](../libraries/tools/design/canva.md) | Moved |
| `design/templates/README.md` | [libraries/templates/design/README.md](../libraries/templates/design/README.md) | Moved |
| `design/tools/README.md` | [libraries/tools/design/README.md](../libraries/tools/design/README.md) | Moved |
| `design/tools/paper.md` | [libraries/tools/design/paper.md](../libraries/tools/design/paper.md) | Moved |
| `design/tools/figma.md` | [libraries/tools/design/figma.md](../libraries/tools/design/figma.md) | Moved |
| `design/ui-libraries/README.md` | [libraries/ui-libraries/README.md](../libraries/ui-libraries/README.md) | Moved |
| `design/tools/shotbase.md` | [libraries/tools/design/shotbase.md](../libraries/tools/design/shotbase.md) | Moved |
| `design/tools/screenshot-to-code.md` | [libraries/tools/design/screenshot-to-code.md](../libraries/tools/design/screenshot-to-code.md) | Moved |
| `design/tools/voicestudio.md` | [libraries/tools/design/voicestudio.md](../libraries/tools/design/voicestudio.md) | Moved |
| `design/tools/mobbin.md` | [libraries/tools/design/mobbin.md](../libraries/tools/design/mobbin.md) | Moved |
| `design/ui-libraries/aicss.md` | [libraries/ui-libraries/aicss.md](../libraries/ui-libraries/aicss.md) | Moved |
| `design/ui-libraries/beui-pro.md` | [libraries/ui-libraries/beui-pro.md](../libraries/ui-libraries/beui-pro.md) | Moved |
| `design/ui-libraries/bestdesignsonx.md` | [libraries/ui-libraries/bestdesignsonx.md](../libraries/ui-libraries/bestdesignsonx.md) | Moved |
| `design/ui-libraries/amicro.md` | [libraries/ui-libraries/amicro.md](../libraries/ui-libraries/amicro.md) | Moved |
| `design/ui-libraries/beautiful-ui.md` | [libraries/ui-libraries/beautiful-ui.md](../libraries/ui-libraries/beautiful-ui.md) | Moved |
| `design/ui-libraries/annnimate.md` | [libraries/ui-libraries/annnimate.md](../libraries/ui-libraries/annnimate.md) | Moved |
| `design/ui-libraries/astryx.md` | [libraries/ui-libraries/astryx.md](../libraries/ui-libraries/astryx.md) | Moved |
| `design/ui-libraries/book-of-shapes.md` | [libraries/ui-libraries/book-of-shapes.md](../libraries/ui-libraries/book-of-shapes.md) | Moved |
| `design/ui-libraries/bencho.md` | [libraries/ui-libraries/bencho.md](../libraries/ui-libraries/bencho.md) | Moved |
| `design/ui-libraries/feralui.md` | [libraries/ui-libraries/feralui.md](../libraries/ui-libraries/feralui.md) | Moved |
| `design/ui-libraries/dialkit.md` | [libraries/ui-libraries/dialkit.md](../libraries/ui-libraries/dialkit.md) | Moved |
| `design/ui-libraries/kage.md` | [libraries/ui-libraries/kage.md](../libraries/ui-libraries/kage.md) | Moved |
| `design/ui-libraries/halaska.md` | [libraries/ui-libraries/halaska.md](../libraries/ui-libraries/halaska.md) | Moved |
| `design/ui-libraries/jakubkrehel-skills.md` | [libraries/ui-libraries/jakubkrehel-skills.md](../libraries/ui-libraries/jakubkrehel-skills.md) | Moved |
| `design/ui-libraries/components.md` | [libraries/ui-libraries/components.md](../libraries/ui-libraries/components.md) | Moved |
| `design/ui-libraries/evil-buttons.md` | [libraries/ui-libraries/evil-buttons.md](../libraries/ui-libraries/evil-buttons.md) | Moved |
| `design/ui-libraries/cue.md` | [libraries/ui-libraries/cue.md](../libraries/ui-libraries/cue.md) | Moved |
| `design/ui-libraries/md-resources.md` | [libraries/ui-libraries/md-resources.md](../libraries/ui-libraries/md-resources.md) | Moved |
| `design/ui-libraries/libraries-dev.md` | [libraries/ui-libraries/libraries-dev.md](../libraries/ui-libraries/libraries-dev.md) | Moved |
| `design/ui-libraries/kinetics.md` | [libraries/ui-libraries/kinetics.md](../libraries/ui-libraries/kinetics.md) | Moved |
| `design/ui-libraries/page-mascot.md` | [libraries/ui-libraries/page-mascot.md](../libraries/ui-libraries/page-mascot.md) | Moved |
| `design/ui-libraries/liquid-glass.md` | [libraries/ui-libraries/liquid-glass.md](../libraries/ui-libraries/liquid-glass.md) | Moved |
| `design/ui-libraries/openui.md` | [libraries/ui-libraries/openui.md](../libraries/ui-libraries/openui.md) | Moved |
| `design/ui-libraries/kobra.md` | [libraries/ui-libraries/kobra.md](../libraries/ui-libraries/kobra.md) | Moved |
| `design/ui-libraries/keyline-icons.md` | [libraries/ui-libraries/keyline-icons.md](../libraries/ui-libraries/keyline-icons.md) | Moved |
| `design/ui-libraries/reverseui.md` | [libraries/ui-libraries/reverseui.md](../libraries/ui-libraries/reverseui.md) | Moved |
| `design/ui-libraries/quiver-ai.md` | [libraries/ui-libraries/quiver-ai.md](../libraries/ui-libraries/quiver-ai.md) | Moved |
| `design/ui-libraries/scrolltide.md` | [libraries/ui-libraries/scrolltide.md](../libraries/ui-libraries/scrolltide.md) | Moved |
| `design/ui-libraries/specialized-galleries.md` | [libraries/ui-libraries/specialized-galleries.md](../libraries/ui-libraries/specialized-galleries.md) | Moved |
| `design/ui-libraries/playgrnd.md` | [libraries/ui-libraries/playgrnd.md](../libraries/ui-libraries/playgrnd.md) | Moved |
| `design/ui-libraries/shadcn.md` | [libraries/ui-libraries/shadcn.md](../libraries/ui-libraries/shadcn.md) | Moved |
| `design/ui-libraries/shadcncraft.md` | [libraries/ui-libraries/shadcncraft.md](../libraries/ui-libraries/shadcncraft.md) | Moved |
| `design/ui-libraries/spectrum.md` | [libraries/ui-libraries/spectrum.md](../libraries/ui-libraries/spectrum.md) | Moved |
| `development/skills/README.md` | [business-workflows/development/skills/README.md](../business-workflows/development/skills/README.md) | Moved |
| `design/ui-libraries/uisfx.md` | [libraries/ui-libraries/uisfx.md](../libraries/ui-libraries/uisfx.md) | Moved |
| `design/ui-libraries/typeface-fyi.md` | [libraries/ui-libraries/typeface-fyi.md](../libraries/ui-libraries/typeface-fyi.md) | Moved |
| `development/lessons/README.md` | [insights/development/README.md](../insights/development/README.md) | Moved |
| `development/templates/README.md` | [libraries/templates/development/README.md](../libraries/templates/development/README.md) | Moved |
| `development/README.md` | [business-workflows/development/README.md](../business-workflows/development/README.md) | Moved |
| `design/ui-libraries/xiod.md` | [libraries/ui-libraries/xiod.md](../libraries/ui-libraries/xiod.md) | Moved |
| `design/ui-libraries/vibeprompts.md` | [libraries/ui-libraries/vibeprompts.md](../libraries/ui-libraries/vibeprompts.md) | Moved |
| `development/tools/resend.md` | [libraries/tools/development/resend.md](../libraries/tools/development/resend.md) | Moved |
| `lychee.toml` | [lychee.toml](../lychee.toml) | Retained in place |
| `development/tools/vercel.md` | [libraries/tools/development/vercel.md](../libraries/tools/development/vercel.md) | Moved |
| `development/tools/supabase.md` | [libraries/tools/development/supabase.md](../libraries/tools/development/supabase.md) | Moved |
| `development/tools/railway.md` | [libraries/tools/development/railway.md](../libraries/tools/development/railway.md) | Moved |
| `development/tools/README.md` | [libraries/tools/development/README.md](../libraries/tools/development/README.md) | Moved |
| `development/tools/github.md` | [libraries/tools/development/github.md](../libraries/tools/development/github.md) | Moved |
| `development/tools/nextjs.md` | [libraries/tools/development/nextjs.md](../libraries/tools/development/nextjs.md) | Moved |
| `news-and-insights/README.md` | [insights/news-and-insights/README.md](../insights/news-and-insights/README.md) | Moved |
| `marketing/lessons/README.md` | [insights/marketing/README.md](../insights/marketing/README.md) | Moved |
| `marketing/skills/README.md` | [business-workflows/marketing/skills/README.md](../business-workflows/marketing/skills/README.md) | Moved |
| `marketing/tools/README.md` | [libraries/tools/marketing/README.md](../libraries/tools/marketing/README.md) | Moved |
| `marketing/tools/elevenlabs.md` | [libraries/tools/marketing/elevenlabs.md](../libraries/tools/marketing/elevenlabs.md) | Moved |
| `marketing/tools/higgsfield.md` | [libraries/tools/marketing/higgsfield.md](../libraries/tools/marketing/higgsfield.md) | Moved |
| `marketing/README.md` | [business-workflows/marketing/README.md](../business-workflows/marketing/README.md) | Moved |
| `marketing/templates/README.md` | [libraries/templates/marketing/README.md](../libraries/templates/marketing/README.md) | Moved |
| `updates/README.md` | [updates/README.md](../updates/README.md) | Retained in place |
| `updates/2026-October-update.md` | [updates/2026_10_update.md](../updates/2026_10_update.md) | Monthly filename normalized; author copy retained; stable entry IDs added |
| `workflows/README.md` | [business-workflows/project-playbooks/README.md](../business-workflows/project-playbooks/README.md) | Moved |
