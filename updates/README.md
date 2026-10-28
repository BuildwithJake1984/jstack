# Updates

Monthly changelogs for new lessons, skills, and other published material in J-Stack. The author's update is separate from any personalized suggestions an assistant may offer.

## File naming

Use one Markdown file per calendar month: `updates/YYYY_MM_update.md`.

- `updates/2026_10_update.md` — October 2026.
- `updates/2026_11_update.md` — November 2026 naming example, not a published file.

Use **month and year** in titles and copy (for example, “October 2026”), not month/day/year dates in update posts. Add newest months at the top of the index when they are created; do not invent a future author's update.

## Entry format and stable IDs

Each monthly file has a top-level heading (`# October 2026 Update`) and one or more entries. Every entry includes:

1. **Stable entry ID** — an HTML comment immediately before the entry heading, such as `<!-- entry-id: 2026-10-design-tokens -->`.
2. **Title** — same as the linked lesson or article, as a level-2 heading.
3. **Summary** — one or two sentences on what it covers and why it matters.
4. **Link** — a relative Markdown link to the full piece in this repo, such as `../insights/ai-agents/build-ai-features-as-a-graph.md`.

IDs use `YYYY-MM-short-slug`, are unique across the repository, and stay unchanged when copy, ordering, or links change. Never reuse a retired ID for a different entry. Add a distinct ID for a substantive new update or correction that should be delivered again; reference the earlier ID where helpful. An editorial correction to an existing entry retains its ID and does not silently resend it.

Monthly files accumulate entries over the month. A check-in must compare **entry IDs**, not mark a whole filename or month as delivered. Preserve the author's entry wording when presenting it; do not mix personalized suggestions into the author’s text. Existing October copy is retained, with only repository link destinations repaired and stable IDs added. Its descriptions of the previous layout are historical, not the current navigation.

## Optional relevance check

See [Monthly relevance checks](../libraries/guides/monthly-relevance-check.md) for the complete guidance. Present two separate sections:

- **Your J-Stack update** — undelivered author entries, intact and linked to their source.
- **Ideas for you** — a few explained matches based on the **full catalog** and available, permitted user context, not only this month's additions. No useful match is an acceptable result.

Any delivered-ID record belongs in user-approved private host context, never committed here. Without reliable prior state, ask the user what they have seen rather than guessing. Scheduling is optional and host-provided; this repository creates no scheduler, monitoring, telemetry, or account changes.

## Index

| Month | File |
| --- | --- |
| October 2026 | [October 2026 Update](2026_10_update.md) |
