**You said**

how best to setup kaparthy obsidian wiki

---

**ChatGPT said**

The cleanest Karpathy-style setup is:

**Obsidian for browsing, Codex or Claude Code for maintaining, Git for rollback.** Avoid stuffing it with plugins or building a vector database upfront.

Karpathy’s actual pattern is three layers: immutable sources, an AI-maintained wiki, and an instruction file governing the AI. Obsidian is effectively the viewer/editor. [Karpathy’s original LLM Wiki outline](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f?utm_source=chatgpt.com).

## Recommended vault structure

```
knowledge/
├── AGENTS.md               # Use CLAUDE.md with Claude Code
├── raw/
│   ├── inbox/
│   └── assets/
├── wiki/
│   ├── index.md
│   ├── log.md
│   ├── sources/
│   ├── concepts/
│   ├── entities/
│   └── syntheses/
└── outputs/
```
- `raw/`: Original articles, PDFs, transcripts and notes. The AI must never modify these.
- `wiki/`: AI-generated summaries and interconnected knowledge.
- `outputs/`: Temporary reports, comparisons and lint results.
- `AGENTS.md`: The important part. It defines how the agent behaves.

## Obsidian settings

Configure:

- New attachments → `raw/assets/`
- Web Clipper destination → `raw/inbox/`
- Use `[[wikilinks]]`
- Turn on automatic link updating
- Keep community plugins minimal

Useful additions:

- Obsidian Web Clipper
- Git, or another proper backup/version-history system
- Dataview only after you know which metadata you actually need

Do not install ten “second brain” plugins. They create incompatible conventions and maintenance noise.

## Starter AGENTS.md

```markdown
# Knowledge Wiki Instructions

This vault is a persistent, AI-maintained knowledge base.

## Ownership

- \`raw/\` contains immutable source material. Never edit or delete it.
- \`wiki/\` is maintained by the agent.
- The user chooses sources, reviews conclusions and directs research.
- Never present an inference as a sourced fact.

## Page types

- \`wiki/sources/\`: one summary per source
- \`wiki/concepts/\`: ideas, methods and recurring themes
- \`wiki/entities/\`: people, companies, projects and products
- \`wiki/syntheses/\`: analyses combining multiple sources
- \`wiki/index.md\`: catalog of wiki pages with one-line descriptions
- \`wiki/log.md\`: append-only history of operations

## Ingest workflow

When asked to ingest a source:

1. Read the source from \`raw/\`.
2. Create or update its page under \`wiki/sources/\`.
3. Extract important claims, evidence, caveats and open questions.
4. Search existing wiki pages before creating new pages.
5. Update relevant concept and entity pages.
6. Add meaningful \`[[wikilinks]]\` in both directions.
7. Record disagreements or contradictions explicitly.
8. Update \`wiki/index.md\`.
9. Append an entry to \`wiki/log.md\`.
10. Report which files changed and anything requiring human review.

Never invent missing metadata or conclusions.

## Query workflow

1. Read \`wiki/index.md\`.
2. Search relevant wiki pages.
3. Verify important claims against \`raw/\` when possible.
4. Answer with links to supporting wiki pages and raw sources.
5. Offer to save substantial new synthesis under \`wiki/syntheses/\`.

## Maintenance workflow

Check for:

- Broken links
- Orphan pages
- Duplicate concepts or entities
- Unsupported claims
- Contradictions
- Stale summaries
- Missing source references
- Pages that should be merged or split

Do not silently resolve genuine disagreements between sources.
```

## Daily workflow

Use four plain prompts:

```
Ingest raw/inbox/article-name.md
```
```
Process all unprocessed files in raw/inbox, one at a time.
```
```
Using the wiki and original sources, compare X with Y.
Save useful new synthesis.
```
```
Lint the wiki. Report contradictions, broken links, orphan
pages, duplicates and unsupported claims. Fix safe issues.
```

## What matters in practice

- Start with one focused vault, not your entire life.
- Ingest sources individually for the first 20–30 items.
- Review the agent’s changes while conventions stabilize.
- Commit to Git before large ingestion or maintenance runs.
- Keep `index.md` useful rather than exhaustive.
- Add local search such as `qmd` only when ordinary text search starts missing material. Karpathy says the index-first approach works surprisingly well at roughly 100 sources and hundreds of pages.
- Treat AI summaries as compiled interpretations, not ground truth. The originals in `raw/` remain authoritative.

The main failure mode is letting the agent generate hundreds of shallow pages. Tell it to update existing concept pages whenever possible and only create a new page when the subject will matter independently later.

---

**You said**

how do I set the web clipper to point there, I can't see a setting anywhere and it by default goes to Clippings

---

**ChatGPT said**

You’re looking in the wrong section. The destination folder is stored **inside each Clipper template**, not in General settings.

1. Click the Obsidian Web Clipper extension.
2. Click the **gear icon**.
3. Open **Templates**.
4. Select the template you use—probably **Default**.
5. Find **Note location**.
6. Replace `Clippings` with:
```
raw/inbox
```
7. Under **Vault**, select the correct vault rather than “Last used.”
8. Close settings. Changes should save automatically.

Use a vault-relative path— `raw/inbox`, not `/raw/inbox` and not a full filesystem path. The folder will normally be created if it does not exist.

If **Note location** still isn’t visible, update the browser extension and edit the template from **Templates → Default** rather than the main Clipper popup. Obsidian confirms that templates control how pages are saved, and the community support thread shows the destination being set through the template’s Note location field. [Obsidian Web Clipper](https://obsidian.md/clipper?utm_source=chatgpt.com), [folder-setting example](https://forum.obsidian.md/t/obsidian-web-clipper-set-default-folder/96186?utm_source=chatgpt.com).