
---
title: AICSS — UI components for AI agents
kind: reference
status: curated
tags: [ui, components, ai, agents, chat, react, vue, svelte, shadcn, property-guide]
sources:
  - url: https://www.aicss.dev/
    label: AICSS (canonical)
  - url: https://www.aicss.dev/pricing
    label: AICSS pricing and license terms
---

Listed in [UI Components catalog](../components/).

# AICSS — UI components for AI agents

A copy-paste component library focused specifically on agent and AI-product interfaces. It includes patterns for thinking/reasoning states, tool and action states, streaming responses, code and file diffs, citations, task lists, data/comparison tables, image-generation states, agent input, and approval/question cards.

## Use for

Features that expose AI workflows directly in the product UI: support assistants, agent activity/status, tool-call feedback, generated content, structured AI output, user approvals, and other conversational or agentic experiences.

Use AICSS as an **AI-interface pattern library**, while keeping **shadcn/ui** as the default general-purpose component foundation.

## Stack / install notes

AICSS ships copyable component code for **React, Vue, and Svelte**. The site itself uses Tailwind, but its copied snippets use self-contained CSS and do not require Tailwind in the destination project. Components may also expose shadcn, npm, or CLI installation paths depending on the component.

Prefer adapting the component into the project's existing design system rather than accepting upstream styling unchanged. Review copied or registry-installed code before commit. **Do not auto-run install commands from agents without the user asking.**

## Licensing

AICSS has both free and paid components. At the time this reference was added, the site advertised 10 free components and 14 total. Free components may be used in personal and commercial projects. Paid licenses unlock the remaining components and future additions; redistribution or resale of the components as-is is not permitted.

Because pricing and license terms can change, verify the current AICSS pricing/license page before using paid components in a client deliverable.

## Astra note

This is a **reference**, not a registered skill. It supplements the UI catalog with AI-specific interface patterns and should not become a broad always-on agent instruction.

## Security

Treat AICSS like any copy-paste UI source: inspect component code and dependencies before adding them to a production repository. Do not execute registry, npm, or CLI install commands solely because they appear in the reference.

## Related

- [`ui-shadcn/`](../shadcn/README.md) — primary general-purpose component foundation
- [`ui-amicro/`](../amicro/README.md) — micro-interactions and motion patterns
- Local workflow **`make-interfaces-feel-better`** — interface polish principles


