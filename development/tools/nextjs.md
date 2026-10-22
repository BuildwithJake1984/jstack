
---
type: tool
title: Next.js — React framework for the web
purpose: App Router, SSR, and full-stack React patterns Jake ships on Vercel.
status: curated
tags: [tools, development, nextjs, react, framework, vercel]
sources:
  - url: https://nextjs.org/
    label: Next.js
  - url: https://nextjs.org/docs
    label: Next.js documentation
  - url: https://github.com/vercel/next.js/releases
    label: Next.js GitHub releases
---

# Next.js — React framework for the web

## When to use

- Starting or extending a **React** app with routing, SSR, RSC, or API routes.
- Following Next.js release notes before upgrading production apps on [Vercel](vercel.md).
- Aligning UI from [Paper](../../design/tools/paper.md) or [Figma](../../design/tools/figma.md) with app structure.

## What it is

[Next.js](https://nextjs.org/) is a **React framework** for production web apps maintained by Vercel. The [App Router](https://nextjs.org/docs/app) is the modern default for routing, layouts, server components, and data fetching patterns documented at [nextjs.org/docs](https://nextjs.org/docs).

## What it can do

### App Router and React Server Components

**Server Components** render on the server by default, reducing client JavaScript for data-heavy pages. **Client Components** handle interactivity where needed. Nested **layouts** and **loading UI** keep navigation fast.

### Data fetching and caching

Next.js documents `fetch` caching, **revalidation**, and **Server Actions** for mutations without separate API boilerplate—pair with [Supabase](supabase.md) or other backends using server-only credentials.

### Routing and middleware

File-system **routes**, dynamic segments, **route groups**, and **middleware** support auth gates, localization, and experiments at the edge on [Vercel](vercel.md).

### Image and font optimization

Built-in **`next/image`** and **`next/font`** improve performance with sensible defaults—important for marketing pages and product UI alike.

### Incremental adoption and tooling

Next.js supports incremental migration from legacy React apps and ships with **Turbopack** (per current docs) for faster local development—confirm defaults in the version you run.

## How it fits Jake's stack

**Default application framework** for web products. Design exploration happens in [Paper](../../design/tools/paper.md); production components live in GitHub repos deployed to Vercel with Supabase backends and Resend email.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [nextjs.org/blog](https://nextjs.org/blog), [GitHub releases](https://github.com/vercel/next.js/releases), [docs](https://nextjs.org/docs), and [@nextjs on X](https://x.com/nextjs). Link [this file](nextjs.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://nextjs.org/](https://nextjs.org/) — framework home
- [https://nextjs.org/docs](https://nextjs.org/docs) — App Router, data fetching, deployment
