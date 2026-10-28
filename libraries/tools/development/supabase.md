
---
type: tool
title: Supabase — Postgres backend as a service
purpose: Managed Postgres, auth, storage, and realtime for full-stack apps.
status: curated
tags: [tools, development, supabase, postgres, auth, database, baaS]
sources:
  - url: https://supabase.com/
    label: Supabase
  - url: https://supabase.com/docs
    label: Supabase documentation
---

# Supabase — Postgres backend as a service

## When to use

- Standing up **Postgres**, **Auth**, **Storage**, or **Realtime** without running your own database fleet.
- Pairing a Next.js or Vercel frontend with a managed backend and row-level security.
- Evaluating migrations, Edge Functions, or Supabase changelog items for active projects.

## What it is

[Supabase](https://supabase.com/) is an open-source **Postgres development platform**: hosted database, authentication, object storage, realtime subscriptions, and auto-generated APIs. Guides and references live at [supabase.com/docs](https://supabase.com/docs).

## What it can do

### Managed Postgres

Each project includes a full **PostgreSQL** database with SQL editor, migrations, backups (per plan), and extensions documented in Supabase guides. Use familiar SQL and Postgres tooling while Supabase operates the cluster.

### Auth

**Supabase Auth** supports email/password, magic links, OAuth providers, and phone flows (provider list in docs). JWT-based sessions integrate with [Next.js](nextjs.md) server and client components and **Row Level Security** policies in SQL.

### Storage

**Storage buckets** hold user-generated files with access rules tied to Auth users or service roles—common for avatars, uploads, and CMS media.

### Realtime

**Realtime** channels broadcast database changes or custom messages to subscribed clients—useful for live dashboards and collaborative features without operating a separate websocket fleet.

### Edge Functions

**Edge Functions** (Deno) run server-side logic close to users for webhooks, light transforms, and privileged operations that should not live in the browser.

## How it fits Jake's stack

**Default data and auth layer** for apps on [Vercel](vercel.md) + [Next.js](nextjs.md). Agents in [Cursor](../ai-agents/cursor.md) use the Supabase MCP in some workflows; schema changes should still go through migrations and review. Transactional email often pairs with [Resend](resend.md) for auth and product messages.

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [supabase.com/blog](https://supabase.com/blog), [changelog](https://github.com/supabase/supabase/blob/master/CHANGELOG.md) and docs updates, [@supabase on X](https://x.com/supabase). Link [this file](supabase.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://supabase.com/](https://supabase.com/) — product overview
- [https://supabase.com/docs](https://supabase.com/docs) — Auth, Database, Storage, Realtime, Functions
