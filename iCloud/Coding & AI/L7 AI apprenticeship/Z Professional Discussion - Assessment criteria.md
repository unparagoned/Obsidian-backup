**Artificial Intelligence Data Specialist — Level 7 Apprenticeship**
**Learner:** Jesse Karadia
**Organisation:** HMRC

This document organises professional-discussion preparation around the EPA assessment criteria. Each criterion lists the relevant KSBs, one or more STARR answers and short technical notes for likely follow-ups. Use them as speaking notes, not a script: keep the first-person language, adapt depth to the question and be ready to name supporting artefacts (test results, decision matrices, GitLab issues, dashboards, DPIAs, stakeholder feedback, wiki guidance, experiment records). The grading table assesses KSBs collectively within each theme, so the per-criterion KSB lists are a practical evidence map, not official marking units.

## Evidence boundary and status

The EPA clarification repeatedly requires **my own practical application in my current role and organisation**. The notebooks in `Code/` are technical artefacts, not a substitute for workplace evidence about deployment, users, governance or business impact. Three evidence categories are used throughout:

- **Code-backed** — directly demonstrated by source or saved output in `Code/`.
- **Workplace evidence** — statements about internal Hubble, HMRC systems, stakeholders, deployment or impact that need an approved artefact or witness as well as my explanation.
- **Proposed/future** — a control or improvement I can justify but must not describe as implemented.

The public notebooks use Companies House accounts and deliberately simplify the internal implementation: Python/BeautifulSoup extraction of description and concept only, whereas the internal extraction is R-led, integrates R/Python/SQL and captures contextual features such as table name and heading. Present the notebooks as reproducible corroboration of the methodology and experiments; use separate workplace artefacts to prove internal architecture, operational scale, user changes and business outcome.

### Code artefact map

| Artefact | Demonstrates |
|---|---|
| `00_ixbrl_data_extraction.ipynb` | Python parser over a Companies House monthly accounts archive; table descriptions and iXBRL concept labels to Parquet. |
| `01_ixbrl_eda_preprocessing.ipynb` | EDA, ambiguity/imbalance analysis, text cleaning, canonicalisation, label engineering, embedding comparisons, fixed seeded splits. |
| `03_ixbrl_experiment_models.ipynb` | Classical-model search, stratified CV, TF-IDF/embedding comparisons, bootstrap intervals, robustness cases, LIME/SHAP, final LinearSVC configuration. |
| `04_ixbrl_nn.ipynb` | Optuna-led neural-network/CNN experimentation, class-weighting tests, robustness testing. |
| `05_xbrl_transformers.ipynb` | Hugging Face/PyTorch transformer comparison, SEC-BERT tuning, sampling/weighting experiments, explainability, resource trade-offs. |
| `06_compare_models.ipynb` | Three-model comparison using objective measures, confidence intervals and an operational rubric. |

### Key figures to quote

- Corpus: ~2.9 million extracted rows across 956 raw concepts; ~2.5 million rows and 826 engineered labels after cleaning. Modelling used the 141 labels with at least 350 examples; the 685 rarer labels were excluded.
- Fixed seeded 80/10/10 train/test/holdout split, with a 10,000-row holdout sample for like-for-like model comparisons.
- The top 75 raw concepts cover ~95% of items; generic descriptions such as "Total" map to many concepts — this ambiguity and long tail motivated contextual features and macro-F1.
- Final classical pipeline: word TF-IDF (1–3)-grams with IDF and L2 normalisation; LinearSVC with `C=2.8`, L1 penalty, squared-hinge loss and balanced class weights.
- Holdout comparison (accuracy / macro-F1): LinearSVC **0.975 / 0.800**; CNN **0.977 / 0.808**; SEC-BERT **0.977 / 0.823**. The 95% bootstrap intervals overlap, so SEC-BERT's ~2-point macro-F1 advantage is a point-estimate difference, not a statistically established improvement.
- Operational measures (training / full-test inference / model size): LinearSVC ~2.5 min / 0.6 s / 8 MB; CNN ~44 min / 24 s / 30 MB; SEC-BERT ~67 min / 143 s / 1.8 GB. State the hardware before generalising.
- Embeddings: on one 1% run MPNet beat TF-IDF by ~0.003 macro-F1 at ~67× the fit time; a later 1% run showed a ~0.0001 difference, not significant at 95%. Keep the two runs separate.

### Limitations to state rather than hide

- The split stratifies individual rows, not filings or descriptions, so related rows can cross partitions and the saved metrics may be optimistic. Production evidence needs a grouped (filing/company) and/or temporal holdout.
- The CNN and transformer output layers cover all 826 labels although only 141 have training examples; remap to the 141 classes and rerun before treating the cross-family ranking as final.
- The decision matrix has a field-name mismatch that omits interpretability from its calculated score, and its subjective ratings and min-max scaling over three candidates are sensitive to weights. Correct and sensitivity-test before quoting the numeric ranking; the qualitative conclusion (LinearSVC favoured operationally) still stands.
- Canonicalisation reduces identity signal in the model feature; it does not anonymise the source data or replace access, retention and lawful-purpose controls.
- Fairness metrics (demographic parity, equalised odds) and live drift monitoring are proposed work, not implemented controls. Class imbalance, per-class performance, robustness and residual errors were analysed.
- The notebooks prove a validated model comparison and research method, not deployment, live monitoring, user acceptance, accessibility testing or business benefit.

## Evidence gaps — search for `TODO:`

### Theme 1

- **T1.1** — TODO: a verified measure of extra analytical coverage, manual effort avoided or profiling improvement attributable to classification specifically (not extraction generally).
- **T1.2** — TODO: remap the 141 classes and rerun CNN/SEC-BERT on the same grouped split. TODO: the exact statistical comparison (test, folds, assumptions, p-value, CI, effect size). TODO: acceptance-testing record (date, users, criteria, blank-description and dimensional-data changes). TODO: usability-testing record (dashboard task, confusion evidence, change made, retest). TODO: natural-vs-numeric key benchmark status.
- **T1.3** — TODO: agent-risk Welch test details (safe sample sizes, statistics, p-value, CI, effect size; confirm the "99% confidence" wording and name the artefact).
- **T1.4** — TODO: artefact showing the R→Python and Oracle-output boundary and an integration issue resolved. TODO: keep the simulation claim narrow (controlled computational experiments, not Monte Carlo). TODO: a specific commercial-benefit measure from the mixed-language design.
- **T1.5** — TODO: HMRC's classification of enterprise/private/public components plus a nameable architecture/security document. TODO: ODC configuration, volumes, runtimes and stability evidence. TODO: S3 proxy details (dataset, user group, approval flow) and evidence it worked. TODO: auto-scaling cost comparison record. TODO: verify the "days rather than nine months" timeline and name a witness.
- **T1.6** — TODO: the exact interfaces implemented (Oracle driver, `dbplyr`, Solr endpoint, S3 proxy, FSx, Parquet library). TODO: what "~128 concurrent" means (workers, cores or documents) and the observed bottleneck. TODO: Oracle/Parquet before/after workflow and analyst reuse. TODO: LLM-to-Solr status — built, prototyped or proposed.
- **T1.7** — TODO: wide-to-long challenge details (owner, investigation, approval, improvement, artefact). TODO: tagged-as-supervision baseline and coverage before/after. TODO: calculation-error challenge — safe description, my role, quantified impact, what can be discussed.

### Theme 2

- **T2.1** — TODO: verify DAP growth (1 → 150+ users), period and definition, with a report or witness. TODO: one anonymised mentoring outcome. TODO: proof-of-concept model details and how it progressed. TODO: verify the 233% extraction increase and "millions of pounds" separately.
- **T2.2** — TODO: named technical-audience meeting/artefact and an objection addressed. TODO: named non-technical artefact and the plain-language translation used. TODO: the conditions under which SEC-BERT or another assured model would become preferable.
- **T2.3** — TODO: internal dissemination titles, dates, audience, reuse and one changed practice. TODO: where/when Graffiti was shared, audience, feedback and one concrete reuse.
- **T2.4** — TODO: the specific reports/papers reviewed and the social/public-sector implications drawn. TODO: AI-guidance change record (date, feedback, decision-maker, revised wording). TODO: grounded-LLM justification sources, safeguards and external feedback.
- **T2.5** — TODO: DAP licence/compute decision record. TODO: database-versus-S3 decision record. TODO: Hubble model decision record (stakeholder preferences, pre-agreed weights, corrected matrix, approval route).
- **T2.6** — TODO: engineer contributors and one example where an engineer's input changed the implementation. TODO: the organisational testing/version-control/documentation standard complied with. TODO: test/CI/README evidence and a defect prevented or detected.

### Theme 3

- **T3.1** — TODO: one verified organisational outcome, distinguishing extraction impact from classifier impact. TODO: label industry impact as potential unless demonstrated. TODO: the credible societal link and counter-risks, without over-claiming.
- **T3.2** — TODO: DPIA risk categories, ratings, mitigations, owner and artefact name. TODO: blank-description and dashboard issue discovery, fix, retest and remaining limitation. TODO: distinguish operating controls from proposed drift/performance monitoring.
- **T3.3** — TODO: Graffiti before/after or user example. TODO: a measured team-workflow improvement (reproducibility, setup time, defects, review quality).
- **T3.4** — TODO: name the actual HMRC policies, UK GDPR requirements and approvals relevant to Hubble. TODO: who checked compliance, when, and how changes trigger reassessment. TODO: a safe consequence example; verify any penalty figure from an official source.

### Theme 4

- TODO: Hubble lawful basis, controller/processor roles, retention, access roles and actual approvals from the DPIA. TODO: which identifiers were canonicalised, what remained identifiable and where processing occurred. TODO: Companies House pipeline status — same or separate, real environment, controls implemented. TODO: WCAG review details (product, date, version/level, findings, my fixes, retest). TODO: Graffiti alternative-install testing and assistive-technology checks. TODO: dashboard user-diversity evidence (roles, task, feedback, change, retest). TODO: licence/IP/contract checks actually completed — otherwise keep as knowledge. TODO: user groups actually consulted, one need/response each.

### Theme 5

- **T5.1** — TODO: dated CPD record linking the strongest sources to decisions changed. TODO: community/conference evidence (do not imply attendance if it was online reading). TODO: link specific literature to a concrete experiment and decision. TODO: team development process and one before/after capability outcome; describe informal mentoring accurately.
- **T5.2** — TODO: confirm final model status — deployed, recommended for deployment, or validated prototype — and use one wording throughout. TODO: final production evidence if any (holdout performance, infrastructure, monitoring, acceptance, DPIA). TODO: consistency audit of scores, class counts, split, deployment status and impact claims across this document.

---

# Theme 1: Use and knowledge of computing and statistical foundations of AI and data science

**Theme KSBs:** K7, K16, K18, K19, K22, K25, S1, S16, S19, S20, S26.

**Distinction integration:** pass answers also identify the norm challenged, the investigation, the proposed solution and its impact where natural; the standalone distinction answers remain the fullest versions.

## Describes how to use statistical, AI and machine learning methodologies such as data mining, supervised/unsupervised machine learning, natural language processing and machine vision to meet business objectives

**Relevant KSBs:** K19, K22, K25, S26.

### STARR — selecting methodologies for Hubble

**Situation:** Company accounts and tax computations are submitted as iXBRL, but some tax computations had only ~30% of figures tagged, so conventional extraction omitted much of the available information. Hubble could extract the untagged descriptions, but the same accounting concept could be described many ways, making profiling through manual regular expressions problematic and tedious, e.g. VechicleCosts. 

**Task:** So I challenged the status quo and suggest that we use ML to turn inconsistent, untagged descriptions into standard taxonomy concepts so analysts could profile more reliably across the extracted data. 

**Action:** I treated this as a text-classification problem, challenging the assumption that population analysis had to rely on tagged items or matching rules: I investigated whether tagged descriptions could supervise classification of untagged content. Data mining on the ~2.5 million cleaned rows — frequency ranks, Pareto concentration, description/concept overlap, cosine similarity, class balance and residual errors — showed a long-tailed, ambiguous problem. Because tagged items supplied target concepts, supervised learning was the main approach. I compared Naive Bayes, tree ensembles, SVC/LinearSVC, SGD-style models, CNN/neural approaches, SEC-BERT and MPNet/e5 embeddings, using embedding geometry and labelled-class silhouette scores as exploratory analysis. Candidates were assessed on macro-F1, accuracy, per-class results, stratified CV, bootstrap intervals, speed, infrastructure, explainability, provenance, maintainability and cost.

**Result:** TF-IDF with LinearSVC was the strongest operational recommendation, not the highest point estimate on every metric: holdout macro-F1 0.800 against CNN 0.808 and SEC-BERT 0.823, with overlapping intervals, but far faster CPU-only training, inspectable coefficients and lower lifecycle risk. The business-impact claim — making untagged content usable for risk identification — still requires a workplace artefact and is kept separate from the technical result.

**Reflection:** Method selection must begin with the business objective, label availability, data type and deployment constraints. Supervised NLP was appropriate; unsupervised methods stayed exploratory; frontier LLMs were disproportionate. The best technical score alone does not define the best business solution.

### Technical detail / likely follow-up

- **Supervised learning** — learns a labelled input→output mapping; tagged iXBRL concepts were the labels, and classification (not regression) fitted the known taxonomy target.
- **Unsupervised learning** — structure without labels (K-means, hierarchical, DBSCAN; anomaly detection). The notebook used known concept labels in silhouette comparisons of vector spaces — an exploratory representation test, not an operationalised clustering model; a real clustering result would need SME interpretation.
- **Semi-supervised** — self-training/pseudo-labelling could help if verified labels were scarce, at the risk of reinforcing wrong pseudo-labels. **Self-supervised** — creates targets from raw data (masked-word prediction); underpins BERT-style pre-training. **Reinforcement learning** — policy learning from rewards; not appropriate for a fixed labelled classification problem.
- **Data mining** — frequency, overlap, ambiguity, imbalance and error-pattern analysis established whether sufficient labels existed and where taxonomy or source quality limited achievable performance.
- **NLP pipeline** — parse iXBRL/XHTML; select descriptions and context; lower-case; normalise; canonicalise names/companies/dates/postcodes/numbers; tokenise; n-grams; TF-IDF or embeddings; classify; retain prediction, score and provenance. Learned transformations must be fitted on training data only and reused unchanged in production to avoid leakage and divergence.
- **Machine vision** — not justified because the text and structure were already extractable from iXBRL. If scanned PDFs became an input, OCR/layout models could extract text but would add an error-producing stage needing its own testing.
- **Business connection** — the chosen method had to widen coverage, reduce manual grouping and improve risk identification; suitability came from labels, costs, explainability, infrastructure and failure modes matching that objective.

## Explains how to solve problems and evaluate software solutions via analysis of test data and results from research, feasibility, acceptance and usability testing in line with organisational requirements

**Relevant KSBs:** K7, S26.

### STARR — evaluating the Hubble classification solution

**Situation:** Analysts could not practically profile extracted untagged descriptions: wording was inconsistent and there were hundreds of taxonomy classes with a long tail of rare examples.

**Task:** Define the problem, research feasible solutions, test them objectively, and confirm the chosen output was usable and met HMRC requirements for security, explainability, infrastructure and analyst adoption.

**Action:** I challenged the practice of treating headline accuracy or the most advanced model as the answer, defining success more broadly first: classify minority as well as common concepts, run at operational scale, remain explainable, use supportable technology, protect data and be usable by analysts. I researched classical ML, neural, transformer and embedding approaches; feasibility covered CPU/GPU needs, throughput, cost, provenance, maintainability and whether the estate could run the model. Evaluation used fixed seeded 80/10/10 splits with a 10,000-row holdout sample; five-fold `StratifiedKFold` with `GridSearchCV`/`HalvingRandomSearchCV` for scikit-learn models; Optuna and MLflow for neural/transformer runs; and macro-F1, accuracy, precision/recall, confusion/residual analysis, bootstrap intervals, runtime and model size. Crafted robustness cases diagnosed failure modes (LinearSVC stronger on adversarial/contextual/OCR categories, SEC-BERT on Unicode substitution, both weak on abbreviations and typos) — diagnostics, not population estimates. I then involved users: acceptance testing exposed predictions made from blank descriptions using only headings, so I changed production logic to return no prediction there; users needed more dimensional data, so I generalised the extraction; usability testing showed the top-five-matches display and raw scores confused users, so I limited the display to confident matches and added explanatory text. A request for numeric rather than natural database keys is being treated as a performance question to benchmark, not a preference to accept.

**Result:** TF-IDF plus LinearSVC balanced quality with speed, explainability, supportability and security (holdout macro-F1 0.800; SEC-BERT's higher point estimate was not interval-separated, and the operational rubric favoured the simpler model). Acceptance testing changed extraction and prediction behaviour; usability testing made the dashboard clearer — both need named internal artefacts. The defensible status from the notebooks is a validated comparison/proof of concept, not proven production deployment.

**Reflection:** Research established tooling before writing bespoke evaluation code — Optuna automated what I had partly built myself. Training, test and production preprocessing need a single controlled implementation so rules like blank-description handling cannot diverge. I would agree acceptance criteria earlier, automate pipeline-parity checks and keep a traceable decision log.

### Technical detail / likely follow-up

- **Research and feasibility** — literature, documentation and empirical comparison; feasibility is more than "the code ran": infrastructure, cost, provenance, security approval, maintainability, retraining time.
- **Train/validation/test/holdout** — training fits parameters; validation/CV selects hyperparameters; an untouched holdout estimates final performance (repeatedly checking it would make it another validation set). The row-level stratified split is the known weakness; the stronger design is `StratifiedGroupKFold` or a grouped split by filing/company plus a chronological or unseen-taxonomy holdout, with learned preprocessing fitted inside each fold.
- **Cross-validation** — K-fold reduces dependence on one lucky split at ~K× cost; five folds gave comparative evidence but only five paired observations, so inferential claims stay cautious.
- **Overfitting/underfitting** — strong train + weak validation vs poor on both; mitigations include regularisation, simpler models, more representative data, dropout, CV; the bias–variance trade-off frames it.
- **Metrics** — per-class one-versus-rest TP/FP/FN/TN; accuracy, precision, recall, F1; macro-F1 was principal because accuracy and weighted variants are dominated by common concepts; support counts still needed because macro-F1 is unstable for very rare classes.
- **Statistical vs practical significance** — the bootstrap intervals answer a different question from a paired fold t-test; overlap is not a formal test but is enough to avoid claiming established superiority. A stronger comparison would bootstrap the paired prediction difference and report the CI for the difference alongside cost/assurance criteria.
- **Decision matrix** — combines objective measures with scored rubrics (interpretability, deployment, maintenance, lifecycle risk). Two qualifications: the interpretability field-name defect and the sensitivity of subjective weights with min-max scaling over three candidates. Correct, document who agreed each weight, and sensitivity-test before using the ranking as a decision record.
- **Acceptance vs usability** — acceptance asks whether the solution meets the need (missing dimensions, blank-description predictions); usability asks whether people can use it effectively and safely (confusing alternatives and raw scores).
- **Production monitoring (proposed)** — extraction failures, missing-description rate, taxonomy changes, input/prediction distributions, holdout macro-F1, per-class metrics, latency, low-confidence coverage, analyst overrides; PSI/KS/chi-square to flag drift, then diagnose, contain, relabel, revalidate, retrain or roll back.

## Describes the relationship between mathematical principles and core techniques in AI and data science within the organisational context

**Relevant KSBs:** K19, K22.

### STARR — the mathematics behind the Hubble model choice

**Situation:** Hubble needed to classify short, inconsistent accounting descriptions into a large, imbalanced set of standard concepts, and stakeholders needed both reliable outputs and an explanation of how the method worked.

**Task:** Select and explain a technique whose mathematical properties suited sparse text, unequal class frequencies and HMRC's need for fast, supportable, interpretable processing.

**Action:** I represented each canonical description as a numeric vector using word TF-IDF (1–3)-grams with smoothed IDF and L2 row normalisation. LinearSVC then used vector geometry and convex optimisation to find one-versus-rest separating hyperplanes (`C=2.8`, L1 penalty, squared-hinge loss, balanced class weights). L1 drove many feature weights to zero, giving a smaller, inspectable coefficient set; balanced weights increased the influence of minority-class errors. I challenged the stakeholder preference for accuracy as the headline measure — 75 concepts covered ~95% of items — and made macro-F1 the selection metric so each eligible class contributed equally, retaining accuracy, precision/recall, support and confusion analysis alongside. Stratified CV estimated generalisation; bootstrap intervals expressed uncertainty in the holdout measures.

**Result:** The mathematics supported an organisationally appropriate choice: fast on existing CPUs, explainable through coefficients and better aligned to minority concepts than selection on accuracy. Reframing evaluation around macro-F1 made rare-class performance visible and gave stakeholders an impartial basis for comparison.

**Reflection:** Mathematical principles explain why a technique behaves as it does and whether its output suits a decision. I would never present a p-value or metric as certainty — sample size, assumptions, class representation, effect size and business consequences all matter.

### STARR — testing whether an agent presented higher risk

**Situation:** In separate agent-level risk work, qualitative review suggested one agent might present higher risk than the comparison group.

**Task:** Test that suspicion quantitatively rather than let an impression drive the conclusion.

**Action:** I set the null hypothesis that the agent's risk equalled the comparison group's. The data was two independent groups on a ratio-scale measure, approximately normal, with 30+ observations and unknown population variances. An F-test indicated unequal variances, so I selected Welch's t-test rather than Student's.

**Result:** At a 99% confidence level I rejected the null and concluded the agent presented higher risk, giving the business quantitative evidence rather than judgement alone.

**Reflection:** The test must follow the data and its assumptions. I would present the confidence interval and effect size as well as the p-value, because statistical significance alone does not show operational importance.

### Technical detail / likely follow-up

- **TF-IDF mathematics** — term frequency is the raw n-gram count; with smoothing, `IDF(t) = log((1+N)/(1+df(t))) + 1`; multiply and L2-normalise each vector. Common words are down-weighted; distinctive terms up-weighted; (1–3)-grams preserve phrases like "interest receivable".
- **LinearSVC mathematics** — score `w_c · x + b_c` per class, predict the argmax; one-versus-rest with L1 penalty and squared-hinge loss, conceptually `||w||₁ + C Σ max(0, 1 − yᵢ(w·xᵢ + b))²`. Large `C` penalises margin violations more (overfit risk); balanced class weights scale contributions inversely to frequency. Efficient on large sparse matrices; a linear boundary may miss deeper context and raw scores are not calibrated probabilities.
- **L1 vs L2 regularisation** — L1 (sum of absolute values) drives weights to exactly zero, acting as feature selection; L2 (sum of squares) shrinks smoothly. Too much regularisation underfits. State the exact supported penalty/loss/dual combination from the experiment record, not memory.
- **Embeddings** — dense vectors (MPNet, e5) capture semantic similarity across wording; slower, less interpretable, and generic pre-training can miss specialist accountancy usage. The recorded gains over TF-IDF were ~0.003 macro-F1 at ~67× fit time on one run and negligible/not significant on another.
- **Neural networks** — weighted sum + bias + activation; trained by loss minimisation via gradients, backpropagation and SGD/Adam. CNNs learn phrase-like local patterns; LSTMs gate a hidden state through sequences. Useful experimentally; unnecessary complexity for short descriptions.
- **Transformers** — self-attention `softmax(QKᵀ/√d_k)V` lets every token attend to every other; BERT is a bidirectional encoder pre-trained with masked-language modelling, classifying via `[CLS]`. SEC-BERT's financial pre-training was attractive, but GPU needs, throughput, explainability and provenance reduced organisational suitability.
- **Macro-F1** — mean of per-class F1, each class equal; aligned with not ignoring rare concepts; high variance for tiny classes, so report support and intervals alongside.
- **Paired model comparison** — same folds, difference per fold, `t = mean(d)/(sd(d)/√n)`; pairing controls for split difficulty; with five folds it is supporting evidence, not proof.
- **Welch's t-test** — `t = (m₁ − m₂)/√(s₁²/n₁ + s₂²/n₂)`; compares independent means without assuming equal variances; still assumes independence and approximate normality/large samples. Rejecting at 99% means the difference is unlikely under equal means — not a 99% probability the conclusion is true.
- **Wider relationship** — linear algebra represents documents and weights; calculus/optimisation fits models; probability/statistics quantifies uncertainty; geometry explains similarity and separation. Organisationally these translate into CPU cost, minority-class coverage, interpretability and a defensible choice.

## Explains how they have used programming languages and modern machine learning libraries for commercially beneficial scientific analysis, simulation and data engineering to meet business needs

**Relevant KSBs:** K18, K25, S26.

### STARR — using R, Python and SQL as one Hubble pipeline

**Situation:** Company returns (XML) and accounts (iXBRL/XHTML) contained valuable structured and semi-structured data. The analysts who would maintain and use the extraction worked primarily in R, while the strongest documented ML ecosystem for the classification experiments was Python.

**Task:** Select languages and libraries for extraction, cleaning, model experimentation and delivery without forcing the whole pipeline into one language or creating an unsupported workflow — challenging the norm that a project stays in the language it started in.

**Action:** I investigated package maturity, team capability, platform support and long-term maintenance rather than choosing by preference. In the workplace implementation I used R for the fuller XML/HTML extraction because it matched the supported analyst workflow, with `reticulate`, SQL/Oracle and `dbplyr` at the pipeline boundaries (internal artefacts needed — not in `Code/`). The public implementation is Python end to end: BeautifulSoup/Pandas parsing to Parquet; Polars/NumPy for EDA and engineering; scikit-learn for TF-IDF, classical modelling, CV and halving searches; SentenceTransformers for MPNet/e5; TensorFlow/Keras for neural/CNN; PyTorch and Hugging Face for SEC-BERT; Optuna for search; MLflow for tracking. I cleaned and canonicalised text (lower-casing, whitespace/punctuation normalisation, typed placeholders for names, companies, dates, postcodes, numbers) and tested preprocessing choices empirically — replacing forward slashes reduced performance, so it was not retained.

**Result:** The code demonstrates a complete experimental path from semi-structured filings to repeatable model comparisons over millions of rows, and why a CPU-compatible scikit-learn model could beat GPU-heavy alternatives operationally. The workplace result — an R-first analyst interface with controlled Oracle outputs — and claims about wider coverage and adoption need internal measures.

**Reflection:** The correct language is contextual: data format, library maturity, user capability, platform, supportability. Python support is growing in HMRC's AWS lakehouse, so I would reassess the boundary over time, migrating only where benefit outweighs disruption.

### Technical detail / likely follow-up

- **R extraction layer** — mature XML/HTML tooling and the supported analyst workflow; keeping extraction in R reduced the support burden. Workplace claim: name the actual R packages and artefact before relying on it.
- **Python modelling layer** — the notebooks are stronger evidence for scientific analysis and comparison than for production deployment.
- **`reticulate`** — embeds Python in R and converts objects between languages, letting the R pipeline call the mature Python model without a rewrite. Risks: environment mismatch, conversion overhead, cross-language error handling — so pinned versions, a reproducible environment and an integration test are part of the solution.
- **SQL/Oracle/`dbplyr`** — durable relational outputs with mature access control; `dbplyr` lazily translates tidyverse verbs to SQL so filtering/joins execute in the database. Inspect generated SQL and query plans for expensive operations.
- **Cleaning and features** — typed placeholders (`hubble_name`, `hubble_date`, `hubble_number`) removed high-cardinality identifiers while preserving that a name/date/number was present; the same tested function must create training and production features to prevent skew.
- **Simulation boundary** — controlled computational experiments comparing model/hyperparameter scenarios are defensible experimental analysis, but not a physical or Monte Carlo simulation; state that boundary explicitly.
- **Commercial benefit** — not "using three languages" but combining their strengths to widen usable data, reduce manual preparation and deliver through a supportable workflow.

## Uses applied research and data modelling to design and refine the infrastructure and architectures to deliver secure, stable and scalable data products, including enterprise, private and public cloud resources and services

**Relevant KSBs:** K16, S1, S16, S19.

### STARR — refining Hubble's data-product architecture

**Situation:** Hubble processed high-volume, varied data (XML, iXBRL/XHTML, PDFs). The POSIT Data Analytics Platform suited development but not full-volume extraction, and outputs had to remain secure, stable and accessible to analysts.

**Task:** Define and refine an architecture that could burst for large extraction jobs, recover reliably and provide queryable outputs without overloading the shared platform.

**Action:** I investigated taxonomy change, Oracle width limits, workload shape and user needs. I proposed a long-form data model storing descriptions, contexts, concepts, predictions and metadata without rebuilding wide tables per taxonomy. I worked with platform engineers to establish On-Demand Compute — temporary EC2 capacity (large-core or GPU configurations when justified) spun up per job and shut down after — and used dynamic work allocation because document sizes varied and static splitting left cores idle. Apache Solr provided distributed text search and resilience; Oracle held structured outputs for querying. The DPIA, controlled-environment processing and rejection of unassured models supported security and governance.

**Result:** The architecture separated large jobs from the main platform, scaled compute only when needed, and provided fast search plus structured analyst access. The long-form model was taxonomy-independent, removed wide annual mappings and supported access to new submissions within days rather than the previous ~nine-month ingestion delay.

**Reflection:** Scalability includes operability, workload balance and governance, not just throughput. I would handle long-running-job token refresh centrally rather than sharing refreshed S3 credentials via a file. Longer term, Spark/EMR and Redshift or lakehouse-native storage may integrate better, subject to benchmarking and access-control assurance.

### STARR — controlling access to S3 data

**Situation:** Valuable data in S3 buckets should not have been available to every user of the connected analytics system.

**Task:** Define and supervise an access route for authorised users without opening the buckets broadly.

**Action:** I created a proxy and controlled access through a distribution list, keeping the cloud resource behind an organisationally controlled route limited to people with demonstrated need.

**Result:** Only the intended group could reach the data; the control met the security requirement, at some reliability and performance overhead from the extra layer.

**Reflection:** System-level access is a weaker substitute for direct user-level authorisation; a future lakehouse design should enforce per-user permissions at the data layer.

### STARR — challenging auto-scaling as the default database architecture

**Situation:** For a smaller project I initially built a database on native AWS auto-scaling services because they were easy to provision.

**Task:** Determine whether that architecture was technically and financially sustainable for the actual workload.

**Action:** I reviewed charges at low and zero usage and compared the managed design with fixed-price or self-hosted EC2 alternatives. Serverless billing was opaque and the baseline cost disproportionate for a small, intermittent workload — so I challenged the assumption that cloud-native auto-scaling is automatically the most efficient choice.

**Result:** Fixed-price or self-hosted capacity was more predictable for this project and could still be resized when demand genuinely grew — separating the technical ability to scale from whether the scaling model was commercially appropriate.

**Reflection:** A scalable service must also be financially sustainable; I would use measured workload profiles and total-cost comparisons before selecting serverless or auto-scaling infrastructure.

### Technical detail / likely follow-up

- **Resource types** — enterprise/private: POSIT DAP, Oracle, Solr, internal services; public cloud: AWS EC2/ODC and S3 within organisational accounts and governance. "Public cloud" describes the provider model, not public data.
- **Relational vs document search** — Oracle for governed structured data, SQL joins and access control; Solr for distributed free-text search with sharding and replication; each store used for the access pattern it suits.
- **Long-form model** — wide annual-taxonomy tables create structural change and width pressure; a long model (document, context, concept, description, value as rows) is taxonomy-independent and avoids annual remapping, at the cost of row count and occasional pivots.
- **Parallel processing** — extraction was embarrassingly parallel; static partitioning created stragglers from varied document sizes, dynamic scheduling improved utilisation; scaling stops helping when I/O, database writes, serial setup or credential management becomes the bottleneck (Amdahl's law in practice).
- **On-Demand Compute** — burst scale and cost control; risks include spin-up time, environment reproducibility, expiring credentials, orphaned resources and committing outputs before shutdown.
- **Security and stability** — DPIA, minimisation, controlled processing, model assurance, distribution-list access, controlled Oracle/S3 outputs; replicated Solr, tested code, durable outputs and workload isolation for stability.
- **Lake/lakehouse** — a lake stores mixed data cheaply but risks becoming a swamp without governance; a lakehouse adds transactions, schema enforcement and warehouse-style analytics — a future direction after benchmarking and permission assurance.
- **Financial feasibility** — compare total cost of ownership against measured concurrency, storage, idle time, support effort and growth, not headline compute prices.

## Explains how to design algorithms for accessing and analysing large amounts of data, including Application Programming Interfaces (API) to different databases and data sets

**Relevant KSBs:** K16, S19, S20.

### STARR — moving Hubble from files to scalable data access

**Situation:** The first Hubble workflow saved results to files, often exported as CSV/Excel; runs were slow, limited to selected populations, and repeated file movement made querying, joins and reuse difficult.

**Task:** Redesign access and processing so Hubble could handle large document populations without saturating the main platform, exposing results through stores analysts already used.

**Action:** I challenged the file-based workflow, investigated where time and manual effort were lost, and proposed document-level parallel processing with queryable shared storage. I worked with DevOps to provision ODC and used dynamic parallel scheduling so ~128 returns could be processed concurrently without the long tail caused by static batches of differently sized documents. Structured outputs went to Oracle rather than loose files; R's database interface and `dbplyr` provided the programmatic API layer, translating familiar tidyverse operations lazily into SQL executed close to the data. Where a SAS-writing package proved unreliable, I used a shared FSx route with Parquet for interoperable columnar output. Solr supported fast distributed text retrieval; the S3 proxy controlled object access. Throughout I considered data locality, batching, query pushdown, parallelism, storage format and serialisation cost.

**Result:** Large extraction jobs ran on isolated temporary capacity without degrading the shared platform, and database/Parquet outputs made results easier to query, join and reuse while R analysts kept familiar syntax.

**Reflection:** An efficient algorithm is part of a wider data-access design — parallelism only helps if work is balanced, credentials stay valid and output avoids new bottlenecks. I would benchmark natural vs numeric keys on actual Oracle/SAS workloads and add service interfaces only where they improve reuse.

### Technical detail / likely follow-up

- **What counts as the API** — a defined programmatic interface, not necessarily REST: R database drivers/DBI calls, `dbplyr`, Solr's query interface, the S3 proxy and Parquet-on-FSx storage interfaces. Name the exact driver/client from the artefact; do not describe a file copy as an API.
- **Lazy execution and pushdown** — `dbplyr` sends translated SQL only when results are collected, so filters, aggregation and joins execute near the data; the benefit depends on indexes and pushdown-friendly predicates.
- **Locality and batching** — moving computation to the data beats repeatedly transferring it; batching amortises overhead but oversize batches raise memory/retry cost; writes need transaction boundaries or idempotent keys for safe retries.
- **Dynamic parallelism** — a work queue with workers pulling the next document; measure throughput with utilisation, memory, network and write latency; the correct worker count is just before contention removes the benefit.
- **Parquet and FSx** — compressed columnar format reading only required columns with predicate pruning; far more efficient than CSV for analytical data; schema evolution and concurrent writers still need management.
- **Storage roles** — Oracle for structured joinable outputs; Solr for text search; S3 for objects; FSx for shared-file exchange; one store for everything would weaken at least one access pattern.
- **Natural vs surrogate keys** — natural keys are meaningful but long and potentially mutable; numeric surrogates are compact and stable but need lookups; benchmark representative workloads before changing the design.
- **LLM-generated Solr queries** — only with a controlled schema, syntactic validation, field/operator allow-lists, authorisation in the user's context, result limits, injection escaping, audit logging and preview/confirmation; the LLM must not bypass access controls.

## Distinction — Explains when they have challenged the norm through investigating and proposing a solution and the impact this had

**Relevant KSBs:** K7, S1, S20, S26.

### STARR — replacing annual wide-table ingestion with a taxonomy-independent model

**Situation:** The established approach relied on tagged iXBRL and wide annual Oracle tables. New taxonomies needed manual mapping, tables approached Oracle width limits, and ingestion could take over nine months — leaving little of HMRC's roughly one-year enquiry window for profiling and case action. Untagged values and free-text descriptions were largely unavailable at scale.

**Task:** Investigate whether a different data model could remove the annual ingestion bottleneck without making the result unusable for analysts.

**Action:** I challenged the assumption that the output needed to be a manually mapped wide table. I profiled the source, investigated taxonomy change and database limitations, proposed a long-form taxonomy-independent representation and consulted analysts to confirm they could work with long data before committing.

**Result:** New taxonomies could be ingested without annual structural remapping, and analysts could begin profiling submissions within days rather than ~nine months.

**Reflection:** Challenging the norm works when based on evidence and user validation, not novelty. The long format traded some human readability for adaptability and scale, so consulting analysts was essential. I would retain benchmarks, acceptance records and before/after timings.

### STARR — reusing tagged descriptions to classify untagged content

**Situation:** The norm was to rely on tagged data or manually maintained matching rules; inconsistent wording made population-level profiling of untagged descriptions impractical.

**Task:** Investigate whether untagged content could be mapped to the taxonomy without an impossibly large set of regular expressions.

**Action:** I challenged the assumption that tagged and untagged data had to be treated separately, proposing correctly tagged descriptions as supervised training labels. I researched and compared classical ML, embeddings, neural networks and transformers, selecting TF-IDF with LinearSVC on quality, speed, explainability, security, infrastructure and maintainability rather than raw score.

**Result:** The classifier provided a reusable way to categorise untagged descriptions, extended analytical coverage and reduced dependence on manual rules — giving analysts access to data they could not previously exploit at scale.

**Reflection:** The novel element was recognising that an existing labelled subset could supervise a previously unusable unlabelled subset. I would retain the decision matrix, experiment record and user evidence so this impact is distinguishable from the long-format ingestion change.

### STARR — extracting contextual features before a calculation issue emerged

**Situation:** Hubble's original requirement focused on untagged figures, but iXBRL documents also contain headings, table names and positional context, and future needs were unknown.

**Task:** Decide whether to meet only the narrow requirement or design a more general extraction preserving useful context.

**Action:** I challenged the narrow scope and added general support for contextual features in advance. Later, a material issue involving very large incorrect figures produced by software companies required analysts to recreate calculations; tagged-only data was insufficient (relevant figures could be mistagged or untagged) and the volume was too large for manual checking. I used Hubble's untagged values and contextual features to support the reconstruction.

**Result:** Hubble could extract the needed information without a new development cycle, allowing calculations to be checked at a scale manual work and tagged-only data could not support.

**Reflection:** Designing for likely reuse can create significant value but must be balanced against unnecessary collection. I would document the design decision, the exact features used and the verified outcome, avoiding sensitive operational detail.

---

# Theme 2: Professional practice in a commercial environment

**Theme KSBs:** K8, K10, S6, S8, S14, S23, S28, B1, B4, B7.

**Distinction integration:** pass answers also consider the wider public-sector/social context and current AI trends where natural; the standalone distinction answers remain the fullest versions.

## Explains how they have developed their professional working practices and leadership techniques in regard to AI and data science and how this has improved organisational practice

**Relevant KSBs:** K10, S6, B1, B4.

### STARR — leading the growth of the Data Analytics Platform

**Situation:** The Data Analytics Platform began with one user and needed to support growing numbers of analysts using R, Python, data engineering and ML.

**Task:** As platform owner, keep the service useful and funded, expand capability, give technical direction and help users develop skills.

**Action:** I worked with budget holders to justify licence growth, arranged upgrades and new functionality, collaborated with engineers on On-Demand Compute and GPU access, supported users directly, mentored project teams and ran discussions about ML opportunities. I created and maintained practical wiki guidance on virtual environments, secure data access, reproducibility and platform use, tailoring communication for analysts, engineers, suppliers and decision-makers.

**Result:** DAP grew from one user to more than 150 and supported teams building analytical and ML tools; users developed tools and integrations themselves, extending capability beyond my own delivery.

**Reflection:** My leadership developed from answering individual questions to shaping a service and the practices around it. I would strengthen it with formal skills reviews, succession planning and measured mentoring outcomes.

### STARR — taking ownership of Hubble's technical direction

**Situation:** No off-the-shelf solution could categorise untagged iXBRL descriptions, and initial simple NLP approaches performed poorly; Hubble spanned extraction, cleaning, modelling, validation and delivery.

**Task:** Take personal responsibility for the technical direction, overcome infrastructure and modelling problems and prove the business problem was tractable.

**Action:** I investigated alternative architectures and model families, rebuilt training datasets, fine-tuned BERT and tested classical and neural approaches. When GPU and throughput constraints emerged, I adapted the workflow to the available infrastructure and compared candidates against operational as well as model-quality criteria. I managed the lifecycle end to end and introduced lightweight project controls as contributors grew.

**Result:** A validated classification proof of concept that established the business case for ML in data profiling; the wider Hubble product extracted substantially more data than the previous approach and supported analysts identifying tax risk.

**Reflection:** Ownership meant accountability for the complete outcome, including limitations and deployment fit, not just a model. I would make the prototype-versus-production status and final performance evidence more explicit in the project record.

## Justifies their choice of techniques, explaining the risks and benefits and offers an alternative to technical and non-technical audiences

**Relevant KSBs:** K8, S6, S8, S28.

### STARR — communicating the LinearSVC decision

**Situation:** Stakeholders had different preferences: accuracy as the headline measure, Random Forest suggestions from analysts, and interest in transformers because they were current and powerful.

**Task:** Make an impartial recommendation, explain benefits and risks, provide credible alternatives, and communicate appropriately to technical and non-technical audiences.

**Action:** I consulted stakeholders and converted their concerns into a comparison covering macro-F1 and per-class reliability, accuracy, speed, compute cost, explainability, security/provenance, maintainability and deployment fit. The comparison narrowed to LinearSVC, CNN and SEC-BERT on one holdout plus rubric-scored operational criteria: SEC-BERT had the highest macro-F1 point estimate (0.823 vs 0.808 and 0.800) but overlapping intervals, while LinearSVC trained in minutes rather than the better part of an hour, ran inference orders of magnitude faster and was ~8 MB rather than ~1.8 GB, with stronger deployment, maintenance and dependency-risk ratings. To technical audiences I explained sparse TF-IDF vectors, L1 regularisation, imbalance, cross-validation, bootstrap uncertainty and CPU/GPU constraints; to non-technical audiences I described macro-F1 as reliability across rare as well as common concepts, CPU execution as lower cost, and coefficients as understandable evidence of which phrases influenced a result. I offered SEC-BERT or another assured domain model as the alternative if a remapped, grouped evaluation established a worthwhile gain and future infrastructure could support it. I would not present the current numeric decision score unqualified — the matrix has a known field-name defect and untested weights — and explaining that defect is itself part of impartial, evidence-led decision making.

**Result:** TF-IDF with LinearSVC was the operational recommendation: competitive quality, fast CPU-compatible processing, clearer explanations, lower lifecycle risk. A named meeting, decision paper or approval is still needed to prove how stakeholders received it.

**Reflection:** Communicating alternatives strengthens a recommendation by showing the choice is deliberate. I would agree metric definitions and risk tolerances even earlier and keep a short decision record with both a technical comparison and a plain-English version.

## Explains how they share and disseminate AI and data science practices across organisations to improve industry practice

**Relevant KSBs:** S23, B7.

### STARR — sharing practice internally through DAP guidance and mentoring

**Situation:** DAP users came from different teams with varying experience of environments, data access, reproducibility, testing and ML limitations.

**Task:** Make safe, effective practice reusable across the organisation rather than repeatedly solving the same problems for individuals.

**Action:** I shared guidance through Teams channels, direct mentoring, demonstrations and a maintained wiki, covering virtual environments, secure data access, reproducibility, testing, model limitations, human-in-the-loop use and proportionate model selection. I documented Hubble with a full README and detailed design notes so contributors could understand how to run it and why key choices were made.

**Result:** Users gained reusable guidance; Hubble contributors adopted more consistent, reproducible workflows; documentation reduced reliance on individual knowledge.

**Reflection:** Internal dissemination requires maintenance, feedback and examples, not just publishing a page. I would track wiki use, mentoring outcomes and reuse by other teams.

### STARR — sharing grounded-LLM practice through Graffiti

**Situation:** The wider iXBRL community was exploring LLMs, but passing a complete noisy HTML filing to a model produced poor results and could encourage overconfidence in ungrounded answers.

**Task:** Demonstrate and share a safer, more effective pattern without exposing HMRC data or presenting an experiment as settled best practice.

**Action:** I built Graffiti on public filings: extract and structure the iXBRL first, select relevant context, and supply that context with the user's question to the LLM. I shared developments with leading iXBRL experts, explaining both the benefit of grounding and the limitations — hallucination, prompt injection, data leakage, opacity, cost, over-automation.

**Result:** Graffiti provided a practical external demonstration of grounded LLM analysis over iXBRL and a vehicle for discussing responsible use with the professional community.

**Reflection:** External dissemination should distinguish demonstrated behaviour from claims of industry impact. I would retain details of audiences, feedback, reach and any concrete reuse.

## Distinction — Critically analyses the wider social context and current issues and trends, applying the findings with justification and shares these with the wider community

**Relevant KSBs:** K8, S23, B7.

### STARR — challenging overly broad internal AI guidance

**Situation:** New organisational guidance, introduced in response to generative-AI risk, treated conventional ML as having the same risk profile and restricted work to LLM-oriented platforms that did not support ordinary ML development.

**Task:** Interpret the guidance in its wider public-sector context, protect the organisation from genuine AI risk, and avoid disproportionate restrictions blocking valuable lower-risk work.

**Action:** I compared the risks of conventional supervised ML with those of generative models (hallucination, prompt injection, ungrounded generation, data leakage, over-automation), tested the guidance against practical workflows, showed specifically where it was unimplementable or costly without addressing the actual risks, and supplied detailed usable amendments rather than only objecting.

**Result:** The guidance was changed in line with my comments, giving a more proportionate basis for governing different types of AI work.

**Reflection:** Responsible practice requires the confidence to challenge policy with evidence. Proportional governance protects public trust better than treating every technique as identical, and guidance should keep being reviewed as technology and regulation change.

### STARR — applying and sharing a grounded-LLM pattern through Graffiti

**Situation:** Foundation models created strong interest in natural-language analysis of filings. Industry evidence suggested whole-document prompting performed poorly while structured iXBRL context improved grounding; in a public-sector setting an over-trusted answer could damage confidence.

**Task:** Critically assess the trend, apply it where justified, and share a practical pattern with the wider iXBRL community.

**Action:** I weighed the accessibility and productivity benefits of LLMs against hallucination, prompt injection, data leakage, opacity, bias, cost and over-automation. I built Graffiti on public filings, extracting the iXBRL first and supplying structured context with the query; kept the tool analytical rather than an automated decision-maker; made human review explicit; and discussed the pattern and its limitations with iXBRL experts.

**Result:** Graffiti demonstrated a grounded-LLM approach to the professional community without exposing HMRC data or suggesting model output should replace professional judgement.

**Reflection:** The social licence for AI depends on transparency, accountability and accessible challenge, not just capability. As MCP and tool use expand I would keep external demonstrations on public or synthetic data and make the model's limits visible.

## Explains how they have made independent impartial decisions respecting the opinions and views of others in complex, unpredictable and changing circumstances to benefit the business

**Relevant KSBs:** S8, S28, B4.

### STARR — balancing licence, compute and funding priorities for DAP

**Situation:** As DAP owner I received competing demands: users needing licences and GPU capability, engineers with platform constraints, budget holders needing a defensible case.

**Task:** Respect those perspectives and provide capacity where it benefited the organisation without committing to unaffordable permanent infrastructure.

**Action:** I gathered evidence of demand and the work additional capacity would enable, justified licence growth with budget holders, and worked with engineers to provide On-Demand Compute — including GPU instances started for specific work and shut down afterwards.

**Result:** DAP grew beyond 250 users with appropriate licences, and ODC provided large CPU/GPU capacity cost-effectively when projects needed it.

**Reflection:** The solution came from separating the underlying need — occasional high-capacity compute — from the requested implementation of permanent capacity. I would keep short decision records showing demand, options, cost and outcome.

### STARR — choosing an existing database route over a new S3 path

**Situation:** Some users wanted data written directly to S3 for POSIT Connect access, while an existing controlled database route could satisfy much of the need.

**Task:** Decide impartially between user convenience and the security, support and maintenance implications of another data path.

**Action:** I clarified the outcome users needed, consulted stakeholders, compared the routes, explained the additional access-control and support burden of the new path and recommended the existing route where it met the requirement.

**Result:** Avoiding an unnecessary new path limited security, maintenance and delivery overhead while users still got the data they required.

**Reflection:** Respecting a proposal does not mean accepting its implementation; impartial decisions separate the user's need from their preferred solution and make the trade-off visible.

### STARR — making an impartial Hubble model decision

**Situation:** Stakeholders held different views: accuracy as headline metric, Random Forest suggestions, enthusiasm for transformers.

**Task:** Choose the model that best benefited the business while ensuring those views were heard and tested fairly.

**Action:** I gathered the requested models and metrics, explained why imbalance made macro-F1 more informative than accuracy, agreed comparison criteria before final selection, tested candidates against quality, speed, explainability, security, maintainability, infrastructure and cost, and documented the trade-offs.

**Result:** TF-IDF with LinearSVC became the evidence-led recommendation rather than the fashionable choice — competitive macro-F1, much faster training, coefficient-level explanations, lower operational risk. The workplace decision/approval still needs to be named.

**Reflection:** Impartiality is easier to demonstrate when criteria are agreed before results are known; I would make the decision record routine so stakeholders can challenge it if evidence changes.

## Explains how they have worked with software engineers to ensure suitable testing and documentation processes are implemented in line with organisational requirements

**Relevant KSBs:** S14, B1.

### STARR — engineering controls for Hubble

**Situation:** Hubble became a complex tool with varied real-world documents, several contributors and many users; a small parsing or preprocessing change could silently affect extraction, model inputs or analyst outputs.

**Task:** Establish, with engineers and contributors, proportionate testing, change control and documentation supporting safe delivery without a heavyweight process.

**Action:** In the workplace repository I established that changes require tests — if a function had no test, one was written before modifying it, and the suite had to pass before merging to main. Unit tests covered individual functions; integration-style cases covered complex documents, because input variation cannot be covered by isolated tests alone. I used GitLab issues, templates, epics and milestones for traceability and a lightweight Kanban board for planning; wrote a full README for the multi-system setup; and maintained Markdown documentation covering architecture, workflows, limitations and the reasons behind key decisions. I collaborated with platform/DevOps engineers on ODC, data paths and environment constraints, turning operational findings into tests or documentation. In a public-sector context, undocumented behaviour or an unrepeatable result can undermine trust even when a metric looks strong — reproducibility and traceability were treated as requirements, not extras. `Code/` contains research notebooks only, so the internal test suite, CI gates, README and reviews need workplace artefacts.

**Result:** New users could set up the project from the README, contributors could change tested functions with confidence, and issues/milestones gave an audit trail from requirement to implementation — to be evidenced with a test report/CI result, README, representative merge request and an engineer witness.

**Reflection:** Up-front tests and documentation reduce future change cost and dependency on individual knowledge, and make AI work more open to review. The largest remaining risk is source-document diversity, so I would expand a versioned representative corpus, automate integration tests in the merge pipeline and link requirements, tests and release notes explicitly.

---

# Theme 3: Awareness of the current and future impact of AI and data science for industry and society

**Theme KSBs:** K11, K17, K21.

## Describes how the potential roles and impact of AI and data science could affect own organisation, industry and society

**Relevant KSBs:** K11.

### STARR — Hubble's organisational and societal impact

**Situation:** Incomplete tagging made large parts of company accounts and tax computations difficult to analyse systematically; manual interpretation did not scale.

**Task:** Combine data engineering, data science and AI so analysts could exploit more of the information, while considering the wider impact of this kind of automation.

**Action:** I used data engineering to extract, clean, canonicalise and structure iXBRL; data science to analyse quality, balance and performance; and supervised NLP to categorise descriptions, delivering results to controlled stores so the model supported analyst judgement. I considered similar methods beyond HMRC — fraud detection, medical imaging, demand forecasting — and the societal risks: over-trusted outputs, opaque decisions, privacy loss, under-representation of rare classes, deskilling and staff resistance.

**Result:** The code demonstrates the **potential** to reduce repetitive grouping by mapping varied descriptions to consistent concepts; the workplace account is that Hubble expanded analytical coverage and supported tax-risk profiling (needs an internal measure or witness). At industry level the notebooks are a reproducible example, not proof practice changed; at societal level better evidence may support fairer, more efficient revenue work, but Hubble does not make tax decisions or directly prove increased public funding.

**Reflection:** A narrow technical pipeline can have material social consequences. Positive impact depends on human oversight, transparent limitations, secure processing and monitoring; the defensible role of AI here is augmenting analysts, not replacing them.

## Explains how they have assessed and addressed the potential business impact of ethical issues relating to AI and data science, the way procedures and methods are selected, and the unintended consequences to the business when they are applied

**Relevant KSBs:** K11, K17; cross-reference S12 and B3 in Theme 4.

### STARR — ethical impact assessment for Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information; a classifier used in a tax-risk context could create privacy, bias, transparency and accountability risks if its categories were treated as fact or used out of purpose.

**Task:** Assess those ethical issues before and during development, choose proportionate procedures and methods, and reduce the likelihood of unintended model behaviour causing legal, operational or reputational harm.

**Action:** I completed a DPIA before work began and reviewed it as the design evolved. In the pipeline I canonicalised names, companies, dates, postcodes and numbers so high-cardinality identifiers were not the trained feature — feature minimisation, not anonymisation, since the source description is retained and access/retention/purpose controls remain necessary. Processing stayed inside controlled environments. I assessed imbalance and representation through frequency distributions, macro-F1, per-class measures, confusion matrices and residual examples; tested balanced class weights, biased sampling and oversampling (the final LinearSVC used balanced weights; several neural/transformer weighting approaches made performance worse). Demographic fairness (parity, equalised odds) remains proposed, not completed. I selected an explainable pipeline partly so coefficients, LIME and SHAP could expose feature influence. Acceptance testing found an unintended consequence — blank descriptions classified from surrounding context — so I stopped predictions where the description was absent, and I simplified a confusing top-five dashboard display after usability feedback (both user changes need internal evidence).

**Result:** The code supports the narrower conclusions: identity-like tokens removed from the modelling feature, minority-class and robustness failures made visible, and a simpler model enabling direct inspection. Workplace controls kept the model as decision support rather than an automated determinant — name the DPIA, human-oversight instruction and user evidence to substantiate this.

**Reflection:** Ethical assessment must cover the whole sociotechnical process: data, labels, metrics, model, interface, users and downstream decisions. A technically explainable model can still be misused, so future improvements include monitoring, enforced workflow controls, periodic DPIA review and clearer warnings for low-reliability classes.

## Describes how they have applied solutions, demonstrated awareness and explained the changes and trends that have led to enhancement of working practices within their organisation and other members of the team

**Relevant KSBs:** K17, K21.

### STARR — testing modern model families before selecting a simpler Hubble model

**Situation:** Transformers, domain BERT models, embeddings and neural networks were prominent developments, and stakeholders could reasonably expect Hubble to consider them.

**Task:** Test whether those developments improved the problem enough to justify their infrastructure, assurance and maintenance costs.

**Action:** I followed research literature, technical documentation and practical communities, then implemented comparisons across classical ML, MPNet/e5 embeddings, CNN/neural architectures and SEC-BERT on fixed data flags, assessing macro-F1 and per-class performance alongside runtime, CPU/GPU needs, provenance, explainability and deployment fit. The evidence was concrete: MPNet's advantage over TF-IDF was small-to-negligible across runs; SEC-BERT's higher point estimate came with overlapping intervals; robustness categories exposed different failure modes. I explained the evidence through project documents, demonstrations and stakeholder discussions.

**Result:** Testing showed the simpler TF-IDF/LinearSVC pipeline was the stronger operational recommendation. The code proves the recommendation was researched; an internal approval or user measure is still needed to show deployed benefit.

**Reflection:** Awareness of a trend does not require adopting it — applying the trend meant testing it credibly and letting the result improve the team's model-selection practice.

### STARR — applying the grounded-LLM trend in Graffiti

**Situation:** iXBRL International material showed whole-document LLM prompting performed poorly while structured extraction gave more relevant context.

**Task:** Apply that finding in a usable tool and explain both the opportunity and the risks to colleagues and the wider community.

**Action:** I built Graffiti to extract the iXBRL, select relevant structured content and combine it with the user's query, and explained hallucination, prompt injection, data leakage, cost, governance and the need for human review through demonstrations and discussions.

**Result:** Graffiti provided a clearer route for interrogating public filings and demonstrated how grounding improves LLM analysis without treating output as an automated decision.

**Reflection:** I would monitor LLM tool use and MCP, applying new capability only after controlled testing and explicit assessment of what systems and data the model could access.

### STARR — converting current practice into reusable team workflows

**Situation:** Colleagues needed practical ways to adopt changing ML practice consistently, not occasional updates about new tools.

**Task:** Turn relevant developments into working practices improving reproducibility, review and appropriate use across the team.

**Action:** I promoted experiment tracking, repeatable environments, tests, per-class evaluation, documented limitations and human-in-the-loop use through Teams, mentoring, README/design documents and the DAP wiki.

**Result:** Team members had reusable guidance and a stronger basis for matching model complexity to evidence, governance and business need.

**Reflection:** The next step is measuring the effect on speed, quality and reproducibility rather than assuming published guidance proves enhancement.

## Explains the impact, consequences and risks of non-compliance to the business

**Relevant KSBs:** K11, K17; cross-reference S12 and B3 in Theme 4.

### STARR — designing to prevent non-compliance in Hubble

**Situation:** Hubble used sensitive data in a regulated public-sector environment; non-compliance could arise through excessive collection, personal-data leakage, weak access controls, unassured technology, opaque model use or decisions without appropriate human review.

**Task:** Understand the impact of those failures and build preventive controls into the pipeline so the product remained legally, ethically and organisationally defensible.

**Action:** I used the DPIA to identify data-protection and governance risks; minimised and canonicalised personal information; kept processing in controlled environments; restricted S3 and Oracle access; considered provenance in model selection; documented lineage and design choices; and retained human review. I treated compliance as an operational requirement during model and infrastructure selection, not a final approval step, and communicated that classifications were suggestions, not the defining factor in action.

**Result:** The work avoided any known privacy or security incident and proceeded with proportionate controls, reducing the likelihood of regulatory investigation, legal challenge, invalid decisions, operational rollback, financial loss, reputational damage and loss of public trust.

**Reflection:** For a public body the largest consequence may be loss of legitimacy and trust, even without a financial penalty. Compliance evidence must remain current as data, users, models and infrastructure change; I would schedule formal DPIA/control reviews linked to releases.

### Technical detail / likely follow-up

- **Data-protection non-compliance** — processing without a lawful purpose, excessive collection, over-retention, inaccuracy, unauthorised access, inability to demonstrate accountability → investigation, remediation, processing restrictions, legal challenge, invalid results, lost trust. Verify any penalty figure against current official guidance rather than quoting from memory.
- **Automated-decision risk** — UK GDPR Article 22 restricts solely automated decisions with legal or similarly significant effects; Hubble's classifications were advisory inputs. A nominal human-in-the-loop is insufficient if the person lacks time, information or authority to disagree.
- **Operational impact** — a control failure can force the pipeline to be stopped, outputs quarantined, decisions reviewed, data corrected, code rolled back and users notified — often costing more than lifecycle governance would have.
- **Financial impact** — remediation, incident response, legal support, duplicated analysis and delayed outcomes can exceed a formal penalty; uncontrolled cloud resources and unmonitored models add ongoing cost.
- **Reputational and social impact** — unfair, opaque or insecure AI use harms affected people, reduces willingness to use later tools and increases scrutiny across unrelated programmes.
- **Security and supply chain** — weak access control, vulnerable/unmaintained packages and models, prompt injection, adversarial inputs, data poisoning; controls: approved sources, dependency scanning, pinned versions, least privilege, adversarial testing, audit logs, an incident route.
- **Control lifecycle** — identify requirements and owners; document risks (DPIA); implement minimisation, access, assurance, human oversight; test; approve; monitor; review whenever data, purpose, model, users or infrastructure changes, with evidence linked to the same version of data, code and model.

---

# Theme 4: Development of suitable AI and data science solutions with consideration for ethical, legal, regulatory, governance and accessibility issues

**Theme KSBs:** K29, S12, B3.

## Evaluates the regulatory, ethical and legal requirements that affect implementation of solutions, including the need for accessibility for all users and diversity of user needs

**Relevant KSBs:** K29, S12, B3.

### STARR — applying governance and privacy controls to Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information; its classifications could create privacy, fairness, transparency and accountability risks if used out of purpose.

**Task:** Evaluate legal, ethical, regulatory and governance requirements across the end-to-end data process and make the pipeline defensible in a public-sector environment.

**Action:** I completed a DPIA before development and reviewed controls as the design evolved. For the modelling feature I replaced unnecessary names, companies, dates, postcodes and numbers with typed placeholders before training — reducing identity signal reaching the model, while the retained source still needs access, retention and lawful-purpose governance. HMRC data stayed in controlled environments, outputs used controlled stores and model provenance formed part of selection. I chose an established, explainable TF-IDF/LinearSVC pipeline and documented classifications as advisory with human review.

**Result:** The design reduced unnecessary personal-data signal in the model feature and made model use easier to explain and challenge. The DPIA, retention/access controls and controlled-environment evidence are needed to show the identifiable source data itself was governed.

**Reflection:** Governance is a lifecycle activity, not a one-off approval; I would link DPIA and control reviews to material changes in data, purpose, model, users or infrastructure.

### STARR — protecting personal data in a Companies House modelling pipeline

**Situation:** In a pipeline using Companies House filings, otherwise public documents could still contain director names or personal information.

**Task:** Ensure model development did not unnecessarily retain personal information or create leakage risk.

**Action:** I applied privacy by design during cleaning, replacing names, company names, dates, postcodes and numbers with typed placeholders so they were not raw model features. The notebooks prove that transformation, though their saved data retains the original description and shows a local demonstration rather than the controlled AWS/Oracle route — if that route is a separate workplace pipeline, its architecture and access-control artefacts are needed and the separation should be stated.

**Result:** The modelling workflow could be demonstrated without raw identifiers as training features; controlled access to retained source data is a separate workplace result.

**Reflection:** Public availability does not remove the need for data minimisation. I would still document lawful purpose, retention, access roles and dependency/model-licence checks for the specific implementation.

### STARR — reviewing an existing product with a WCAG specialist

**Situation:** On another project, an existing product lacked evidence it met the accessibility needs of all users.

**Task:** Identify the gaps with appropriate expertise and establish a practical remediation route.

**Action:** I engaged a WCAG specialist, reviewed the product with them, agreed a remediation plan and began implementing fixes.

**Result:** The project gained an expert-informed accessibility remediation plan and started moving accessibility work into the delivery process.

**Reflection:** Retrofitting accessibility is harder than designing it in. I would introduce an accessibility checklist, acceptance criteria and representative user testing during discovery, and retain the WCAG version, findings and retest evidence.

### STARR — providing an accessible installation route for Graffiti

**Situation:** Graffiti was normally installed by dragging a bookmarklet to the bookmarks bar — an interaction some users cannot perform.

**Task:** Provide another way to install the tool without that drag-and-drop action.

**Action:** I wrote alternative installation guidance achieving the same outcome without dragging.

**Result:** Users who could not use the default interaction had an alternative route.

**Reflection:** Accessibility includes setup instructions and interaction methods, not only the main UI. I would validate the alternative with affected users and include keyboard and assistive-technology checks in future releases.

### STARR — reducing cognitive confusion in the Hubble dashboard

**Situation:** The dashboard showed the top five candidate concepts and raw scores; user testing showed weak alternatives and unfamiliar scores confused non-specialist users.

**Task:** Make the output clearer for users with different technical and domain knowledge while avoiding false confidence in the model.

**Action:** I reviewed the feedback, limited the display to more confident matches and added explanatory wording about what the scores meant and how predictions should be used.

**Result:** The dashboard presented less distracting information and clearer context for interpreting model suggestions.

**Reflection:** Accessibility includes cognitive clarity and language matched to the audience. I would test the revised presentation with representative analysts, SMEs and accessibility users and retain the evidence.

### Technical detail / likely follow-up

- **UK GDPR principles** — lawfulness/fairness/transparency, purpose limitation, minimisation, accuracy, storage limitation, integrity and confidentiality, accountability. Hubble: defined analytical purpose; identifiers removed from model signal; controlled processing and outputs; DPIA, decision record, lineage and tests for accountability.
- **Lawful basis** — consent, contract, legal obligation, vital interests, public task, legitimate interests. The correct basis and any statutory power must come from the approved DPIA, not be guessed. Public Companies House data is still personal data where a person is identifiable.
- **Special-category and equality considerations** — special-category data (ethnicity, politics, religion, union membership, genetics, biometrics, health, sex life, orientation) and Equality Act protected characteristics; even unintended proxies and uneven representation can create differential outcomes, so the data and error profile need review.
- **DPIA** — required where processing is likely high risk; records nature/scope/context/purpose, necessity, risks, controls, residual risk, consultation and approval; begins before processing and is revisited on material change.
- **Article 22 and human oversight** — restricts solely automated significant decisions; Hubble outputs remained advisory. Meaningful oversight requires users who understand limitations, see evidence, recognise low-reliability classes and have authority to reject the output.
- **Ethical evaluation** — examine label quality, representation, imbalance, proxies, error distribution, explainability, uncertainty, function creep and the downstream decision — technical fairness metrics do not replace assessing people, process and consequences.
- **Security** — least privilege, controlled networks/storage, encryption, secrets management, audit logging, approved dependencies, patching, incident response. Canonicalisation reduced exposure in features but did not anonymise the source.
- **Legal and commercial checks** — dependency and model licences, IP, supplier contracts, data-sharing conditions, processing roles, retention duties, support status, right to audit. A technically strong niche model may be unsuitable if provenance or maintenance cannot be assured.
- **Accessibility** — apply the organisation's WCAG version/level: keyboard operation, visible focus, semantic structure, text alternatives, labels, contrast, zoom/reflow, no colour-only signals. Combine automated checks with keyboard, screen-reader and representative-user testing.
- **Cognitive and procedural accessibility** — raw scores, jargon and many weak alternatives create barriers even when automated checks pass; use plain language, explain uncertainty, and provide equivalent instructions where a workflow assumes a mouse gesture.
- **Diversity of user needs** — analysts need examples and per-class reliability; SMEs need taxonomy meaning and edge cases; managers need value/cost/risk; DevOps need dependencies and monitoring; governance reviewers need DPIA, lineage and auditability. Representative discovery and usability testing turn these into acceptance criteria.

---

# Theme 5: Continuous professional development

**Theme KSBs:** B5, B8.

## Analyses how they take responsibility for their own and their team's currency of knowledge and skills, and their professional and personal growth and development

**Relevant KSBs:** B5, B8.

### STARR — taking responsibility for my own structured development

**Situation:** The apprenticeship provided more material than could be absorbed passively, while AI, NLP, cloud platforms and governance continued to change quickly.

**Task:** Prioritise my learning, develop genuine understanding and maintain the standard alongside workplace responsibilities.

**Action:** I completed the structured QA material, made detailed notes and selected relevant recommended books and academic sources for deeper study. Where I did not understand a point I investigated it rather than leaving a superficial explanation, prioritising sources by relevance and credibility.

**Result:** My structured study contributed to an assessment result of 80% and strengthened the technical foundation I applied at work.

**Reflection:** CPD requires deliberate prioritisation, curiosity and evidence of understanding. I would keep a dated development log linking each important source to the knowledge or decision it changed.

### STARR — using current research to improve Hubble model selection

**Situation:** Hubble needed a credible text-classification approach while transformers, domain BERT models, embeddings and experimentation tools were developing rapidly.

**Task:** Keep my technical knowledge current enough to test those approaches properly, avoiding both obsolete methods and fashion.

**Action:** I used transformer literature, practical sources, Hugging Face documentation, relevant GitHub repositories and documentation for scikit-learn, TensorFlow/Keras, Optuna and MLflow, applying the learning by testing TF-IDF, LinearSVC, embeddings, BERT/SEC-BERT and CNN/MLP/RNN models and improving experiment comparison and reproducibility.

**Result:** The learning directly informed the evidence-led selection of TF-IDF with LinearSVC and gave the model comparison greater technical credibility.

**Reflection:** Staying current is useful when it changes a real decision — here, testing modern methods strengthened the justification for a simpler operational choice.

### STARR — converting personal learning into team capability

**Situation:** DAP users needed current practical guidance, and useful knowledge has limited organisational value if it stays with one person.

**Task:** Transfer relevant learning into reusable team practice and support colleagues' development.

**Action:** I recorded learning in project documentation, setup scripts and the DAP wiki, demonstrated approaches and mentored teams — covering virtual environments, reproducibility, testing, secure data access, human oversight, model limitations and technique selection.

**Result:** Team members gained guidance and support to build their own tools, while DAP grew from one user to more than 150.

**Reflection:** Team development needs stronger evidence than publication counts. I would formalise skills reviews, agree learning goals, check progress and gather feedback on what colleagues can do independently afterwards.

## Explains how they selected and applied the most effective/appropriate AI and data science techniques to solve a complex business problem in line with organisational and regulatory requirements

**Relevant KSBs:** B5, B8; cross-reference S26.

### STARR — evidence-led selection for a regulated Hubble deployment recommendation

**Situation:** Hubble needed to map inconsistent, often untagged account descriptions to standard taxonomy concepts. The data was large, imbalanced and domain-specific (826 engineered labels, of which the 141 with sufficient examples were modelled), and HMRC required secure, explainable, supportable processing.

**Task:** Choose and apply a technique that solved the business problem at scale while meeting organisational policy, data-protection, security, infrastructure, cost and maintenance requirements.

**Action:** I defined the problem and success criteria before recommending a model. The pipeline extracted and cleaned millions of rows, canonicalised high-cardinality identifiers and created fixed seeded splits. I established baselines, then evaluated classical models, MPNet/e5 embeddings, SEC-BERT and CNN/neural alternatives using macro-F1, per-class measures, confusion/residual analysis, stratified CV and bootstrap intervals — accuracy alone hid minority-class performance — alongside training/inference time, model size, CPU/GPU needs, explainability, provenance, maintainability and deployment complexity. On the common holdout LinearSVC recorded 0.800 macro-F1 against CNN 0.808 and SEC-BERT 0.823 with overlapping intervals; the label-space remap for the neural/transformer heads remains outstanding before the cross-family difference is treated as final. In the workplace pipeline I integrated Python ML into the supported R workflow with controlled ODC/Oracle delivery (internal artefacts needed for the DPIA, integration and user changes).

**Result:** The evidence supports an operational recommendation for TF-IDF plus LinearSVC: CPU-compatible, directly inspectable and free of SEC-BERT's lifecycle burden for an uncertain point-estimate gain. Until workplace status is confirmed, call this a validated comparison and deployment recommendation, then separately describe any internal production outcome with evidence.

**Reflection:** The most effective technique is the one that meets the complete business and regulatory need, not the highest laboratory score. My CPD let me test modern methods credibly while judgement favoured the simpler recommendation. Before formal deployment evidence I would fix the decision-matrix key, group splits by filing, add time/taxonomy validation, define acceptance thresholds, verify test/production parity and implement monitored human oversight.

---

# Technical answer bank

For "what does that mean?", "why did you use it?" and "strengths and weaknesses?" follow-ups. Give a plain-English explanation first, then the formula. (Broader exam-style material — regression metrics, association rules, clustering algorithm details — lives in the technical test notes, not here.)

## Learning paradigms and data quality

- **Supervised** — learns from labelled examples; Hubble uses tagged iXBRL concepts as labels to predict concepts for untagged descriptions.
- **Unsupervised** — structure without labels (clustering, anomaly detection); useful for EDA and spotting unusual documents. Silhouette score (−1 to 1) measures cluster cohesion/separation.
- **Semi-supervised** — small labelled + large unlabelled set (self-training, label propagation, pseudo-labelling); useful when labels are expensive or limited.
- **Self-supervised** — the model generates its own targets from raw data (masked words); underpins LLMs and BERT pre-training.
- **Reinforcement** — an agent learns a policy from rewards through interaction; robotics, game AI, control — not fixed labelled classification.
- **Data mining** — discovering patterns, relationships and exceptions in large datasets; in Hubble: frequency, ambiguity, distribution and error-pattern analysis.
- **Data quality dimensions** — accuracy, completeness, consistency, validity, timeliness, uniqueness, lineage, relevance. Hubble: canonicalisation improved consistency; identifier removal improved relevance and privacy; source/taxonomy tracking supports lineage; per-class checks reveal where output is not reliable.

## Overfitting, validation and imbalance

- **Overfitting** — learns training noise: high train, low test performance; mitigate with regularisation, simpler models, more representative data, dropout, CV. **Underfitting** — too simple: poor on both; mitigate with better features, less regularisation, more capacity. The **bias–variance trade-off** frames total error as bias² + variance + noise.
- **Cross-validation** — K folds, train on K−1, validate on the rest, average; **stratified** CV keeps class proportions per fold — essential for imbalanced data. Data-derived preprocessing must be fitted inside each training fold to avoid leakage.
- **Imbalance handling** — accuracy misleads (always-majority can score 99%); use class weighting (weight ≈ N/(K·n_k)), oversampling/SMOTE, undersampling, and macro-F1/per-class metrics rather than raw accuracy. Hubble's final model used balanced class weights; several weighting/oversampling variants made neural/transformer performance worse.

## Classification metrics

Per class one-versus-rest: TP (predicted, correct), FP (predicted, wrong — Type I), FN (missed — Type II), TN (correctly rejected).

- **Accuracy** = (TP+TN)/total — misleading under imbalance; monitored but not the selection metric.
- **Precision** = TP/(TP+FP) — trustworthiness of a predicted class; low precision means over-prediction and more careful review.
- **Recall** = TP/(TP+FN) — coverage of real positives; matters when missing a concept is costly.
- **F1** = 2PR/(P+R) — harmonic mean, penalises extreme imbalance between the two.
- **Macro-F1** — mean of per-class F1, every class equal; fits Hubble's long-tailed taxonomy; report support counts alongside because tiny classes make it unstable. **Micro/weighted F1** — dominated by or weighted toward frequent classes; secondary metrics.
- *Hubble answer:* "I used macro-F1 because Hubble had hundreds of taxonomy concepts with a long tail of rare classes. Accuracy would mostly tell me about common concepts; macro-F1 told me whether the model worked across the taxonomy."

## Text representation and classifiers

- **TF-IDF** — TF × log-scaled inverse document frequency, L2-normalised; common words down-weighted, distinctive terms up-weighted. Fast, CPU-friendly, interpretable, strong with sparse linear models and domain-specific text; no synonym/context understanding, vocabulary drift, noisy features from misspellings.
- **N-grams** — (1–3)-grams capture phrases like "interest receivable" at the cost of feature count and sparsity.
- **Embeddings (MPNet, e5, BERT-style)** — dense vectors capturing semantic similarity; less interpretable, slower, and generic pre-training can miss specialist accountancy language. TF-IDF often wins on domain-specific tasks with distinctive vocabulary — as it did here on the cost-adjusted comparison.
- **LinearSVC** — one-versus-rest maximum-margin hyperplanes over sparse features; predict the highest `w_c·x + b_c`. Strong with TF-IDF, fast CPU inference, coefficients show which terms push toward a class; linear boundary, no calibrated probabilities. Kernel SVMs handle non-linear boundaries but scale poorly to large sparse text.
- **Regularisation** — L1 zeroes unhelpful features (feature selection and interpretability in a huge sparse space); L2 shrinks smoothly; `C` trades margin width against violations (large C → overfit risk).
- **Class weighting** — inversely scales class contributions so rare taxonomy concepts influence training rather than being optimised away.

## Neural networks and transformers

- **Neural network** — layered function approximator: weighted sum + bias + activation per neuron; trained by minimising a loss (cross-entropy for classification) via backpropagation (chain rule computing each weight's contribution to error) and gradient descent (`w ← w − η·∂L/∂w`; mini-batch SGD or Adam in practice). Activations: ReLU as the hidden-layer default, softmax for multi-class output.
- **CNN for text** — filters over token sequences learn phrase-like local patterns, pooling keeps the strongest; fast and effective but less interpretable than coefficients.
- **RNN/LSTM** — sequential hidden state; LSTM gates mitigate vanishing gradients; largely superseded by transformers and unnecessary for short descriptions.
- **Transformers/BERT** — self-attention `softmax(QKᵀ/√d_k)V`; BERT is a bidirectional encoder pre-trained with masked-language modelling (and next-sentence prediction), classified via `[CLS]`, WordPiece tokenisation. SEC-BERT adds financial-domain pre-training. Strengths: contextual understanding, specialist terminology. Weaknesses: GPU needs, slow inference, weaker explainability, provenance/supply-chain risk, maintenance cost. *Hubble answer:* "SEC-BERT was technically attractive but the operational trade-off was poor — the extra complexity didn't justify the marginal, statistically unproven performance difference for HMRC."

## Hyperparameter tuning

Hyperparameters are set around training (C, learning rate, depth); parameters are learned (weights). Grid search is exhaustive; random search samples; successive halving concentrates resource on promising candidates; Bayesian optimisation (Optuna) uses prior trials to pick informative next trials. Select on validation/CV performance, then one final untouched holdout evaluation. In practice: `HalvingGridSearchCV` for the scikit-learn models, Optuna for the neural/transformer models, MLflow for tracking.

## Statistical tests

- **Paired t-test** — `t = mean(d)/(sd(d)/√n)` on per-fold score differences; pairing controls for split difficulty; assumes roughly normal differences; five folds → supporting evidence, not proof. Statistical ≠ practical significance: a tiny significant gain may not justify 67× the cost.
- **Welch's t-test** — `t = (m₁−m₂)/√(s₁²/n₁ + s₂²/n₂)`; independent means with unequal variances (checked via an F-test first); used in the agent-risk analysis.
- **Chi-square** — `Σ((O−E)²/E)`; association between categorical variables; needs adequate expected counts; shows association, not causation.
- **ANOVA** — compares means across 3+ groups without inflating error from many pairwise t-tests.
- **Quick recall** — t/Z-tests compare means; chi-square tests categorical relationships; ANOVA compares 3+ group means.
- **Bootstrap intervals** — resample the holdout to express uncertainty in a metric; overlapping intervals are not a formal paired test but justify caution about superiority claims; a stronger design bootstraps the paired prediction difference.

## Drift and monitoring

- **Types** — data drift (input distribution shifts), concept drift (input→output relationship changes), prediction drift (output distribution changes before labels arrive), label/taxonomy drift (target meaning changes), extraction drift (upstream HTML/iXBRL structure changes the fields supplied).
- **Detection** — compare training vs production distributions with PSI (bin both, `Σ(A−E)·ln(A/E)`; <0.10 none, 0.10–0.25 moderate, >0.25 significant), KS test (continuous) or chi-square (categorical); track performance on recent labelled data with a sliding window for concept drift.
- **Response** — confirm the drift type, contain risk (outputs are advisory), check extraction and taxonomy changes, collect fresh labels, retrain, re-validate, redeploy, reset baselines.
- **KPIs under poor data quality** — raw accuracy misleads; prefer robust signals: stability trends, drift KPIs (PSI, missing-rate), confidence/coverage rates, override and rollback rates, cost of wrong predictions.

## Lifecycle, DataOps and MLOps

- **CRISP-DM** — business understanding → data understanding → preparation → modelling → evaluation → deployment (SEMMA: sample-explore-modify-model-assess). Hubble mapping: untagged iXBRL limits profiling → EDA on ambiguity/imbalance → extraction, cleaning, canonicalisation, labels → model comparison → macro-F1 plus cost/explainability → R/Python integration, ODC batch, Oracle outputs, analyst guidance.
- **DataOps** — collaboration, automation, reuse, analytics-as-code, testing, monitoring, short cycles, data-driven improvement.
- **MLOps** — reproducibility, accountability (trace output to code/data/model/parameters), versioned collaboration, continuous testing and monitoring, reusable infrastructure. Hubble: GitLab issues/epics/milestones, README and docs, unit/integration tests, MLflow tracking, fixed holdout with per-class metrics, human-in-the-loop feedback.

## Data architecture options

Relational database (Oracle) — governed structured querying, joins, access control. Solr — distributed text search and document profiling. Data lake — cheap native-format storage, swamp risk without governance. Lakehouse — lake storage plus transactions, schema enforcement and warehouse analytics; Hubble's likely future direction (EMR/Spark processing, Redshift/lakehouse outputs) subject to benchmarking. Data fabric — metadata-driven central layer; powerful but complex.

## Legal and governance quick answers

- **UK GDPR principles** — lawfulness/fairness/transparency, purpose limitation, minimisation, accuracy, storage limitation, integrity/confidentiality, accountability.
- **Lawful bases** — consent, contract, legal obligation, vital interests, public task, legitimate interests.
- **Special-category data** — ethnicity, politics, religion, union membership, genetics, biometrics, health, sex life, orientation. **Protected characteristics** — age, disability, gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual orientation.
- **Article 22** — restricts solely automated decisions with legal or similarly significant effects; hence Hubble outputs are advisory with a human in the loop.
- **DPIA** — required for likely high-risk processing; completed before Hubble work began and revisited on change.
- **EU AI Act** — risk-based tiers (banned / high-risk regulated / transparency duties / minimal); not the primary UK control for HMRC but a useful reference for documentation, oversight and robustness principles.

## Accessibility

UI accessibility where tools have interfaces; alternative instructions where a workflow assumes a mouse/drag action (the Graffiti bookmarklet); clear documentation for technical and non-technical users; outputs understandable by analysts, SMEs, managers, DevOps and governance reviewers; no hidden barriers from jargon, unclear confidence warnings or inaccessible dashboards.

## Communication by audience

Senior managers — business problem, value, risk, cost, timescale, decisions needed. Analysts — examples, confusion matrices, per-class reliability, when to check raw descriptions. SMEs — taxonomy meaning, ambiguous concepts, edge cases. DevOps/engineers — infrastructure, dependencies, runtime, tests, monitoring. Governance reviewers — DPIA, minimisation, security, model limitations, human oversight, auditability.

## Generic frameworks for open-ended questions

- **Selecting the right technique** — start with the business decision and KPIs, not the model; check whether ML is needed at all; map to a task type; assess data readiness (labels, quality, leakage, freshness); build a fast interpretable baseline; choose via a decision matrix against interpretability, performance, latency and governance — the simplest model that meets all requirements; validate with risk-aligned metrics; treat monitoring/retraining as part of the solution.
- **Disseminating practice** — standardise (methodologies, templates, documentation), enable (communities of practice, wikis, training), provide reusable assets, embed governance, demonstrate value through pilots, make results visible, foster culture with sponsorship.
- **Tracking trends** — research and publication tracking, vendor/ecosystem monitoring, adoption-pattern analysis, community engagement, hands-on PoCs — then filter hype by scalability, cost/benefit and governance fit before recommending adoption.

## Will AI change jobs?

AI more often changes jobs than eliminates them: most roles mix routine tasks (automatable), judgement tasks (harder) and accountability tasks (often required by policy). Independent research agrees on scale — the WEF projects large churn by 2030 (~170m roles created, ~92m displaced); the IMF estimates ~40% of global employment exposed (~60% in advanced economies); the ILO finds clerical work particularly exposed. Framing: **displacement** where enough tasks are automated; **augmentation** where AI drafts/triages and people keep judgement, oversight and exception handling — and the biggest individual risk is people-with-AI-skills versus people-without. The organisational response is work redesign and reskilling, not automation for its own sake.

## Risks of adopting AI (and mitigations)

Data (quality, privacy, access control) · model (bias, opacity) · operational (drift, latency, weak monitoring) · business (wrong predictions, over-dependence eroding oversight) · security (adversarial inputs, data poisoning, supply chain) · compliance (missing audit trails, no approval process) · skills/adoption (gaps, resistance) · financial (cost exceeding unclear benefit) · ethical/societal (unfair impact, loss of accountability). **Mitigations:** data governance and quality controls; least privilege; validation and explainability (SHAP/LIME); drift and performance monitoring; meaningful human review; adversarial/security testing; formal approval and audit; training and change management. Hubble applied this pattern through its DPIA, human oversight, explainable model choice and per-class review.

---

# Final evidence and rehearsal checks

- Verify the strongest numerical claims and bring an artefact where possible: 233% more extracted data, DAP growth to 150+ users, days rather than nine months, identified tax risk, model scores, the 80% assessment result.
- Keep label counts straight: 826 labels survived preprocessing; 141 met the frequency threshold and were modelled; 685 were excluded.
- Treat the current scores as proof-of-concept estimates: the split is row-level, not grouped, and the CNN/SEC-BERT heads need remapping before a final cross-family claim.
- Quote like-for-like: macro-F1 0.800/0.808/0.823 with overlapping intervals; LinearSVC minutes-vs-hours training, sub-second-vs-minutes inference, megabytes-vs-gigabytes size. State the hardware.
- Correct the decision-matrix interpretability key and sensitivity-test the weights before quoting its numeric ranking.
- Be precise about prototype versus production: the code establishes TF-IDF with LinearSVC as an operational **recommendation**, not proof of deployment; add the internal release/approval artefact before saying it was deployed.
- Do not imply Hubble makes tax decisions — it categorises data to support analyst judgement with a human in the loop.
- When asked about APIs, describe the interfaces actually used — database drivers, `dbplyr`, Solr, S3 proxy, storage interfaces — before suggesting future REST or LLM-driven options.
- Where evidence is knowledge rather than a completed workplace action, say so clearly and connect it to the decision made; do not invent a project.
- For each answer, be ready to name: the artefact, another person who saw the work, the business outcome, the principal trade-off, the largest risk and what would be improved next.
