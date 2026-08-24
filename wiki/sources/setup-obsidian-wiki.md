---
title: Setup Obsidian Wiki
type: source
source: raw/inbox/Setup Obsidian Wiki.md
origin: ChatGPT conversation (user prompts + ChatGPT replies)
date_ingested: 2026-08-24
---

# Setup Obsidian Wiki

**Raw source:** `raw/inbox/Setup Obsidian Wiki.md` — a saved ChatGPT conversation. The date of the conversation and the ChatGPT model used are not recorded in the source.

## Summary

Two questions were asked. First, how to set up a Karpathy-style wiki in Obsidian; second, how to make Obsidian Web Clipper save into `raw/inbox` instead of the default `Clippings` folder.

ChatGPT's recommended setup is [[llm-wiki]]: Obsidian for browsing, an agent (Codex or Claude Code) for maintaining the wiki, Git for rollback. It proposes a folder layout (`raw/inbox`, `raw/assets`, `wiki/{index,log,sources,concepts,entities,syntheses}`, `outputs/`, plus `AGENTS.md`/`CLAUDE.md`) and a starter `AGENTS.md` — the one now used verbatim in this vault.

## Key claims

- The pattern attributed to [[andrej-karpathy]] has three layers: immutable sources, an AI-maintained wiki, and an instruction file governing the AI. Cited link: Karpathy's LLM Wiki gist (`gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`).
- The index-first approach (agent reads `index.md`, then greps) "works surprisingly well at roughly 100 sources and hundreds of pages"; add local search (e.g. `qmd`) only when text search starts missing material. *Attributed by ChatGPT to Karpathy — not verified against the gist.*
- Main failure mode: the agent generating hundreds of shallow pages. Mitigation: update existing concept pages; only create a new page if the subject will matter independently later.
- Practical advice: start with one focused vault; ingest the first 20–30 sources individually; review agent changes while conventions stabilise; commit to Git before large ingest/maintenance runs; treat AI summaries as compiled interpretations, with `raw/` as authoritative.
- Obsidian settings: attachments → `raw/assets`; Web Clipper → `raw/inbox`; use wikilinks (`[[...]]`); enable automatic link updating; keep plugins minimal (avoid stacking "second brain" plugins; Dataview only once metadata needs are known).
- [[obsidian-web-clipper]]: the destination folder is set per **template** (gear → Templates → Default → *Note location*), not in General settings. Use a vault-relative path (`raw/inbox`), and pick the vault explicitly rather than "Last used".

## Four daily prompts

1. `Ingest raw/inbox/<file>.md`
2. `Process all unprocessed files in raw/inbox, one at a time.`
3. `Using the wiki and original sources, compare X with Y. Save useful new synthesis.`
4. `Lint the wiki. Report contradictions, broken links, orphan pages, duplicates and unsupported claims. Fix safe issues.`

## Caveats

- This is a ChatGPT answer, not a primary source. Its claims about Karpathy's approach are second-hand; the gist is linked but its contents are not in `raw/`.
- The Web Clipper instructions cite an Obsidian forum thread and the Clipper product page; UI labels may change with extension versions.
- Source recommends `outputs/`; this vault uses `output/` (singular). Minor divergence, noted not resolved.

## Open questions

- Does the Karpathy gist actually state the ~100 sources / index-first scaling claim, or is that ChatGPT's paraphrase? Ingesting the gist itself would settle this.
- Whether `qmd` refers to a specific tool is unclear from the source.
