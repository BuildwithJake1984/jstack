
---
title: OpenUI — open standard for generative interfaces
kind: reference
status: curated
tags: [ui, generative-ui, agents, ai, streaming, react, vue, svelte, react-native, mcp, mit, free]
sources:
  - url: https://www.openui.com/
    label: OpenUI
  - url: https://github.com/thesysdev/openui
    label: OpenUI GitHub
---

# OpenUI

[OpenUI](https://www.openui.com/) is an open standard and framework for agent-driven generative interfaces. Instead of returning only prose or arbitrary generated code, an AI agent can stream a constrained UI description that renders through components the application already trusts.

## What it supports

- Live charts, forms, cards, tables, dashboards, and complete application screens.
- Progressive rendering while the model is still responding.
- Interaction after generation: clicking, choosing, typing, and submitting.
- Current data from application tools and MCP servers at runtime.
- React, Vue, Svelte, React Native, email, and plain script-tag clients.
- OpenAI, Anthropic, Gemini, Mistral, and common agent frameworks.
- Existing design systems, including custom components, shadcn/ui, Material, and DaisyUI.
- A safety boundary where the model composes registered components rather than executing arbitrary UI code.

## Pricing and licensing

| Layer | Status |
| --- | --- |
| OpenUI framework | **Free and open source; MIT** |
| Direct model use | Bring your own provider and pay its normal usage costs |
| OpenUI Gateway | Optional managed production service; pricing should be verified before adoption |
| OpenUI Observability | Optional managed analytics product; currently presented as a separate service/waitlist |

The open framework does not require the hosted Gateway. The Gateway adds stream validation and repair, provider fallback, and an OpenAI-compatible endpoint. Observability is intended to show how users experience generated interfaces.

## Why it matters

OpenUI could become useful when a product moves beyond fixed chat responses and needs agents to produce structured, interactive results such as:

- A property-analysis dashboard assembled around the user’s question.
- A repair or valuation workflow with forms and charts.
- Interactive research results instead of a long text response.
- A micro-tool whose UI changes based on the task.
- Agent-generated internal operations panels.

## Adoption guidance

- Treat this as an architecture choice, not a drop-in decorative component.
- Begin with a tightly limited component registry and explicit data/tool permissions.
- Reuse the product’s existing shadcn components and design tokens.
- Validate accessibility, keyboard behavior, loading, errors, approvals, and destructive actions.
- Keep deterministic screens for core workflows where predictability matters more than flexibility.
- Review provider cost, latency, telemetry, and data handling before enabling hosted Gateway or Observability services.

## Classification

**Free MIT generative-UI framework with optional managed production services.**


