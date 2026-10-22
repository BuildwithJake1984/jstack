---
type: lesson
title: Build AI Features as a Graph, Not One Giant Prompt
slug: build-ai-features-as-a-graph
date: 2026-10-21
tags: [ai-agents, llm, workflows, architecture]
status: published
---

# Build AI Features as a Graph, Not One Giant Prompt

*Draft for Gravity Web Studio. Not published. Destined for JStack.*

When you first add AI to a product, it's tempting to write one big prompt that does everything: read the input, reason about it, check it, and write the answer. It works in a demo. Then it gives a bad answer in production, and you can't tell which part went wrong.

## The core idea
Build the feature as a graph of small steps. Each step has one input, one output and one job. Then connect the steps with explicit paths:

- **Branches.** If the data is missing a field, skip that step.
- **Fallbacks.** If validation fails, retry once, then flag it for a human.
- **Plain-code checks.** Between LLM steps, use ordinary code to confirm the output is shaped the way the next step expects.

Each step can now be logged, tested, cached and swapped out on its own.

## Why a giant prompt hurts
A single giant prompt is hard to debug, hard to retry and hard to test. When it fails, the whole thing fails, and you rerun the whole thing to find out why.

## The same lesson, learned in code
Jake ran into this exact problem on Property Guide, with a code change rather than a prompt. One big feature change bundled too much at once: new data handling, UI updates and unrelated fixes all in one pull request. When one piece broke, the failures cascaded. Tests failed in places that had nothing to do with the real bug, and nothing could ship until all of it worked. He fixed it by breaking the work into smaller vertical slices. Each slice was one change, end to end, that could be tested and shipped on its own.

That is the same isolation principle. In an LLM graph, each node is one slice:
- It's **testable**, because you can feed it a fixed input and check the output.
- It's **loggable**, because you can store what each step produced.
- It's **swappable**, because you can change one model or prompt without touching the rest.

And when a node fails, the fallback is simple: retry once, then flag it. One failure doesn't sink the whole run.

## A small example (Next.js + Supabase)
```ts
const extracted = await extractFacts(listing);      // LLM: strict JSON out
const checked   = validate(extracted);              // plain code, no LLM
if (!checked.ok) return flagForReview(listing.id);  // fallback branch
const draft     = await writeGuide(checked.data);   // LLM: prose
await supabase.from('guide_runs').insert({ listing_id: listing.id, extracted, draft });
```

## The takeaway
You don't learn engineering in one giant leap, any more than you ship it in one giant PR. You learn one concept at a time, the same way you ship one slice at a time. Small, isolated, testable pieces win in code, in AI systems and in learning.

---
*Part of an ongoing mentorship series. Articles like this will be published on Gravity Web Studio and feed into JStack, Jake's free, open-source knowledge library and plugin for Claude, Codex and Grok bots.*
