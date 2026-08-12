**Source documents used to build this draft** ** *(working note — not part of the submitted repo*t)* 

|Document | What was taken from it | Why |
|---|---|---|
| [[Z Project Report - Report]] | Primary content source for this revision: business-problem detail (taxonomy update lag, Oracle column limits, deliberate non-tagging), agile/GitLab rationale, testing and documentation practices, Companies House exploratory dataset, failed cleaning experiments, rejected alternatives (regex repository, frontier LLM API), embedding trade-off timings, decision matrix design, robustness/sensitivity testing, bias analysis by company size and software provider, drift-monitoring thresholds, benefits realisation, and limitations. | Newest and richest set of raw notes (7 Aug 2026). Material was scattered across sections and duplicated, so it has been de-duplicated and moved to the section of the EPA structure where each point earns marks. |
| [[Z Project Report - L7_AI_Data_Specialist_AM1-Project_and_Presentation_Guidance_V2.1]] | The mandatory 13-part report structure, the 5,000-word ±10% limit, the rule that appendices are excluded from the count and must not carry new information, and the full pass/distinction grading table. | This is the BCS specification the independent assessor grades against. Section headings and ordering are taken verbatim so nothing can be marked as missing. |
| [[Z Project Report - Jesse Karadia - Project Approved]] | The signed-off project title and brief, the KSB mapping, and — critically — the two EPAO feedback comments: *"final report should show the class-level results clearly, especially where minority classes perform less well"* and *"final report should make clear how the ML category is governed in practice… supports analyst review rather than automated decisions."* | The report must not drift from the approved brief, and the EPAO's two written requests must be visibly answered. Both are now addressed in §8 and §9. |
| [[Z Project Report - Review and to do]] | Notebook-by-notebook facts and figures (dataset sizes, Pearson correlations, silhouette scores, hyperparameters, macro-F1 results) plus the identified gaps against EPA criteria. | Supplies the verified numbers, and its gap list (bias analysis, data governance narrative, CRISP-DM framing, deployment/scalability, statistical significance) drove what to add. |
| [[Z Project Report - Work_Based_Project_Guidance (1)]] | Per-section content expectations and the four "distinction behaviours": explicit commercial trade-offs, critical evaluation of alternatives, audience-appropriate communication, and evidenced organisational impact. | Used as the shaping test for each section — every major decision now states the criteria, the alternative rejected, and the business consequence. |
| [[Z Project Report - notes]] | Consolidated KSB-to-evidence mapping across the six grading themes, and the phrasing on bias ("representation bias, not demographic fairness"). | Used to check every AM1 KSB has a home in the report body, and to keep terminology consistent with the presentation prep. |
| [[Z Project Report - AM1 Previously Asked Questions in Presentation]] | The assessor question bank (model choice, failure response, bias, ROI, trade-offs, lessons learned). | Content likely to be questioned is stated explicitly in the report rather than left to the Q&A. |
| [[Z Project Report - Assignment - planning and writing]] | TEEL paragraph structure and per-section word budgeting. | Applied to keep paragraphs claim-led and evidence-backed within the word limit. |
| [[Z Project Report - qa-apprenticeships-harvard-referencing-full-guide]] | Cite Them Right Harvard format. | Raw URLs in the source notes have been converted to author–date citations with a reference list. |

**Word count:** body ≈ 5,495 of 5,500 permitted (5,000 +10%). References, appendices and this header are excluded. There is effectively no headroom — anything added needs something cut. Sections 5 (≈845) and 3 (≈660) are the largest and the first place to look if you need room.

**Eight items need confirming before submission — see "Working notes" at the end of this file.**

# Categorising Data in Financial Documents
*D*Draft — for review and refinement*



## 1.1. Introduction and Background
HMRC receives millions of company tax returns annually, a significant proportion submitted as iXBRL (inline eXtensible Business Reporting Language): semi-structured (x)HTML documents in which financial items are optionally tagged with concepts from a fixed taxonomy. The concept attached to a tagged item — `CalledUpShareCapital`, say — is a nominal categorical label from a controlled vocabulary, and it is what makes automated extraction and population-scale analysis possible.

Where tagging is comprehensive, existing HMRC workflows reliably extract, structure and analyse the figures. In practice tagging quality varies sharply by document type: well-tagged types average around 70% of figures tagged, while some critical types — including certain tax computation formats — average only 30%. The causes range from limitations in the accounting software used to prepare the document through to preparers deliberately leaving untagged the items they would prefer HMRC not to review. Either way the majority of the data in some of the most analytically valuable documents has been unavailable for automated analysis, and deliberately untagged items in particular have passed unrisked.

Two constraints compounded this. Legacy extraction requires a complex schema update whenever new taxonomies are published, taking up to nine months; HMRC has only twelve months from receipt to open an enquiry, so much of that window could be consumed before the data was usable. The legacy wide-format storage was also approaching the Oracle column limit, capping further coverage.

This report describes Hubble, an internal tool I designed and built to close that gap. It extracts both tagged and untagged items and uses supervised machine learning to classify untagged items into the appropriate taxonomy concept. The central technical challenge is that untagged items carry only a free-text description with no fixed vocabulary or required format, so items of one conceptual class have many textual representations, expressed in domain-specific terminology — "deferred consideration", "amounts owed to group undertakings" — that analysts are not uniformly familiar with.

I led the technical side of the project from business understanding through to production deployment, structuring the work with CRISP-DM (Chapman *et al.*, 2000) and managing delivery in iterative increments using a Kanban approach in GitLab. The tool has since been adopted by multiple analyst teams for population profiling, policy analysis and tax risk identification.

---

## 2. Outline of the Issue and Business Problem

The business problem is that a significant portion of the financial data submitted to HMRC in iXBRL format cannot be reliably used, because it lacks machine-readable categorisation. Analysts either restrict analysis to the tagged subset — incomplete, and systematically unrepresentative because the untagged remainder is not missing at random — or manually review free-text descriptions, which is slow, inconsistent between analysts and dependent on specialist domain knowledge.

The consequences are analytical and operational. Population-level profiling informs government policy and the allocation of compliance resource; an analysis restricted to 30% of figures under-represents entire categories of financial data, particularly in sections preparers have not prioritised for tagging, and risk indicators in untagged items go undetected — a direct cost in compliance yield. Combined with the taxonomy update lag, the department was both missing data and receiving what it did have too late to act on inside the statutory enquiry window.

The opportunity is that tagged figures *within the same documents* provide an authoritative supervision signal at no annotation cost: the concept was assigned by the preparer at submission, so the labels reflect expert human judgement applied at the point of document creation. Learning the relationship between descriptions and concepts from tagged examples allows untagged items to be predicted, extending coverage from 30% towards the full extracted population.

Before recommending machine learning I tested whether it was justified commercially. The first version of Hubble extracted untagged figures and their descriptions, and analysis relied on hand-written regular expressions developed with subject matter experts (SMEs) — incomplete, error-prone and slow. I then extracted the full description set for key classes and worked through the variation with SMEs: some classes had over 23,000 unique descriptions, including domain-specific terms not all analysts would recognise. Manual or rule-based classification at that scale was not viable, and a rule base would need permanent SME maintenance while still failing on the long tail. This formed the evidence base for recommending a supervised classifier.

---

## 3. Methods Used and Justification

**CRISP-DM.** CRISP-DM was chosen because it explicitly accommodates the cyclical nature of applied ML: modelling discoveries prompt revisions to data preparation, and evaluation findings can send you back to business understanding. Each phase produced documented artefacts — data quality reports, EDA notebooks, experiment logs, evaluation summaries — giving an evidence base for every decision. That structured iteration, grounded in error analysis each cycle, is the mechanism by which the solution improved from macro-F1 below 0.50 to 0.787 (§8).

**Project management.** I selected an agile approach (Beck *et al.*, 2001) over a fixed waterfall plan, but tailored practices to the team rather than adopting a framework wholesale — normal practice according to Atlassian (n.d.). The emphasis was Kanban rather than Scrum: the team was small, so Scrum ceremony would have been overhead, and members had competing demands that made fixed-length sprints impractical, whereas a continuously updated board accommodated variable availability. This mattered because the project's direction could not have been foreseen at the outset. Delivery proceeded in usable increments — descriptions and values, then iXBRL data, which made an ML category possible, then headings and table names, which improved it, then database storage, which made outputs widely available — with feasibility, risk and benefit reassessed before each expansion. A waterfall plan written against the original requirement would have delivered something considerably less useful.

GitLab is not commonly used for project management in HMRC, so there was a learning curve, but the transparency, auditability and documentation benefits outweighed it; without it, handover would depend on individual memory. Epics supported the longer-term planning management cared about, while the issues board served as the Kanban board and the focus of stand-ups, using a template I created requiring reproduction steps, expected versus actual behaviour and a proposed fix. Branching with independent review of merge requests controlled change quality, which needed training the team on branching and on merging the target branch before raising a request. Team members documented in the repository's docs folder and were asked to comment code with *why* rather than *what*.

**Testing.** I wrote the initial unit, integration and system tests using `testthat`, including tests over the ML outputs, then assigned ownership of testing to a colleague — partly to free capacity, principally to get an independent view of the system. Because unit tests must not contain customer data, synthetic and anonymised fixtures were used, and I introduced a policy that any issue raised should be accompanied by a test demonstrating it. User acceptance testing produced two changes I would not have anticipated: analysts preferred numeric surrogate keys to natural keys for join performance, and asked for output structured closer to the tables they already used.

**Languages and tools.** R was used for extraction and pre-processing: it is the analytical default at HMRC, has strong HTML parsing and parallel processing packages handling hundreds of documents concurrently, and — importantly for continuity — is maintainable by far more people here than the alternatives. Python was used for ML, where the ecosystem (scikit-learn, TensorFlow/Keras, HuggingFace Transformers, Optuna, MLflow) is far more mature for text classification and hyperparameter optimisation; the two were integrated with `reticulate`, and `dbplyr` gave analysts a tidyverse-style interface to Oracle. Jupyter notebooks gave the exploratory work a reproducible narrative record, and MLflow tracked data version, model version, parameters, metrics and artefacts for every run.

**Scientific method.** Experiments were designed with explicit hypotheses and a controlled baseline. A `DummyClassifier` at every phase established the performance floor and confirmed genuine predictive signal. Macro-F1 was the primary metric, weighting all classes equally and so testing the business requirement that the model works across the taxonomy rather than only on common concepts. Stratified five-fold cross-validation ensured all classes appeared in every fold and reduced variance; paired t-tests on the fold scores identified which configurations were not statistically distinguishable from the best run at the 95% level, allowing a simpler or faster model to be preferred where the difference was not real.

---

## 4. Scope of the Project and Key Performance Indicators

The scope covered the complete pipeline for one key document type — business understanding; assessment of existing extraction and storage constraints; extraction of description, heading, table name, structural position (table, row and column number), iXBRL concept and dimensional data, references, footnotes and value; processing and formatting; model development; ingestion to Oracle for bulk profiling; and an automated architecture running extraction, categorisation and storage end to end — with the design deliberately extensible to further document types.

Success criteria were agreed with analysts and managers at the outset.

- **Macro-F1 ≥ 0.70** — primary ML indicator, weighting all classes equally including minority concepts. Chosen over accuracy to address class imbalance directly.
- **Inference latency < 10μs per record** — enabling daily batch processing of millions of records on existing CPU infrastructure without GPU compute.
- **Coverage ≥ 95%** of extracted figures assigned a taxonomy concept.
- **Accuracy ≥ 95%** on majority classes, a secondary metric for practical usability.
- **Short-term milestone:** sub-population outputs to file, demonstrating value and gathering analyst feedback early.
- **Long-term milestone:** full daily population ingestion to Oracle within the agreed timeline.

Secondary KPIs used in selection were precision, recall, training time and interpretability; operationally, accuracy, macro-F1, pipeline logs and the automated test suite evidence completeness. These were set against HMRC's stated priorities of maintainability, reliability, cost control, data protection, AI safeguards, security and scaling to millions of records, so feasibility was a selection criterion from the start rather than a deployment-stage surprise.

---

## 5. Data Selection, Collection and Pre-Processing

**Data selection.** HMRC's analytical environments are tightly controlled and, at the time, offered no ready access to GPU compute, making broad exploratory comparison of architectures impractical internally. I therefore ran the exploratory phase against publicly filed Companies House accounts, which are also iXBRL, on a standalone GPU machine, using those with HTML tables from the 298,461 accounts filed in November 2025. A whole month's filings is broadly representative, though many companies choose 31 December or 31 March year-ends; this has no material bearing on the methodological conclusions, and public data meant the methodology could be shared without disclosing protected data. The implementation phase then used accounts and tax computations submitted to HMRC. The exploratory dataset yielded 2.8m rows across 956 concepts.

**Labels.** Tagged figures provide authoritative supervision without additional annotation or inter-annotator variability. Different document types use different taxonomies — FRC for company accounts, HMRC CT600 for tax computations — which name semantically similar items differently, so one model across all of them would inject label noise. Following SME consultation, I trained a separate model per document type on that type's main taxonomy only, then applied those labels across all documents of the type: a little precision on secondary taxonomies traded for consistent class names, which is what makes the output usable to analysts.

**Exploratory data analysis.** Three findings had direct modelling consequences. The label distribution was long-tailed, with power-law analysis showing a lognormal fit better supported than a power law; the top 75 concepts accounted for 95% of items, with a tail beyond 900. This motivated macro-F1, since a model predicting only common classes would score well on accuracy and be useless analytically. Second, descriptions and concepts are many-to-many: cosine similarity analysis showed some co-occurring concepts are near-synonymous — "Taxation and social security costs" appears against several closely related ones — while bare dates or generic terms like "total" attach to many unrelated concepts, setting a real ceiling on any model using description alone. It also showed the taxonomy is specified more finely than the visible content of the accounts can support, and that concepts vary widely in how tightly their descriptions cluster, ruling out unsupervised grouping as a route to a simplified category set. Third, descriptions span several measurement types — nominal financial terms, names, temporal values in inconsistent formats, numeric values — requiring differentiated treatment rather than uniform cleaning.

**Pre-processing and canonicalisation.** Pre-processing reduced noise, standardised the feature representation and ensured compliance with the Data Protection Act 2018 and UK GDPR, under a Data Protection Impact Assessment completed beforehand.

1. **Text cleaning:** lowercasing and replacement of special characters with spaces. Not every step helped — replacing forward slashes reduced macro-F1 and was dropped, which is why each was tested rather than assumed.
2. **Dates and numbers:** 31 March 1982, which has specific capital gains significance, was mapped to its own token; all other dates became a generic `hubble_date`, and numeric and monetary values `hubble_number`. SMEs confirmed most dates carry no classificatory meaning but a few do.
3. **PII removal:** personal names, company names, addresses and postcodes were identified by regular expression and by taxonomy concept (for example `NameEntityOfficer`, `AdvancesCreditsDirectors`) and replaced with typed tokens such as `hubble_name`; SMEs advised that bare names attach to multiple classes and carry no signal, so records whose concepts related to names or addresses were removed entirely. This satisfied privacy requirements, removed a high-cardinality source of vocabulary inflation, and improved generalisation by preventing overfitting to entities.
4. **Length filtering:** the interquartile range of description length was 2–5 words. Descriptions of two characters or fewer carry too little information to classify; those of 16 words or more proved on review not to be line-item descriptions at all. Both were removed.
5. **Label engineering:** records whose description reduced entirely to a single placeholder were relabelled accordingly (for example `HubbleName`) — a placeholder alone cannot identify the original concept, but knowing the item is a name or a date is itself useful.

Canonicalisation reduced unique descriptions from 266,178 to 10,591 (96%) and labels from 956 to 826, retaining 86% of rows, and moved macro-F1 from under 0.50 to over 0.70.

**Data quality controls.** Controls were aligned to HMRC expectations and the six DAMA UK dimensions (DAMA UK, 2013) referenced by the Government Data Quality Framework (Cabinet Office, 2020). *Completeness* improved because untagged figures are now extracted; *consistency* because tagged and untagged items sit on the same tables in the same format; *timeliness* because data is categorised within days rather than months. *Validity* and *accuracy* were addressed by dropping missing, low-quality and ambiguous descriptions rather than letting them poison training; access is restricted to named users.

**Splitting.** Data was split 80/10/10 into train, test and holdout by stratified sampling so all 826 classes appear proportionally in each. Because several frameworks had to consume the same data, the splits — including 1%, 10%, 50% and 100% training subsets and sqrt-weighted variants, which apply a square-root transform to class frequencies to amplify minority representation — were generated once up front, guaranteeing every architecture was evaluated on identical data.

---

## 6. Survey of Potential Alternatives

The task is multi-class text classification over 826 nominal categories with strong imbalance. I used theory first to narrow the field to approaches suited to supervised classification of short domain-specific text, then tested empirically.


**Systematised rule base.** The incumbent approach — regular expressions per concept — could have been formalised into a maintained repository of concept-to-regex mappings. It is fully explainable, but requires sustained SME input, remains incomplete against a 23,000-description long tail, and is error-prone. Rejected on maintenance cost and coverage. **Unsupervised grouping** was rejected on the cosine similarity evidence above.

**TF-IDF with scikit-learn classifiers.** Word n-grams capture domain-specific vocabulary directly: "deferred consideration" or "share premium account" are highly discriminative in themselves. LinearSVC, SVC, PassiveAggressiveClassifier, LogisticRegression, RandomForestClassifier and GradientBoostingClassifier were evaluated against a `DummyClassifier` floor by a two-stage search — HalvingRandomSearchCV over 10,000 candidates on the 10% subset, then GridSearchCV over refined ranges for the survivors.

**Neural networks.** A CNN with a trainable embedding layer was evaluated as an approach able to learn local sequential structure beyond bag-of-words. Optuna's TPE sampler with HyperbandPruner searched architecture and hyperparameters over 200+ trials; DNN, LSTM, GRU and bidirectional variants were also tested, with the CNN best and dropout used for regularisation.

**Transformer models.** Four pre-trained models were evaluated — `nlpaueb/sec-bert-base` (pre-trained on SEC financial filings, so carrying relevant accounting semantics), `roberta-base`, `all-mpnet-base-v2` and `all-MiniLM-L6-v2` — with Optuna's MedianPruner terminating under-performing trials early.

**Frontier LLM via API.** A commercial LLM would likely have the strongest semantic understanding, but the input is a short phrase, not a passage, so most of that capability is unused. Against it are per-call cost at population scale, latency, and — decisively — the data protection and governance position of sending taxpayer-derived data to an external API. Rejected on proportionality and governance rather than capability.

**Embedding comparison.** Independently of the classifier, silhouette scores on a 50,000-record sample measured how cleanly each vectorisation separates concepts. An initial run included a word-plus-character n-gram combination whose parameters had been grid-searched on the same sample it was then scored against. It topped the table, but that is not a fair comparison — the search had optimised directly against the evaluation data, so the margin reflects tuning rather than a better representation. I excluded it and reran over the untuned vectorisers, on which the mpnet sentence transformer scored highest.

That is the expected result: dense embeddings capture semantic similarity between differently worded descriptions of one concept, which n-grams cannot. It did not translate into a materially better classifier — downstream, mpnet beat word-only TF-IDF *statistically* but by only about 0.003 macro-F1, at roughly 76× the runtime. Simple word n-grams were therefore selected: statistical significance is not material significance, and the simpler representation is faster, easier to maintain and easier to interpret.

Selection criteria were fixed before evaluation and reflected organisational priorities: macro-F1, inference latency, training time, interpretability, cost, infrastructure requirements and maintainability.

---

## 7. Implementation and Performance Metrics

**Population size validation.** Before committing compute, I tested whether small training subsets rank models the same way as the full dataset. Pearson correlation of macro-F1 between the 1% and 100% subsets was 0.971, and between 10% and 100% was 0.998; a paired t-test confirmed that models not significantly worse at 1% were also not significantly worse at 100%. This justified 1% for coarse filtering and 10% for the bulk of hyperparameter search, cutting experimental compute roughly tenfold without losing ranking confidence.

**LinearSVC optimisation.** HalvingRandomSearchCV narrowed the field to LinearSVC, SVC with a linear kernel, and PassiveAggressiveClassifier; paired t-tests showed LinearSVC significantly better than both at the 95% level. Plotting hyperparameters against score and runtime then guided the refined ranges — a plot with runtime encoded by colour showed `min_df=1` occupying clusters both faster and better scoring than `min_df=2`, which tabulated results do not reveal. The final configuration was TF-IDF (1–3 word n-grams, `min_df=1`, l2 norm) with LinearSVC (`penalty='l1'`, `C=2.8`, squared hinge loss, `dual=False`, `class_weight='balanced'`, `max_iter=10,000`); several values of C were statistically indistinguishable, so the lower end of that range was taken to reduce overfitting risk. The l1 penalty performs implicit feature selection, producing a sparser weight matrix and faster inference, and confidence intervals were computed by bootstrap. Of the training populations tested, 10% sqrt-weighted gave 1.3pp better macro-F1 but marginally lower accuracy than plain 10%, while the full population was better on both and gives the simplest pipeline.

**Neural network and transformer optimisation.** Optuna's automated search and hyperparameter-importance visualisations were a clear improvement on the manual scikit-learn approach. Architecture type was the most important factor for F1, batch size for training time; full configurations are at Appendix C. For imbalance, sqrt-weighted data with an unweighted CNN (0.776) beat both fully balanced weighting (0.721) and the unweighted baseline (0.757). Among transformers, SEC-BERT led on the 1% subset (0.754), consistent with its financial pre-training, and reached 0.782 on the full population — but needed 14.3 hours of GPU training, where the 10% sqrt-weighted configuration reached 0.779 roughly 14× faster.

**Final comparison.**

| Model | Training data | Macro-F1 | Accuracy | Training time | Inference |
|---|---|---|---|---|---|
| LinearSVC | 100% | 0.787 | 0.971 | ~2 hours (CPU) | 2.7μs/record |
| CNN | 10% sqrt-weighted | 0.776 | 0.973 | ~44 minutes (CPU) | ~15μs/record |
| SEC-BERT | 100%, batch 16 | 0.782 | 0.977 | 14.3 hours (GPU) | >1ms/record (CPU) |

Rather than compare on macro-F1 alone, I built a weighted decision matrix over eight objective measures (macro-F1, accuracy, precision, recall, training time, inference time, model size, infrastructure requirement) and six subjective ones (interpretability, explainability, deployment simplicity, maintenance burden, operational risk, analyst usability). Subjective scores were assigned against a written rubric with a supporting narrative so they were defensible rather than impressionistic, and were adjusted where confidence intervals overlapped so that differences which were not statistically real could not drive the outcome. LinearSVC won — and notably its 0.787 is not a concession to SEC-BERT's 0.782 but marginally ahead of it, while needing no GPU and running around 370× faster at inference. At millions of records per daily batch, that dominates the operational economics.

The pairing also fits the working environment: LinearSVC handles the sparse high-dimensional matrices TF-IDF produces very efficiently, and l1 regularisation makes them sparser still, so inner products are fast enough to develop and run on existing shared CPU infrastructure without degrading service for other users.

---

## 8. Results

The deployed model achieved macro-F1 0.787 and accuracy 97.1% on the holdout set at 2.7μs per record on a standard CPU. The CRISP-DM iterations produced documented improvement at each cycle: raw descriptions below 0.50; canonicalisation above 0.70; heading and table name improving the ambiguous classes; full optimisation with balanced weighting reaching 0.787.

**Per-class performance.** Aggregate accuracy is high, but class imbalance means minority concepts perform materially worse and some poorly. This is stated prominently rather than buried: I produced per-class summaries so analysts know which concepts need bespoke description matching rather than the ML category, and — on my recommendation — an interactive dashboard exposing per-class performance, far more usable than a large results file. It also surfaces top-k predictions; analysts found low-scoring alternatives confusing, so it now shows only plausible matches.

**Error analysis.** Confusion matrices show most errors falling between semantically similar concepts — variants of "amounts owed to group undertakings", for example. Frequently the model predicts the commonest concept for a description while the test label is a different concept that has legitimately used the same wording: a limit of the feature, not the model, and SMEs confirmed that for some items the accounts do not contain enough information to determine the concept at all. Heading and table name mitigated part of this; the remainder is irreducible without richer document context.

**Robustness and sensitivity testing.** I built a test suite probing behaviour across abbreviations, synonyms, typographical errors, OCR-style corruption, unicode variants, formatting variations, semantically equivalent rephrasings, long-context inputs, adversarial phrasing designed to mislead, and instruction-injection strings of the kind that would target an LLM. LinearSVC outperformed SEC-BERT overall — unexpected, since domain pre-training and richer semantics should have favoured it. Where LinearSVC was weaker, on typos and surface variation, real exposure is low: accounts are generated by accounting software rather than typed. Testing an assumption I expected to be contradicted, and finding it held, is stronger evidence than the headline metrics alone.

**Bias.** The material bias risk is representation bias across concepts, document types and preparation practices rather than demographic fairness. Large companies scored macro-F1 0.9343 against 0.7898 for small companies; between accounting software providers the spread was wider still, 0.1841 to 0.9133 — likely because smaller companies use cheaper software that tags differently. Interpretation matters: because the labels are the preparer's own tags, part of this gap measures inconsistency in *how software tags items* rather than the model's ability to read a description — an artefact of the training proxy that would not necessarily transfer to untagged items. Residual analysis supports this, with misclassifications concentrated between near-identical classes. It is reported to analysts so small-company outputs are treated more cautiously.

**Explainability.** LinearSVC's coefficients show directly which n-grams drive each class prediction, supporting error analysis and HMRC's AI governance requirement; no equivalent exists for SEC-BERT. LIME and SHAP gave comparable explanations for the CNN and SEC-BERT, so interpretability was compared on evidence rather than assumption.

**Deployment.** The model runs inside the R production pipeline via `reticulate`, with outputs ingested to Oracle, and on-demand compute — designed with DevOps — starts an EC2 instance for the daily batch and shuts it down on completion.


---

## 9. Discussion and Conclusions/Recommendations

The results answer the problem set out in §2: analysts are no longer confined to a tagged minority that is not missing at random, and coverage extends from 30% to close to the full extracted population.

Selecting LinearSVC over transformers shows why solutions must be evaluated against the full operational requirement rather than one metric — SEC-BERT's marginal deficit on macro-F1 arrives alongside GPU infrastructure, far longer training, slower inference and a more complex maintenance profile. Explainability was likewise a first-order requirement, not a nicety: interpretable feature weights are what made error analysis, stakeholder communication and the analyst dashboard possible, and a marginally better black box would have carried a governance risk the business could not accept. Other decisions sacrificed raw performance for usability — a bespoke model per taxonomy would score best but would give analysts inconsistent class names, so one main taxonomy per document type is applied universally. That trade-off came from asking SMEs why predictions that looked right were scored wrong: SME questioning reshaping the design rather than merely validating it.

Communication is worth reporting where it changed an outcome. Early explanations were too detailed to land, so I moved to visual, example-led ones — a decision tree showing what was split on, a two-dimensional SVM boundary, a worked example distinguishing weighted from macro scores. With analysts, presenting confusion matrices and concrete error cases rather than aggregate scores gave them an accurate sense of where the model could be trusted, and use of the ML category in profiling rose as a result. With managers, memos framed as cost-benefit rather than technical progress secured infrastructure funding, and framing the case around delivery capacity got a further developer reallocated. The README and setup script had a similar effect: analysts now install and run the tool themselves, which scaled adoption and freed me to develop.

Two things I would do differently. An early embedding comparison had to be discarded because the candidate had been tuned on the sample it was then scored against, so its advantage was an artefact of that tuning (§6); separating tuning from evaluation data is now a standing rule rather than something checked at write-up. I also ran the scikit-learn search largely by hand before adopting Optuna for the neural and transformer work, and would use automated search from the start.

**Recommendations**

1. **Extend to further document types**, prioritised by tagging gap and analytical value, revalidating taxonomy, extraction and PII assumptions for each. The pipeline is reusable; the assumptions are not.
2. **Operate the defined drift monitoring**: watch inputs for new or changed taxonomies, and treat a 2pp drop in accuracy or macro-F1 with non-overlapping confidence intervals over two consecutive days as the retraining trigger. Retain model, data and preprocessing versions so rollback is available — the main containment against silent degradation reaching analysts.
3. **Establish formal data contracts** with the downstream teams now consuming Hubble output. Undocumented dependencies on a single developer's tool are a continuity risk to those teams as much as to this one.
4. **Validate against human-labelled untagged items.** This is the one gap no amount of further modelling closes (§12), and it needs a ring-fenced allocation of SME time rather than best-efforts capacity.
5. **Maintain the human-in-the-loop control**: the ML category must not drive automated decisions, and per-class performance documentation should accompany any analytical output relying on it.
6. **Adopt a standard structure for technical communications** — headline figures first, plain-English explanation with illustrations, technical detail in an appendix — so findings reach decision-makers without translation loss.
7. **Reduce delivery risk in the stack**: move the test suite into a GitLab CI pipeline, and evaluate porting the R components to Python ahead of the lakehouse migration rather than during it.

---

## 10. Summary of Findings

Against the success criteria agreed with analysts and managers at the outset (§4):

| Criterion | Outcome |
|---|---|
| Macro-F1 ≥ 0.70 | **0.787** |
| Inference < 10μs per record | **2.7μs**, CPU only |
| Accuracy ≥ 95% on majority classes | **97.1%** overall |
| Coverage ≥ 95% of extracted figures classified | Met on standard-structure documents; the ~15% using non-standard HTML need bespoke extraction (§12) |
| Short-term: sub-population outputs to file | Delivered |
| Long-term: daily population ingestion to Oracle | Delivered and in production |

Three findings are worth carrying forward. Data preparation mattered more than model choice: canonicalisation alone moved macro-F1 from below 0.50 to above 0.70, a larger gain than any change of architecture. The simplest candidate won on more than cost — LinearSVC matched the transformer on macro-F1 and beat it on robustness, so the usual performance-for-simplicity trade did not arise. And the residual errors are mostly a property of the data, not the model, which sets where further effort should go: richer contextual features, not larger models.

---

## 11. Implications

**Analytical capability.** The wider population now also arrives within days rather than after the taxonomy update cycle, and the combination changes what is achievable inside the twelve-month enquiry window. This improves the statistical basis for policy advice and the completeness of risk identification; Hubble has supported projects that identified hundreds of billions of pounds of incorrectly stated figures in returns.

**Business value and quality.** The tool meets HMRC quality standards for completeness and consistency: nearly all figures are extracted, and the ML category gives one vocabulary across tagged and untagged data. Benefits recorded manually by users ran to tens of millions of pounds in estimated value, but recording was incomplete, so I arranged for benefit tracking to be built into the central management system rather than a spreadsheet. Demonstrated benefit has already secured funding to expand capability and reliability.

**Reusable patterns.** The project establishes a methodology for supervised ML on semi-structured tax data — existing tags as supervision, sub-population correlation validation to make experimentation affordable, sqrt-weighted sampling for imbalance, weighted decision matrices for selection — and the on-demand compute pattern is a template for other periodic high-volume workloads.

**Governance.** The DPIA, PII canonicalisation, human-in-the-loop requirement, per-class performance documentation and analyst dashboard together form a governance model proportionate to the risk, demonstrating that operationally useful ML can be delivered inside HMRC's data governance framework.

---

## 12. Caveats and Limitations

**Evaluation is on tagged data; the use case is untagged data.** This is the most significant limitation. The model is trained and evaluated entirely on items the preparer chose to tag, but its purpose is to classify items they did not. If the two populations differ systematically — for instance where an item was left untagged precisely because no suitable concept exists — measured performance will overstate real performance. The mitigation is a human-labelled sample of untagged items (Recommendation 4); until then, monitoring prediction distributions, analyst feedback and the human-in-the-loop control are what stand in its place.

**Minority classes and irreducible ambiguity.** Despite balanced weighting, concepts with few training examples score below the 0.787 average and some score poorly; the per-class dashboard exists so analysts can check reliability first. Separately, generic descriptions such as "total" or "additions" legitimately correspond to several concepts. Heading and table name partially mitigate this; the remainder would need richer context such as surrounding rows or document section, which is harder to extract reliably.

**Bias measurement is confounded.** Without human-labelled data, the model's own weakness cannot be fully separated from differences in tagging practice in the §8 gaps.

**Scaling behaviour.** LinearSVC does not scale efficiently to much larger datasets, so retraining on substantially more data is impractical — though 10% to 100% gained only 0.4pp macro-F1, so larger datasets are unlikely to help materially. Increasing dataset size at a fixed minimum-count cutoff also admits more labels and can reduce headline macro-F1, and label distributions differ by document type, so scores are not comparable across types or sources.

**Taxonomy evolution and extraction coverage.** New concepts and secondary taxonomies will not be classified correctly without periodic retraining, and preparation practices change over time. Around 15% of documents use non-standard HTML without standard table nodes, needing bespoke positional extraction logic; this is implemented but remains an ongoing development area.

**PII handling edge cases.** Regular expressions and taxonomy-based detection catch most PII, but edge cases remain — directors' names without common salutation prefixes, for example — documented in the DPIA with a committed mitigation plan.

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

1. **Final hyperparameters conflict across sources.** [[Z Project Report - Report]] (7 Aug) states TF-IDF 1–3 n-grams, `min_df=1`, l2 norm, LinearSVC `C=2.8`, `max_iter=10,000`. [[Z Project Report - Review and to do]] (24 Jul, taken from notebook 03) states TF-IDF 1–2 n-grams, `C=2`, `max_iter=5,000`. The signed-off brief says 1–3 n-grams. This draft uses the Report's values. **Confirm against MLflow.**
2. **Silhouette scores — resolved, but add the numbers.** The grid-searched word+char combination was tuned on the sample it was scored against, so its 0.477 was not a real improvement and has been excluded; §6 now reports mpnet as the best untuned vectoriser and explains why the other was dropped. **Add mpnet's score and the range across the remaining untuned vectorisers** once you have the rerun figures — the argument works without them but is stronger with them.
3. **Heading/table name uplift.** The Report has "improved f1-macro from x to y" — the actual figures are needed, or the claim should stay qualitative as it currently is.
4. **Inference latency units.** Source notes variously say 2.7μs, 2.7ms and 2.7s. This draft uses 2.7μs, which is the only value consistent with the "370× faster than SEC-BERT" claim and the <10μs KPI. **Confirm.**
5. **Benefits figures.** Both source figures are stated as written: "tens of millions" in estimated recorded benefits, and "hundreds of billions of pounds" of incorrectly stated figures identified. The second is a striking number and an assessor is likely to ask about it, so have the framing ready — it is the value of figures identified as incorrect across projects Hubble fed, not tax recovered and not attributable to Hubble alone. Worth naming the source system or project so it can be evidenced if challenged.
6. Consider whether the 12 million annual returns figure from the earlier draft can be sourced; it is currently generalised to "millions".
7. **Check the same leak elsewhere.** The silhouette problem was evaluation data being used for tuning. Worth confirming the downstream mpnet-vs-TF-IDF macro-F1 comparison (~0.003, 76×) was measured on held-out data, since §6 now rests on it alone.
8. **Coverage KPI.** §10 now reports outcomes against every success criterion from §4, and coverage is the only one without a measured number — it currently reads "met on standard-structure documents." **Get the actual percentage of extracted figures assigned a concept**, or soften the KPI in §4 to match what you can evidence. An assessor reading the table will notice the one row that has no figure in it.
