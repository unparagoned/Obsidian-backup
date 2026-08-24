# Knowledge Wiki Instructions

This vault is a persistent, AI-maintained knowledge base.

## Ownership

- `raw/` contains immutable source material. Never edit or delete it.
- `wiki/` is maintained by the agent.
- The user chooses sources, reviews conclusions and directs research.
- Never present an inference as a sourced fact.

## Page types

- `wiki/sources/`: one summary per source
- `wiki/concepts/`: ideas, methods and recurring themes
- `wiki/entities/`: people, companies, projects and products
- `wiki/syntheses/`: analyses combining multiple sources
- `wiki/index.md`: catalog of wiki pages with one-line descriptions
- `wiki/log.md`: append-only history of operations

## Ingest workflow

When asked to ingest a source:

1. Read the source from `raw/`.
2. Create or update its page under `wiki/sources/`.
3. Extract important claims, evidence, caveats and open questions, using the claim/quote/link format and evidence grading from Writing style.
4. Search existing wiki pages before creating new pages.
5. Update relevant concept and entity pages.
6. Add meaningful `[[wikilinks]]` in both directions.
7. Record disagreements or contradictions explicitly.
8. Update `wiki/index.md`.
9. Append an entry to `wiki/log.md`.
10. Report which files changed and anything requiring human review.

Never invent missing metadata or conclusions.

## Query workflow

1. Read `wiki/index.md`.
2. Search relevant wiki pages.
3. Verify important claims against `raw/` when possible.
4. Answer with links to supporting wiki pages and raw sources.
5. Offer to save substantial new synthesis under `wiki/syntheses/`.

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
- Quotes without a framing sentence
- Duplicate quotes
- Unlabelled low-quality sources presented as evidence

Do not silently resolve genuine disagreements between sources.

## Writing style

Pages should read like the user's existing notes (see `iCloud/Heath & Supplements/` for examples). Rules:

- **Claim, quote, link.** The atomic unit is: one or two plain sentences stating the takeaway, then a `>` blockquote of the source's own wording, then the URL on its own line. Never paraphrase a study without quoting it; never quote without a framing sentence.
- **Write factually, in the third person.** The agent never writes "I recommend", "I suspect" or similar. First person belongs only to the user. When rewording or rewriting text the user wrote, keep their first-person voice and attribute it (e.g. "The user's view: ..."). On fresh ingestion, state what the source shows and mark the agent's own inferences with "Likely:" or "Unverified:", never as fact.
- **Separate voice from evidence.** Sourced claims are stated plainly with their quote. Opinions found in a source stay attributed to that source's author, not restated as fact.
- **Grade the evidence in a few words** at the top of a treatment/intervention section, using this scale: *Strong evidence* / *Good evidence, modest effect* / *Some evidence* / *Weak evidence* / *Mixed evidence* / *No real evidence* / *None in humans* / *Don't take*. Add a dose range one-liner where relevant (`200-450mg`).
- **Name the study design** when it matters: RCT, meta-analysis, Mendelian randomisation, cohort, animal (say the species), n. Bold "causal" language only when the design supports it, and flag reverse-causation risk explicitly.
- **Label source quality** when it isn't obvious from the URL: primary paper, review, press release, news article, YouTube, Reddit/anecdote, insider claim. Don't drop lower-quality sources; keep them in an `## Examples` or `## Anecdotes` section.
- **Debunks get their own heading**, stated as the corrected claim ("It's not true that..."). When the user or a source changes position, record both the old view and why it changed.
- **Organise pages by what to do**: causes/determinants, then treatments/interventions, aids/supplements, drugs, mechanisms, and finally notes/TODO. Mechanisms go near the bottom.
- **Terse.** Short sentences, no filler, no hedging boilerplate. A section can be a heading, one line and one quote.
- **Links and tags.** Use `[[Page#Heading]]` links to specific sections. Put `#tags` inline at the section they apply to, not just in frontmatter. End pages with a `# TODO` listing things to research next.
- **Hygiene.** Strip tracking parameters from URLs. Deduplicate quotes that appear in multiple sections (link to the first instead). Fix mangled markdown links.
