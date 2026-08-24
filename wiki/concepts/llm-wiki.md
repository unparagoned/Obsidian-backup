---
title: LLM Wiki
type: concept
---

# LLM Wiki

A pattern for a persistent, AI-maintained knowledge base, attributed to [[andrej-karpathy]]. Three layers:

1. **Immutable raw sources** (`raw/`) — the agent never edits or deletes them.
2. **AI-maintained wiki** (`wiki/`) — summaries, concepts, entities, syntheses, an index and an append-only log.
3. **Instruction file** (`AGENTS.md` / `CLAUDE.md`) — governs how the agent ingests, queries and maintains.

Obsidian acts as viewer/editor; Git provides rollback. Retrieval is index-first (read `index.md`, then grep), with local search added only when that stops working.

## Guidance recorded in sources

- Prefer updating existing concept pages over creating new ones; the main failure mode is many shallow pages. ([[setup-obsidian-wiki]])
- Ingest the first 20–30 sources one at a time and review conventions. ([[setup-obsidian-wiki]])
- Commit before large ingest or lint runs. ([[setup-obsidian-wiki]])

## Sources

- [[setup-obsidian-wiki]] — ChatGPT's description of the pattern and the vault layout adopted here.
