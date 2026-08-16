**Source documents used to build this draft** ** *(working note — not part of the submitted repo*t)* 

| Document                                                                                | What was taken from it                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Why                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Z Project Report - Report]]                                                           | Primary content source for this revision: business-problem detail (taxonomy update lag, Oracle column limits, deliberate non-tagging), agile/GitLab rationale, testing and documentation practices, Companies House exploratory dataset, failed cleaning experiments, rejected alternatives (regex repository, frontier LLM API), embedding trade-off timings, decision matrix design, robustness/sensitivity testing, bias analysis by company size and software provider, drift-monitoring thresholds, benefits realisation, and limitations. | Newest and richest set of raw notes (7 Aug 2026). Material was scattered across sections and duplicated, so it has been de-duplicated and moved to the section of the EPA structure where each point earns marks. |
| [[Z Project Report - L7_AI_Data_Specialist_AM1-Project_and_Presentation_Guidance_V2.1]] | The mandatory 13-part report structure, the 5,000-word ±10% limit, the rule that appendices are excluded from the count and must not carry new information, and the full pass/distinction grading table.                                                                                                                                                                                                                                                                                                                                        | This is the BCS specification the independent assessor grades against. Section headings and ordering are taken verbatim so nothing can be marked as missing.                                                      |
| [[Z Project Report - Jesse Karadia - Project Approved]]                                 | The signed-off project title and brief, the KSB mapping, and — critically — the two EPAO feedback comments: *"final report should show the class-level results clearly, especially where minority classes perform less well"* and *"final report should make clear how the ML category is governed in practice… supports analyst review rather than automated decisions."*                                                                                                                                                                      | The report must not drift from the approved brief, and the EPAO's two written requests must be visibly answered. Both are now addressed in §8 and §9.                                                             |
| [[Z Project Report - Review and to do]]                                                 | Notebook-by-notebook facts and figures (dataset sizes, Pearson correlations, silhouette scores, hyperparameters, macro-F1 results) plus the identified gaps against EPA criteria.                                                                                                                                                                                                                                                                                                                                                               | Supplies the verified numbers, and its gap list (bias analysis, data governance narrative, CRISP-DM framing, deployment/scalability, statistical significance) drove what to add.                                 |
| [[Z Project Report - Work_Based_Project_Guidance (1)]]                                  | Per-section content expectations and the four "distinction behaviours": explicit commercial trade-offs, critical evaluation of alternatives, audience-appropriate communication, and evidenced organisational impact.                                                                                                                                                                                                                                                                                                                           | Used as the shaping test for each section — every major decision now states the criteria, the alternative rejected, and the business consequence.                                                                 |
| [[Z Project Report - notes]]                                                            | Consolidated KSB-to-evidence mapping across the six grading themes, and the phrasing on bias ("representation bias, not demographic fairness").                                                                                                                                                                                                                                                                                                                                                                                                 | Used to check every AM1 KSB has a home in the report body, and to keep terminology consistent with the presentation prep.                                                                                         |
| [[Z Project Report - AM1 Previously Asked Questions in Presentation]]                   | The assessor question bank (model choice, failure response, bias, ROI, trade-offs, lessons learned).                                                                                                                                                                                                                                                                                                                                                                                                                                            | Content likely to be questioned is stated explicitly in the report rather than left to the Q&A.                                                                                                                   |
| [[Z Project Report - Assignment - planning and writing]]                                | TEEL paragraph structure and per-section word budgeting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Applied to keep paragraphs claim-led and evidence-backed within the word limit.                                                                                                                                   |
| [[Z Project Report - qa-apprenticeships-harvard-referencing-full-guide]]                | Cite Them Right Harvard format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Raw URLs in the source notes have been converted to author–date citations with a reference list.                                                                                                                  |

**Word count:** body ≈ 5,542 of 5,500 permitted (5,000 +10%) — **42 over.** References, appendices and this header are excluded. A de-duplication pass (13 Aug) recovered ~110 words, but adding the production-pipeline paragraph to §7 spent more than that. §7 (≈890) is now much the largest section, then §5 (≈770) and §3 (≈675). The pending §8 per-class rebuild should recover the overage: the tooling half of §8's per-class paragraph (~60 words) duplicates §9's communication paragraph and belongs there.

**Read the "Working notes" at the end of this file first — this revision reverses the model-comparison argument based on your updated report, and four other things need confirming.**

# Categorising Data in Financial Documents
*Draft — for review and refinement*



## 1. Introduction and Background
HMRC receives millions of financial documents annually — company accounts and tax computations — carrying information used for operational and government policy and to identify tax risk. They arrive as iXBRL (inline eXtensible Business Reporting Language): semi-structured (x)HTML in which key items are tagged with concepts from fixed taxonomies. That concept is a nominal categorical label from a controlled vocabulary, and it is what makes automated extraction and population-scale analysis possible.

For fully tagged documents, previous workflows extracted and analysed the figures reliably. Initial analysis showed some document classes have only around 30% of figures tagged, leaving 70% unusable. The causes range from limitations in the software used to create the documents through to people deliberately leaving untagged the items they would prefer HMRC not to review — so the missing data is not missing at random, and deliberately untagged items in particular have passed unrisked.

Two constraints compounded this. Legacy extraction requires a complex schema update whenever new taxonomies are published, taking up to nine months; HMRC has only twelve months from receipt to open an enquiry, so much of that window could be consumed before the data was usable. The legacy wide-format storage was also approaching the Oracle column limit, capping further coverage.

This report describes Hubble, the tool I built to close that gap. It extracts both tagged and untagged items and uses supervised multi-class text classification to categorise the untagged ones. It also addresses both structural constraints: the system scales with workload, and a long-format Oracle schema replaces the wide one, so any taxonomy is accommodated without a schema rewrite and data is ingested within days of receipt. The central technical challenge is that untagged items carry only a free-text description with no fixed vocabulary, so one conceptual class has many textual representations, in domain-specific terminology — "deferred consideration", "amounts owed to group undertakings" — that analysts are not uniformly familiar with.

I built the initial tool alone, writing the majority of the code and all of the machine learning. As it became more significant to HMRC I made the case for further resource and went on to lead a virtual team delivering it, structuring the technical work with CRISP-DM (Chapman *et al.*, 2000) and managing delivery in increments through GitLab. The tool is now used by multiple analyst teams for population profiling, policy analysis and tax risk identification.

---

## 2. Outline of the Issue and Business Problem

The business problem is that a significant amount of data submitted to HMRC could not be used in bulk analysis, because previous workflows did not extract untagged items. Numerical analysis was restricted to the tagged figures and so could be missing 70% of the numbers in a document. Profiles built on that data lack what they need to identify high-risk returns, directly limiting the compliance yield HMRC can bring in, and the department could not produce accurate statistics for policy decisions. Combined with the nine-month taxonomy lag, this was creating serious operational problems.

The initial requirement was only to extract the raw descriptions, but items can be described in many ways with no fixed vocabulary. Analysis showed some classes had over 23,000 unique descriptions, many of them domain-specific technical terms SMEs confirmed not all analysts would know, with a tail longer than could practically be investigated. Early use therefore depended on complex regular expressions written with SME input: error-prone, incomplete, slow, and — as §6 sets out — not extensible to that long tail at this scale. Since the 30% that *is* tagged is tagged by software or accountants and so makes good-quality training data, I recommended a supervised multi-class classifier trained on it and applied to the rest.

---

## 3. Methods Used and Justification

**CRISP-DM.** CRISP-DM was chosen because it accommodates the cyclical nature of applied ML: modelling discoveries prompt revisions to data preparation, and evaluation findings can send you back to business understanding. Heavier alternatives such as TDSP were rejected as disproportionate — I was the only person on the ML work, so their team roles and process artefacts would have added ceremony without adding rigour. Each phase produced documented artefacts — data quality reports, EDA notebooks, experiment logs, evaluation summaries — giving an evidence base for decisions taken later. That structured iteration, grounded in error analysis each cycle, is the mechanism behind the performance gains reported in §8.

**Project management.** I selected an agile approach (Beck *et al.*, 2001) over a fixed waterfall plan, tailoring practices to the team rather than adopting a framework wholesale — normal practice according to Atlassian (n.d.). The emphasis was Kanban rather than Scrum: the team was small, so Scrum ceremony would have been overhead, and competing business demands made fixed sprints impractical, whereas regular board updates kept this project moving while other commitments were accommodated. Delivery proceeded in usable increments — raw data to file, then more fields and iXBRL information, then ML categories, then improved architecture and the database — each evaluated for feasibility, benefit and risk before proceeding. The original customer requirements would not have foreseen how the project developed, which is precisely the argument for agile over waterfall here.

GitLab is not commonly used for project management in HMRC, so there was a learning curve, but the transparency, auditability and documentation benefits outweighed it; without it, handover would depend on individual memory. Epics supported the longer-term timelines management cared about; the issues board served as the Kanban board; and templates I wrote for issues, tasks and merge requests — requiring reproduction steps, expected versus actual, and a proposed fix — kept quality consistent across the team. Branching with independent review controlled change quality, which needed training the team on branching and on merging the target branch first. Team members documented in the repository's markdown docs and were asked to comment code with *why* rather than *what*.

**Testing.** Testing scope, coverage and implementation across unit, integration and system levels were worked through collaboratively during code review, using `testthat`, which brought an independent view of the system rather than only my own. A firm constraint was that tests must contain no customer data, so synthetic and anonymised fixtures were used throughout. I introduced a policy that new issues and bugs should be accompanied by a test reproducing them, which makes the same class of fault cheaper to diagnose next time; a single command runs the suite, and moving it into a CI pipeline remains outstanding. User acceptance testing produced two changes I would not have anticipated: analysts preferred numeric surrogate keys to natural keys for join performance, and asked for output structured closer to the tables they already used.

**Languages and tools.** R handled extraction and pre-processing: it is the analytical default at HMRC, so is maintainable by far more people here than the alternatives, and `rvest`/`xml2` parse the HTML, `parallel` processes hundreds of documents concurrently, `dbplyr` gives Oracle access in familiar syntax and `testthat` covers testing. Python handled the ML, where the classification ecosystem is far more mature — scikit-learn for traditional models, TensorFlow/Keras for neural networks, HuggingFace Transformers for pre-trained models, Optuna for tuning, and MLflow tracking data version, model version and metrics for every run. `reticulate` imports the Python functions into the R workflow, and Jupyter notebooks gave the exploratory work a reproducible narrative record.

**Scientific method.** Experiments used explicit hypotheses and controlled comparison, with `DummyClassifier` baselines establishing the performance floor, stratified cross-validation reducing variance, and paired t-tests at the 5% level determining whether a configuration was statistically distinguishable from the best run — which let a simpler or faster model be preferred wherever the difference was not real. Class imbalance drove the choice of macro-F1 as the primary metric (§4), and on the modelling side prompted testing of balanced weights and square-root-weighted training samples.

---

## 4. Scope of the Project and Key Performance Indicators

The scope evolved over time: from pure extraction of core data such as descriptions and values to file; to extracting and formatting related fields — headings, table names, structural position (table, row and column number) and iXBRL data (concept, dimensional data); to adding ML classification; to an automated pipeline extracting into an Oracle database. Each expansion was a deliberate decision rather than a drift in requirements, and the architecture was kept extensible to further document types throughout.

Working with stakeholders, four success criteria were established.

- **Macro-F1 > 0.6** — the primary performance metric, weighting all classes equally so that common concepts cannot dominate the score.
- **Accuracy > 0.7** — a secondary metric, retained because it is more intuitive for stakeholders than macro-F1 and easier to reason about in discussion.
- **Automated extraction coverage > 95%** of figures extracted and classified without manual intervention.
- **Timely extraction < 1 week** from date of receipt — the criterion that speaks directly to the enquiry window.

Secondary indicators used in model selection and operation covered performance (precision, recall, training and inference time), sustainability (interpretability, explainability, maintainability, reliability) and HMRC's operational constraints (cost control, data protection, AI safeguards, security, logging, and scaling to millions of records quickly). Carrying this many was deliberate: several — interpretability, cost, deployment risk — later outweighed raw score in the final selection (§7), and fixing them as criteria up front is what made that decision defensible rather than retrospective.

---

## 5. Data Selection, Collection and Pre-Processing

**Data selection.** HMRC's systems are locked down with no readily available GPU access, making exploratory work with complex models difficult, so I ran that phase on a standalone GPU machine over the 298,461 publicly filed iXBRL accounts submitted to Companies House in November 2025 — which also meant the methodology could be shared without disclosing protected data. A month of filings is broadly representative, though many companies choose 31 December or 31 March year-ends; that should have no material impact on the analysis. This yielded 2.8m rows across 956 concepts. The implementation phase then used accounts and tax computations submitted to HMRC.

**Labels.** Tagged figures provide authoritative supervision without additional annotation. The source documents are complex, with inconsistent HTML, varying iXBRL data and multiple taxonomies. Asking SMEs about errors where the predicted class was the one I expected but the recorded concept differed revealed why: concept names vary between taxonomies. A bespoke model per taxonomy would score best but would confuse analysts, so I trained only on the main taxonomy and applied those classes across all of them — precision on secondary taxonomies traded for consistent class names.

**Exploratory data analysis.** Three findings had direct modelling consequences. Rank-frequency plots of both description and concept showed a long tail, with a Pareto chart putting the 75 most common concepts at 95% of items and the distribution closer to lognormal than power-law — the imbalance behind the choice of macro-F1 over accuracy (§4). Second, descriptions and concepts are many-to-many: cosine similarity analysis showed some descriptions such as "Taxation and social security costs" map to very similar concepts, while bare dates map to many unrelated ones. It also showed the taxonomy is specified far beyond what is required or predictable from the human-readable content of the accounts, which sets a real ceiling on any model. Third, the description feature is heterogeneous — nominal text, temporal dates, nominal names, numeric figures — requiring differentiated treatment rather than uniform cleaning. The label itself is nominal and drawn from a fixed taxonomy: a single CamelCase token which, split into words, is human-readable and gives similar concepts similar wording.

**Pre-processing and canonicalisation.** Pre-processing reduced noise and standardised the feature representation.

1. **Text cleaning:** lowercasing and replacement of special characters with spaces. Not every step helped — replacing forward slashes reduced macro-F1 and was dropped, which is why each was tested rather than assumed.
2. **Dates and numbers:** 31 March 1982, which has specific capital gains significance, was mapped to its own token; all other dates became a generic `hubble_date`, and numeric and monetary values `hubble_number`. SMEs confirmed most dates carry no classificatory meaning but a few do.
3. **PII removal:** personal names, company names, addresses and postcodes were identified by regular expression and by taxonomy label and replaced with typed tokens such as `hubble_name`. This served four purposes at once: it preserved privacy and minimised the personal data carried into later stages; it removed a high-cardinality source of vocabulary inflation; it improved generalisation by preventing overfitting to particular entities; and it is more ethical, since a model that never sees a name cannot treat a less common ethnic name differently from a common one.
4. **Length filtering:** descriptions of two characters or fewer carry too little information to classify, and those over 16 words proved on review not to be line-item descriptions at all. Both were removed.
5. **Label engineering:** SMEs advised that a bare placeholder carries too little information to categorise, so records reducing to one were relabelled to match (for example `HubbleName`). The original concept becomes unpredictable, but knowing the item is a name is itself useful in analysis.

Canonicalisation reduced unique descriptions from 266,178 to 10,591 (96%) and labels from 956 to 826, retaining 86% of rows, and moved macro-F1 from under 0.50 to over 0.70.

**Data quality controls.** Controls were aligned to HMRC expectations and the six DAMA UK dimensions (DAMA UK, 2013) referenced by the Government Data Quality Framework (Cabinet Office, 2020). *Completeness* improved because untagged figures are now extracted; *consistency* because tagged and untagged items sit on the same tables in the same format; *timeliness* because data is categorised within days rather than months; *validity* and *accuracy* through the filtering above. Access is restricted to named users, and together these measures satisfied HMRC and regulatory requirements, the DPIA and the Data Protection Act 2018/UK GDPR.

**Splitting.** Because the same data had to serve several frameworks, stratified 80/10/10 train/test/holdout splits — with 1%, 10%, 50% and 100% training subsets and square-root-weighted variants that amplify minority representation — were generated once up front, guaranteeing every architecture was evaluated on identical data.

---

## 6. Survey of Potential Alternatives

The task is multi-class text classification over 826 nominal categories with strong imbalance. I used theory first to narrow the field to approaches suited to supervised classification of short domain-specific text, then tested empirically.


**Three approaches were rejected before experiment.** Systematising the existing regular expressions into a maintained repository of concept-to-regex mappings would be fully explainable, but demands sustained SME time, stays incomplete against a 23,000-description long tail, and remains error-prone — not a feasible business solution at this scale. Unsupervised grouping was attractive because the taxonomy is specified more finely than analysts need, so clustering similar concepts could have simplified the output; the cosine similarity analysis ruled it out, since the variety of descriptions within some concepts is too great for clusters to align with them. A frontier LLM would likely have the best semantic understanding of all, but the input is a short phrase rather than a passage, so most of that capability would go unused — and per-call cost at population scale, plus the data protection and governance position of sending taxpayer-derived data to an external API, made it unfeasible regardless of capability.

**Three families were carried into experiment.** Traditional ML classifies short simple text well, and account descriptions have less variety and more domain-specific vocabulary than generic free text, so terms like "deferred consideration" are discriminative in themselves; scikit-learn offers a strong set of candidates — SVC, LinearSVC, SGDClassifier, DecisionTreeClassifier, RandomForestClassifier, MultinomialNB, ComplementNB and PassiveAggressiveClassifier. Conventional neural networks can learn patterns beyond a fixed algorithm, and DNN, LSTM, GRU, CNN and bidirectional variants are all applicable to text classification. Transformers are a more advanced architecture with better semantic understanding, and pre-training bakes in knowledge from far larger corpora than I could train on; I selected `roberta`, `sec-bert`, `mpnet` and `MiniLM` to span different sizes, architectures and training data, with SEC-BERT of particular interest because it was pre-trained on SEC financial filings and should carry accountancy semantics directly relevant here.

**Feature representation** was a separate axis. Sparse vectorisation (TF, TF-IDF over word and character n-grams) captures domain-specific terminology and phrasing directly and runs fast across many model types. Dense embeddings (mpnet, E5) capture semantic meaning, so should recognise differently worded descriptions of the same concept, particularly ones not seen in training. Both were carried forward for measurement (§7).

---

## 7. Implementation and Performance Metrics

**Population size validation.** Comparing every model and hyperparameter over the full training set was not possible, so I first tested whether smaller populations rank models the same way. Pearson correlation of macro-F1 to the full population was 0.971 at 1% and 0.998 at 10%, and paired t-tests confirmed that models not significantly worse at 1% were also not significantly worse at 100%. This justified filtering on small populations and using 10% for the bulk of the search, cutting experimental compute roughly tenfold without losing ranking confidence.

**Feature representation.** Classifier-independent analysis using silhouette scores put mpnet highest at 0.467 against plain TF-IDF's 0.41, confirming that dense embeddings do separate the concepts more cleanly. That advantage did not survive contact with the downstream task: with the final LinearSVC model, mpnet beat simple TF-IDF on macro-F1 significantly at the 5% level, but by 0.003 and at 76× the runtime. Sparse word n-grams were therefore selected — statistical significance is not material significance, and the sparse representation is faster, easier to maintain and easier to interpret. (An earlier word-plus-character variant was excluded from this comparison: it had been grid-searched on the sample it was then scored against, making the margin an artefact rather than a finding.)

**Traditional ML optimisation.** HalvingRandomSearchCV over 10,000 candidates covered many models and hyperparameters efficiently against a `DummyClassifier` floor; stratified cross-validation reduced variance and let paired t-tests narrow the field at each stage to those not significantly worse at the 5% level. Plotting hyperparameters against score with runtime encoded by colour guided the refined ranges: `min_df=1` occupied clusters both faster and better scoring than `min_df=2`, the speed advantage being a surprise that tabulated results would not have revealed. After tuning on the full training set, LinearSVC beat the alternatives at the 5% level. The final pipeline was TF-IDF (1–3 word n-grams, `min_df=1`, l2 norm) with LinearSVC (`penalty='l1'`, `C=2.8`, squared hinge loss, `dual=False`, `class_weight='balanced'`, `max_iter=10,000`); several values of C performed similarly, so the lower end was taken to limit overfitting. The l1 penalty performs implicit feature selection, producing a sparser weight matrix and faster inference.

**Neural network and transformer optimisation.** Here I used Optuna rather than the manual search above: its TPE sampler explored architectures and hyperparameters over 200+ trials, pruners terminated under-performing trials early, and the built-in importance visualisations showed which choices actually mattered. The CNN was the best conventional network, with dropout as regularisation to limit overfitting; SEC-BERT was the best transformer, consistent with its financial pre-training. Full configurations are at Appendix C.

**Class imbalance.** Three approaches were tested and none generalised across architectures. Balanced class weighting worked well for LinearSVC but degraded the neural models; square-root-weighted training data gave useful macro-F1 gains for small accuracy costs across several models (1.3pp against 0.06pp at 10%); random oversampling reduced transformer performance. The neural models did better on a smaller reweighted training set, LinearSVC best on the full set with balanced weighting — so the treatment had to be chosen per architecture rather than fixed once.

**Final comparison.** Fair comparison required holding the data constant, so LinearSVC, the CNN and SEC-BERT were all trained on the same 10% square-root-weighted population and tested on the same holdout sample — a constraint imposed as much by memory and time as by method. This was a selection experiment rather than the production build: once LinearSVC was chosen it was refitted on the full training set, and that is the model reported in §8. Confidence intervals were bootstrapped at the 5% level rather than using consistent cross-validation folds, which would have been prohibitively expensive across three frameworks.

Rather than compare on macro-F1 alone, I built a weighted decision matrix over eight objective measures — the accuracy, macro-averaged, speed and model-size metrics — and six subjective ones covering interpretability, deployment simplicity, maintenance burden, domain fit, model lifecycle and dependency risk (Appendix C). Subjective scores followed a written rubric with a supporting narrative so they were defensible rather than impressionistic, and were adjusted where confidence intervals overlapped, so differences that were not statistically real could not drive the outcome.

**SEC-BERT had the best macro-F1. I did not select it.** It scored poorly on interpretability, deployment simplicity and dependency risk, and the 2.3pp it gained was not worth a solution needing GPU infrastructure, running roughly 13× slower, on a faster-moving dependency stack. LinearSVC also suits the environment: it handles the sparse high-dimensional matrices TF-IDF produces very efficiently, and l1 regularisation makes them sparser still, so it runs on existing shared CPU infrastructure without degrading service for other users.

**Production pipeline.** On receipt, R parses the iXBRL with `rvest`/`xml2`, `parallel` handling document batches concurrently, and applies the canonicalisation of §5 to produce the description, heading and table-name features. `reticulate` passes these to the fitted Python pipeline, and predictions are written through `dbplyr` into the long-format Oracle tables beside the tagged items, so analysts query one vocabulary across both. On-demand compute — designed with DevOps — starts an EC2 instance for the daily batch and shuts it down on completion, which is what makes the one-week KPI affordable on shared infrastructure. MLflow records data, model and metric versions for every run, so any output can be traced to the model that produced it and rollback stays available. The category is stored as an attributed prediction supporting analyst review, never as a fact driving an automated decision.

---

## 8. Results

The selected LinearSVC, refitted on the full training set and evaluated over the full holdout, achieved accuracy 0.975 (CI 0.975–0.976) and macro-F1 0.785 (CI 0.780–0.788), against KPIs of 0.7 and 0.6 respectively. The CRISP-DM iterations produced documented improvement at each cycle: raw descriptions below 0.50; canonicalisation above 0.70; adding heading and table name as features lifting macro-F1 by a further 9.8pp.

**Per-class performance.** Aggregate accuracy is high, but some classes perform very poorly. I produced per-class summaries so analysts know which concepts need bespoke description matching or alternative filtering rather than the ML category, and an interactive dashboard where users can both test the model on their own text and see how it performs on a given concept — far more usable than a large dataset they would have to filter themselves. It also surfaces top-k predictions; analysts found low-scoring alternatives confusing, so it now shows only plausible matches.

**Error analysis.** Confusion matrices paired with worked examples serve two purposes: they are the evidence stakeholders find easiest to read, and they show what kind of mistake the model makes per concept. Most errors fall between semantically similar concepts. "Amounts owed to group undertakings", for instance, is legitimately associated with several — so the underlying problem is arguably multi-label, while I have modelled it as multi-class. Where a description carries too little information the model predicts the commonest concept for that wording and is scored wrong against a label that is also defensible: a property of the data, not a defect of the model, and SMEs confirmed some items contain nothing anywhere in the document that would determine the concept. This is further evidence that a simplified category set would help, particularly for evaluation.

**Robustness and sensitivity testing.** I built a test suite probing abbreviations, synonyms, typographical errors, OCR corruption, unicode variants, formatting variations, semantically equivalent rephrasings, long context, adversarial phrasing designed to mislead, and instruction-injection strings of the kind that would target an LLM. LinearSVC outperformed SEC-BERT overall — unexpected, since domain-specific training and better theoretical semantic understanding should have favoured it. Where LinearSVC was weaker, on typos and variations, real exposure is low: accountancy documents are generated by software rather than typed. This matters because it is the one place the simpler model could have been quietly worse and was not.

**Bias.** The material bias risk is representation bias across concepts, document types and preparation practices rather than demographic fairness. Large companies scored macro-F1 0.9343 against 0.7898 for small companies; between software providers the spread was wider still, 0.1841 to 0.9133 — likely because smaller companies use cheaper software that tags differently. Because the labels are the preparer's own tags, part of this gap measures inconsistency in *how software tags items* rather than the model's ability to read a description — an artefact of the training proxy that would not arise with human-labelled classes and would not necessarily transfer to untagged items. Residual analysis supports this, misclassifications being concentrated between near-identical classes. It is reported to analysts so small-company outputs are treated more cautiously.

**Explainability.** LinearSVC's coefficients show directly which n-grams drive each prediction, supporting error analysis and HMRC's AI governance requirement; no equivalent exists for SEC-BERT. LIME and SHAP gave comparable explanations across all the models, so interpretability was compared on evidence rather than assumption.


---

## 9. Discussion and Conclusions/Recommendations

The results answer the problem set out in §2: analysts are no longer confined to a tagged minority that is not missing at random, and coverage extends from 30% to close to the full extracted population.

Metrics like macro-F1 rank similar models well, but the decision that mattered here could not be made on score. SEC-BERT won on macro-F1 and was still rejected (§7): in a governed process feeding compliance work, interpretability is a core requirement rather than a tiebreaker. LIME and SHAP partially mitigate the gap and gave comparable explanations across all three models (§8), but post-hoc methods explain a decision where LinearSVC's coefficients expose the mechanism, and that distinction is what lets me show an assessor or an analyst exactly why a description was classified as it was. The same trade recurred wherever an analyst had to act on the output — the single-taxonomy decision (§5) sacrificed precision for class names they could rely on.

Communication is worth reporting where it changed an outcome, and the medium was chosen per audience — presentations, markdown guides, interactive dashboards, working meetings. Early explanations were too detailed to land, so I moved to visual, example-led ones: a decision tree showing what was split on, a two-dimensional SVM boundary, a worked example distinguishing weighted from macro scores rather than the formulas. With analysts, confusion matrices and concrete error cases rather than aggregate scores gave an accurate sense of where the model could be trusted, and use of the ML category rose as understanding did. With managers, a memo framed as cost-benefit — covering improved timeliness and the newly available untagged data — secured infrastructure funding, and framing the case around delivery capacity got further people onto development. Documentation compounded: a clear README let analysts run the tool themselves, and centralising extraction of the full population into Oracle went further, so most users now need only a database query.

Two things I would do differently. An early embedding comparison had to be discarded because the candidate had been tuned on the sample it was then scored against, so its advantage was an artefact of that tuning (§7); separating tuning from evaluation data is now a standing rule rather than something checked at write-up. I also ran the scikit-learn search largely by hand before adopting Optuna for the neural and transformer work, and would use automated search from the start.

**Recommendations**

1. **Extend to further document types**, prioritised by tagging gap and analytical value, revalidating taxonomy, extraction and PII assumptions each time. The pipeline is reusable; the assumptions are not.
2. **Operate the defined drift monitoring**: watch inputs for new taxonomies, and treat a 2pp drop in accuracy or macro-F1 with non-overlapping confidence intervals over two consecutive days as the retraining trigger. Version model, data and preprocessing so rollback stays available.
3. **Establish formal data contracts** with downstream teams now consuming Hubble output; undocumented dependencies on one tool are a continuity risk to them as much as to us.
4. **Complete the manual evaluation against untagged items.** This is the one gap further modelling cannot close (§12), and it needs ring-fenced SME time rather than best-efforts capacity.
5. **Maintain the human-in-the-loop control** (§7): per-class performance documentation should accompany any output relying on the ML category.
6. **Adopt a standard structure for technical communications** — headline figures first, plain-English explanation with illustrations, technical detail in an appendix.
7. **Reduce delivery risk in the stack**: move the test suite into a CI pipeline, and evaluate porting the R components to Python ahead of the lakehouse migration rather than during it.

---

## 10. Summary of Findings

Against the success criteria agreed with analysts and managers at the outset (§4):

| Criterion | Outcome |
|---|---|
| Macro-F1 > 0.6 | **0.785** (CI 0.780–0.788) |
| Accuracy > 0.7 | **0.975** (CI 0.975–0.976) |
| Automated extraction coverage > 95% | Met; the residual is documents using non-standard HTML, which need bespoke positional extraction (§12) |
| Timely extraction < 1 week from receipt | Met — data is extracted, classified and ingested within days, against a previous lag of up to nine months |

Three findings are worth carrying forward. Data preparation mattered more than model choice: canonicalisation moved macro-F1 from below 0.50 to above 0.70, and adding heading and table name added 9.8pp more — both larger than any gain from changing architecture. Second, the best-scoring model was not the right model: SEC-BERT led on macro-F1 by 2.3pp and was still rejected, because interpretability, deployment simplicity and dependency risk mattered more in this context than the margin did. Third, the residual errors are mostly a property of the data rather than the model — the task is arguably multi-label — which sets where further effort should go: richer features and a simplified category set, not larger models.

---

## 11. Implications

**Analytical capability.** The wider population now arrives within days rather than after the taxonomy update cycle, which changes what is achievable inside the twelve-month enquiry window. This improves the statistical basis for policy advice and the completeness of risk identification; Hubble has supported projects that identified hundreds of billions of pounds of incorrectly stated figures in returns.

**Business value and quality.** The tool meets HMRC quality standards for completeness and consistency: nearly all figures are extracted, and the ML category gives one vocabulary across tagged and untagged data. Benefits recorded manually by users ran to tens of millions of pounds in estimated value, but recording was incomplete, so I arranged for benefit tracking to be built into the central management system rather than a spreadsheet. Demonstrated benefit has already secured funding to expand capability and reliability.

**Reusable patterns and governance.** The project establishes a methodology for supervised ML on semi-structured tax data — existing tags as supervision, sub-population correlation validation, square-root-weighted sampling for imbalance, weighted decision matrices for selection — with on-demand compute as a template for other periodic high-volume workloads. The DPIA, PII canonicalisation, human-in-the-loop requirement, per-class documentation and analyst dashboard together form a governance model proportionate to the risk, showing that operationally useful ML can be delivered inside HMRC's governance framework.

---

## 12. Caveats and Limitations

**Evaluation is on tagged data; the use case is untagged data.** This is the most significant limitation. The model is trained and evaluated entirely on items the preparer chose to tag, but its purpose is to classify items they did not. If the two populations differ systematically — for instance where an item was left untagged precisely because no suitable concept exists — measured performance will overstate real performance. Fully human-tagging enough untagged items would require tax-trained SMEs who do not have that capacity, but they will feed into a manual evaluation stage, which is the practical route to quantifying the gap; until then, monitoring prediction distributions, analyst feedback and the human-in-the-loop control stand in its place.

**Minority classes and irreducible ambiguity.** Despite balanced weighting, concepts with few training examples score below the 0.785 average and some score poorly; the per-class dashboard exists so analysts can check reliability first. Separately, generic descriptions such as "total" or "additions" legitimately correspond to several concepts. Heading and table name partially mitigate this; the remainder would need richer context such as surrounding rows or document section, which is harder to extract reliably.

**Scaling behaviour.** LinearSVC does not scale efficiently to much larger datasets, so retraining on substantially more data is impractical — though 10% to 100% gained only 0.4pp macro-F1, so larger datasets are unlikely to help materially. Increasing dataset size at a fixed minimum-count cutoff also admits more labels and can reduce headline macro-F1, and label distributions differ by document type, so scores are not comparable across types or sources.

**Taxonomy evolution and extraction coverage.** New concepts and secondary taxonomies will not be classified correctly without periodic retraining, and preparation practices change over time. Around 15% of documents use non-standard HTML without standard table nodes, needing bespoke positional extraction logic; this is implemented but remains an ongoing development area.

**Technical stack.** The R/Python integration works, but `reticulate` adds setup complexity and other teams have had difficulty with it; with HMRC moving towards a lakehouse architecture and increasing Python use, porting is worth considering.

---

## References

Atlassian (n.d.) *Agile coach: what is agile?* Available at: https://www.atlassian.com/agile (Accessed: 7 August 2026).

Beck, K. *et al.* (2001) *Principles behind the Agile Manifesto*. Available at: https://agilemanifesto.org/principles.html (Accessed: 7 August 2026).

Cabinet Office (2020) *The Government Data Quality Framework*. Available at: https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework (Accessed: 7 August 2026).

Chapman, P. *et al.* (2000) *CRISP-DM 1.0: step-by-step data mining guide*. SPSS Inc.

DAMA UK (2013) *The six primary dimensions for data quality assessment*. Available at: https://www.dama-uk.org/resources/the-six-primary-dimensions-for-data-quality-assessment (Accessed: 7 August 2026).

---

## Appendices

*The following appendices support this report and are not included in the 5,000-word count.*

**Appendix A — Code and documentation**
Jupyter notebooks 00–06 covering data extraction, exploratory data analysis and preprocessing, scikit-learn model experiments, neural network experiments, transformer experiments, and final model comparison. R extraction and pipeline code with `testthat` unit, integration and system tests. GitLab project documentation: data structures and types, Oracle table setup and credential guides, decision log, issue template, and README/setup script.

**Appendix B — Statistical rigour**
Bootstrap confidence intervals for final model metrics. Paired t-test results from HalvingRandomSearchCV and GridSearchCV experiments, including the LinearSVC/SVC/PassiveAggressive comparison and the embedding comparison. Population correlation analysis (Pearson r for 1%, 10% and 100% subset scores). Silhouette score comparison across the untuned vectorisation approaches, with the excluded grid-searched variant and the reason for its exclusion. Per-class F1 breakdown. Bias analysis by company size and software provider.

**Appendix C — Figures and visualisations**
Pareto chart and frequency-rank plots of concept distribution with power-law/lognormal fit comparison; word count distribution; hyperparameter score-versus-runtime plots including the `min_df` comparison; confusion matrices for the final LinearSVC model; Optuna hyperparameter importance and optimisation history; weighted decision matrix and subjective scoring rubric; per-class performance dashboard screenshots.

**Appendix D — KSB mapping**
Mapping of this report to the KSBs for Assessment Method 1: K1, K3, K5, K6, K13, K14, K23, K26, K28; S2, S3, S4, S5, S7, S9, S10, S11, S15, S17, S18, S22, S24, S25, S27; B2, B6.

**Appendix E — Employer verification**
Verification by HMRC that this project report is a true reflection of Jesse Karadia's involvement and is their own work.

---

## Working notes — resolve before submission

*(Not part of the report.)*

**Resolved by the 13 Aug report update** — hyperparameters (TF-IDF 1–3 n-grams, `min_df=1`, l2, `C=2.8`, `max_iter=10,000`) are now consistent across sources; silhouette figures are in (mpnet 0.467 vs TF-IDF 0.41); the heading/table-name uplift is 9.8pp; and the headline results are 0.975 accuracy / 0.785 macro-F1 with CIs. All are now in the draft.

**Corrections made this pass — check I have read these right:**

1. **The model comparison is reversed from the previous draft.** Your updated report says SEC-BERT had the *best* macro-F1 and was rejected on interpretability, deployment simplicity and dependency risk, with LinearSVC 2.3pp behind and ~13× quicker. The earlier draft claimed LinearSVC was marginally *ahead* of SEC-BERT (0.787 vs 0.782). §7, §9 and §10 now argue the trade-off version. This is the stronger argument for the grading criteria — rejecting the best-scoring model on stated business criteria is exactly the distinction descriptor — but it must be right.
2. **The comparison table is gone.** Your report now says all three architectures were trained on 10% square-root-weighted data and tested on the same holdout sample for fairness, which contradicts the old table (LinearSVC 100%, CNN 10% sqrt, SEC-BERT 100%). **The per-model numbers under the fair protocol are missing** — if you have them, a three-row table would be strong evidence. Otherwise §7 stands on prose.
3. **KPIs changed.** §4 now uses your four criteria (macro-F1 > 0.6, accuracy > 0.7, coverage > 95%, extraction < 1 week). The old inference-latency KPI and the short/long-term milestones are gone, and §10's table follows the new set.
4. **Testing paragraph rewritten.** The earlier draft said you wrote the tests then assigned ownership to a colleague; your report says testing scope and coverage were worked through collaboratively during code review. §3 now says the latter.

**Still open:**

5. **Inference latency.** Your report says 2.7ms; earlier notes said 2.7μs and 2.7s. All specific latency figures have been removed from the draft rather than guess. **Confirm the unit** and it can go back into §7 — it is a good number either way.
6. **Coverage KPI has no measured figure** — §10 reads "met". Get the actual percentage, or leave as is.
7. **"Hundreds of billions" is no longer in your report.** You asked for it restored, so it remains in §11. Your updated report only carries the "tens of millions" recorded-benefits figure. Decide which you can evidence.
8. **Canonicalisation statistics** (266,178 → 10,591 unique descriptions; 956 → 826 labels; 86% of rows retained) come from the notebook review, not your report. They are good evidence — **confirm they still hold** for the current pipeline.
9. **Extraction edge cases.** The earlier "~15% of documents use non-standard HTML" figure sits awkwardly beside a >95% coverage KPI. §12 now describes it without the percentage. The PII edge-case limitation was dropped, since your updated report no longer carries it — restore if it is still true.
10. Consider whether the 12 million annual returns figure can be sourced; currently generalised to "millions".

---

# KSB and requirements gap check against `Z Project Report - Report mod`

*Checked 15 August 2026 against the signed-off mapping document and the QA Harvard guide. Each item names the section of Report mod it needs to go into.*

## A. EPAO written feedback — these were explicitly requested and must be visibly answered

### A1. Class-level results are not shown — goes in §8, plus a new Appendix B entry

EPAO wrote: *"final report should show the class-level results clearly, especially where minority classes perform less well and need analyst review."*

Report mod currently carries one sentence in §8: "Residual analysis identified which classes performed poorly, and summaries with confusion matrices for good and poor quality classes were produced for analysts (Appendix A3.10 and B24)." The words "per-class" and "minority" do not appear anywhere in the body, and there is no per-class F1 table in Appendix B — B24 holds confusion matrices for a handful of individual classes only.

Needed:
- **§8** — a short paragraph giving the shape of the per-class distribution: how many of the 826 classes fall below, say, 0.5 macro-F1, what the median per-class F1 is, and what an analyst should do when a concept they need falls in that group. This is the single highest-value addition left in the report, because it was asked for in writing.
- **New Appendix B entry** — per-class F1 breakdown, or at minimum the distribution (histogram or decile table) plus the worst-performing named concepts. The data is in notebook `03_ixbrl_experiment_models.ipynb` section 10 (residual analysis) and section 7.3.

### A2. ML governance is described as a caveat, not as practice — goes in §7.6

EPAO wrote: *"final report should make clear how the ML category is governed in practice, particularly that it supports analyst review rather than automated decisions."*

The human-in-the-loop statement currently sits only in §12 Caveats and limitations. Placed there it reads as a limitation of the model; the EPAO asked how the category is *governed in practice*, which is a design statement and belongs with the production system.

Needed:
- **§7.6 Wider system** — two or three sentences stating the control as implemented: the ML category is stored alongside the tagged value rather than replacing it, is attributed as a prediction, is never an input to an automated decision, and is accompanied by per-class performance documentation and the dashboard so an analyst can check reliability before relying on it. MLflow lineage means any output traces back to the model that produced it.
- Keep the §12 statement as well — it is legitimate there, but it should not be the only place.

## B. Assessment criteria with no clear evidence in the body

### B1. Autonomous versus collaborative working — goes in §9

Pass criterion (theme 5): *"Explains how to work autonomously and collaboratively with multidisciplinary teams indicating when each would be appropriate."* Also underpins **B2** (reliable, objective, capable of independent and team working).

"Autonomous" appears zero times in the body; there is a single mention of collaboration in §7.6. This criterion asks specifically for the *judgement about when each is appropriate*, which is not stated anywhere.

The signed-off mapping already has the material. Needed in **§9**, roughly:
- Worked autonomously where deep focus was required — core modelling, building and evaluating models — then demonstrated the approach and took feedback in review meetings.
- Worked collaboratively with SMEs on evaluation, where their taxonomy knowledge was the binding constraint; with DevOps on infrastructure, where they held the expertise and the access; and on other team members' tasks to share knowledge and upskill them.

### B2. Working with software engineers on testing *and* documentation — goes in §3.5

Pass criterion (theme 5): *"Explains how to work with software engineers to ensure suitable testing and documentation processes are implemented."*

§3.5 says "While working with others to review the code base, we discussed the scope, coverage and implementation of unit, integration and system testing." It does not name software engineers or developers, and the documentation half of the criterion is handled separately in §3.3 with no link between them.

Needed in **§3.5** — name who the review was with, and connect it to the documentation practices in §3.3 so the two halves of the criterion read as one process rather than two unrelated paragraphs.

### B3. Truthful presentation of data and conclusions — goes in §8

**B6** requires *"Presents data and conclusions in a truthful and appropriate manner."* The report demonstrates this repeatedly but never claims it, and one relevant disclosure is missing.

You have strong evidence already: §8 quotes the full-holdout macro-F1 of 0.785, which is the **lowest** of the four evaluation sets (test 5% 0.791, test full 0.789, holdout 10k 0.817, holdout full 0.785 — see Appendix B38); §8 reports a bias spread of 0.184 to 0.913 that does not flatter the model; and §8 reports the SEC-BERT robustness result that contradicted your stated expectation.

Needed:
- **§8** — one sentence stating that the most conservative evaluation figure is the one reported, and why.
- **§12** — an omission worth closing: the final LinearSVC fit on the 100% training population logged repeated `ConvergenceWarning: Liblinear failed to converge` at `max_iter=10,000` (notebook cell 131). Cross-validation scores were stable across folds (0.782–0.792), so it did not affect the result, but it is not mentioned anywhere in the report and is a fair question. Disclosing it costs a sentence and supports B6 directly.

### B4. Maintaining the service, not only building it — goes in §7.6 or §9

**S15** is *"Identify, develop, build and maintain the services and platforms that deliver AI and data science."* §7.6 covers identify, develop and build well. Maintenance in operation — who runs it now, what the retraining trigger is in practice, what monitoring exists today as opposed to what is recommended — is not stated. Drift monitoring appears only as a recommendation in §9.

Needed in **§7.6** — one or two sentences distinguishing what is operating now from what is recommended, so the reader can tell which is which.

### B5. Lower priority, already largely covered

These are met but thin; only worth touching if words allow:
- **S5** (manage expectations, present findings to stakeholders) — §9's dashboard paragraph and the analyst education on model error cover this; the word "expectations" is not used, which is fine.
- **S18** (tools that visualise data systems and structures for monitoring and performance) — the dashboard in §9 is the evidence. Making explicit that it visualises per-concept performance would strengthen it, and overlaps with A1 above.

## C. Appendix D is empty

`## Appendix D. Mapping of the project report to AM1 KSBs.` is a heading with no content beneath it. Appendix D needs the actual mapping table.

The definitive KSB list, taken from the signed-off document's "underpinning assessment criteria" rows, is **25 KSBs**:

- **K1, K3, K5, K6, K13, K14, K23, K26, K28**
- **S2, S3, S4, S5, S9, S10, S11, S15, S17, S18, S22, S24, S25, S27**
- **B2, B6**

Note: the Appendix D list earlier in this draft includes **S7**, which does not appear anywhere in the signed-off mapping document. Either it came from another source or it is an error — worth checking before it goes into the submitted appendix.

Suggested format: one row per KSB, with the report section and the appendix reference that evidences it. Appendices are excluded from the word count, so this costs nothing against the 5,500.

## D. Harvard referencing compliance (QA Cite Them Right 11th edition)

Checked the 49 entries in §13 against the guide.

**Compliant:** alphabetical order; `no date` used for undated sources; `et al.` for four or more authors; multiple citations ordered earliest to latest and separated by semicolons; full clickable URLs with access dates; article titles in single quotation marks; `Data Protection Act 2018` italicised in-text with no brackets, as the guide requires for Acts.

**Not compliant — affects all 49 entries:** no italics are used anywhere in the reference list. Cite Them Right requires italics on:
- book, report and webpage **titles** — e.g. `Beck, K. (2003) *Test-driven development: by example*. Boston, MA: Addison-Wesley.`
- **journal and conference proceedings names** — e.g. `... 'Optuna: a next-generation hyperparameter optimization framework', *Proceedings of the 25th ACM SIGKDD ...*`
- the title of an Act in its reference list entry

Article titles stay in single quotes, which you already do correctly. This is a mechanical pass over §13 and does not affect the word count.

**One thing to confirm rather than fix:** the QA guide requires generative AI content to be acknowledged and states that work submitted for assessment must be your own. Check QA's position on AI assistance for the EPA project report specifically, and whether any acknowledgement is expected. This is a question for your provider, not something to guess at.

## E. Criteria that are already well evidenced — no action needed

Recorded so these are not redone:

- **K13, K14** (trade-offs, business value) — §2 quantifies the problem and the value; §7.5 states the 2.3pp trade against interpretability, speed and dependency risk; §11 carries realised benefit.
- **K23** (performance and accuracy metrics) — §4 KPIs, §7, §8, Appendix B38.
- **S3** (critically evaluate arguments and incomplete data) — §6 rejections, §8 bias reading, §12.
- **S17** (data curation and quality controls) — §5.3 DAMA dimensions, DPIA, DPA 2018/UK GDPR.
- **S2, S9, S10, S22, S25** — §5, §6, §7.1, §7.2.
- **K6, S24** (methodology and project management) — §3.1, §3.2, §3.3.
- **K28, S4, S27** (communication, SME questioning) — §5.1, §5.3, §9.
- **K1, K3, K5, K26, S11** (methods, statistics, scientific method) — §3.5, §7.1, §7.2, Appendix C.
- **Distinction descriptors** — commercial trade-offs (§7.5), critical evaluation of alternatives (§6), audience-appropriate communication (§9), evidenced organisational impact (§11).

## F. Ordered by value if word budget is tight

Body is currently ~6,236 words against 5,500, so everything below has to be traded against something else.

1. **A1 class-level results (§8)** — asked for in writing by the EPAO. Do this even if something else has to go.
2. **A2 governance in practice (§7.6)** — also asked for in writing.
3. **Appendix D KSB mapping** — free, appendices are not counted.
4. **§13 italics** — free, formatting only.
5. **B1 autonomous/collaborative (§9)** — a whole pass criterion with no evidence; roughly 40 words.
6. **B3 convergence disclosure (§12)** — one sentence, supports B6.
7. **B2 software engineers (§3.5)** — rewording rather than addition.
8. **B4 maintenance (§7.6)** — one sentence.

---

# State and decisions — handover note, 15 August 2026

*Written so a fresh session can pick up without re-litigating settled questions. Everything above in this gap check is now closed except Appendix D.*

## Where things stand

Body is **6,456 words against the 5,500 limit — 956 over**. Per section:

| § | Words | | § | Words |
|---|---|---|---|---|
| 1 | 186 | | 7 | 1,103 |
| 2 | 298 | | 8 | 508 |
| 3 | 678 | | 9 | **1,247** |
| 4 | 217 | | 10 | 111 |
| 5 | **1,016** | | 11 | 116 |
| 6 | 560 | | 12 | 339 |

Cutting targets are **§9, §7 and §5**, which are 52% of the body between them. §9 has never had a density pass and has grown by ~250 words this session. §10 and §11 are already lean at ~110 each, so the §8–11 deduplication once mapped is worth far less than first estimated.

## Open items

1. **Appendix D** — still an empty heading. The KSB mapping table. Deliberately left until last. Appendices are not word-counted, so it costs nothing. Definitive list is the 25 KSBs in section C above; note **S7 is not in the signed-off mapping** despite appearing in the older Appendix D list in this draft.
2. **`{which was?}`** in §12 — the only editorial note left in the document. Asks what the performance variation on HMRC data actually was. That figure is not in the public notebooks, so it needs to come from HMRC-side results or the sentence should be cut.
3. **~956 words to cut.**

## Settled — do not re-suggest

- **The 9-month / 12-month enquiry window detail** was deliberately cut as too much detail. Consequence accepted: §4's one-week KPI has no stated rationale on the page.
- **The person-hours total** in §2 (2 people × ~2 hours × hundreds of concepts) was declined on word budget.
- **A "most conservative figure" sentence in §8** and **a maintenance sentence in §7.6** were both considered and dropped, given the overage. B38 already carries the four evaluation sets, so the conservative-reporting point is evidenced without the sentence.
- **Em dashes, `however`/`thus`/`moreover`, colon-elaborations and short punchy sentences** are not the author's voice. See the `epa-report-voice` skill.
- **Cross-references use `(Section 11)` and `(Appendix B24)`**, never `§` or bare `(B24)`.
- **Corrections should be minimal** — `from → to` with a plain reason, not rewritten paragraphs.

## Verified figures — recomputed from the model, not taken on trust

Loading `grid_search.joblib` and scoring the holdout reproduces **accuracy 0.9754 / macro-F1 0.7849**, matching the report. From the same run:

- Median per-class F1 **0.966** against a mean (macro-F1) of 0.785 — this gap is what explains the accuracy/macro-F1 difference
- **141** of 826 labels reach training, because `MIN_EXAMPLES = 350`; the 685 excluded carry 26,151 rows
- 27 of 141 concepts score below 0.5, eight score zero; 94.1% of holdout rows sit in concepts scoring above 0.9
- `max_iter` was searched over 5,000 / 10,000 / 20,000 with no significant difference, so the convergence warning is a documented non-issue

## Hygiene before submission

Regressions appear every editing round. Re-run both just before submitting — they are at `~/.claude/skills/epa-report-voice/scripts/`:

- `formalise.pl` — expands contractions, normalises curly apostrophes, skips `{...}` notes
- `fixparens.pl` — adds the missing space before `(`, skips inline code

Both take a line range for sections 1–12 and print counts for verification. Also check for stray `{...}` notes outside code fences, and that the reference list italics survive whatever export route is used, since they are Markdown asterisks rather than real formatting.

---

# Review pass — 15 August 2026, late evening

*(Not part of the report. Review of `Z Project Report - Report mod` against the Z Project Report documents and the Code/ notebooks. Changes below marked **done** were made directly in Report mod; everything under "For your review" is a suggested change to the report body and has NOT been made.)*

## Done directly in Report mod

**Typo and grammar fixes (body, minimal):** lead → led a virtual team (§1); "every year especially" → "every year, especially" (§2); SCRUM → Scrum (§3.1); evidenced-back → evidence-backed (§3.5); "scope covered, extraction" → "scope covered extraction" and "time(Section 9)" → "time (Section 9)" (§4); "In some situation" → "In some situations", "expressions and labels replaced" → "expressions and labels, and replaced", "taxonomy and without hitting" → "taxonomy without hitting", "measure such as" → "measures such as" (§5); "some successes" → "some success", "often outperforms" → "often outperform" (§6); "not only cheaper and more available" → "not only cheaper but also more available", missing full stop after "B35 and B36", "database7 a" → "database" (§7.6); "the predicting one" → "the predicted one" (§9); "keys for joining rather than natural keys for join performance reasons" → dropped the duplicated "for joining" (§9); "was a reasonable choice ... due computations cost" → "which was a reasonable choice ... due to computational cost", stray "Al" removed, "f1-macro" → "macro-F1", "different than" → "different from", "e.g. An item" → "For example, an item", "suggest like Python" → "suggest that Python" (§12).

**Appendix heading typos:** A2.4.1 "Descripbe" → "Describe"; A3.4.3 "poulation" → "population"; A4.3.1 "200 trails" → "200 trials".

**Appendix D filled** with the KSB mapping table: 25 KSBs grouped under the six grading themes from the sign-off document, criterion wording verbatim from the signed-off mapping, with a detailed evidence column referencing report sections and appendices. S7 was excluded as agreed (it is not in the signed-off mapping). Worth a read-through to check the evidence column says what you would say.

**New Appendix A7** for the `Code/ixbrl_ai/` module you added: intro paragraph plus full code for `data_prep.py`, `sample.py`, `data.py`, `test.py` and `display.py` (`eda.py` and `__init__.py` are empty and were skipped). Body references to `clean_field` etc. still point at Appendix A2.3, which remains valid since the notebook copies are still there; if you would rather point them at A7.1, that is a one-line change per reference.

**Hygiene scripts re-run** over the body: one fix found (the `time(Section 9)` space), no contractions. Note the scripts have hardcoded line ranges that no longer match the file; I ran them with corrected ranges. If you edit further, re-run them with the body's current line range (the reference list must stay out of range, since fixparens corrupts DOIs like `10.1016/0377-0427(87)90125-7`).

**A warning:** while I was editing you had the file open in Obsidian, and one save reverted about half my fixes (everything from §7.6 onward, plus Appendix D) before I re-applied them. Everything is verified present as of this note, but if Obsidian was holding older unsaved state, re-check before submitting: the greps to run are `grep -c "database7 a"` (want 0) and `grep -c "The 25 KSBs assigned"` (want 1).

## Figures verified against Code/

- **7,795 unique descriptions after canonicalisation is correct.** The notebook's actual output is 7,795; the "10,591" in the notebook's markdown commentary (and in this draft's earlier header) is stale. The report is right; the notebook commentary cell in `01_ixbrl_eda_preprocessing.ipynb` is worth updating to match its own output.
- **67× is confirmed** for the TF-IDF versus MPNet timing (notebook: "only 0.003 worse f1-macro score but was 67 times faster"). This draft's earlier "76×" was wrong.
- **0.3pp** for 10% → 100% training gain is what the notebooks support; this draft's earlier 0.4pp was wrong.
- **220× could not be fully verified from the public notebooks.** The decision matrix output shows SEC-BERT inference at 0.051282 s/sample but LinearSVC's row was not extractable from the saved output. The ratio is plausible (≈0.23 ms/sample for LinearSVC). Confirm against Appendix B32 before submission; note the signed-off mapping said "quicker(13x)", so the assessor may ask which is right — 13× may have been training time and 220× inference, worth being able to say which.

## For your review — suggested body changes (NOT made)

**1. The `{which was?}` note in §12** is the only editorial note left. The HMRC-side performance figure is not in the public notebooks, so either supply it or cut the clause. Suggested cut, from:
> "...making comparison difficult across different populations, document types and sources. So performance varied when implementing on HMRC data.{which was?}"

to:
> "...making comparison difficult across different populations, document types and sources."

Saves 12 words and removes the unevidenced claim. If you do have the HMRC figure, instead end: "So performance on HMRC data was Xpp lower, which was expected for these reasons."

**2. Filter thresholds in §5.3 do not match the code.** `filter_data` in `ixbrl_ai/data_prep.py` (now Appendix A7.1) keeps descriptions with more than 2 characters and at most 15 words (`MAX_WORDS = 15`). §5.3 says "shorter than 2 characters ... or longer than 16 words". Suggested, from:
> "removing descriptions shorter than 2 characters, missing, low-quality, or longer than 16 words"

to:
> "removing descriptions of 2 characters or fewer, missing, low-quality, or longer than 15 words"

No word cost. Truthful-presentation point (B6), and the code is now in the appendix where an assessor can check it. (The code comment saying "less than 12 words" is stale too — worth fixing in the module.)

**3. Word budget.** Body is **6,350 words against 5,500 — about 850 over.** Current section counts: §1 191, §2 313, §3 684, §4 228, §5 1,023, §6 566, §7 1,122, §8 511, §9 1,252, §10 116, §11 119, §12 225. The cuts below are ordered by how little they cost you in marks; together they save roughly 480 words. The remaining ~370 needs a decision only you can make, noted at the end.

**Cut A — §9, the coefficients example (~58 words).** Remove the sentence beginning "For example, the phrase "cost of" appears near the bottom of the positive coefficients...". The preceding sentence already makes the claim, and the example itself is in Appendix B23 and B39 where the assessor can see it. Highest-value cut in the report.

**Cut B — §9, the TF-IDF/LinearSVC mechanics paragraph (~38 words saved).** "The short domain-specific descriptions lend themselves well..." duplicates §7.5 (CPU infrastructure) and §7.2 (the pipeline). Suggested replacement:
> "TF-IDF suits the short domain-specific descriptions, and LinearSVC with L1 regularisation works efficiently with the sparse matrices it creates, so I could develop the model on existing infrastructure without impacting other users."

**Cut C — §9, Optuna/MLflow lessons paragraph (~45 words saved).** Suggested replacement:
> "I discovered Optuna while working on the neural networks, and its automated tuning and built-in visualisations could have replaced much of the manual scikit-learn search, just as MLflow replaced my manual code for storing results. So going forwards I would research existing packages before coding my own solution."

**Cut D — §9, readme paragraph (~35 words saved).** Suggested replacement:
> "The project readme uses markdown headings, instructions and code blocks, and has let many analysts set up and run the tool themselves. Further development centralised extraction of the full population into Oracle, so most users now just need a database query. When users have issues or questions, I update the relevant documents to cover them."

**Cut E — §9, dashboard paragraph (~35 words saved).** Suggested replacement:
> "Repeated questions about the machine learning led me to create an interactive dashboard where users can test the model and see how it performs per concept, including the kind of mistake to expect. It initially showed the top-5 predictions, but the poor matches confused users, so I changed it to show only plausible matches. As users' understanding improved, their use increased."

**Cut F — §9, the agile/waterfall sentence (~30 words).** "The customer requirements at the beginning would not have foreseen the way the project developed, highlighting the benefit of an agile approach as opposed to a more fixed waterfall approach." §3.1 already justifies agile; the paragraph's first sentences already say iterating delivered value.

**Cut G — §9, UAT paragraph (~33 words).** The numeric-keys and familiar-structure points are nice but §9 already evidences acting on user feedback twice (dashboard, docs). Cut whole paragraph, or keep if you want the join-performance detail for questioning.

**Cut H — §9, second SEC-BERT security paragraph (~19 words saved).** Merge the two sentences:
> "Since SEC-BERT is not from a well-established provider, security aspects may have prevented use even if it had won the decision matrix; if it had been materially superior we would need to consider training our own BERT based model."

**Cut I — §3.4, package lists to prose (~70 words saved).** Keep every package name (S25 evidence) but drop the per-bullet glosses, e.g.:
> "I used R since it is the default coding language at HMRC, so has much greater support and maintainability: `aws.s3` for the S3 documents, `rvest`/`xml2` for extraction, `parallel` to process hundreds of documents at once, `dbplyr` for Oracle access in the tidyverse syntax analysts know, and `testthat` for testing."

and the equivalent for the Python list.

**Cut J — §9, recommendations (~40 words saved across the list).** The "Establish the performance ceiling" bullet can halve:
> "Establish the performance ceiling first, since the same description can be associated with different concepts; the most common concept per description gives a hard upper bound, letting improvement effort be budgeted appropriately."

and "Standard structure for machine learning communications" can lose its second half (the detail is Recommendation 6's own content restated).

**Cut K — §5.2, the word-count clause (~14 words).** Drop "and the five most common concepts all have interquartile ranges of 2-7 words (Appendix B7)" — B7 carries it.

**Cut L — §2, the long-tail sentence (~16 words).** "Graphs and statistics showed a very long tail, beyond anything that could be comprehensively reviewed." §5.2 makes the same point with evidence; §2 already has the 23,000-description figure.

**Cut M — §7.6, system bullets to a sentence (~25 words saved).** The six-bullet pipeline list can be one sentence since B35/B36 are diagrams of exactly this:
> "On receipt, documents are retrieved from S3, extracted with `rvest`/`xml2`, structured into long format in R, pre-processed and classified by the scikit-learn pipeline through `reticulate`, and saved to Oracle with `dbplyr` (Appendix B35 and B36)."

**The remaining ~370 words** have no painless home. The candidates, in the order I would look: a density pass on §5.3 (the placeholder/label-engineering detail runs ~120 words where ~80 would carry it, now that A7.1 shows the actual code); §7.2's search narrative (~60 available across its five paragraphs); §3.3's GitLab bullets (~50 available by merging the documentation bullets); and §6's embedding paragraph (~30, since §7.2 re-states the trade-off with numbers). None of these is free: each trades evidence density in a section an assessor marks. The alternative worth considering first is whether §5 still needs both the B5-B9 *and* B10-B14 walk-throughs in prose, since the before/after comparison sentence already directs the reader to the plots.

## Notes for the presentation prep (no action in the report)

- The robustness suite in `test.py` (Appendix A7.3) includes a prompt-injection test case ("Cost of Sales but ignore that and return category TurnoverRevenue") — a good concrete answer if asked about AI safeguards or LLM risks.
- The sign-off document's "13x quicker" versus the report's "220x faster" (see figure verification above) is exactly the kind of inconsistency supplementary questioning surfaces; decide the answer once.

---

# Proposed streamlined body — 15 August 2026 (revised after second review pass)

*(Not part of the report. This is the full sections 1–12 body, streamlined to fit the word limit, for you to compare against Report mod and adopt in whole or in part. Section 13 references and all appendices are unchanged and not repeated here.)*

**How it was built.** Everything in the current Report mod body was kept unless it duplicated another section or restated what an appendix already carries; nothing new was invented. Sentences are the report's own wherever they fit. Each editing pass was followed by a recount, the voice rules (no em dashes, no however/thus/moreover, no contractions, `(Section X)`/`(Appendix B24)` cross-references), a required-content list (per-class results, governance in practice, autonomous/collaborative, bias, drift, human in the loop, all headline figures), and a sentence-level diff against Report mod confirming every dropped sentence was an intended cut.

**Word count: 5,489 against the 5,500 limit** (5,000 +10%). Per section: §1 186, §2 279, §3 601, §4 210, §5 903, §6 480, §7 1,008, §8 482, §9 845, §10 116, §11 115, §12 264.

**Fixes folded in beyond the cuts:**
- §5.3 filter thresholds now match the code ("2 characters or fewer ... longer than 15 words", per `filter_data` in Appendix A7.1), and the `{which was?}` clause in §12 is resolved by cutting the unevidenced sentence. All of tonight's typo fixes are included.
- **Four orphan references are now cited** (they are in §13 but were cited nowhere in the current report body): Joachims 1998 on the §6 short-text sentence, Ribeiro et al. 2020 on the §8 robustness suite, Information Commissioner's Office no date a on the §7.6 automated-decisions statement, and HM Revenue and Customs 2024 on the §1 opening. Cite Them Right requires the reference list to contain only cited works, so if you prefer not to cite one of these, delete its §13 entry instead.
- **Appendix A7 is now referenced** from §5.3 (A7.1) and §8 (A7.3), so the new module is anchored to the body.
- **The autonomous/collaborative sentence in §9 now answers the criterion as written** ("indicating when each would be appropriate"): autonomous where deep focus was required, collaborative where SMEs or DevOps held the knowledge or access. This was the one pass criterion the current wording only half-answered.

**What was cut, by theme:** §9 lost its duplicated arguments (the coefficients worked example now lives only in Appendix B23/B39, the TF-IDF mechanics paragraph merged to one sentence, the agile-versus-waterfall repeat of §3.1, the UAT paragraph, and the DevOps clause of the communications paragraph); §3.4's package glosses tightened around the same package lists; §5 and §6 lost restatements of points made elsewhere; §7.6's pipeline bullets became one sentence since B35/B36 diagram it. Every number, package name, KSB evidence point and both EPAO-requested items survive; the guidance document's per-section expectations and four distinction behaviours were checked against the final text.

# 1. Introduction and background.

HMRC receives millions of financial documents such as company accounts and tax computations (HM Revenue and Customs, 2024) that contain a large amount of information used to provide insight for departmental/government policy and to identify tax risk. They are iXBRL documents; semi-structured (x)HTML where key items are tagged with concepts from fixed taxonomies (XBRL International, no date).

Previous workflows allowed us to reliably extract, structure and analyse fully tagged documents, but a large proportion of figures in some document types are untagged, for various reasons from limitations in accountancy software to people deliberately leaving items they do not want HMRC to review untagged.

The business priority was to make all the key data items usable analytically promptly after receipt.

Hubble is a tool I developed that extracts both tagged and untagged items from iXBRL documents and classifies them. I initially worked on Hubble myself, writing the vast majority of the code and all the machine learning, but as the project became bigger and more important to HMRC I arranged for more resource and led a virtual team working on the project.

# 2. Outline of the issue or opportunity and the business problem to be solved.

Initial analysis showed that some document types only have approximately 30% of the figures tagged, so bulk numerical analysis could not use 70% of the figures. Profiles therefore did not have access to billions of figures to properly identify errors and high-risk returns, limiting compliance yield HMRC can bring in by at least tens of millions of pounds (Section 11). We could not always provide accurate data or statistics for the department/government to make informed decisions. The previous workflows to extract iXBRL data required complex and long schema updates every year, especially with Oracle's 1,000 column limit being hit, significantly limiting how current the data was.

Initial requirements just included extracting raw data such as descriptions, but items can be described in many different ways with no fixed taxonomy. Analysis showed that some classes had a large variety of descriptions, some with over 23,000 unique ones, and subject matter experts (tax professionals) highlighted that many are domain-specific technical terms not all analysts would be familiar with. Existing ad-hoc approaches took an hour or two for an analyst and subject matter expert to properly explore a single concept, with some projects having hundreds of potential concepts, which was not feasible.

The 30% of items that are tagged were tagged by software or accountants, so were expected to be reasonable quality training data for supervised learning that could then be applied to the untagged 70%. I recommended creating a supervised multi-class text classification machine learning model to classify the items. This would save significant analyst and subject matter expert time; reduce errors; and improve analysis quality.

# 3. Methods used and justification

## 3.1. Project management

I selected an agile approach for the overall project (Beck et al., 2001), not strictly adhering to a specific framework but selecting practices that were appropriate (Atlassian, no date). It was more Kanban focused since the project team was small and the overhead of Scrum would not be appropriate. Competing business demands meant fixed sprints were impractical, but regular Kanban updates ensured progress on this project while other business needs were met.

## 3.2 CRISP-DM

I used CRISP-DM since it accommodates the cyclical nature of machine learning and provides a clear intuitive structure (Chapman et al., 2000). I worked on the machine learning myself, so CRISP-DM is more appropriate than larger methodologies like TDSP (Microsoft, 2023). Each stage produced documented artefacts, allowing evidence backed decisions in other steps.

## 3.3 Version control and documentation

While using GitLab to manage projects is not common in HMRC (bespoke spreadsheets are normally used), I decided that the advantages of transparency, auditability and documentation outweighed the costs of learning a new tool.
- Documentation covered data structures and types, Oracle table/credential setup, and key decisions with the reasons why they were made.
- The issues board worked well as the Kanban board tracking work, and the epics were useful for management, who focus on longer term timelines.
- Templates I created for issues, tasks and PR ensured they were completed to a consistent level by all team members, covering the steps to recreate the issue, expected vs actual, and proposed fixes.
- I encouraged team members to document issues in detail on GitLab, update project markdown documents, and write code comments about why rather than what.
- Version control, branches and independent review of PR helped ensure changes were of sufficient quality and limit issues. This required training the team to use branches, which I videoed for reference.

## 3.4 Languages and packages

I used R since it is the default language for analysts at HMRC, so has much greater support and maintainability, and has the relevant packages: `aws.s3` for the iXBRL documents in AWS S3, `rvest`/`xml2` for html extraction, `parallel` to process hundreds of documents at once, `dbplyr` for Oracle access in familiar tidyverse syntax, and `testthat` for testing.

I used Python for the machine learning aspects since the classification packages are more mature and have more support: `scikit-learn` for traditional machine learning models (Pedregosa et al., 2011), `tensorflow`/`keras` to build and train NN, HuggingFace `transformers` for pre-trained transformer based models (Wolf et al., 2020), `optuna` for hyperparameter tuning (Akiba et al., 2019), and `mlflow` to track data version, model version and performance metrics. The `reticulate` package imports the Python functions into the R based workflow, at the cost of some added setup and coding complexity.

I used Jupyter notebooks for exploratory work, allowing detailed narrative alongside the code, and SQL to set up and manage the Oracle database and tables.

## 3.5 Scientific method and testing

I used the scientific method: hypothesis formulation and testing; comparisons against baseline; and statistical testing rather than simply comparing raw values, so the choices were evidence-backed rather than assumed.

While working with people with more software engineering experience to review the code base, we discussed the scope, coverage, and implementation of unit, integration, and system testing. Constraints included that tests should not contain any customer data, so we used synthetic or anonymised fixtures instead. While we were not using formal test driven development (Beck, 2003), I instructed the team to create tests alongside new issues, since it makes it easier to investigate the issue and verify fixes.

# 4. The scope of the project (including key performance indicators).

The scope covered extraction of descriptions, headings, table names, values, structural data and iXBRL data (concept, dimensional data), machine learning to classify features, and an automated pipeline extracting to Oracle database. Out of scope was any analytical work based on the data, any automated decision making based on the machine learning category or human labelling. The scope evolved iteratively over time (Section 9).

Working with stakeholders, I established success criteria.
- Macro-F1 > 0.6, primary performance metric, weighting all classes equally, so common classes do not dominate (Sokolova and Lapalme, 2009).
- Accuracy > 0.7, a secondary metric that is more intuitive to stakeholders and reflects real-world performance.
- Automated extraction coverage > 95%, data automatically extracted and classified
- Timely extraction < 1 week from date of receipt to allow sufficient time to review and act on the data.
- Interpretability and explainability, so we can know why a choice was made or provide a human understandable explanation of the factors that drove it.
- Security (dependency risk), should meet HMRC security policy.

Secondary KPIs were precision, recall, train and inference time, maintainability, reliability, cost control, data protection, AI safeguards, logging, and scaling to millions of records quickly.

# 5. Data selection, collection and pre-processing.

## 5.1 Data selection

HMRC's central systems are locked down without readily available GPU access, so exploratory work with complex models was done on a standalone GPU device over 298,461 publicly available iXBRL accounts submitted to Companies House (Companies House, 2026), which avoided using internal customer data. Subject matter experts explained that many companies select specific year-end dates like 31 December or 31 March, so a single month might not be completely representative, but this is unlikely to have any material impact on the analysis. This resulted in 2.8 million lines of data with 956 concepts (labels) (Appendix A1 and B15). For the production phase, company accounts and tax computations submitted to HMRC were used.

The source iXBRL documents are complex with inconsistent HTML structures, iXBRL data and multiple taxonomies (Appendix B1, B2, B3). In some situations table names and headings are also important features (Appendix B4). I asked subject matter experts about errors where the predicted class was what I expected but the iXBRL concept was slightly different, and they explained that some concept names differ between taxonomies. A bespoke model for each taxonomy would give the best raw scores, but it would be confusing for analysts, so I recommended training only on the main taxonomy, giving consistent categories.

## 5.2 Exploratory Data Analysis (EDA)

Rank frequency plots of both description and concept had a long tail (Appendix B5), a Pareto chart showed the 75 most common concepts cover 95% of items (Appendix B8), and the distribution was closer to lognormal than power-law (Appendix B9) (Clauset, Shalizi and Newman, 2009). This motivated using macro-F1 over accuracy as the primary metric (Section 4).

The main feature is a description with various types, nominal text, temporal dates, nominal names and numeric figures. Most descriptions are 1-9 words with a mode of 2 (Appendix B6 and B7).

The XBRL concept (label) is a categorical nominal label from a fixed taxonomy, a single CamelCase word which split into words is human readable, with similar concepts normally having similar wording.

The descriptions and concepts are many-to-many (Appendix A2.2.7 and A2.2.8), with cosine similarity analysis showing that some descriptions like "Taxation and social security costs" were used for similar concepts, but others such as "total" were used for dissimilar concepts. It also highlighted that the taxonomy is specified beyond what could be predicted from the human readable data in the accounts, which creates a real upper limit on any model.

Classifier-independent analysis showed that MPNet (Song et al., 2020) had the best silhouette score (0.467) (Rousseeuw, 1987), suggesting it captures meaning better than plain TFIDF (0.41), but this might not carry over to categorisation performance (Appendix A2.5 and B16).

## 5.3 Preprocessing

The text features like description were normalised, lowercasing and replacing special characters with spaces. Not all preprocessing was effective, for example replacing forward slashes with spaces actually reduced performance, so it was dropped (`clean_field`, Appendix A2.3).

I canonicalised the description, so most dates were replaced by a placeholder `hubble_date`, except for 31 March 1982, which subject matter experts explained has a special meaning for tax, so it became `hubble_date_1982_03_31` (`canonicalize_field`, Appendix A2.3).

Similarly company names, individual names, postcodes and numbers were identified using regular expressions and labels, and replaced by placeholders. This helps avoid overfitting and improves generalisation; reduces noise; preserves privacy; and enhances data security through data minimisation. It is also more ethical since it treats less common ethnic names the same as more commonly used names.

Subject matter experts advised that a placeholder by itself would not be enough information to categorise, so I did label engineering and changed those labels to placeholders like `HubbleName`; while we cannot predict the actual concept, knowing it is a name can be useful in analysis (`target_engineer`, `standardise_names`, Appendix A2.3 and B12).

I implemented data quality controls aligned with HMRC expectations and DAMA UK's quality dimensions (DAMA UK, 2013; Government Data Quality Hub, 2020).
- Completeness improved since untagged data was now extracted.
- Consistency since untagged and iXBRL tagged data are structured the same way on the same tables, with consistent machine learning categories.
- Timeliness, since the long-format data structure handles any taxonomy without hitting database column limits, allowing extraction within days of receipt.
- Validity and accuracy were addressed by removing descriptions of 2 characters or fewer, missing, low-quality, or longer than 15 words, which analysis showed were not valid (`filter_data` and `filter_out_labels`, Appendix A2.3 and A7.1).

This reduced the unique descriptions from 266,178 to 7,795 and labels from 956 to 826 (Appendix B15). A limit of 350 examples was added to ensure there were enough samples even with the 1% train population, which reduced labels to 141 while keeping 85% of the rows of data. The effect on the distributions can be seen by comparing the plots before and after preprocessing (Appendix B5-B9 against B10-B14). Along with measures such as restricting data access to specific users, this ensured compliance with HMRC and regulatory requirements, DPIAs and *Data Protection Act 2018*/UK GDPR (Data Protection Act 2018; Regulation (EU) 2016/679; Information Commissioner's Office, no date b).

Because the data was used over various model architectures and packages, I created stratified 80/10/10 train, test and holdout splits upfront, plus sub splits and square-root weighted splits (`stratified_split`, `sample_split` and `add_sqrt_weight`, Appendix A2.6). The holdout ensures the final comparison is over unseen data, giving a better view of performance against real data.

# 6. Survey of potential alternatives.

This is multi-class text classification with 141 nominal classes and strong class imbalance. I initially used data exploration and theory to limit the solutions to those that would work well with classifying the short domain-specific terminology, reviewed the feasibility within the business context, then evaluated the leading candidates (Sebastiani, 2002).

I considered systemising a rule-based system using regular expressions, which could have some success but would use too much subject matter expert time and would not cover the long tail, so it was not a feasible business solution.

While the data was tagged, often the specificity was beyond what was required, so unsupervised methods were considered as a way to group similar concepts together. But the cosine similarity analysis highlighted that the variety in descriptions for some concepts was too great, so I focused on supervised learning models.

Traditional machine learning models can perform well with classifying short text, since there is a high signal to noise ratio (Joachims, 1998). Scikit-learn provides various high quality models for text classification, such as `SVC`, `LinearSVC`, `SGDClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `MultinomialNB`, `ComplementNB` and `PassiveAggressiveClassifier` (full search space at Appendix A3.4.1).

There were two main methods used to embed the descriptions, sparse vectorisation (TF, TFIDF over word and character n-grams) and dense vector embeddings (MPNet, E5) (Sparck Jones, 1972; Cavnar and Trenkle, 1994; Song et al., 2020; Wang et al., 2022). TFIDF captures domain-specific terminology and phrasing well, works with a variety of models and is fast. Dense vector embeddings (Reimers and Gurevych, 2019) capture more of the semantic meaning, so should recognise phrases with similar meaning even if the words are different, especially on unseen descriptions (Appendix A2.5 and A3.5.2).

A neural network has the advantage of learning patterns beyond a fixed algorithm used in traditional machine learning. Various NN can be used for text classification such as DNN, LSTM, GRU, CNN and BiLSTM, all of which were included in the architecture search (`create_model`, Appendix A4.2.2) (Kim, 2014).

Transformer based models are a more advanced architecture with better semantic understanding and often outperform other neural network architectures (Vaswani et al., 2017), and pre-trained models have semantic understanding from large amounts of text built in (Devlin et al., 2019). Various transformer based models were tested: RoBERTa (Liu et al., 2019), SEC-BERT (Loukas et al., 2022), MPNet (Song et al., 2020), and MiniLM (Wang et al., 2020), covering different sizes, architectures, and training data (Appendix A5.1 and A5.2). SEC-BERT was trained on SEC filings (US financial filings), so should have better semantic understanding of accountancy terms.

A frontier LLM, such as ChatGPT, would be expected to have the best semantic understanding of text, but it would be excessive for short phrases like these. At the time it was not possible to send taxpayer data to an external API under the HMRC data security and governance requirements, making this approach unfeasible.

# 7. Implementation - performance metrics.

## 7.1 Population size validation

Comparing every model and hyperparameter over the full train dataset was not possible, so I first tested whether smaller populations gave representative results, over 1%, 10% and 100% train populations (Appendix A3.3, B17 and B18). The Pearson correlation to the full population for the 1% and 10% samples was 0.971 and 0.998 respectively (Appendix B19 and B20). Paired T-tests showed that models that were not significantly worse over the 1% were also not significantly worse at 100%, so I could filter out models and hyperparameters using a smaller sample, and have reliable results from the 10%.

## 7.2 Traditional machine learning algorithms

To narrow the initial models and hyperparameters I used HalvingRandomSearchCV over 10,000 candidates against a DummyClassifier floor to ensure real performance (Appendix A3.4.1, A3.4.2, B21 and B37) (Bergstra and Bengio, 2012; Li et al., 2018). Stratified cross validation reduced variance and paired T-tests indicated which models were not significantly worse at the 5% level, narrowing the field at each stage. Where models could not be separated by macro-F1, train times were the secondary measure.

I plotted hyperparameters against scores to narrow the ranges for subsequent iterations (Appendix A3.4.2.1 and A3.5.1.1.1); a 2D graph using colours showed min_df 1 had clusters with better speed and macro-F1 than min_df 2, which was surprising on the speed aspect (Appendix B22).

After fine tuning and training on the full train dataset, LinearSVC beat the alternatives at a 5% significance level (Appendix A3.4.3 and A3.4.4).

I tried both sparse and dense embeddings, and at the 5% significance level MPNet beat a simple TFIDF embedding on macro-F1, but only by 0.3pp while taking 67 times as long (Appendix A3.5.2). So I used the simpler TFIDF word-only embedding, which is faster, easier to maintain and easier to interpret.

LinearSVC did not fully converge but there was no significant difference in score for max_iter from 5,000 to 20,000, so I selected max_iter of 10,000, since 20,000 was slower for no real gain (Appendix A3.6).

The final pipeline used TFIDF (1-3 word n-grams, min_df 1, norm l2) with LinearSVC (penalty l1, C 2.8, loss squared_hinge, dual False, class_weight balanced, max_iter 10000) (Appendix A3.7). A range of C values performed similarly, so a lower C was selected to prevent overfitting and enhance generalisability.

## 7.3 Conventional and Transformer based Neural Networks

I used Optuna to compare and find the optimal architecture and hyperparameters such as activation, learning rates, dropout rates, embedding dimensions and number of layers (Appendix A4.3 and B37). CNN was the best performing conventional neural network and was tuned further in a dedicated study, with dropout as regularisation to limit overfitting and improve generalisability (Srivastava et al., 2014) (Appendix A4.4, B26 and B27). SEC-BERT was the best performing transformer based model, with a macro-F1 of 0.754 against 0.743 for RoBERTa, 0.714 for MPNet and 0.681 for MiniLM, demonstrating that domain-based pre-training was beneficial (Appendix A5.2, B29 and B30).

## 7.4 Class imbalance

To deal with class imbalance (He and Garcia, 2009) and reduce systematic bias towards majority classes, I explored various methods:
- Weighting models worked well with LinearSVC but reduced performance on the NN models (Appendix A4.4.1.1 and A5.3.7).
- Square-root weighted training data provided good macro-F1 increases for very small accuracy decreases, e.g. 1.3pp gained vs 0.0573pp lost (Appendix A3.7.7).
- Random oversampling actually reduced performance on the transformer based models (Appendix A5.3.9).

A smaller modified training dataset improved neural net performance whereas LinearSVC performed best on the full train dataset with a weighted model.

## 7.5 Model selection

To compare the architectures a decision matrix was used (Appendix A6 and B37), covering objective and subjective measures (Saaty, 2008).

- Accuracy
- Macro-F1
- Macro-recall
- Macro-precision
- Weighted-F1
- Train time
- Inference time
- Model size
- Interpretability & explainability
- Deployment simplicity
- Maintenance burden
- Domain fit
- Model life cycle
- Dependency risk
- Cost

Each measure was weighted, with a confidence factor of 0.35 applied where overlapping confidence intervals meant a model could not be separated from the best (Appendix B33). A rubric set the standard for the subjective scores with an accompanying narrative (Appendix A6.2.5 and B31).

For fair comparison, and because of memory/time constraints, all models were trained on 10% square-root weighted data and evaluated on the same holdout subset, with bootstrap 95% confidence intervals rather than cross validation due to computational cost (Kohavi, 1995) (Appendix B32).

While SEC-BERT had the best macro-F1 score I chose LinearSVC, trading marginal performance (2.3pp) for a solution that is simpler to maintain, is more explainable (feature coefficients), runs 220x faster, deploys on existing CPU-based infrastructure, scales cost effectively, and relies on well-established, regularly updated packages (Appendix B32, B33 and B34).

## 7.6 Production system and governance

Scaling needed additional infrastructure, so I worked with DevOps to set up on-demand-compute, which starts up an EC2 instance running POSIT just for a job and shuts it down when finished, much more cost effective than a large machine running all the time; EC2 instances without a GPU were also cheaper and more available.

The overall system (Appendix B35 and B36) retrieves raw iXBRL documents from AWS S3, extracts them using `rvest`/`xml2`, structures them into long format in R, pre-processes the features and classifies them with scikit-learn's `Pipeline` (`TfidfVectorizer` and `LinearSVC`) through `reticulate`, and saves the output to an Oracle database using `dbplyr`.

I would often work collaboratively on others' non-machine learning tasks, partially to share knowledge and up-skill them.

The pipeline now runs automatically daily, so analysts just need to query the database.

Governance is built into the design. Documentation and guidance explain whether an item was tagged by the customer or is a machine learning prediction. Analysts know that the machine learning category can be wrong, that it should never be used in automated decisions (Information Commissioner's Office, no date a), and that there should always be a human in the loop. Per-class performance is available in a dashboard so analysts can check before anything is relied upon.

# 8. Results.

LinearSVC trained on the full dataset and tested over the full holdout has an accuracy of 0.975 (CI 0.975-0.976) and macro-F1 of 0.785 (CI 0.780-0.788), beating KPIs of 0.7 and 0.6 respectively and a stratified DummyClassifier baseline of 0.007 (Appendix A3.7.3 and B38). The production system also meets the remaining KPIs: extracting over 99% of records automatically against a target of 95%; within 3 days against a target of one week; and an interpretable, explainable model.

Residual analysis identified which classes performed poorly and summaries were created for analysts (Appendix A3.10). Per-class results were varied, with a median per-class F1 of 0.966, but 27 of the 141 modelled concepts scored below 0.5 and eight scored zero, pulling down the macro-F1 score. By volume the exposure is smaller, with 94% of holdout records falling in concepts scoring above 0.9 (Appendix B40). When I worked with analysts I focused on outcomes, showing confusion matrices for good and poor quality classes and looking at examples (Appendix B24), and the dashboard let them check a concept's reliability before using it.

Subject matter experts explained that in some cases there is simply not enough information in the document to predict the specific concept. For example, the description "amounts owed to group undertakings" is associated with multiple but similar concepts. This highlights that a simplified list of categories could be beneficial, especially for evaluation.

Sensitivity analysis and model robustness were tested over various categories (Ribeiro et al., 2020), abbreviations, adversarial (phrased to be misleading), scenario planning, command (attempts to inject LLM instructions), contextual (semantically the same), long context, OCR issues, synonyms, typos, unicode and variations (Appendix A3.8, A5.3.5, A7.3 and B25). Overall LinearSVC outperformed SEC-BERT in robustness testing, scoring equal or better in nine of the eleven categories, which was surprising since the domain-specific training and theoretically better semantic understanding should have favoured SEC-BERT. Also the areas where LinearSVC did worse, like typos and variations, would be rare over real data since accountancy documents are primarily generated by computers.

Bias was investigated both against size of companies and software provider (Mehrabi et al., 2021). Large companies had a macro-F1 score of 0.934 vs 0.790 for small companies, which could be explained by smaller companies using cheaper software, with some software providers having a score of 0.184 vs 0.913. Residual analysis showed that while there were some real misclassifications, often they were between very similar classes without enough information to differentiate them, suggesting the specificity of the evaluation is too fine-grained. Different software providers do tag things differently, but it is a training proxy, and such issues would not apply to untagged items, or if we had human labelled classes this issue would not show up. But it is still a real issue, worth working with providers to make tagging more consistent, especially since tagged concepts would be considered more reliable than a machine learning category.

# 9. Discussion and conclusions/recommendations.

An Agile approach worked well with CRISP-DM. Iterating delivered usable products at each stage: basic raw data on file, iXBRL information, machine learning categories, improved architectures and database, with each step evaluated for feasibility, benefits and risk, proving the approach and providing business value. Regular meetings and a workshop helped validate business understanding and get feedback, such as the issues with raw descriptions. The iterative approach improved macro-F1 from under 0.50 to 0.785, and adding table name and heading as features improved macro-F1 by a further 9.8pp on the production dataset.

While using metrics like macro-F1 works well for comparing similar classes of models, it is important to consider all the business requirements using methods like decision matrices. But some factors like interpretability and security are core requirements that could override a raw score.

The coefficients of LinearSVC provide real interpretability that could be explained to technical audiences, which was not possible with neural networks (Appendix A3.9.1) (Rudin, 2019). But tools like LIME (Ribeiro, Singh and Guestrin, 2016) and SHAP (Lundberg and Lee, 2017) provide explainability, which partially mitigates such risks for models that are not interpretable (Appendix A3.9.2, A3.9.3, B23 and B39).

Since SEC-BERT is not from a well-established provider, security aspects may have prevented use even if it had won the decision matrix; if it had been materially superior we would need to consider training our own BERT based model (Sculley et al., 2015; National Cyber Security Centre, 2023).

TF-IDF suits the short domain-specific descriptions, and LinearSVC with L1 regularisation works efficiently with the sparse matrices it creates, so I could develop the model on existing infrastructure without impacting other users.

I worked autonomously where deep focus was required, such as core modelling and building and evaluating models, then demonstrated the approach and took feedback in review meetings. I worked collaboratively with subject matter experts on evaluation, where their taxonomy knowledge was needed, and with DevOps, who had expertise and control over infrastructure I did not.

My communication approach evolved based on how stakeholders reacted to early explanations, with methods tailored per audience, such as presentations, markdown guides, meetings and workshops. Initial technical descriptions were too detailed for some audiences, so I shifted towards Problem-Solution-Outcome for non-technical audiences and more visual and example-based explanations for others. I communicated residual analysis through confusion matrices with examples of errors, simple visual decision trees showing what attribute was split on, and a graphed SVM 2D decision boundary, and a simple example to illustrate weighted against macro scores rather than formulas.

Repeated questions about the machine learning led me to create an interactive dashboard where users can test the model and see how it performs per concept, including the kind of mistake to expect. It initially showed the top-5 predictions, but the poor matches confused users, so I changed it to show only plausible matches. As users' understanding improved, their use increased.

With managers I focused on the business level, so benefits and outcomes, funding, blockers, timeframes, and the benefits of more people on the project, which resulted in additional people to help with development. Memos with a cost-benefit analysis, highlighting improved timeliness and the newly extracted untagged data, resulted in additional funding for infrastructure.

The project readme uses markdown headings, instructions and code blocks, and has let many analysts set up and run the tool themselves. Further development centralised extraction of the full population into Oracle, so most users now just need a database query. When users have issues or questions, I update the relevant documents to cover them.

I discovered Optuna while working on the neural networks, and its automated tuning and built-in visualisations could have replaced much of the manual scikit-learn search, as MLflow did for storing results. So going forwards I would research existing packages before coding my own solution.

Recommendations:
- Increase coverage to 100% and enhance robustness, with a better scheduling system, a fully supported Oracle server and tests moved to a CI pipeline, to be able to replace existing systems.
- Data contracts for data sources and downstream systems that use this data.
- Monitor drift (Gama et al., 2014).
	- Monitor input drift, checking for new taxonomies.
	- Drift on outputs detected for both accuracy and macro-F1, using a 2pp drop with non-overlapping confidence intervals over two consecutive days.
	- Automated drift can only check tagged items, there should also be occasional manual check of untagged items.
- Standard structure for machine learning communications: headline figures first, plain explanations of technical terms with illustrations and examples, and technical detail in an appendix (Mitchell et al., 2019).
- Human evaluation of tagging.
- Establish the performance ceiling first, since the same description can be associated with different concepts; the most common concept per description gives a hard upper bound, letting improvement effort be budgeted appropriately.
- Consider a simplified taxonomy of concepts, since grouping similar concepts would be more user friendly for analysts.
- Record the MLflow model version on the outputs, so predictions can be traced back to the exact model and training dataset.

# 10. Summary of findings.

I developed a supervised, multi-class classifier to categorise untagged items in financial iXBRL documents. A variety of models were evaluated using macro-F1, with the final candidate models, LinearSVC, CNN and SEC-BERT, being compared using a decision matrix. While SEC-BERT led on macro-F1 it was rejected because it was not as good on interpretability, deployment simplicity and dependency risk.

The chosen pipeline was TF-IDF 1-3 word n-gram with LinearSVC.

The biggest factors were actually pre-processing, which increased macro-F1 by 20pp, and adding additional features by 9.8pp. Going forwards I expect the main improvements would come from pre-processing or from simplifying the taxonomy used rather than changing the architectures or tweaking the hyperparameters.

# 11. Implications.

Hubble helped us meet our quality standards. The machine learning categories reduced the manual regex-style work previously done, improved consistency and reliability of the analysis.

Hubble is widely used by multiple teams, with data integrated into various dashboards across multiple tax heads.

With untagged data now being extracted and classified, we have been able to perform data analysis previously not possible, which has been fed into improving departmental/government policy.

The data has been used to better identify companies to investigate, and the estimated benefits stored on a spreadsheet are in the tens of millions, but recording is incomplete so I arranged for benefit monitoring to be built into the central management system.

# 12. Caveats and limitations.

The model and evaluation were all based on tagged data, but the main use case is untagged data, which could be systematically different. For example, an item might have been left untagged since no relevant taxonomy concept exists. Fully human tagging the untagged data would require tax-trained experts who do not have that capacity, but they will feed into a manual evaluation stage, which is the practical route to quantifying any gap.

Traditional machine learning model comparisons used 5-fold cross validation, a reasonable choice for the initial filtering due to computational cost, but overlapping training sets can understate variance; later stages should have used something like 5x2 CV, which uses disjoint training sets and limits Type I error (Dietterich, 1998).

LinearSVC does not scale as well to larger datasets, so training on much larger datasets is not practical. But going from the 10% train data set to 100% saw only a 0.3pp increase in macro-F1, so larger datasets are unlikely to increase performance much (Appendix A3.7.7).

Increasing data set size while keeping the 350 example threshold results in more labels, so model performance actually decreased with more data. Also different document types/sources had very different label distributions, making performance comparison difficult across populations and document types.

The integration of R and Python, while working well, does add setup complexity and other teams have had issues with the reticulate package. With the long term move to a lakehouse and higher Python use in HMRC, initial investigations suggest that Python has more support for the ETL, so porting is worth considering.

---

# Per-class table and worked example — 16 August 2026

*(Appendix changes made directly in Report mod; body changes below are displayed only, NOT applied.)*

**Done in the appendix:**
- **B40 now carries the full 141-row per-class table** (precision, recall, F1, support, sorted by F1 ascending so the failures lead). Regenerated from the fitted model at `~/Code/AI_L7/EPA` (run `79a24e86`, holdout of 243,991 rows, reproduces accuracy 0.9751 / macro-F1 0.784); every row agrees with the band tables B40 already carried. The old opener claiming a full table "would not be readable" is gone.
- **B24 now carries a quantified worked example** for CashBankOnHand against CashOnHand: a small TP/FN/FP table plus the description counts. The key numbers: "cash at bank and in hand" appears under both concepts in the source data, 5,670 times one way and 21 the other, and all 21 minority taggings are necessarily scored as errors; 13 of CashBankOnHand's 16 misses are "cash and cash equivalents" going the other way. It is the label-collision argument §8 makes, now with exact counts.

**Body changes for you to consider (displayed only, NOT applied).** All word counts are computed on the proposal body (currently 5,489 of 5,500), not estimated.

**Change 1 — swap the unquantified §8 example for the quantified one. Must be taken together with its cut; on its own it puts the body 13 over.**

REMOVE:

> For example, the description "amounts owed to group undertakings" is associated with multiple but similar concepts.

REMOVE also (the closing sentence of the same paragraph):

> This highlights that a simplified list of categories could be beneficial, especially for evaluation.

REPLACE the first with:

> For example, "cash at bank and in hand" is tagged CashBankOnHand 5,670 times and CashOnHand 21 times in the source data, so the model routes every instance to the dominant concept and the minority taggings score as errors (Appendix B24).

The full paragraph after change 1:

> Subject matter experts explained that in some cases there is simply not enough information in the document to predict the specific concept. For example, "cash at bank and in hand" is tagged CashBankOnHand 5,670 times and CashOnHand 21 times in the source data, so the model routes every instance to the dominant concept and the minority taggings score as errors (Appendix B24).

Why: the same claim with counts an assessor can check, anchoring the new B24 worked example. The cut sentence is safe to lose because the simplified-taxonomy point is already made in the §8 bias paragraph, in §10 and in the recommendations. Body after change 1: **5,499**.

**Change 2 — remove "scenario planning" from the §8 robustness list. Take this regardless: it is a factual fix, not a trim.** "Scenario planning" is not a category in the robustness suite (zero occurrences in `test.py`, Appendix A7.3, and absent from the B25 table), so the list as written claims a test that does not exist. The rewording of the command gloss recovers two more words.

REMOVE:

> , scenario planning, command (attempts to inject LLM instructions),

REPLACE with:

> , command (LLM instruction injection),

The full sentence after change 2:

> Sensitivity analysis and model robustness were tested over various categories (Ribeiro et al., 2020), abbreviations, adversarial (phrased to be misleading), command (LLM instruction injection), contextual (semantically the same), long context, OCR issues, synonyms, typos, unicode and variations (Appendix A3.8, A5.3.5, A7.3 and B25).

Body after change 2 alone: **5,485**.

**Change 3 (optional) — name the full per-class table where §8 cites B40.** Worth it because the EPAO's written request was to show class-level results clearly; only affordable if change 2 is also taken.

REMOVE:

> (Appendix B40)

REPLACE with:

> (full per-class results at Appendix B40)

The full sentence after change 3:

> By volume the exposure is smaller, with 94% of holdout records falling in concepts scoring above 0.9 (full per-class results at Appendix B40).

**Outcomes, computed:**

| Taken | Body word count |
|---|---|
| Nothing (current proposal) | 5,489 |
| Change 2 only | 5,485 |
| Changes 1 + 2 | 5,495 |
| Changes 1 + 2 + 3 | **5,499** |
| Change 1 without change 2 | 5,499 |
| Changes 1 + 3 without change 2 | 5,503 — over, do not take |

Recommendation: take all three, landing on 5,499 with every claim quantified and the phantom test category gone.

**Note on figures:** my re-scoring gives macro-F1 0.784 against the published 0.785 (accuracy 0.9751 vs 0.9754) — inside the published confidence intervals, and the per-class rows match B40's existing tables exactly, so nothing in the body needs changing. The tiny headline difference is presumably a split-version or library-version artefact.
