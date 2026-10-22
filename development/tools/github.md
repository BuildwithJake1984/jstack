
---
type: tool
title: GitHub — source control and collaboration
purpose: Git hosting, PRs, Actions, and releases for JStack repos and client projects.
status: curated
tags: [tools, development, github, git, ci, collaboration]
sources:
  - url: https://github.com/
    label: GitHub
  - url: https://docs.github.com/
    label: GitHub documentation
  - url: https://github.blog/changelog/
    label: GitHub changelog
---

# GitHub — source control and collaboration

## When to use

- Hosting repos, opening PRs, and running **GitHub Actions** checks (as in JStack).
- Tracking **release feeds** for dependencies such as Claude Code, OpenAI SDKs, or xAI SDKs.
- Connecting [Vercel](vercel.md) or [Railway](railway.md) deploys to branches and tags.

## What it is

[GitHub](https://github.com/) is Microsoft's **Git hosting and collaboration** platform: repositories, pull requests, issues, Actions CI/CD, releases, and packages. Documentation: [docs.github.com](https://docs.github.com/); platform changes: [github.blog/changelog](https://github.blog/changelog/).

## What it can do

### Pull requests and code review

**Pull requests** combine diffs, reviews, checks, and merge strategies (merge, squash, rebase). JStack and app repos rely on PR gating before deploy.

### GitHub Actions

**Actions** run workflows on events (push, PR, schedule) for linting, tests, security scans, and deployments. JStack’s `checks` workflow is an example pattern.

### Releases and dependency tracking

**Releases** and `releases.atom` feeds announce SDK and CLI updates—listed in [News & Insights](../../news-and-insights/README.md) for `anthropics/*`, `openai/*`, and `xai-org/*` repositories.

### Issues, projects, and permissions

**Issues** and **Projects** track work; **branch protection** and **environments** enforce approval flows for production.

### Integrations

GitHub Apps connect [Vercel](vercel.md), [Cursor](../../ai-agents/tools/cursor.md) Cloud Agents, and third-party CI without sharing long-lived passwords.

## How it fits Jake's stack

**System of record for code**—including this JStack repo and Property Guide–style apps. Deploy previews flow to Vercel; agents open PRs from [Cursor](../../ai-agents/tools/cursor.md); changelog monitoring feeds weekly digests.

## News and insights

Included in the weekly [News & Insights](../../news-and-insights/README.md) sweep. Follow [github.blog/changelog](https://github.blog/changelog/), [GitHub Blog](https://github.blog/), release Atom feeds for tracked repos, and [@github on X](https://x.com/github). Link [this file](github.md) in digests.

## Sources

Pages checked for this reference (2026-10-22):

- [https://github.com/](https://github.com/) — product home
- [https://docs.github.com/](https://docs.github.com/) — Actions, PRs, releases
- [https://github.blog/changelog/](https://github.blog/changelog/) — platform changelog
