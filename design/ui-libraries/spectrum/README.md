
---
title: Spectrum UI — components and MCP registry
kind: reference
status: curated
tags: [ui, components, react, tailwind, shadcn, mcp, agents]
sources:
  - url: https://ui.spectrumhq.in/docs
    label: Spectrum UI components
  - url: https://ui.spectrumhq.in/docs/mcp
    label: Spectrum UI MCP setup and tools
---

Listed in [UI Components catalog](../components/).

# Spectrum UI — components and MCP registry

Supplemental UI component resource. Use its component registry and MCP discovery alongside [shadcn/ui](../shadcn/README.md), the primary foundation, and [AICSS](../aicss/README.md) for AI interfaces.

## Use for

Find reusable interface components before creating complex UI from scratch. Adapt selected components to the project's approved design, accessibility requirements and existing stack.

## MCP setup

For Claude Code, add this server definition to your project's `.mcp.json`:

```json
{
  "mcpServers": {
    "spectrum-ui": {
      "command": "npx",
      "args": ["-y", "@spectrumui/mcp"]
    }
  }
}
```

For Codex, add the equivalent entry to `.codex/config.toml`. Keep both server commands and argument lists synchronized. Open this repository as a trusted Codex project and restart the client/server to load it; project settings do not configure other checkouts or make the server available in an already-running session. See [Codex MCP configuration](https://developers.openai.com/codex/mcp/).

For Cursor, merge the same JSON server entry into `.cursor/mcp.json`; other clients must use their own documented configuration location. Preserve existing server entries.

Requires Node.js 18+ and npm/npx on the agent's PATH, plus network access to download the package and query the registry. No global package install is needed.

## Discovery and adoption

After loading the configuration, verify the connection with `list_categories` or `list_components`, then use `search_components` and `get_component` to inspect candidates. Configuration alone is not proof of a live connection.

The `install_component` tool writes project files through the shadcn CLI. Run it only within the authorized implementation scope and in the intended destination project, after inspecting dependencies and setup. Component installation expects Next.js, Tailwind CSS and shadcn/ui configuration; connecting this server does not install components into the project's applications.

## Licensing and review

Check the selected component's current license, dependencies and accessibility before adoption. Review generated or copied code and adapt styling to the approved design; resource approval does not automatically approve every component or dependency.

## Astra note

This is a **reference**, not a registered skill. Keep setup and library details here and UI selection guidance in your project's design guide.


