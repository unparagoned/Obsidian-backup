# AM1 presentation draft - Extracting and categorising data in company accounts

*(Working draft for reference, not a submission. Built from Z Project Report - Report mod as primary source, the EPA plan (st0763), the AM1 guidance V2.1, and the previously asked questions list.)*

## Format requirements (from the EPA plan)

- 30 minutes presentation, then 45 minutes supplementary questioning (minimum 10 questions, follow-ups do not count). Assessor may extend by up to 10%.
- One-to-one with the independent assessor, face to face or video call.
- Visual aids and equipment must be declared 1 week before the presentation date.
- Graded holistically with the report against the same six themes, so the presentation is a second chance to evidence every pass and distinction descriptor.
- Must cover: high-level summary; context, implications and recommendations; research undertaken; practical application of KSBs; business recommendations; follow-on outcomes; actions and next steps.
- Open book: notes are permitted and encouraged during both the presentation and the questioning, so the prepared question-and-answer sheet can be on the desk.
- The deck itself is a submitted artefact (via ACE, with the training provider's help), designed to last 30 minutes.
- The seven coverage bullets are requirements for content, not marked criteria. Grading is holistic: report, presentation and questioning are judged together against the six-theme pass/distinction table, so this deck is a second chance at every descriptor. The professional discussion is a separate assessment method and is not part of this grading.

## Structure and timing plan

The deck is organised so the seven coverage bullets from the EPA plan ARE the section headings, in order, so the assessor can tick coverage off as it happens. Seventeen slides in seven sections fills 30 minutes: title (1), summary (3), context (4), research (11), KSB application (8), recommendations and outcomes and next steps (5, splitting roughly 2, 1.5, 2). Slides 2, 10 and 12 are the ones to protect if running long; slides 5, 6 and 16 compress to a minute each.

---

## Slide 1 - Title (1 min)

- Extracting and categorising data in company accounts
- Jesse Karadia, HMRC
- Hubble: extraction and supervised classification of untagged items in iXBRL financial documents

Speaker notes: One sentence of who I am and my role. State upfront: I built the tool, wrote the vast majority of the code and all of the machine learning, and led the virtual team it grew into.

---
# Section 1. A high-level summary of the main aspects of the project report

## Slide 2 - The project on one page (3 min)
- HMRC receives millions of iXBRL financial documents; some document types have only about 30% of figures tagged, so 70% was unusable in bulk analysis
- Hubble extracts every item, and the 30% tagged items become free training data: a supervised multi-class classifier (TF-IDF with LinearSVC) assigns concepts to the untagged 70%
- Accuracy 0.975, macro-F1 0.785 on a 243,991 row holdout; over 99% of records extracted automatically, available within 3 days instead of months
- SEC-BERT scored highest and was rejected: 2.3pp traded for interpretability, 220x speed, CPU deployment and lower dependency risk
- In production daily, used by multiple teams, recorded benefits in the tens of millions of pounds

Speaker notes: The whole project in one slide, everything on it gets its own detail later. The one-sentence version: the data labels itself, the model extends those labels to the rest, and the best scoring model was not the right one.
Covers: high-level summary (the section heading is the guidance bullet).

---
# Section 2. Context, implications and recommendations from the report

*(Context in depth here; implications and recommendations get their own sections 5 to 7.)*

## Slide 3 - The business context (2 min)

- HMRC receives millions of company accounts and tax computations as iXBRL documents
- Tagged items drive risk profiling, policy statistics and compliance yield
- Some document types have only about 30% of figures tagged, so 70% was unusable in bulk analysis
- Untagged items include those deliberately left untagged, so the missing data is not random

**Image:** the iXBRL visual, a rendered account beside its underlying HTML (this is the "what iXBRL is" slide image). "Cash at bank and in hand" carries this year's figure tagged as `d:CashBankOnHand` in an `ix:nonfraction` node, while the prior year figure beside it sits in an untagged span. One picture shows the format, a tagged item and an untagged item. Annotated in the same style as the report figure B1: Description, Tagged and Untagged called out on the rendered side; XBRL tag and Untagged value circled on the code side.

![[ixbrl annotated example.jpg]]

Raw unannotated original, kept for reference or re-annotation:
[[15109f31b291451ed890802ce79da328_MD5.jpg|Open: Pasted image 20260819123452.png]]
![[15109f31b291451ed890802ce79da328_MD5.jpg]]

Speaker notes: Keep this non-technical, it is the problem an executive would recognise. The deliberate non-tagging point lands the risk angle. Bonus link for questioning: the tagged concept in this screenshot, CashBankOnHand, is the same concept in the label collision on slide 10.
Covers: context; business value theme (K14

[[634d7ad0a38d93d13f817eaa1ca79a91_MD5.jpg|Open: Pasted image 20260819124106.png]]
![[634d7ad0a38d93d13f817eaa1ca79a91_MD5.jpg]]

---
## Slide 4 - The problem quantified (2 min)

- Analysts could not access billions of figures to identify errors and high-risk returns
- Schema updates took months each year, with Oracle's 1,000 column limit being hit
- Descriptions have no fixed vocabulary: `CurrentAssets` alone has 23,803 unique descriptions
- Manual and regex approaches could not scale, and needed scarce subject matter expert time

**Images:** why raw descriptions are not enough ("Total" means nothing without the table name and heading), and the long tail no regex repository can cover.

![](report_figures/B04-features-table-name-heading.png)

![](report_figures/B05-rank-frequency-raw.png)

Speaker notes: This slide justifies why machine learning rather than more analysts or more regex. The 23,803 figure is the memorable one.
Covers: outline of the issue; critical evaluation theme (S3).

---
# Section 3. Research undertaken

## Slide 5 - Data selection and exploration (2 min)

- Exploratory work on 298,461 public Companies House accounts (2.8m rows, 956 concepts), so no customer data left HMRC systems
- Production on HMRC-held accounts and tax computations
- EDA findings drove design: long-tailed lognormal concept distribution, descriptions and concepts are many-to-many, descriptions mix text, dates, names and numbers
- Those findings chose the metric (macro-F1), the preprocessing and the features

**Image:** the Pareto chart, 75 concepts cover 95% of items, which is the argument for macro-F1 in one picture.

![](report_figures/B08-pareto-raw.png)

Speaker notes: The research-undertaken box is ticked here. Emphasise EDA translating directly into decisions rather than being decorative.
Covers: research undertaken; systematic methodology theme (S9, S10).

---
## Slide 6 - Preprocessing, privacy and data quality (2 min)

- Canonicalisation: dates, numbers, names, postcodes to typed placeholders (31 March 1982 kept its own token on SME advice)
- Label engineering: placeholder-only rows relabelled, so knowing an item is a name is still useful
- Privacy by design: PII replaced before modelling; DPIA; Data Protection Act 2018/UK GDPR; more ethical since rare ethnic names are treated the same as common ones
- Data quality controls aligned to DAMA UK dimensions; preprocessing moved macro-F1 from under 0.50 to over 0.70

**Image:** word counts by concept after canonicalisation, with `HubbleDate` and `HubbleName` now among the most common labels, which makes the label engineering visible.

![](report_figures/B12-word-count-by-concept-processed.png)

Speaker notes: The 20pp preprocessing gain against 2.3pp between architectures is the headline finding, trail it here and land it on slide 12. The killer stat if asked how a model copes with 23,803 descriptions: canonicalisation reduces CurrentAssets from 23,803 raw descriptions to 9 canonical ones, the bare-number residue is relabelled to HubbleNumber, and the concept scores a perfect per-class F1. CurrentAssets and CashOnHand are the two ends of the same mechanism: collisions resolve to the dominant class, which is free when you own 99.9% of your wording and fatal when you are the 21-row minority.
Covers: data curation and quality controls (S17); ethics.

---
## Slide 7 - Alternatives considered (2 min)

- Regex repository: explainable but cannot cover the long tail, consumes SME time, rejected on feasibility
- Unsupervised grouping: rejected on evidence, cosine similarity showed description variety breaks the clusters
- Frontier LLM: unusable, taxpayer data could not go to an external API, and excessive for short phrases
- Carried forward: scikit-learn family, neural networks (CNN, LSTM, GRU, BiLSTM), transformers (RoBERTa, SEC-BERT, MPNet, MiniLM)

Speaker notes: Each rejection has a stated reason: feasibility, evidence, governance. That structure is the critical evaluation descriptor in one slide.
Covers: survey of alternatives; critical evaluation theme (S3).

---
## Slide 8 - Experiment design (2 min)

- Population size validation first: 1% and 10% samples correlate 0.971 and 0.998 with full data, so filtering on samples is defensible and cut compute roughly tenfold
- HalvingRandomSearchCV over 10,000 candidates against a DummyClassifier floor; Optuna for neural and transformer studies
- Paired t-tests at the 5% level at every stage, so simpler models are preferred where differences are not real
- Same stratified 80/10/10 splits for every architecture; vectorisers fitted on training data only

**Images:** the selection funnel; the min_df plot (clusters with min_df 1 both faster and better scoring than min_df 2, the surprise a table would not have shown); and the 10% versus 100% population correlation that justified searching on samples.

![[B37 model selection funnel.svg]]
![](report_figures/B22-min-df-clusters.png)
![](report_figures/B19c-scores-10pct-vs-100pct.png)

Speaker notes: This is the scientific-method evidence. The sentence to say out loud: statistical significance is not material significance.
Covers: application of technical knowledge theme (K26, S22, K3, S11).

---
## Slide 9 - Results (2 min)

- Accuracy 0.975 (CI 0.975-0.976), macro-F1 0.785 (CI 0.780-0.788) on a 243,991-row holdout, against KPIs of 0.7 and 0.6
- Over 99% of records extracted automatically against a 95% target; data available within 3 days against a one-week target
- Median per-class F1 is 0.966; 94% of records fall in concepts scoring above 0.9
- But 27 of 141 concepts score below 0.5 and eight score zero, and analysts are told which

**Image (optional):** a well-behaved class confusion matrix as the shape of a good result.

![](report_figures/B24d-cm-turnoverrevenue.png)

Speaker notes: Present the failures as confidently as the successes, that is the truthful-presentation behaviour (B6). The median-versus-mean gap explains why both accuracy and macro-F1 are reported.
Covers: results; performance metrics (K23).

---
## Slide 10 - Errors, robustness and bias (2 min)

- Errors are label collisions, not comprehension failures: "cash at bank and in hand" is tagged CashBankOnHand 5,670 times and CashOnHand 21 times, so the minority tagging always scores as an error
- Robustness suite: abbreviations, typos, OCR, unicode, adversarial phrasing, LLM instruction injection; LinearSVC beat SEC-BERT in nine of eleven categories, against expectation
- Bias checked by company size (0.934 vs 0.790) and software provider (0.184 to 0.913); read as a training proxy artefact, reported to analysts so small-company output is treated cautiously

**Images:** the cash collision pair, the same wording routed to whichever concept dominates.

![](report_figures/B24c-cm-cashbankonhand.png)
![](report_figures/B24a-cm-cashonhand.png)

**What the confusion matrix cells contain.** These decode the two matrices above, cell by cell:

CashOnHand matrix (support 54):

| Cell                                | Rows | The actual descriptions                                                |
| ----------------------------------- | ---- | ---------------------------------------------------------------------- |
| Correct (true positives)            | 33   | "cash and cash equivalents" (23), "cash on hand" (10)                  |
| Missed (false negatives)            | 21   | all 21 are "cash at bank and in hand", predicted as CashBankOnHand     |
| Wrongly attracted (false positives) | 13   | all 13 are "cash and cash equivalents", actually tagged CashBankOnHand |

CashBankOnHand matrix (support 7,791):

| Cell | Rows | The actual descriptions |
|---|---|---|
| Correct (true positives) | 7,775 | "cash at bank and in hand" (5,670), "cash at bank" (1,796), "cash at bank and on hand" (170), "cash in hand" (115) |
| Missed (false negatives) | 16 | "cash and cash equivalents" (13) predicted as CashOnHand, "debtors" (2), "investment" (1) |
| Wrongly attracted (false positives) | 21 | the same 21 "cash at bank and in hand" rows that CashOnHand missed |

Speaker line for the tables: the two matrices are mirror images of each other. Every false negative in one is a false positive in the other, and the descriptions are identical on both sides of the boundary: "cash at bank and in hand" is tagged CashBankOnHand 5,670 times and CashOnHand 21 times, so the model routes all of them to the dominant concept and the 21 minority taggings score as errors. A false positive here is not a misreading, it is the same words carrying two labels in the source data.

Speaker notes: The bias question is guaranteed in questioning; this slide is the prepared answer. Representation bias, not demographic fairness, and the labels are the preparer's own tags. If asked for false positive examples beyond the cash pair, the other big error families to quote from memory: "vat" (RecoverableValue-addedTax predicted as Value-addedTaxPayable, 126 rows, direction is not in the description), "total" (Debtors predicted as Creditors, 121 rows, no information without table context), and the directors loan account (AmountsOwedByDirectors predicted as AmountsOwedToDirectors, 92 rows, same account name, opposite direction). Three families: sibling concepts sharing wording, direction missing from the text, and no information at all. All three point at simplifying the concept set, not a bigger model.
Covers: error and bias mitigation (pass descriptor); truthful presentation (B6).

---
# Section 4. Practical application of knowledge, skills and behaviours

*(Each slide here names the KSBs it applies, this is the section the grading table lives in.)*

## Slide 11 - How I ran the project (2 min)

- CRISP-DM for the technical work: cyclical, evidence at every stage, proportionate for a single ML developer (TDSP rejected as team-oriented ceremony)
- Kanban-focused agile rather than Scrum: small team, competing demands, fixed sprints impractical
- GitLab: epics for management timelines, issues board as the Kanban board, templates, branching with independent review
- Delivered in usable increments: raw data to file, then iXBRL fields, then ML categories, then the automated database pipeline

Speaker notes: Name the continuity risk for the distinction descriptor: without GitLab, handover depends on individual memory.
Covers: AI project and development management theme (K6, S24) plus its distinction descriptor.

---
## Slide 12 - The decision: best score lost (2 min)

- SEC-BERT had the best macro-F1. I did not select it.
- Weighted decision matrix over objective and subjective criteria, with a written rubric and confidence-interval adjustment so statistical noise could not decide it
- LinearSVC traded 2.3pp for: interpretable coefficients, 220x faster operation, CPU-only deployment on existing infrastructure, lower dependency risk, lower cost
- Preprocessing gained 20pp and feature additions 9.8pp; architecture choice was worth 2.3pp

**Image:** score against training time (the speed/performance trade visually).

![](report_figures/B21-f1-vs-train-time-refined.png)


**The interpretability comparison, in three layers, all LinearSVC, all for one real description.** "tangible fixed assets" appears 427 times in the holdout and is predicted as 
PropertyPlantEquipment with a decision score of +0.99 while every other class sits at -1.0.

1. Native, the coefficients ARE the model. Both competing classes for the present n-grams, so the relative weights are visible:

| n-gram                | PropertyPlantEquipment | FixedAssets |
| --------------------- | ---------------------- | ----------- |
| tangible fixed assets | +1.916                 | -0.205      |
| tangible fixed        | +1.282                 | -1.585      |
| assets                | +1.018                 | -0.494      |
| tangible              | +0.802                 | 0.000       |
| fixed                 | +0.248                 | +1.779      |
| fixed assets          | -0.719                 | +1.699      |

The columns are mirror images: FixedAssets owns "fixed" and "fixed assets", PropertyPlantEquipment suppresses them, and FixedAssets suppresses "tangible fixed" right back. Each class has learned to push the other's phrases away. (IntangibleAssets, the third sibling, carries zero weight on every one of these n-grams; it is waiting for the word "intangible".)

2. Post-hoc, SHAP and LIME for the same class and description:

![[presentation figures/shap-tangible-fixed-assets-titled.png]]

![[presentation figures/lime-tangible-fixed-assets-titled.png]]

Speaker line for the comparison: three views of one real, confidently correct prediction. Reading the PropertyPlantEquipment column alone, "fixed" looks mildly helpful at +0.248. SHAP says its net contribution is zero and LIME says slightly negative, and the second column shows why: FixedAssets owns the word "fixed" at +1.779, so any credit "fixed" gives PropertyPlantEquipment is cancelled by the boost it hands the competitor. The prediction rides on "tangible", which FixedAssets does not counter at all. So the coefficients expose the mechanism, and the post-hoc methods add the cross-class context a single coefficient column cannot show, which is why the report uses both. Only LinearSVC offers the coefficient layer at all; for SEC-BERT the post-hoc view is the only view. In a governed compliance process that difference is a core requirement, not a preference.

The mirror example if asked: "intangible fixed assets" predicts IntangibleAssets the same way, riding on "intangible" with "fixed" again contributing nothing. And the SHAP graph here shows exact Shapley values computed at word level, the quantity SHAP approximates; the CostSales probe-phrase figures from the report (B23, B39) remain in presentation figures if the appendix-matching version is wanted.

Speaker notes: This is the distinction slide: commercial awareness shaping the solution. In a governed compliance process, interpretability is a core requirement, not a tiebreaker.
Covers: trade-offs (K13); distinction descriptors on commercial awareness and technical rationale.

---
## Slide 13 - Production and governance in practice (2 min)

- Daily automated pipeline: S3, R extraction, Python classification through reticulate, Oracle long-format storage
- On-demand compute: an EC2 instance starts for the job and shuts down, cost-effective and does not degrade shared platforms
- The ML category is stored as an attributed prediction beside customer tags, never used for automated decisions, always a human in the loop
- Per-class performance dashboard so analysts check reliability before relying on a concept

**Images:** the production architecture and the modelling pipeline.

![[B35 production system architecture.svg]]
![[B36 data and ml pipeline.svg]]

Speaker notes: This answers the EPAO's written feedback directly: governance as practice, not caveat. MLflow versioning means any output traces to the model that produced it.
Covers: services and platforms (S15, S18); governance.

---
## Slide 14 - Communication and working with others (2 min)

- Tailored by audience: worked examples and confusion matrices for analysts, benchmarks and costs for DevOps, cost-benefit memos for managers (which won funding and headcount)
- Interactive dashboard replaced repeated questions; usage rose as understanding rose
- Autonomous where deep focus was needed (modelling), collaborative where others held the knowledge (SMEs on taxonomy, DevOps on infrastructure)
- Documentation and templates made the work reproducible by others; analysts now self-serve

**Image:** a confusion matrix as the artefact analysts actually saw. A dashboard screenshot would be stronger here; one does not exist as a file yet and is worth capturing (no customer data on screen).

![](report_figures/B24a-cm-cashonhand.png)

Speaker notes: Give one concrete story: early explanations were too detailed, so I switched to visual, example-led explanations and use of the ML category rose.
Covers: communication and influencing theme (K28, S4, S5, S27, B2) plus its distinction descriptors.

---
# Section 5. Business recommendations

## Slide 15 - Business recommendations (2 min)
- Increase coverage to 100% so legacy extraction systems can be retired
- Establish data contracts with the teams and systems now consuming Hubble output; undocumented dependencies are a continuity risk to them as much as to us
- Consider a simplified concept taxonomy: the residual errors are mostly sibling concepts sharing wording, so grouping them raises usability and measured reliability together
- Keep benefit tracking in the central management system so realised value is recorded, not estimated from an incomplete spreadsheet

Speaker notes: These are the recommendations a manager can act on without understanding the model. Each traces to evidence: the coverage figure, the adoption footprint, the error analysis, and the undercounted benefits spreadsheet.
Covers: business recommendations (guidance bullet, its own section).

---
# Section 6. Follow-on outcomes

## Slide 16 - Outcomes already realised (1.5 min)

- Used by multiple teams across tax heads, feeding dashboards, profiling and policy analysis
- Recorded benefits in the tens of millions of pounds, with benefit tracking now built into the central management system because the spreadsheet undercounted
- Demonstrated value has already secured further funding and people
- A reusable pattern for HMRC: tags as supervision, on-demand compute, governance model proportionate to risk

Speaker notes: Implications slide. If asked for ROI, the structure is: recorded benefits, analyst time saved, and the compliance yield the profiles now reach.
Covers: implications; evidenced organisational impact (distinction).

---
# Section 7. Actions and next steps

## Slide 17 - Actions, next steps and lessons (2 min)
- Operate the defined drift monitoring: input checks for new taxonomies; retrain on a 2pp metric drop with non-overlapping confidence intervals over two consecutive days; MLflow versioning keeps rollback available
- Complete the manual evaluation of untagged items, the one gap further modelling cannot close, needing ring-fenced SME time
- Harden the delivery stack: tests into a CI pipeline, a more reliable scheduling system, a fully supported Oracle server, and evaluate porting the R components to Python ahead of the lakehouse migration
- Establish the performance ceiling (most common concept per description) so improvement effort is budgeted against what is achievable
- Lessons learned: research existing packages first (Optuna and MLflow would have replaced my manual code), and keep tuning data separate from evaluation data as a standing rule

Speaker notes: End on the biggest limitation stated honestly: evaluation is on tagged data, the use case is untagged data, and the manual evaluation stage is the mitigation. Then thank and invite questions.
Covers: actions and next steps; follow-on work; caveats.

---
## Coverage checklist (EPA plan requirements to sections)

The seven guidance bullets are now the seven section headings, in the guidance's order, so coverage is structural rather than mapped. Research undertaken is section 3 (slides 5 to 10); practical application of KSBs is section 4 (slides 11 to 14).

## Grading theme checklist

| Theme | Slides |
|---|---|
| Business value and growth (K13, K14) | 3, 4, 12, 16 |
| Critical evaluation (K23, S3, S17) | 6, 7, 9, 10 |
| Systematic methodology (S2, S9, S10, S22, S25) | 5, 8 |
| Project and development management (K6, S24) | 11 |
| Communication and influencing (K28, S4, S5, S27, B2, B6) | 9, 10, 14 |
| Technical knowledge (K1, K3, K5, K26, S11, S15, S18) | 2, 8, 12, 13 |

## Likely questions (from the QA list, mapped to prepared answers)

- Why this model and not y? Slide 12; add that a bespoke BERT would need training ourselves if SEC-BERT had been materially superior.
- What if the model goes wrong one day? Slide 16 drift triggers plus MLflow rollback; the category is never automated so failure degrades to analyst review, not wrong decisions.
- Bias and mitigation? Slide 11; representation bias, training proxy, per-class documentation and cautious treatment of small-company output.
- ROI? Slide 15 structure.
- Scope extension? New document types by design (long format, extensible architecture); revalidate taxonomy, extraction and PII assumptions each time.
- Data pipeline? Slide 13; one source (documents received by HMRC), Companies House only for exploration.
- Trade-offs made? Slide 12 plus the single-taxonomy decision: precision on secondary taxonomies traded for consistent class names.
- Lessons learned? Slide 16; also the discarded embedding comparison that taught tuning/evaluation separation.
- Classification metrics? Precision, recall, F1 per class; macro versus weighted averaging; why macro-F1 with imbalance; accuracy kept as the intuitive secondary metric. Know that the report's macro-F1 is the mean of per-class F1s, not the harmonic mean of macro precision and recall.
- Communicating with management? Slide 14 memo story.
- Same content for an external audience? No: remove operational risk detail and anything disclosing compliance thresholds; the Companies House methodology is the shareable version, which is exactly why exploration used public data.

## Images still worth creating for the deck

- Dashboard screenshot for slide 14 (test box plus per-concept reliability view, no customer data on screen). This is the strongest possible communication evidence and does not exist as a file yet.
- A simple coverage graphic for slide 2: 30% of figures usable before, over 99% extracted and classified now, one bar each. Easy to make and lands the headline instantly.
- Slide 12 could show the decision matrix final scores as a three-row table (LinearSVC 0.372, CNN 0.259, SEC-BERT 0.153) rather than an image; tables paste cleanly into PowerPoint from B34.
