
---
type: tool
title: Resend — email API for developers
purpose: Transactional and product email from Next.js apps without running mail servers.
status: curated
tags: [tools, development, resend, email, api, transactional]
sources:
  - url: https://resend.com/
    label: Resend
  - url: https://resend.com/docs
    label: Resend documentation
  - url: https://resend.com/changelog
    label: Resend changelog
---

# Resend — email API for developers

## When to use

- Sending **transactional email** (auth, receipts, notifications) from [Next.js](nextjs.md) or API routes.
- Comparing Resend domains, templates, and deliverability setup for a new product.
- Tracking Resend changelog items that affect production mail.

## What it is

[Resend](https://resend.com/) is an **email API** for developers with SDKs, domain verification, templates, and dashboards. Docs: [resend.com/docs](https://resend.com/docs); product updates: [resend.com/changelog](https://resend.com/changelog).

## What it can do

### Send API and SDKs

The **Send** endpoint delivers HTML/text messages with attachments and tags. Official SDKs (including Node/React examples in docs) integrate with [Next.js](nextjs.md) Route Handlers and Server Actions using server-only API keys.

### Domains and deliverability

Add and verify **DNS records** (SPF, DKIM, DMARC per Resend guides) on your sending domain before production traffic. Resend documents batching, idempotency, and bounce handling patterns.

### Templates and React email

Resend supports **templates** and documents **React Email** integration for component-based message markup—useful for consistent product and auth emails.

### Audiences and broadcasts (product-dependent)

Resend has expanded beyond pure transactional mail into **audiences** and marketing-style sends on some plans—confirm current product boundaries in docs before mixing transactional and promotional mail.

### Webhooks

**Webhooks** notify your [Vercel](vercel.md) or [Supabase](supabase.md) backends about delivery, bounces, and complaints for automation and suppression lists.

## How it fits Jake's stack

**Preferred developer email layer** on Vercel + Next.js—auth messages from [Supabase](supabase.md), product notifications, and lifecycle mail. Marketing blasts may also use [Canva](../design/canva.md) assets but sending infrastructure stays in Resend for code-owned flows.

## News and insights

Included in the weekly [News & Insights](../../../insights/news-and-insights/README.md) sweep. Follow [resend.com/changelog](https://resend.com/changelog), [docs](https://resend.com/docs), Resend blog posts, and [@resend on X](https://x.com/resend). Link [this file](resend.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://resend.com/](https://resend.com/) — product overview
- [https://resend.com/docs](https://resend.com/docs) — API, domains, React Email
- [https://resend.com/changelog](https://resend.com/changelog) — changelog
