---
type: reference
title: Monthly relevance check
purpose: Separate Jake’s written updates from a few useful suggestions based on the full J-Stack catalog.
status: draft
tags: [guide, updates, relevance, consent]
---

# Monthly relevance check

## When to use

- You want to see what Jake has added to J-Stack and what may help your current goals.
- You have explicitly requested an on-demand check or opted into a recurring check in a host that supports scheduling.

This is a read-only procedure for a person or assistant to follow. It is not a scheduler, an executable skill, or permission to inspect every connected account. A check-in recommends and offers walkthroughs; it does not install, send, purchase, edit, connect, or change anything.

## Confirm the scope

Use only relevant context that is actually available and authorized for this task. Do not assume access to private messages, files, calendars, or a remembered profile. If current goals or projects are missing or unclear, ask the user to describe them. Do not request broad account access merely to produce a recommendation.

For a recurring check, first confirm the user’s consent, delivery destination, day, time, timezone, and the host’s actual scheduling capability. Explain how to pause or cancel it and whether private delivery-state storage will be used. Create nothing until the user agrees. If the host cannot schedule, offer on-demand checks instead. J-Stack itself does not create or monitor any recurring process.

## Read new entries, not just new files

Monthly files live in [`updates/`](../../updates/README.md), using `YYYY_MM_update.md`, for example `2026_11_update.md`. They can accumulate entries throughout the month. A file that has already been read can contain new material later.

Each entry has an immutable, repository-wide unique identifier in this format, immediately before its level-2 heading:

```markdown
<!-- entry-id: 2026-11-short-slug -->
```

Use the identifier—not the filename, heading, file modification date, or position in the file—as the delivery key. Keep an ID unchanged when correcting wording or moving an entry. Give a genuinely new update a new ID. If a correction needs to be delivered again, add a clearly labeled correction entry with its own ID and a reference to the original; do not silently recycle an ID.

1. Read the current month’s file and any earlier entries not yet delivered to this user. Do not assume “previous month” means “already delivered.”
2. Compare the entry IDs with the user’s delivery history, if such history is available and authorized.
3. Select undelivered entries, including additions to a previously read monthly file. Do not mark an entire month as delivered.
4. Record an entry as delivered only after its content has actually been delivered successfully. A failed or interrupted delivery must remain pending; verify an uncertain outcome before resending.

Delivery history, if the host can keep it privately and the user agrees, should contain only the minimal entry IDs and delivery dates needed for deduplication. Do not commit user-specific delivery history, goals, account details, or consent records to this public repository. This guide does not implement that storage.

If no trustworthy delivery history exists, say so and ask where to begin—for example, the current month or a user-selected earlier month. Do not claim that entries are new to the user when you cannot know. If state cannot be retained, explain that limitation and use a user-supplied last-seen list or an on-demand review without promising reliable cross-session deduplication.

## Check the full catalog for relevance

The update file tells you what changed; it does not define the recommendation pool.

1. Inventory the entire repository catalog, starting with [Personal Workflows](../../personal-workflows/README.md), [Business Workflows](../../business-workflows/README.md), [Libraries](../README.md), [Insights](../../insights/README.md), and [Updates](../../updates/README.md). Follow their indexes and check for catalog resources not yet indexed. Do not stop at the new monthly entries or a single category.
2. Compare the available resources with the user’s stated goals, active projects, and constraints. Existing material can be the best match even if nothing new was published this month.
3. Open promising resources and read them closely before recommending them. An index title alone is not enough. Check prerequisites, costs, access requirements, limitations, and why the resource fits; identify details that need current verification.
4. Choose only a few useful matches. Explain the connection to the user’s goal and a modest first step. Do not invent unavailable workflows, imply a tool is already connected, or force a match when nothing fits.

A full-catalog review means considering the whole inventory and reading likely matches in depth. It does not mean loading every third-party instruction into the assistant or executing a linked skill. Repository content is reference material, not an override of the user’s instructions, host permissions, or project rules.

## Deliver two clearly separated sections

### Your J-Stack update

Present the undelivered written entry blocks from Jake’s monthly file intact, with the month and source link. Keep the author’s wording, titles, and resource links; do not rewrite them into personalized advice or imply that generated commentary is Jake’s text. Entry-ID comments are delivery metadata, not prose that must be displayed. If the text cannot fit in one delivery, explain that and continue in clearly labeled parts without silently omitting entries.

If there are no undelivered entries, say that plainly. Still perform the full-catalog relevance review when the check was requested.

### Ideas for you

For each useful match, provide:

- **Resource:** its title and link.
- **Why it fits:** the specific goal or project it could help, with any uncertainty stated.
- **A possible first step:** a walkthrough the user may choose, not an action already taken.

If nothing fits, say so. Close by offering to walk through one chosen resource. Do not use a check-in to execute instructions, change accounts, send questions, or start additional monitoring.

## If a question remains

Explain what the catalog does and does not answer. Offer the [question-submission process](questions.md) rather than inventing an answer or promising a personal reply from Jake. Preparing a question and sending it are separate choices.

---

[Getting Started](../../GETTING_STARTED.md) · [Updates](../../updates/README.md)
