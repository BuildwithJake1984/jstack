
---
type: tool
title: Vercel — frontend cloud and deployments
purpose: Host Next.js and modern frontends with previews, edge, and platform integrations.
status: curated
tags: [tools, development, vercel, hosting, deploy, nextjs, edge]
sources:
  - url: https://vercel.com/
    label: Vercel
  - url: https://vercel.com/docs
    label: Vercel documentation
  - url: https://vercel.com/changelog
    label: Vercel changelog
---

# Vercel — frontend cloud and deployments

## When to use

- Deploying **Next.js** or other supported frameworks with preview URLs per branch.
- Using Vercel platform features (analytics, firewall, storage integrations, AI SDK patterns).
- Tracking Vercel changelog items that affect production apps.

## What it is

[Vercel](https://vercel.com/) is a **frontend cloud**: Git-connected deployments, global CDN, serverless and **edge** functions, and first-class **[Next.js](nextjs.md)** support from the framework’s maintainer. Docs: [vercel.com/docs](https://vercel.com/docs); product changes: [vercel.com/changelog](https://vercel.com/changelog).

## What it can do

### Preview and production deployments

Each pull request can receive a **Preview Deployment** with a unique URL; merges to production branches promote to production aliases. Integrates with [GitHub](github.md) checks and comments.

### Serverless and edge runtimes

**Serverless Functions** and **Edge Functions** run API routes and middleware close to users. Choose runtime (Node, Edge) per route following Vercel and Next.js guidance.

### Environment variables and secrets

Per-environment **env vars** separate preview from production secrets—pair with [Supabase](supabase.md) and [Resend](resend.md) keys without leaking to client bundles (use `NEXT_PUBLIC_` only when intentional).

### Observability and protection

Vercel documents **Analytics**, **Speed Insights**, **Web Application Firewall**, and **Deployment Protection** for production hardening—confirm plan availability.

### Marketplace integrations

Official integrations connect storage, databases, auth, and AI providers; use docs to wire [Supabase](supabase.md) or AI gateways without bespoke infra for small teams.

## How it fits Jake's stack

**Primary production host** for Jake’s [Next.js](nextjs.md) apps. [Cursor](../ai-agents/cursor.md) pushes to GitHub; Vercel builds and serves. Backend data lives in Supabase; email in Resend; marketing sites may still use the same monorepo patterns.

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [vercel.com/changelog](https://vercel.com/changelog), [vercel.com/blog](https://vercel.com/blog), [docs](https://vercel.com/docs), and [@vercel on X](https://x.com/vercel). Link [this file](vercel.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://vercel.com/](https://vercel.com/) — platform overview
- [https://vercel.com/docs](https://vercel.com/docs) — deployments, functions, env vars
- [https://vercel.com/changelog](https://vercel.com/changelog) — changelog
