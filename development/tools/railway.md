
---
type: tool
title: Railway — deploy apps and databases
purpose: Simple cloud hosting for services, workers, and databases with git-based deploys.
status: curated
tags: [tools, development, railway, hosting, deploy, infrastructure]
sources:
  - url: https://railway.com/
    label: Railway
  - url: https://docs.railway.com/
    label: Railway documentation
---

# Railway — deploy apps and databases

## When to use

- Hosting APIs, background workers, or small services outside Vercel's sweet spot.
- Provisioning managed databases or Redis-style add-ons with fast iteration.
- Comparing Railway deploy workflows with [Vercel](vercel.md) for a given workload.

## What it is

[Railway](https://railway.com/) is a cloud platform to **deploy applications and data services** from Git repositories or templates, with per-project environments, logs, and metrics. Documentation: [docs.railway.com](https://docs.railway.com/).

## What it can do

### Git-based deploys

Connect a [GitHub](github.md) repo (or CLI deploy) so pushes build container images or Nixpacks builds and roll out to Railway’s network. Preview environments map to branches per Railway docs.

### Services and networking

Run multiple **services** in one project with private networking, public URLs, and configurable **resources** (CPU/RAM). Suitable for APIs, queues workers, and cron-style jobs.

### Databases and plugins

Railway offers managed **PostgreSQL**, **MySQL**, **Redis**, and other data templates as attachable services—helpful when a workload should not share [Supabase](supabase.md) with the main app.

### Observability

Built-in **logs**, metrics, and deployment history support debugging without standing up a separate observability stack for small projects.

## How it fits Jake's stack

**Flexible compute host** when something is not a static/edge [Next.js](nextjs.md) site on [Vercel](vercel.md)—long-running processes, custom Docker images, or auxiliary databases. Primary product web apps still default to Vercel + Supabase unless requirements push elsewhere.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [railway.com](https://railway.com/) blog/changelog, [docs.railway.com](https://docs.railway.com/) updates, and [@Railway on X](https://x.com/Railway). Link [this file](railway.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://railway.com/](https://railway.com/) — product overview
- [https://docs.railway.com/](https://docs.railway.com/) — deploy, services, databases
