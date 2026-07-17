**Artificial Intelligence Data Specialist — Level 7 Apprenticeship**
**Learner:** Jesse Karadia
**Organisation:** HMRC

This document organises professional-discussion preparation around the EPA assessment criteria. Each criterion has the relevant KSBs, one or more STARR answers containing **all the applied evidence** (what I did, with the technical specifics), and a short block of **technical notes** covering the pure knowledge the criterion's clarification expects — definitions, techniques and frameworks, with no applied content mixed in. Use STARRs as speaking notes, not a script: first person ("I", not "we"), adapt depth to the question, and be ready to name supporting artefacts (test results, decision matrices, GitLab issues, dashboards, DPIAs, stakeholder feedback, wiki guidance, experiment records). The grading table assesses KSBs collectively within each theme, so the per-criterion KSB lists are a practical evidence map, not official marking units.

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
- **T3.4** — TODO: name the actual HMRC policies, UK GDPR requirements and approvals relevant to Hubble. TODO: who checked compliance, when, and how changes trigger reassessment.

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

**Situation:** Company accounts and tax computations are submitted as iXBRL, but some tax computations had only ~30% of figures tagged, so conventional extraction omitted much of the available information. Hubble could extract the untagged descriptions, but the same accounting concept could be described many ways, making profiling through manually maintained regular expressions impractical.

**Task:** Turn inconsistent, untagged descriptions into standard taxonomy concepts so analysts could profile far more of the data and identify tax risk more efficiently — and decide which statistical, AI and ML methodologies actually suited the business objective.

**Action:** I worked through the methodologies deliberately rather than selecting a fashionable model, challenging the assumption that population analysis had to rely on tagged items or matching rules. **Data mining first:** on the ~2.5 million cleaned rows I analysed frequency ranks, Pareto concentration, description/concept overlap, cosine similarity, class balance and residual errors. This established that sufficient labels existed, revealed a long-tailed, ambiguous problem — the top 75 raw concepts covered ~95% of items while generic descriptions such as "Total" mapped to many concepts — and showed where taxonomy and source quality would limit any model. **Supervised learning as the core method:** because correctly tagged items supplied target concepts, I framed this as multi-class text classification and compared Naive Bayes, tree ensembles, SVC/LinearSVC, SGD-style models, CNN/neural approaches, SEC-BERT and MPNet/e5 embeddings. **The NLP pipeline I built:** parse the iXBRL/XHTML, select descriptions and context, lower-case, normalise whitespace and punctuation, canonicalise names/companies/dates/postcodes/numbers into typed tokens, tokenise into word (1–3)-grams, vectorise with TF-IDF or embeddings, classify, and retain the prediction, score and provenance — with every learned transformation fitted on training data only and reused unchanged in production to prevent leakage. **Unsupervised methods stayed exploratory:** I compared vector spaces using labelled-class silhouette scores, which is a representation test, not an operationalised clustering model — a genuine clustering result would still need an SME to interpret whether discovered groups meant anything. **Methods I rejected with reasons:** reinforcement learning (a fixed labelled classification problem, no environment or reward signal) and machine vision (the text and structure were already extractable from iXBRL; OCR would only become relevant if scanned image-only PDFs entered scope, and would add an error-producing stage needing its own testing). Candidates were assessed on macro-F1, accuracy, per-class results, stratified CV, bootstrap intervals, speed, infrastructure, explainability, provenance, maintainability and cost.

**Result:** TF-IDF with LinearSVC was the strongest operational recommendation, not the highest point estimate on every metric: holdout macro-F1 0.800 against CNN 0.808 and SEC-BERT 0.823, with overlapping intervals, but far faster CPU-only training, inspectable coefficients and lower lifecycle risk. The method met the business objective — widening coverage, reducing manual grouping, supporting faster risk profiling — which is what made it suitable, not its technical possibility. The business-impact claim still requires a workplace artefact and is kept separate from the technical result.

**Reflection:** Method selection must begin with the business objective, label availability, data type and deployment constraints. Supervised NLP was appropriate; unsupervised methods stayed exploratory; machine vision and frontier LLMs were disproportionate. The best technical score alone does not define the best business solution.

### Technical notes — clarification knowledge

- **Statistical methods** — descriptive statistics summarise data (mean, median, spread, distributions); inferential statistics generalise from samples (hypothesis testing, confidence intervals, regression analysis).
- **Data mining** — discovering patterns and relationships in large datasets; techniques: clustering, association rule mining, anomaly detection.
- **Supervised ML** — trains on labelled data to predict or classify; techniques: linear regression, logistic regression, decision trees, random forests, support vector machines, neural networks.
- **Unsupervised ML** — finds hidden structure in unlabelled data; techniques: K-means clustering, hierarchical clustering, PCA, anomaly detection.
- **Semi-supervised** — a small labelled set plus a large unlabelled set (self-training, label propagation, pseudo-labelling). **Self-supervised** — the model generates its own targets from raw data (masked-word prediction; underpins BERT/LLM pre-training). **Reinforcement learning** — an agent learns a policy from rewards through interaction (Q-learning, Deep Q-Networks; robotics, game AI, control).
- **NLP** — enabling machines to process human language; techniques: tokenisation, sentiment analysis, named entity recognition, topic modelling, text classification.
- **Machine vision** — interpreting visual information; techniques: image classification, object detection, segmentation (CNN-based).
- **Business objectives these serve** — customer retention/experience, operational efficiency, sales and marketing effectiveness, fraud detection, risk management, quality control.

## Explains how to solve problems and evaluate software solutions via analysis of test data and results from research, feasibility, acceptance and usability testing in line with organisational requirements

**Relevant KSBs:** K7, S26.

### STARR — evaluating the Hubble classification solution

**Situation:** Analysts could not practically profile extracted untagged descriptions: wording was inconsistent and there were hundreds of taxonomy classes with a long tail of rare examples.

**Task:** Define the problem, research feasible solutions, test them objectively, and confirm the chosen output was usable and met HMRC requirements for security, explainability, infrastructure and analyst adoption.

**Action:** I first defined success more broadly than headline accuracy: the solution had to classify minority as well as common concepts, run at operational scale, remain explainable, use supportable technology, protect data and be usable by analysts. **Research and feasibility:** I compared literature, package and model documentation and empirical results across classical ML, neural, transformer and embedding approaches; feasibility covered more than whether the code ran — CPU/GPU availability, memory, throughput, cost, package and model provenance, security approval, maintainability, retraining time and whether the production estate could support the complete pipeline. **Test design:** I created fixed seeded 80/10/10 train/test/holdout flags plus a 10,000-row holdout sample so comparisons were like-for-like; used five-fold `StratifiedKFold` with `GridSearchCV`/`HalvingRandomSearchCV` for scikit-learn models and Optuna with MLflow tracking for neural/transformer runs; and analysed macro-F1, accuracy, precision/recall, confusion matrices, residual errors, bootstrap intervals, runtime and model size. I knew the split's weakness and can defend it: it stratifies rows, not filings, so related descriptions can cross partitions — for production evidence I would move to `StratifiedGroupKFold` or a grouped split by filing/company plus a chronological or unseen-taxonomy holdout, with learned preprocessing (vocabulary, IDF weights) fitted inside each fold. **Robustness analysis:** I built crafted adversarial, contextual, long-context, OCR-noise, Unicode and typo cases; LinearSVC beat SEC-BERT on most categories, SEC-BERT won on Unicode substitution, and both were weak on abbreviations — diagnostics of failure modes, not population estimates. **Acceptance testing with users:** analysts checked whether extracted dimensions and classifications supported the agreed business use; this exposed predictions being made from blank descriptions using only headings, so I changed production logic to return no prediction there, and it exposed missing dimensional content, so I generalised the extraction rather than coding a narrow subset. **Usability testing:** users found the top-five-matches display and raw scores confusing, so I limited the display to confident matches and added explanatory text about what scores meant. A remaining request for numeric rather than natural database keys is being treated as a performance question to benchmark on real Oracle and SAS workloads, not a preference to accept.

**Result:** TF-IDF plus LinearSVC balanced quality with speed, explainability, supportability and security (holdout macro-F1 0.800; SEC-BERT's higher point estimate was not interval-separated, and the operational rubric favoured the simpler model — noting the rubric's interpretability-key defect must be fixed before its numeric ranking is quoted). Acceptance testing changed extraction and prediction behaviour; usability testing made the dashboard clearer — both need named internal artefacts. The defensible status from the notebooks is a validated comparison/proof of concept, not proven production deployment.

**Reflection:** Research established tooling before writing bespoke evaluation code — Optuna automated what I had partly built myself. Training, test and production preprocessing need a single controlled implementation so rules like blank-description handling cannot diverge. If this went to production I would monitor extraction failures, missing-description rate, input and prediction distributions, per-class metrics and analyst overrides, with drift tests flagging when to diagnose, contain, relabel and retrain or roll back. I would agree acceptance criteria earlier, automate pipeline-parity checks and keep a traceable decision log.

### Technical notes — clarification knowledge

- **Problem solving** — define the business problem clearly; research potential solutions; assess feasibility across technical, operational and financial dimensions.
- **Testing phases** — **unit** (individual components correct), **integration** (modules work together), **system** (complete system meets requirements), **acceptance/UAT** (end-users confirm it meets their needs), **usability** (ease of use and user experience, via interviews, task testing, surveys).
- **Analysis of test data** — collect data from all testing phases; use statistical methods to identify patterns, trends and anomalies; document findings and report actionable insights to stakeholders.
- **Evaluation and decision-making** — compare solutions on performance, usability and feasibility; assess the risks of each; decide on the evidence.
- **Train–validate–test (the gold standard)** — training data fits parameters; validation data tunes hyperparameters; a final untouched test/holdout set evaluates the finished model. Cross-validation folds the train/validate phase together: K folds, train on K−1, validate on the held-out fold, rotate, average. Repeatedly checking the holdout while tuning turns it into another validation set.
- **Overfitting** — high training performance, weak test performance (learned noise); mitigate with regularisation, simpler models, more data, dropout, early stopping, CV. **Underfitting** — poor on both; mitigate with better features, more capacity, less regularisation. The **bias–variance trade-off**: total error ≈ bias² + variance + irreducible noise.

## Describes the relationship between mathematical principles and core techniques in AI and data science within the organisational context

**Relevant KSBs:** K19, K22.

### STARR — the mathematics behind the Hubble model choice

**Situation:** Hubble needed to classify short, inconsistent accounting descriptions into a large, imbalanced set of standard concepts, and stakeholders needed both reliable outputs and an explanation of how the method worked.

**Task:** Select and explain a technique whose mathematical properties suited sparse text, unequal class frequencies and HMRC's need for fast, supportable, interpretable processing.

**Action:** **Linear algebra:** I represented each canonical description as a numeric vector using word TF-IDF over (1–3)-grams — raw n-gram counts multiplied by smoothed inverse document frequency, `IDF(t) = log((1+N)/(1+df(t))) + 1`, then L2-normalised per description — so common words were down-weighted and distinctive phrases like "interest receivable" kept their signal. **Optimisation and geometry:** LinearSVC then found one-versus-rest separating hyperplanes by convex optimisation: score `w_c·x + b_c` per class, predict the argmax, with the objective conceptually `||w||₁ + C Σ max(0, 1 − yᵢ(w·xᵢ + b))²` at `C=2.8` with squared-hinge loss. I chose the L1 penalty deliberately because it drives many weights exactly to zero, producing a sparse, inspectable coefficient set in a huge feature space; balanced class weights scaled each class's contribution inversely to its frequency so minority-concept errors mattered. **Probability and statistics:** I challenged the stakeholder preference for accuracy as the headline measure — with 75 concepts covering ~95% of items, accuracy mostly measures common classes — and made macro-F1 (the unweighted mean of per-class F1) the selection metric so each eligible class contributed equally, while retaining accuracy, per-class precision/recall, support counts and confusion analysis. Stratified cross-validation estimated generalisation; bootstrap intervals expressed uncertainty in holdout measures, which is why I would not claim SEC-BERT's 0.823 beat LinearSVC's 0.800 — the intervals overlap. I also quantified the embedding trade-off: MPNet's ~0.003 macro-F1 advantage over TF-IDF cost ~67× the fit time on one run, and a later run showed a ~0.0001 difference that was not significant at 95% — mathematically real numbers that translated directly into an organisational decision about GPUs, cost and explainability.

**Result:** The mathematics supported an organisationally appropriate choice: fast on existing CPUs, explainable through coefficients and better aligned to minority concepts than selection on accuracy. Reframing evaluation around macro-F1 made rare-class performance visible and gave stakeholders an impartial basis for comparison.

**Reflection:** Mathematical principles explain why a technique behaves as it does and whether its output suits a decision. I would never present a p-value or metric as certainty — sample size, assumptions, class representation, effect size and business consequences all matter.

### STARR — testing whether an agent presented higher risk

**Situation:** In separate agent-level risk work, qualitative review suggested one agent might present higher risk than the comparison group.

**Task:** Test that suspicion quantitatively rather than let an impression drive the conclusion.

**Action:** I set the null hypothesis that the agent's risk equalled the comparison group's, then checked the assumptions before choosing the test: two independent groups, a ratio-scale measure, approximately normal distributions, more than 30 observations, unknown population variances. An F-test indicated unequal variances, so Student's pooled-variance t-test was inappropriate and I selected Welch's t-test, `t = (m₁ − m₂)/√(s₁²/n₁ + s₂²/n₂)`, with adjusted degrees of freedom.

**Result:** At a 99% confidence level I rejected the null and concluded the agent presented higher risk, giving the business quantitative evidence rather than judgement alone. Rejecting at 99% means the observed difference would be unlikely if the means were equal — not a 99% probability the conclusion is true, a distinction I am careful to keep.

**Reflection:** The test must follow the data and its assumptions. I would present the confidence interval and effect size as well as the p-value, because statistical significance alone does not show operational importance.

### Technical notes — clarification knowledge

- **Linear algebra** — vectors and matrices represent data and model weights; matrix decompositions (SVD) underpin PCA, recommendation systems and compression.
- **Calculus** — differentiation drives optimisation; gradient descent minimises the loss function; partial derivatives and the chain rule are the machinery of backpropagation.
- **Probability and statistics** — probability distributions model uncertainty; Bayesian inference updates beliefs from evidence; hypothesis testing, confidence intervals and regression infer patterns from samples.
- **Optimisation** — convex optimisation (a single global minimum) underpins SVMs and linear models; stochastic optimisation (SGD, Adam) handles large datasets efficiently.
- **How the maths maps to core techniques** — regression/classification (least squares, maximum likelihood, hinge loss); neural networks (matrix multiplication + non-linear activations, trained by gradient descent); clustering (distance minimisation, e.g. K-means minimises Σ‖x − centroid‖²); dimensionality reduction (variance maximisation via eigen-decomposition); transformers (attention as scaled dot-products: `softmax(QKᵀ/√d_k)V`).
- **Key formulas to recall** — macro-F1 = (1/K)ΣF1_k; paired t-test `t = mean(d)/(sd(d)/√n)`; Welch's `t = (m₁−m₂)/√(s₁²/n₁+s₂²/n₂)` (unequal variances, checked by F-test); SVM objective `min ½‖w‖² + CΣmax(0, 1−yᵢ(w·xᵢ+b))`.
- **Organisational relevance** — mathematical properties translate into compute cost, minority-class coverage, interpretability, uncertainty quantification and the ability to defend a decision to stakeholders and auditors.

## Explains how they have used programming languages and modern machine learning libraries for commercially beneficial scientific analysis, simulation and data engineering to meet business needs

**Relevant KSBs:** K18, K25, S26.

### STARR — using R, Python and SQL as one Hubble pipeline

**Situation:** Company returns (XML) and accounts (iXBRL/XHTML) contained valuable structured and semi-structured data. The analysts who would maintain and use the extraction worked primarily in R, while the strongest documented ML ecosystem for the classification experiments was Python.

**Task:** Select languages and libraries for extraction, cleaning, model experimentation and delivery without forcing the whole pipeline into one language or creating an unsupported workflow — challenging the norm that a project stays in the language it started in.

**Action:** I investigated package maturity, team capability, platform support and long-term maintenance rather than choosing by preference. **Data engineering in R (workplace):** I used R for the fuller XML/HTML extraction because it matched the supported analyst workflow and had mature parsing tooling — keeping extraction in the language its maintainers actually used reduced the support burden (internal artefacts needed; not in `Code/`). **The cross-language boundary:** `reticulate` embedded a Python session inside R and converted objects between the languages, letting the R pipeline call the more mature Python model without rewriting the analyst-facing workflow. I treated its risks — dependency and environment mismatch, conversion overhead, cross-language error handling — as part of the design, with pinned R/Python/package versions, a reproducible environment and an integration test. **Delivery through SQL/Oracle:** `dbplyr` represented remote tables lazily and translated tidyverse verbs into SQL, so filtering, grouping and joins executed in the database rather than after downloading the dataset; I inspected generated SQL and query plans for expensive operations rather than assuming translation was optimal. **Scientific analysis in Python (code-backed):** BeautifulSoup/Pandas parsing to Parquet; Polars/NumPy for EDA and engineering; scikit-learn for TF-IDF, classical modelling, CV and halving searches; SentenceTransformers for MPNet/e5; TensorFlow/Keras for neural/CNN; PyTorch and Hugging Face for SEC-BERT; Optuna for hyperparameter search; MLflow for experiment tracking. **Feature engineering was empirical:** lower-casing and whitespace/punctuation normalisation reduced accidental vocabulary variation; typed placeholders (`hubble_name`, `hubble_date`, `hubble_number`) removed high-cardinality identifiers while preserving that a name, date or number was present; and I tested rather than assumed each choice — replacing forward slashes with spaces reduced performance, so it was not retained. The same tested functions create training and production features to prevent skew. On simulation I keep the claim narrow: controlled computational experiments comparing model and hyperparameter scenarios on fixed splits are a defensible form of experimental analysis, but not a physical or Monte Carlo simulation, and I say so explicitly.

**Result:** The code demonstrates a complete experimental path from semi-structured filings to repeatable model comparisons over millions of rows, and why a CPU-compatible scikit-learn model could beat GPU-heavy alternatives operationally. The commercial benefit was not "using three languages" — it was combining their strengths to widen usable data, reduce manual preparation and deliver through a workflow the organisation could support. The workplace claims about coverage and adoption need internal measures.

**Reflection:** The correct language is contextual: data format, library maturity, user capability, deployment platform, supportability. Python support is growing in HMRC's AWS lakehouse, so I would reassess the boundary over time, migrating only where benefit outweighs disruption.

### Technical notes — clarification knowledge

- **Programming languages** — Python (dominant for data analysis and ML: extensive libraries, easy syntax), R (statistical analysis, visualisation, strong in analyst communities), SQL (declarative querying of relational data), Java/Scala (JVM data engineering, Spark).
- **ML libraries** — scikit-learn (classical ML, preprocessing, model selection), TensorFlow/Keras and PyTorch (deep learning), Hugging Face Transformers (pre-trained language models), XGBoost/LightGBM (gradient boosting). Libraries provide tested implementations, so effort goes into the problem rather than reimplementing algorithms.
- **Scientific analysis** — analysing large datasets to identify trends, make predictions and optimise processes; results must be reproducible and evidence-led.
- **Simulation** — modelling real-world scenarios computationally so outcomes can be explored before committing (Monte Carlo methods, what-if scenario modelling, agent-based models).
- **Data engineering** — collection, cleaning, transformation and preparation of data; reliable pipelines and formats (e.g. Parquet) ensure analysis and models receive accurate, consistent input.
- **Meeting business needs** — the test of the technical work is business impact: efficiency gained, cost reduced, revenue or coverage increased, decisions improved.

## Uses applied research and data modelling to design and refine the infrastructure and architectures to deliver secure, stable and scalable data products, including enterprise, private and public cloud resources and services

**Relevant KSBs:** K16, S1, S16, S19.

### STARR — refining Hubble's data-product architecture

**Situation:** Hubble processed high-volume, varied data (XML, iXBRL/XHTML, PDFs). The POSIT Data Analytics Platform suited development but not full-volume extraction, and outputs had to remain secure, stable and accessible to analysts.

**Task:** Define and refine an architecture that could burst for large extraction jobs, recover reliably and provide queryable outputs without overloading the shared platform.

**Action:** **Applied research and data modelling:** I investigated taxonomy change, Oracle width limits, workload shape and user needs, and proposed a long-form data model — document, context, concept, description and value as rows — instead of the wide annual-taxonomy tables that created structural change and width pressure every year. The long model costs row count and occasional pivots but is taxonomy-independent and removes annual schema remapping; I consulted analysts before committing to confirm they could work with it. **Scalable compute:** I worked with platform engineers to establish On-Demand Compute — temporary EC2 capacity (large-core or GPU configurations when justified) spun up per job and shut down after — isolating heavy workloads from the shared platform and controlling cost. Because document sizes varied widely, static partitioning left workers idle while stragglers finished, so I used dynamic work allocation: workers pulled the next document when free. I also understood where scaling stops helping — when I/O, database writes, serial setup or credential management becomes the bottleneck (Amdahl's law in practice). **Storage matched to access pattern:** Apache Solr provided distributed, replicated free-text search across servers; Oracle held governed structured outputs for SQL querying and joins — each store used for what it suits rather than forcing one to do both. **Security and stability:** the DPIA, data minimisation, controlled-environment processing, model assurance, distribution-list access and controlled Oracle/S3 outputs addressed confidentiality; replicated Solr, tested code, durable database outputs and workload isolation supported stability.

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

**Action:** I reviewed charges at low and zero usage and compared the managed design with fixed-price or self-hosted EC2 alternatives, weighing total cost of ownership — concurrency, storage, idle time, support effort, recovery, growth — rather than headline compute prices. Serverless billing was opaque and the baseline cost disproportionate for a small, intermittent workload, so I challenged the assumption that cloud-native auto-scaling is automatically the most scalable choice.

**Result:** Fixed-price or self-hosted capacity was more predictable for this project and could still be resized when demand genuinely grew — separating the technical ability to scale from whether the scaling model was commercially appropriate.

**Reflection:** A scalable service must also be financially sustainable; I would use measured workload profiles and total-cost comparisons before selecting serverless or auto-scaling infrastructure.

### Technical notes — clarification knowledge

- **Applied research and data modelling** — using research methods and modelling techniques to understand a problem before designing the solution: profiling sources, prototyping schemas, benchmarking alternatives.
- **Secure / stable / scalable** — secure: protected from unauthorised access (least privilege, controlled networks, encryption, audit); stable: reliable, consistent performance with recovery from failure (replication, tested code, durable storage); scalable: handles growing data and users (horizontal scaling, parallelism, elastic compute).
- **Enterprise vs private vs public cloud** — enterprise: an organisation's own internal platforms and services; private cloud: dedicated cloud resources for a single organisation; public cloud: third-party provider services (AWS, Azure, GCP) consumed on demand — using a public provider does not make the data public; it stays within organisational accounts, networks and governance.
- **Data architecture options** — relational database (governed structured querying, joins, access control); document/text search engine (distributed indexes, sharding, replication); data lake (cheap native-format storage; swamp risk without metadata and governance); lakehouse (lake storage plus transactions, schema enforcement, warehouse-style analytics); data fabric (metadata-driven virtual layer; powerful but complex).
- **Parallel-processing concepts** — embarrassingly parallel workloads; static vs dynamic scheduling; stragglers; Amdahl's law (serial fractions and shared bottlenecks cap speed-up).

## Explains how to design algorithms for accessing and analysing large amounts of data, including Application Programming Interfaces (API) to different databases and data sets

**Relevant KSBs:** K16, S19, S20.

### STARR — moving Hubble from files to scalable data access

**Situation:** The first Hubble workflow saved results to files, often exported as CSV/Excel; runs were slow, limited to selected populations, and repeated file movement made querying, joins and reuse difficult.

**Task:** Redesign access and processing so Hubble could handle large document populations without saturating the main platform, exposing results through stores analysts already used.

**Action:** I challenged the file-based workflow, investigated where time and manual effort were lost, and designed around data locality, batching, query pushdown, parallelism, storage format and serialisation cost. **Parallel access design:** I worked with DevOps to provision ODC and used dynamic parallel scheduling — a work queue with workers pulling the next document when free — so ~128 returns could be processed concurrently without the long tail caused by static batches of differently sized documents; the correct worker count is just before contention at S3, network, parsing memory or Oracle writes removes the benefit of more cores. **The API layer:** an API is a defined programmatic interface, not necessarily REST. The interfaces I actually used were R database drivers/DBI-style calls to Oracle, `dbplyr` as a higher-level query interface, Solr's query interface, the controlled S3 proxy and Parquet-on-FSx storage interfaces — and I am careful not to describe an ordinary file copy as an API. `dbplyr`'s lazy execution builds a query representation and sends translated SQL only when results are collected, so filters, aggregation and joins execute close to the data, cutting transfer and client memory; the benefit depends on suitable indexes and pushdown-friendly predicates. **Storage and format decisions:** structured outputs went to Oracle rather than loose files; where a SAS-writing package proved unreliable I used a shared FSx route with Parquet — a compressed columnar format where analytical queries read only the required columns and use metadata for predicate pruning, far more efficient than CSV. Batched database writes used sensible boundaries so a failed batch could be retried without duplicates. Solr handled fast distributed text retrieval; the S3 proxy controlled object access. The analysts' request for numeric surrogate keys over natural keys is held as an open benchmarking question — index size, query plans and end-to-end user effort on representative Oracle and SAS workloads — rather than a change made on preference. A possible future LLM-to-Solr natural-language query route stays clearly proposed: it would need a controlled schema, syntactic validation, field/operator allow-lists, authorisation in the user's own context, result limits, injection escaping, audit logging and preview — the LLM must not become a route around access controls.

**Result:** Large extraction jobs ran on isolated temporary capacity without degrading the shared platform, and database/Parquet outputs made results easier to query, join and reuse while R analysts kept familiar syntax and let the database do the heavy work.

**Reflection:** An efficient algorithm is part of a wider data-access design — parallelism only helps if work is balanced, credentials stay valid and output avoids new bottlenecks. I would add service interfaces only where they improve reuse rather than adding a REST API for its own sake.

### Technical notes — clarification knowledge

- **Designing algorithms for large data** — choose methods for processing at scale (sorting, filtering, aggregating); efficiency and scalability matter as volumes grow; complexity is about the whole data path, not one function.
- **Accessing data via APIs** — APIs let algorithms retrieve data from external sources: web services (REST/JSON), database drivers (ODBC/JDBC/DBI), cloud storage SDKs, query endpoints. They abstract the storage details behind a defined interface.
- **Analysing data** — statistical analysis, machine learning and data mining turn raw data into information for business decisions.
- **Different databases and data sets** — SQL/relational databases (structured, joins, transactions), NoSQL (document, key-value, wide-column; flexible schemas at scale), search indexes, object stores, file formats (CSV vs columnar Parquet/ORC). Integration means algorithms can work seamlessly across these sources.

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

### Technical notes — clarification knowledge

The distinction criterion has four elements to hit explicitly: **the norm challenged** (the existing practice, process or belief needing change), **the investigation** (research, data analysis, expert consultation showing the challenge was informed, not assumed), **the proposed solution** (what was innovative and how it differed from the norm), and **the impact** (measurable benefit — efficiency, cost, performance — and how it was validated).

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

### Technical notes — clarification knowledge

- **Developing working practices** — adopting new tools and technologies, staying current with industry trends, continuous learning through courses, workshops and self-study.
- **Leadership techniques** — leading projects, mentoring, fostering collaboration, making strategic decisions, giving technical direction, tailoring communication to the audience.
- **Organisational impact categories** — enhanced efficiency (streamlined processes), innovation (new AI/data solutions, competitive advantage), improved decision-making (data-driven insights), team development (skills and motivation through mentorship).

## Justifies their choice of techniques, explaining the risks and benefits and offers an alternative to technical and non-technical audiences

**Relevant KSBs:** K8, S6, S8, S28.

### STARR — communicating the LinearSVC decision

**Situation:** Stakeholders had different preferences: accuracy as the headline measure, Random Forest suggestions from analysts, and interest in transformers because they were current and powerful.

**Task:** Make an impartial recommendation, explain benefits and risks, provide credible alternatives, and communicate appropriately to technical and non-technical audiences.

**Action:** I consulted stakeholders and converted their concerns into a comparison covering macro-F1 and per-class reliability, accuracy, speed, compute cost, explainability, security/provenance, maintainability and deployment fit. The comparison narrowed to LinearSVC, CNN and SEC-BERT on one holdout plus rubric-scored operational criteria: SEC-BERT had the highest macro-F1 point estimate (0.823 vs 0.808 and 0.800) but overlapping intervals, while LinearSVC trained in minutes rather than the better part of an hour, ran inference orders of magnitude faster and was ~8 MB rather than ~1.8 GB, with stronger deployment, maintenance and dependency-risk ratings. **Risks and benefits both ways:** LinearSVC's risks are its linear boundary and lack of contextual understanding; SEC-BERT's are GPU dependency, slower throughput, weaker explainability, provenance/assurance concerns and lifecycle cost. **To technical audiences** I explained sparse TF-IDF vectors, L1 regularisation, imbalance handling, cross-validation, bootstrap uncertainty and CPU/GPU constraints; **to non-technical audiences** I described macro-F1 as reliability across rare as well as common concepts, CPU execution as lower cost and easier deployment, and coefficients as understandable evidence of which phrases influenced a result. **The alternative offered:** SEC-BERT or another assured domain model, if a remapped, grouped evaluation established a worthwhile gain and future infrastructure, assurance and maintenance could support it. I would not present the current numeric decision score unqualified — the matrix has a known field-name defect and untested weights — and explaining that defect openly is itself part of impartial, evidence-led decision making.

**Result:** TF-IDF with LinearSVC was the operational recommendation: competitive quality, fast CPU-compatible processing, clearer explanations, lower lifecycle risk. A named meeting, decision paper or approval is still needed to prove how stakeholders received it.

**Reflection:** Communicating alternatives strengthens a recommendation by showing the choice is deliberate. I would agree metric definitions and risk tolerances even earlier and keep a short decision record with both a technical comparison and a plain-English version.

### Technical notes — clarification knowledge

- **Justifying a technique** — suitability against the problem: efficiency, accuracy, scalability, relevance, cost.
- **Risks and benefits** — risks: limitations, potential errors, resource requirements, maintenance burden; benefits: performance, cost savings, capability. Present both, not a sales pitch.
- **Offering alternatives** — show the choice was deliberate by presenting credible alternatives and the conditions under which they would win.
- **Audience tailoring** — technical: algorithms, data structures, metrics, infrastructure; non-technical: practical implications — what problem it solves, what it costs, what could go wrong, what decision is needed.

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

### Technical notes — clarification knowledge

- **Sharing internally** — training sessions, workshops, demonstrations, wikis, communities of practice, mentoring.
- **Disseminating externally** — conference presentations, publications, professional networks and forums, open demonstrations on public data.
- **Improving industry practice** — influencing standards and best practice, contributing to guidelines; be honest about the difference between sharing (done) and demonstrated industry change (needs evidence).

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

### Technical notes — clarification knowledge

Four elements to hit explicitly: **critical analysis of the wider social context** (ethics, privacy, economic impact, public perception — evidenced, not asserted), **current issues and trends** (technology advances, regulatory change, emerging debates), **applying findings with justification** (link the action taken back to the analysis), and **sharing with the wider community** (articles, presentations, forums, demonstrations).

## Explains how they have made independent impartial decisions respecting the opinions and views of others in complex, unpredictable and changing circumstances to benefit the business

**Relevant KSBs:** S8, S28, B4.

### STARR — balancing licence, compute and funding priorities for DAP

**Situation:** As DAP owner I received competing demands: users needing licences and GPU capability, engineers with platform constraints, budget holders needing a defensible case.

**Task:** Respect those perspectives and provide capacity where it benefited the organisation without committing to unaffordable permanent infrastructure.

**Action:** I gathered evidence of demand and the work additional capacity would enable, justified licence growth with budget holders, and worked with engineers to provide On-Demand Compute — including GPU instances started for specific work and shut down afterwards.

**Result:** DAP grew beyond 150 users with appropriate licences, and ODC provided large CPU/GPU capacity cost-effectively when projects needed it.

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

### Technical notes — clarification knowledge

- **Independent and impartial** — decisions based on objective analysis and evidence rather than personal bias or external pressure.
- **Respecting others' views** — active listening, valuing diverse perspectives, incorporating relevant feedback into the decision process — while still deciding on the evidence.
- **Complex/unpredictable/changing circumstances** — unexpected challenges, new information, shifting priorities; adapt the decision process rather than the standard of evidence.
- **Business benefit** — efficiency, conflict resolution, innovation, strategic goals; be specific about the outcome.

## Explains how they have worked with software engineers to ensure suitable testing and documentation processes are implemented in line with organisational requirements

**Relevant KSBs:** S14, B1.

### STARR — engineering controls for Hubble

**Situation:** Hubble became a complex tool with varied real-world documents, several contributors and many users; a small parsing or preprocessing change could silently affect extraction, model inputs or analyst outputs.

**Task:** Establish, with engineers and contributors, proportionate testing, change control and documentation supporting safe delivery without a heavyweight process.

**Action:** In the workplace repository I established that changes require tests — if a function had no test, one was written before modifying it, and the suite had to pass before merging to main. **Unit tests** covered individual functions; **integration-style cases** covered complex real documents, because input variation cannot be covered by isolated tests alone; **user acceptance** came through the analyst testing described under T1.2. I used GitLab issues, templates, epics and milestones for traceability and a lightweight Kanban board for planning. **Documentation at three levels:** a full README for the multi-system setup (process documentation for new users), detailed Markdown design notes covering architecture, workflows and the reasons behind key decisions (technical documentation), and analyst guidance on interpreting outputs (user documentation). I collaborated with platform/DevOps engineers on ODC, data paths and environment constraints, turning operational findings into tests or documentation. In a public-sector context, undocumented behaviour or an unrepeatable result can undermine trust even when a metric looks strong — reproducibility and traceability were treated as requirements, not extras. `Code/` contains research notebooks only, so the internal test suite, CI gates, README and reviews need workplace artefacts.

**Result:** New users could set up the project from the README, contributors could change tested functions with confidence, and issues/milestones gave an audit trail from requirement to implementation — to be evidenced with a test report/CI result, README, representative merge request and an engineer witness.

**Reflection:** Up-front tests and documentation reduce future change cost and dependency on individual knowledge, and make AI work more open to review. The largest remaining risk is source-document diversity, so I would expand a versioned representative corpus, automate integration tests in the merge pipeline and link requirements, tests and release notes explicitly.

### Technical notes — clarification knowledge

- **Collaboration with engineers** — regular communication, joint planning, collaborative problem-solving on requirements and constraints.
- **Testing levels** — unit (individual components), integration (modules together), system (complete system against requirements), user acceptance (end-users validate functionality and usability).
- **Documentation types** — technical (architecture, code, APIs), user (guides and manuals), process (development, testing and maintenance procedures).
- **Organisational alignment** — testing and documentation must comply with organisational standards, industry best practice, regulatory requirements and quality-assurance guidelines.

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

### Technical notes — clarification knowledge

- **Organisational impact** — operational efficiency (automation, optimised workflows), innovation (new products/services, competitive advantage), data-driven insight (trend discovery, prediction, strategic decisions).
- **Industry impact** — changed market dynamics and business models, disruption of traditional practice, new regulation and standards, cross-sector partnerships and integration.
- **Societal impact** — ethics (privacy, bias, fairness), economic change (job creation and displacement, changed nature of work, growth), social change (healthcare, education, public services).
- **AI and jobs (balanced answer)** — AI more often changes jobs than eliminates them: most roles mix routine tasks (automatable), judgement tasks (harder) and accountability tasks (often required by policy). Scale estimates: WEF projects large churn by 2030 (~170m roles created, ~92m displaced); IMF estimates ~40% of global employment exposed (~60% in advanced economies); ILO finds clerical work particularly exposed. Displacement vs augmentation framing; the organisational response is work redesign and reskilling.

## Explains how they have assessed and addressed the potential business impact of ethical issues relating to AI and data science, the way procedures and methods are selected, and the unintended consequences to the business when they are applied

**Relevant KSBs:** K11, K17; cross-reference S12 and B3 in Theme 4.

### STARR — ethical impact assessment for Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information; a classifier used in a tax-risk context could create privacy, bias, transparency and accountability risks if its categories were treated as fact or used out of purpose.

**Task:** Assess those ethical issues before and during development, choose proportionate procedures and methods, and reduce the likelihood of unintended model behaviour causing legal, operational or reputational harm.

**Action:** **Assessing:** I completed a DPIA before work began and reviewed it as the design evolved, and I assessed representation and imbalance quantitatively — frequency distributions, macro-F1, per-class measures, confusion matrices and residual examples rather than overall accuracy. **Addressing:** in the pipeline I canonicalised names, companies, dates, postcodes and numbers so high-cardinality identifiers were not the trained feature — feature minimisation, not anonymisation, since the source description is retained and access/retention/purpose controls remain necessary; processing stayed inside controlled environments. I tested balanced class weights, biased sampling and oversampling (the final LinearSVC used balanced weights; several neural/transformer weighting approaches made performance worse). Demographic fairness (parity, equalised odds) remains proposed, not completed, and I say so. **Method selection shaped by ethics:** I chose an explainable TF-IDF/LinearSVC pipeline partly so coefficients, LIME and SHAP could expose feature influence, and model provenance was part of the selection decision. **Unintended consequences found and fixed:** acceptance testing found blank descriptions being classified from surrounding context — I stopped predictions where the description was absent; usability feedback showed the top-five display created false confidence — I simplified it (both user changes need internal evidence).

**Result:** The code supports the narrower conclusions: identity-like tokens removed from the modelling feature, minority-class and robustness failures made visible, and a simpler model enabling direct inspection. Workplace controls kept the model as decision support rather than an automated determinant — name the DPIA, human-oversight instruction and user evidence to substantiate this.

**Reflection:** Ethical assessment must cover the whole sociotechnical process: data, labels, metrics, model, interface, users and downstream decisions. A technically explainable model can still be misused, so future improvements include monitoring, enforced workflow controls, periodic DPIA review and clearer warnings for low-reliability classes.

### Technical notes — clarification knowledge

- **Assessing ethical issues** — identify concerns (privacy, algorithmic bias, transparency, accountability) through ethical audits, stakeholder consultation and impact assessments (DPIA).
- **Addressing them** — data-protection measures, fairness checks, transparency/explainability, documented frameworks (GDPR, ethical AI principles).
- **Method selection** — weigh the ethical implications of alternative approaches alongside performance; the decision criteria should be explicit.
- **Unintended consequences** — anticipate via risk assessment; detect via monitoring and user testing; correct and retest when found.
- **Business impact of getting it right** — customer/public trust, avoided legal issues, reputation.
- **Ethical concern areas for AI generally** — transparency, accountability, bias, accuracy, privacy. Reference frameworks: UK responsible-AI principles (safety/security/robustness; transparency and explainability; fairness; accountability and governance; contestability and redress), OECD AI guidelines, EU AI Act.

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

### Technical notes — clarification knowledge

- **Applied solutions** — concrete implementations addressing organisational challenges: new technologies, methodologies or strategies actually put into practice.
- **Demonstrated awareness** — staying informed: courses, conferences, publications, professional networks, research tracking, vendor/ecosystem monitoring, hands-on proof-of-concepts.
- **Explaining changes and trends** — communicating the significance and potential impact of developments to team and organisation, not just knowing about them.
- **Enhancement of working practices** — tangible improvements: efficiency, collaboration, quality, reproducibility — with measurable examples.

## Explains the impact, consequences and risks of non-compliance to the business

**Relevant KSBs:** K11, K17; cross-reference S12 and B3 in Theme 4.

### STARR — designing to prevent non-compliance in Hubble

**Situation:** Hubble used sensitive data in a regulated public-sector environment; non-compliance could arise through excessive collection, personal-data leakage, weak access controls, unassured technology, opaque model use or decisions without appropriate human review.

**Task:** Understand the impact of those failures and build preventive controls into the pipeline so the product remained legally, ethically and organisationally defensible.

**Action:** I used the DPIA to identify data-protection and governance risks; minimised and canonicalised personal information; kept processing in controlled environments; restricted S3 and Oracle access; considered provenance in model selection; documented lineage and design choices; and retained human review — Hubble's classifications were advisory inputs, which matters because UK GDPR Article 22 restricts solely automated decisions with legal or similarly significant effects, and a nominal human-in-the-loop is insufficient if the person lacks time, information or authority to disagree. I treated compliance as an operational requirement during model and infrastructure selection, not a final approval step, and communicated that classifications were suggestions, not the defining factor in action. I ran the control lifecycle as a cycle: identify requirements and owners, document risks in the DPIA, implement minimisation/access/assurance/oversight, test, approve, monitor, and review whenever data, purpose, model, users or infrastructure changes — with compliance evidence linked to the same version of data, code and model that produced the output.

**Result:** The work avoided any known privacy or security incident and proceeded with proportionate controls, reducing the likelihood of regulatory investigation, legal challenge, invalid decisions, operational rollback, financial loss, reputational damage and loss of public trust.

**Reflection:** For a public body the largest consequence may be loss of legitimacy and trust, even without a financial penalty. Compliance evidence must remain current as data, users, models and infrastructure change; I would schedule formal DPIA/control reviews linked to releases.

### Technical notes — clarification knowledge

- **Impact on operations** — disrupted activities, interrupted service delivery, forced shutdown of processing, outputs quarantined, decisions reviewed, systems rolled back.
- **Legal consequences** — penalties, fines, sanctions, enforcement notices, litigation.
- **GDPR penalty figures (a past-learner question)** — UK GDPR/DPA 2018 higher maximum: **£17.5 million or 4% of annual worldwide turnover**, whichever is higher; standard maximum £8.7 million or 2%. EU GDPR: €20 million or 4%; €10 million or 2%. Enforced in the UK by the ICO.
- **Financial risks** — beyond fines: remediation, legal fees, incident response, new systems and processes, duplicated analysis, delayed outcomes.
- **Reputational damage** — eroded customer/public trust, reduced investor and stakeholder confidence; for a public body, loss of legitimacy can outweigh any fine.
- **Operational risks** — data breaches, security vulnerabilities, inefficiencies from uncontrolled processes.
- **Regulatory scrutiny** — increased oversight across otherwise unrelated programmes after a failure.

---

# Theme 4: Development of suitable AI and data science solutions with consideration for ethical, legal, regulatory, governance and accessibility issues

**Theme KSBs:** K29, S12, B3.

## Evaluates the regulatory, ethical and legal requirements that affect implementation of solutions, including the need for accessibility for all users and diversity of user needs

**Relevant KSBs:** K29, S12, B3.

### STARR — applying governance and privacy controls to Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information; its classifications could create privacy, fairness, transparency and accountability risks if used out of purpose.

**Task:** Evaluate legal, ethical, regulatory and governance requirements across the end-to-end data process and make the pipeline defensible in a public-sector environment.

**Action:** I completed a DPIA before development and reviewed controls as the design evolved. I mapped the UK GDPR principles onto the pipeline concretely: purpose limitation meant using the data only for the defined analytical purpose; minimisation meant replacing unnecessary names, companies, dates, postcodes and numbers with typed placeholders before training — reducing identity signal reaching the model while recognising the retained source still needs access, retention and lawful-purpose governance; security meant controlled environments and controlled output stores; accountability meant retaining the DPIA, decision records, lineage and tests. The lawful basis and any statutory power come from the approved DPIA rather than being guessed in discussion. Model provenance formed part of selection, and I chose an established, explainable TF-IDF/LinearSVC pipeline with classifications documented as advisory under human review — keeping the solution clear of Article 22's restriction on solely automated significant decisions.

**Result:** The design reduced unnecessary personal-data signal in the model feature and made model use easier to explain and challenge. The DPIA, retention/access controls and controlled-environment evidence are needed to show the identifiable source data itself was governed.

**Reflection:** Governance is a lifecycle activity, not a one-off approval; I would link DPIA and control reviews to material changes in data, purpose, model, users or infrastructure.

### STARR — protecting personal data in a Companies House modelling pipeline

**Situation:** In a pipeline using Companies House filings, otherwise public documents could still contain director names or personal information — and public availability does not stop it being personal data or supply a lawful basis.

**Task:** Ensure model development did not unnecessarily retain personal information or create leakage risk.

**Action:** I applied privacy by design during cleaning, replacing names, company names, dates, postcodes and numbers with typed placeholders so they were not raw model features. The notebooks prove that transformation, though their saved data retains the original description and shows a local demonstration rather than the controlled AWS/Oracle route — if that route is a separate workplace pipeline, its architecture and access-control artefacts are needed and the separation should be stated.

**Result:** The modelling workflow could be demonstrated without raw identifiers as training features; controlled access to retained source data is a separate workplace result.

**Reflection:** Public availability does not remove the need for data minimisation. I would still document lawful purpose, retention, access roles and dependency/model-licence checks for the specific implementation.

### STARR — reviewing an existing product with a WCAG specialist

**Situation:** On another project, an existing product lacked evidence it met the accessibility needs of all users — a live issue for a public-sector body, where WCAG conformance at Level AA is a legal requirement for digital services.

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

**Action:** I reviewed the feedback, limited the display to more confident matches and added explanatory wording about what the scores meant and how predictions should be used — treating cognitive clarity and plain language as accessibility requirements alongside the technical checklist.

**Result:** The dashboard presented less distracting information and clearer context for interpreting model suggestions.

**Reflection:** Accessibility includes cognitive clarity and language matched to the audience. I would test the revised presentation with representative analysts, SMEs and accessibility users and retain the evidence.

### Technical notes — clarification knowledge

- **UK GDPR principles (seven)** — lawfulness/fairness/transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability.
- **Lawful bases (six)** — consent, contract, legal obligation, vital interests, public task, legitimate interests.
- **Special-category data** — racial/ethnic origin, political opinions, religious/philosophical beliefs, trade-union membership, genetic data, biometric data, health, sex life, sexual orientation. **Equality Act protected characteristics** — age, disability, gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual orientation.
- **DPIA** — required where processing is likely high risk; records nature/scope/context/purpose, necessity and proportionality, risks to people, controls, residual risk, consultation and approval; starts before processing, revisited on material change.
- **Article 22** — restricts solely automated decisions with legal or similarly significant effects unless a valid condition and safeguards apply; meaningful human review requires understanding, evidence and authority to override.
- **UK vs EU GDPR** — the UK incorporated EU GDPR into law as UK GDPR/DPA 2018 on leaving the EU; near-identical, with differences in scope (national security/immigration), age of consent (13 UK vs 16 EU default) and enforcement (ICO vs EDPB/member-state authorities). International transfers rely on adequacy regulations or appropriate safeguards (standard contractual clauses, binding corporate rules).
- **Wider frameworks** — UK responsible-AI principles (safety/security/robustness; transparency and explainability; fairness; accountability and governance; contestability and redress); OECD AI guidelines; EU AI Act (risk-based tiers: banned / high-risk regulated / transparency duties / minimal).
- **Legal and commercial checks** — dependency and model licences, IP, supplier contracts, data-sharing conditions, processing roles, retention duties, support status, right to audit.
- **Accessibility — WCAG** — WCAG 2.2 is the current W3C standard; conformance levels A, AA, AAA. **UK public-sector websites and apps are legally required to meet Level AA** (Public Sector Bodies Accessibility Regulations). Core practice: keyboard operation, visible focus, semantic structure, text alternatives, labels and error messages, contrast, zoom/reflow, captions, no colour-only signals; test with automated checks plus keyboard, screen-reader and representative-user testing. WCAG 2.2 adds criteria for cognitive and learning disabilities, low vision, mobile and input methods.
- **Diversity of user needs** — different cultural, social, economic and ability backgrounds; interface diversity (assistive technology, devices, language, technical confidence) **and data diversity** — unrepresentative training sets produce biased models (e.g. facial recognition misclassifying dark-skinned women); diverse data improves generalisation and equity. Gather user feedback and incorporate diverse perspectives into design.

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

### Technical notes — clarification knowledge

- **Own currency** — continuous learning (courses, certifications, workshops), reading and research (journals, papers, articles), networking (professional groups, conferences, online communities).
- **Team development** — training programmes, mentorship, knowledge-sharing sessions, encouraging a learning culture.
- **Professional growth** — set development goals with plans; regular performance/skills reviews; coaching and recognition.
- **Personal growth** — work-life balance, soft-skills development (communication, leadership, teamwork), supporting broader interests.
- Be ready to name specific courses, books and articles read, with a brief reaction to each, and any professional-community membership.

## Explains how they selected and applied the most effective/appropriate AI and data science techniques to solve a complex business problem in line with organisational and regulatory requirements

**Relevant KSBs:** B5, B8; cross-reference S26.

### STARR — evidence-led selection for a regulated Hubble deployment recommendation

**Situation:** Hubble needed to map inconsistent, often untagged account descriptions to standard taxonomy concepts. The data was large, imbalanced and domain-specific (826 engineered labels, of which the 141 with sufficient examples were modelled), and HMRC required secure, explainable, supportable processing.

**Task:** Choose and apply a technique that solved the business problem at scale while meeting organisational policy, data-protection, security, infrastructure, cost and maintenance requirements.

**Action:** I defined the problem and success criteria before recommending a model, framing it deliberately: the required output was a taxonomy classification; labelled data existed (tagged items), so supervised classification fitted; the data was unstructured text, pointing to NLP pipelines. **Applying the techniques:** the pipeline extracted and cleaned millions of rows, canonicalised high-cardinality identifiers and created fixed seeded splits; I established baselines first, then evaluated classical models, MPNet/e5 embeddings, SEC-BERT and CNN/neural alternatives using macro-F1, per-class measures, confusion/residual analysis, stratified CV and bootstrap intervals — accuracy alone hid minority-class performance — alongside training/inference time, model size, CPU/GPU needs, explainability, provenance, maintainability and deployment complexity. On the common holdout LinearSVC recorded 0.800 macro-F1 against CNN 0.808 and SEC-BERT 0.823 with overlapping intervals; the label-space remap for the neural/transformer heads remains outstanding before the cross-family difference is treated as final. **Organisational and regulatory constraints shaped the choice directly:** the DPIA and minimisation requirements shaped the features; explainability expectations favoured inspectable coefficients over a fine-tuned transformer; infrastructure reality (CPU estate, GPU scarcity) and provenance/assurance concerns weighed against SEC-BERT; and delivery had to fit the supported R workflow with controlled ODC/Oracle delivery (internal artefacts needed for the DPIA, integration and user changes).

**Result:** The evidence supports an operational recommendation for TF-IDF plus LinearSVC: CPU-compatible, directly inspectable and free of SEC-BERT's lifecycle burden for an uncertain point-estimate gain. Until workplace status is confirmed, call this a validated comparison and deployment recommendation, then separately describe any internal production outcome with evidence.

**Reflection:** The most effective technique is the one that meets the complete business and regulatory need, not the highest laboratory score. My CPD let me test modern methods credibly while judgement favoured the simpler recommendation. Before formal deployment evidence I would fix the decision-matrix key, group splits by filing, add time/taxonomy validation, define acceptance thresholds, verify test/production parity and implement monitored human oversight.

### Technical notes — clarification knowledge

- **Framing a problem to select a technique** — What output is wanted? What input data does that need, and does it exist? Is ML needed at all, or do rules/statistics suffice? Supervised (prediction/classification with labels) or unsupervised (pattern discovery, anomaly detection)? Regression (continuous) or classification (categorical)? Structured or unstructured data? Answering these in order narrows the algorithm choice.
- **Then apply constraints** — platform restrictions, GDPR lawful basis and PII handling, explainability requirements (which can rule out deep learning), cost and infrastructure. Only then experiment across remaining candidates with appropriate metrics.
- **Application steps** — data preparation (collect, clean, preprocess), model development (build/train with appropriate tools), validation and testing (unseen data, agreed performance standards).
- **Compliance** — data privacy and security measures, bias/fairness/transparency handling, documentation and reporting for accountability.

---

# Technical answer bank

Pure revision notes for "what does that mean?", "how does X work?" and "strengths and weaknesses?" follow-ups. Give a plain-English explanation first, then the formula. Examiner guidance says common algorithms to be able to explain are: **SVM, decision trees, Naive Bayes, neural networks, K-means, PCA and Apriori** — all covered below. Applied Hubble examples live in the STARRs above, not here.

## Learning paradigms

- **Supervised** — learns from labelled examples to predict labels for new cases (regression, decision trees, SVM, neural networks).
- **Unsupervised** — finds structure without labels (K-means, hierarchical clustering, PCA, Apriori, anomaly detection).
- **Semi-supervised** — small labelled + large unlabelled set (self-training, label propagation, pseudo-labelling); useful when labelling is expensive.
- **Self-supervised** — the model generates its own targets from raw data (masked words); underpins LLMs and BERT pre-training.
- **Reinforcement** — an agent learns a policy from rewards through interaction with an environment (Q-learning, SARSA, Deep Q-Networks); robotics, game AI, control.
- **Deep learning** — multi-layer neural networks learning hierarchical representations; **generative AI** — models that produce new content (text, images) from learned distributions.
- **Data mining** — discovering hidden patterns, trends and relationships in large datasets (clustering, association rules, anomaly detection).
- **Data quality dimensions** — accuracy, completeness, consistency, validity, timeliness, uniqueness, lineage, relevance.

## Overfitting, validation and imbalance

- **Overfitting** — learns training noise: high train, low test performance; mitigate with regularisation, simpler models, more data, dropout, early stopping, pruning, CV. **Underfitting** — too simple: poor on both; mitigate with better features, more capacity, less regularisation. **Bias–variance trade-off** — total error ≈ bias² (oversimplification) + variance (sensitivity to the training sample) + irreducible noise.
- **Train–validate–test** — train fits parameters; validation tunes hyperparameters; test is unseen data used once at the end. **Cross-validation** folds train/validate together: K folds, train on K−1, validate on the held-out fold, rotate, average; **stratified** CV keeps class proportions per fold. Fit data-derived preprocessing inside each training fold to avoid leakage.
- **Imbalance handling** — accuracy misleads (always-majority can score 99%); use class weighting (weight ≈ N/(K·n_k)), oversampling/**SMOTE** (synthetic minority examples by interpolation), undersampling, and macro-F1/per-class metrics/AUC rather than raw accuracy.

## Classification metrics

Per class one-versus-rest: **TP** (predicted, correct), **FP** (predicted, wrong — Type I error), **FN** (missed — Type II error, often the dangerous one in safety contexts), **TN** (correctly rejected). The **confusion matrix** tabulates these across classes.

- **Accuracy** = (TP+TN)/total — overall correctness; misleading under class imbalance.
- **Precision** = TP/(TP+FP) — of everything predicted positive, how much was right; use when false positives are costly.
- **Recall (sensitivity)** = TP/(TP+FN) — of all real positives, how many were found; use when false negatives are costly.
- **F1** = 2PR/(P+R) — harmonic mean of precision and recall; penalises extreme imbalance between them (high precision with near-zero recall still scores low). *Recall vs F1 (past question):* recall only measures coverage of true positives; F1 balances that coverage against precision.
- **Macro-F1** — unweighted mean of per-class F1 (every class equal — rare classes count); **micro-F1** aggregates TP/FP/FN first (dominated by frequent classes); **weighted-F1** weights by class support.
- **Specificity** = TN/(TN+FP) — true-negative rate.
- **ROC curve / AUC** — recall vs false-positive rate across thresholds; AUC is the probability a random positive ranks above a random negative (1.0 perfect, 0.5 random). For heavily imbalanced data prefer the **precision–recall curve** and average precision. **Balanced accuracy** = (sensitivity + specificity)/2.

## Regression metrics

- **MAE** = mean(|y−ŷ|) — average absolute error; robust to outliers; same units as target.
- **MSE** = mean((y−ŷ)²) — penalises large errors; differentiable; squared units.
- **RMSE** = √MSE — same units as target, strongly penalises large errors.
- **R²** = 1 − SS_res/SS_tot — proportion of variance explained (can be negative for a poor fit); **adjusted R²** penalises unnecessary features.
- **Median absolute error** — even more robust than MAE; good answer for evaluation under poor data quality.

## Classic algorithms — how each works

- **Linear regression** — Y = β₀ + β₁x₁ + … + ε, fitted by least squares (convex, single global minimum; normal equation or gradient descent). Assumes linearity, independent errors, constant variance, normal errors for inference.
- **Logistic regression** — sigmoid P = 1/(1+e^−z) over a linear combination, thresholded to classify; interpretable coefficients, probabilistic output; linear boundary.
- **Naive Bayes (past question)** — Bayes' theorem, P(class|features) ∝ P(features|class)·P(class), with the "naive" assumption that features are conditionally independent given the class, so the likelihood factorises into a product of per-feature probabilities. Fast, strong text baseline, works with little data; the independence assumption is unrealistic and calibration is poor. Variants: Multinomial (word counts — the text one), Gaussian (continuous), Bernoulli (binary). Generative (models the data per class), versus logistic regression's discriminative boundary-learning.
- **Decision tree** — recursively split on the feature/threshold that most reduces impurity: **Gini** = 1 − Σp_k², **entropy** = −Σp_k·log₂p_k, **information gain** = parent entropy − weighted child entropy. Easy to explain, handles non-linearity; overfits easily and is unstable. Algorithms: ID3, C4.5, CART (binary splits; basis of random forest and boosting).
- **Random forest** — ensemble of trees via bagging (bootstrap samples) plus random feature selection at each split to decorrelate trees; majority vote/average. Lower variance than one tree; gives feature importance; less interpretable, heavier.
- **Gradient boosting (XGBoost/LightGBM/CatBoost)** — trees built sequentially, each correcting the previous ones' errors via gradient descent in function space; typically higher accuracy than random forest but easier to overfit and more tuning.
- **SVM / LinearSVC** — finds the maximum-margin separating hyperplane: minimise ½‖w‖² + CΣmax(0, 1−yᵢ(w·xᵢ+b)); prediction is the sign (binary) or argmax of per-class scores (one-versus-rest). **C** trades margin width against violations (small C = soft margin, large C = overfit risk). The **kernel trick** (RBF, polynomial) implicitly maps to a higher-dimensional space for non-linear boundaries, at scaling cost; linear SVMs suit large sparse text.
- **KNN** — lazy, non-parametric: classify by majority vote of the K nearest training points. No training phase; expensive at prediction, needs feature scaling, curse of dimensionality.
- **K-means** — minimise Σ‖x − centroid‖²: assign points to nearest centroid, recompute centroids as means, repeat to convergence. Choose K by elbow method or silhouette score (−1 to 1: cohesion vs separation). Fast and scalable; needs K, sensitive to outliers/initialisation (K-means++ helps), assumes compact clusters. **Hierarchical clustering** builds a dendrogram (agglomerative/divisive; linkage: single, complete, average, Ward); no K needed, O(n²)+ cost. **DBSCAN** groups dense regions and labels sparse points noise; handles irregular shapes.
- **PCA** — finds orthogonal directions of maximum variance via eigen-decomposition/SVD of the covariance matrix; project onto top components ranked by explained variance. Reduces dimensionality and noise, removes correlated features; components are linear combinations (not directly interpretable); standardise features first.
- **Apriori** — frequent-itemset mining for association rules: **support**(A) = fraction of transactions containing A; **confidence**(A→B) = support(A∩B)/support(A); **lift**(A→B) = confidence/support(B) (>1 means positive association). Builds up itemsets, pruning below minimum support at each step. Market-basket-style analysis.

## Text representation

- **TF-IDF** — TF(t,d) × IDF(t) where IDF = log(N/df(t)) (smoothed variants add 1s); usually L2-normalised. Common words down-weighted, distinctive terms up-weighted. Fast, CPU-friendly, interpretable, strong with sparse linear models and domain-specific text; no synonym/context understanding, vocabulary drift.
- **N-grams** — unigram/bigram/trigram features capture phrase-level meaning at the cost of feature count and sparsity.
- **Embeddings (Word2Vec, MPNet, e5, BERT-style)** — dense vectors capturing semantic similarity, so related phrases group together across different wording; less interpretable, slower, and generic pre-training can miss specialist domain language — TF-IDF often wins on domain-specific tasks with distinctive vocabulary.

## Neural networks and transformers

- **How a neural network works (past question)** — input layer takes feature values; hidden layers of nodes connect by weighted links. Each node computes a weighted sum plus bias, z = Σwᵢxᵢ + b, then applies a non-linear **activation** (feed-forward). The output layer produces the prediction — softmax over classes for classification, a single node for regression. The loss (cross-entropy for classification, MSE for regression) is computed against labels, and **backpropagation** applies the chain rule to compute each weight's gradient, ∂L/∂w; **gradient descent** updates weights opposite the gradient, w ← w − η·∂L/∂w, batch by batch; a full pass through the data is an **epoch**. Repeat until converged — the final weights are the model parameters.
- **Training decisions** — architecture (layers, sizes), activation functions, loss function, optimiser (SGD, momentum, Adam), learning rate (too large diverges, too small crawls), batch size, epochs, early stopping, dropout.
- **Activations** — sigmoid (0–1, binary output; vanishing gradients), tanh (−1–1, zero-centred), ReLU = max(0,z) (hidden-layer default; dying-ReLU risk; Leaky/PReLU/ELU variants), softmax (multi-class output distribution).
- **CNN** — convolutional filters learn local patterns (image regions; phrase-like patterns over token sequences), pooling downsamples; fully connected layers classify. **RNN/LSTM** — sequential hidden state; LSTM input/forget/output gates mitigate vanishing gradients; largely superseded by transformers for NLP.
- **Transformers/BERT** — self-attention Attention(Q,K,V) = softmax(QKᵀ/√d_k)V lets every token attend to every other token in parallel. BERT: bidirectional encoder, pre-trained with masked-language modelling (and next-sentence prediction), WordPiece tokenisation, `[CLS]` for classification; BERT-Base has 12 layers/768 dims/12 heads. RoBERTa trains longer without NSP; domain models (e.g. SEC-BERT for financial text) add specialist pre-training. Strengths: context and long-range dependencies. Weaknesses: GPU needs, slow inference, explainability, provenance/supply-chain risk.

## Hyperparameter tuning

Hyperparameters control learning and are set around training (split ratio, learning rate, optimiser, activation, loss, layers/units, dropout, epochs, K in clustering, kernel/filter size, batch size); parameters (weights) are learned. Techniques: **grid search** (exhaustive), **random search** (samples; often nearly as good, cheaper), **successive halving** (more resource to promising candidates), **Bayesian optimisation** (e.g. Optuna — uses prior trials to choose the next ones). Select on validation/CV performance; avoid tuning-time overfitting with more data, early stopping, not chasing the single top score, dropout and pruning; confirm on one final untouched holdout.

## Statistical tests

- **Paired t-test** — `t = mean(d)/(sd(d)/√n)` on paired score differences (e.g. two models on the same folds); controls for split difficulty; assumes roughly normal differences. Statistical significance ≠ practical significance — always consider effect size and cost.
- **Welch's t-test** — `t = (m₁−m₂)/√(s₁²/n₁ + s₂²/n₂)`; independent group means with unequal variances (check with an F-test first); safer than Student's pooled t-test in that case.
- **Z-test** — compares means/proportions via the normal distribution; needs large samples (n ≥ 30) and known variance, or adequate counts for proportions.
- **Chi-square** — `Σ((O−E)²/E)`; association between categorical variables or goodness-of-fit; needs adequate expected counts; association, not causation.
- **ANOVA** — compares means across 3+ groups (one-way/two-way) without inflating error from many pairwise t-tests.
- **Quick recall** — t/Z-tests compare means (small vs large samples); chi-square tests categorical relationships; ANOVA compares 3+ group means.
- **Bootstrap intervals** — resample to express uncertainty in a metric; overlapping intervals between models justify caution about superiority claims; the stronger design bootstraps the paired difference.

## Drift and monitoring

- **Types** — data drift (input distribution shifts), concept drift (input→output relationship changes), prediction drift (output distribution changes before labels arrive), label/taxonomy drift, upstream/extraction drift.
- **Detection** — compare training vs production distributions: **PSI** (bin both; Σ(A−E)·ln(A/E); <0.10 none, 0.10–0.25 moderate, >0.25 significant — works for numeric and categorical, threshold-based), **KS test** (continuous, significance-based), **chi-square** (categorical). Track performance on recent labelled data with a sliding window for concept drift.
- **Response** — confirm the drift type, contain risk, collect fresh labels, retrain, re-validate, redeploy, reset baselines.
- **KPIs under poor data quality** — raw accuracy and R² mislead ("garbage in" behind a plausible number); prefer MAE/median absolute error, stability trends, drift KPIs (PSI, missing-rate), confidence/coverage rates, override and rollback rates, cost of wrong predictions.

## Lifecycle, DataOps and MLOps

- **CRISP-DM** — business understanding → data understanding → data preparation → modelling → evaluation → deployment. (**SEMMA**: sample–explore–modify–model–assess.) The operational pipeline expands to: problem definition with KPIs → collection → EDA → cleaning/preprocessing → feature engineering → split → model selection → training → evaluation → tuning → deployment → monitoring and retraining.
- **DataOps** — collaboration, automation, reuse, analytics-as-code, testing, monitoring, short cycles, data-driven improvement.
- **MLOps** — reproducibility (retrain an old model, get comparable results), accountability (trace production output to code/data/model/parameters), versioned collaboration, continuous testing, continuous monitoring, reusable infrastructure.

## Communication by audience

Senior managers — business problem, value, risk, cost, timescale, decisions needed; translate metrics into consequences. Analysts — examples, confusion matrices, per-class reliability, how to use outputs. SMEs — domain meaning, edge cases, correctness. DevOps/engineers — infrastructure, dependencies, runtime, tests, monitoring. Governance reviewers — DPIA, minimisation, security, limitations, human oversight, auditability.

## Generic frameworks for open-ended questions

- **Selecting the right technique** — start with the business decision and KPIs, not the model; check whether ML is needed at all; map to a task type; assess data readiness (labels, quality, leakage, freshness); build a fast interpretable baseline; choose via a decision matrix against interpretability, performance, latency and governance — the simplest model that meets all requirements; validate with risk-aligned metrics; treat monitoring/retraining as part of the solution.
- **Disseminating practice** — standardise (methodologies, templates, documentation), enable (communities of practice, wikis, training), provide reusable assets, embed governance, demonstrate value through pilots, make results visible, foster culture with sponsorship.
- **Tracking trends** — research and publication tracking (arXiv, major labs), vendor/ecosystem monitoring, adoption-pattern analysis, community engagement (forums, conferences), hands-on PoCs — then filter hype by scalability, cost/benefit and governance fit before recommending adoption.
- **Managing resistance to AI** — understand the concern (jobs, trust, competence), involve users early, show augmentation not replacement, train, start with low-risk wins, keep humans in control of decisions.

## Risks of adopting AI (and mitigations)

Data (quality, privacy, access control) · model (bias, opacity) · operational (drift, latency, weak monitoring) · business (wrong predictions, over-dependence eroding oversight) · security (adversarial inputs, data poisoning, supply chain) · compliance (missing audit trails, no approval process) · skills/adoption (gaps, resistance) · financial (cost exceeding unclear benefit) · ethical/societal (unfair impact, loss of accountability). **Mitigations:** data governance and quality controls; least privilege; validation and explainability (SHAP/LIME); drift and performance monitoring; meaningful human review; adversarial/security testing; formal approval and audit; training and change management.

---

# Final evidence and rehearsal checks

**Evidence checks**

- Verify the strongest numerical claims and bring an artefact where possible: 233% more extracted data, DAP growth to 150+ users, days rather than nine months, identified tax risk, model scores, the 80% assessment result.
- Keep label counts straight: 826 labels survived preprocessing; 141 met the frequency threshold and were modelled; 685 were excluded.
- Treat the current scores as proof-of-concept estimates: the split is row-level, not grouped, and the CNN/SEC-BERT heads need remapping before a final cross-family claim.
- Quote like-for-like: macro-F1 0.800/0.808/0.823 with overlapping intervals; LinearSVC minutes-vs-hours training, sub-second-vs-minutes inference, megabytes-vs-gigabytes size. State the hardware.
- Correct the decision-matrix interpretability key and sensitivity-test the weights before quoting its numeric ranking.
- Be precise about prototype versus production: the code establishes TF-IDF with LinearSVC as an operational **recommendation**, not proof of deployment; add the internal release/approval artefact before saying it was deployed.
- Do not imply Hubble makes tax decisions — it categorises data to support analyst judgement with a human in the loop.
- Where evidence is knowledge rather than a completed workplace action, say so clearly and connect it to the decision made; do not invent a project.
- For each answer, be ready to name: the artefact, another person who saw the work, the business outcome, the principal trade-off, the largest risk and what would be improved next.

**Discussion technique**

- Speak in the first person — "I", not "we"; the assessment is of my work.
- Replay the question back before answering; use the KSB language in the answer.
- State my role and responsibilities early; reference the journal/portfolio artefacts by name.
- Use STARR to structure answers; always connect the technique to the business value.
- If asked about an algorithm I have not studied in depth, give the high-level view honestly and say I have not explored its mathematical foundations, rather than improvising.
- Cue cards/notes are allowed — the journal is a memory aid, not a submission.
