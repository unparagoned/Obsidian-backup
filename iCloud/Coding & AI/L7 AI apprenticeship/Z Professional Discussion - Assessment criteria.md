**Artificial Intelligence Data Specialist, Level 7 Apprenticeship**
**Learner:** Jesse Karadia
**Organisation:** HMRC

This document organises professional-discussion preparation around the EPA assessment criteria. Each criterion has the relevant KSBs, one or more STARR answers containing all the applied evidence (what I did, with the technical specifics), and a technical-notes block covering the pure knowledge that the criterion's clarification expects. Technical notes pull in the relevant revision material from past-learner notes (definitions, techniques, frameworks and interview-ready summaries) with no applied workplace content mixed in. The Technical answer bank at the end remains the cross-cutting revision pack for algorithm maths and follow-up questions.

Use the STARRs as speaking notes rather than a script. Speak in the first person ("I", not "we"), adapt the depth to the question, and be ready to name supporting artefacts such as test results, decision matrices, GitLab issues, dashboards, DPIAs, stakeholder feedback, wiki guidance and experiment records. The grading table assesses KSBs collectively within each theme, so the per-criterion KSB lists are a practical evidence map rather than official marking units.

## Evidence boundary and status

The EPA clarification repeatedly requires my own practical application in my current role and organisation. The notebooks in `Code/` are technical artefacts, not a substitute for workplace evidence about deployment, users, governance or business impact. Three evidence categories are used throughout this document.

- **Code-backed:** directly demonstrated by source code or saved output in `Code/`.
- **Workplace evidence:** statements about internal Hubble, HMRC systems, stakeholders, deployment or impact. These need an approved artefact or witness as well as my explanation.
- **Proposed/future:** a control or improvement that I can justify but must not describe as implemented.

The public notebooks use Companies House accounts and deliberately simplify the internal implementation. The public version is a Python/BeautifulSoup extraction of description and concept only, whereas the internal extraction is R-led, integrates R, Python and SQL, and captures contextual features such as table name and heading. I should present the notebooks as reproducible corroboration of the methodology and experiments, then use separate workplace artefacts to prove the internal architecture, operational scale, user changes and business outcome.

### Code artefact map

| Artefact                           | Demonstrates                                                                                                                                                     |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `00_ixbrl_data_extraction.ipynb`   | Python parser over a Companies House monthly accounts archive. Table descriptions and iXBRL concept labels saved to Parquet.                                     |
| `01_ixbrl_eda_preprocessing.ipynb` | EDA, ambiguity and imbalance analysis, text cleaning, canonicalisation, label engineering, embedding comparisons and fixed seeded splits.                        |
| `03_ixbrl_experiment_models.ipynb` | Classical-model search, stratified CV, TF-IDF and embedding comparisons, bootstrap intervals, robustness cases, LIME/SHAP and the final LinearSVC configuration. |
| `04_ixbrl_nn.ipynb`                | Optuna-led neural-network and CNN experimentation, class-weighting tests and robustness testing.                                                                 |
| `05_xbrl_transformers.ipynb`       | Hugging Face and PyTorch transformer comparison, SEC-BERT tuning, sampling and weighting experiments, explainability and resource trade-offs.                    |
| `06_compare_models.ipynb`          | Three-model comparison using objective measures, confidence intervals and an operational rubric.                                                                 |

### Key figures to quote

- Corpus: a Companies House monthly archive of 298,461 accounts, giving 2,857,703 extracted rows across 956 raw concepts (266,178 unique descriptions; mean 7.77 words; mode 2; max 1,762; 19,814 punctuation-only rows). After cleaning: 2,466,052 rows and 826 engineered labels (mean 3.07 words; mode 1; max 15). Modelling used the 141 labels with at least 350 examples each, and the 685 rarer labels were excluded.
- Descriptive EDA: top 75 raw concepts cover about 95% of items; after cleaning the top 50 labels cover 95%. Word-count distributions are long-tailed (rough bell shape with a long right tail); boxplots of the top labels show IQR typically between 2 and 7 words.
- Inferential EDA on the label-frequency distribution (`powerlaw`): raw counts fit a lognormal better than a power law (R=−6.12, p=0.020 vs lognormal; strongly reject exponential). After preprocessing the lognormal preference weakens (R=−2.89, p=0.111). Unsupervised representation check: silhouette on known labels peaked around 0.477–0.53 for tuned n-gram TF-IDF (MPNet about 0.467).
- A fixed seeded 80/10/10 train/test/holdout split was used, with a 10,000-row holdout sample for like-for-like model comparisons.
- The top 75 raw concepts cover about 95% of items, and generic descriptions such as "Total" map to many different concepts. This ambiguity and long tail is what motivated contextual features and macro-F1.
- The final classical pipeline was word TF-IDF with 1-to-3-word n-grams, IDF weighting and L2 normalisation, feeding a LinearSVC with `C=2.8`, an L1 penalty, squared-hinge loss and balanced class weights.
- Holdout comparison (accuracy and macro-F1): LinearSVC **0.975 and 0.800**, CNN **0.977 and 0.808**, SEC-BERT **0.977 and 0.823**. The 95% bootstrap intervals overlap, so SEC-BERT's roughly two-point macro-F1 advantage is a point-estimate difference, not a statistically established improvement.
- Operational measures (training time, full-test inference time, model size): LinearSVC about 2.5 minutes, 0.6 seconds and 8 MB. CNN about 44 minutes, 24 seconds and 30 MB. SEC-BERT about 67 minutes, 143 seconds and 1.8 GB. The MLflow run names show the three compared runs were trained on 10% square-root-weighted samples of the training data, so quote the training times as belonging to those runs. The hardware is not recorded in the notebooks, so state it before generalising these figures.
- Statistical comparison during model selection: the classical search used paired t-tests over the cross-validation folds at the 95% confidence level. SVC (0.774) and PassiveAggressive (0.755) were significantly worse than the leading configuration, and models that were not significantly worse on the 1% population went forward to the full population. Square-root-weighted training samples were significantly better than the plain population. The final three-model comparison used bootstrap confidence intervals instead, which answer a different question.
- Embeddings: on the standard 1% run MPNet (0.7793) beat TF-IDF (0.7761) by about 0.003 macro-F1, a difference that was statistically significant at the 95% level, but it cost roughly 67 times the fit time (9,602 seconds against 143). e5 came second (0.7781) and was not significantly worse than MPNet. On the later square-root-weighted 1% run, TF-IDF (0.7704) was not significantly different from the top score at 95%. Keep the two runs separate when quoting them.

### Limitations to state rather than hide

- The split stratifies individual rows rather than filings or descriptions, so related rows can cross partitions and the saved metrics may be optimistic. Production evidence needs a grouped (filing or company level) or temporal holdout.
- The CNN and transformer output layers cover all 826 labels even though only 141 have training examples. They should be remapped to the 141 classes and rerun before the cross-family ranking is treated as final.
- The decision matrix defect is confirmed in the code: `subjective_inputs` uses the key `interpretability_explainability` while `metric_config` expects `interpretability`, so interpretability is silently dropped from the calculated scores (0.567, 0.476 and 0.218 for LinearSVC, CNN and SEC-BERT). The subjective ratings and min-max scaling over only three candidates are also sensitive to the weights. Correct the key and run a sensitivity test before quoting the numeric ranking. The qualitative conclusion, that LinearSVC is favoured operationally, still stands. One design strength worth stating: the matrix applies a confidence penalty (a 0.35 factor) to any metric where a model's confidence interval overlaps the best model's, so uncertain wins are not over-rewarded.
- Canonicalisation reduces identity signal in the model feature. It does not anonymise the source data, and it does not replace access, retention and lawful-purpose controls.
- Fairness metrics and live drift monitoring are proposed work, not implemented controls. The notebook records a specific plan: detect bias by checking regional names and sexes, assess fairness with demographic parity and equalised odds, and mitigate through re-sampling, re-weighting or a separate model where the classifier works less well for smaller companies. None of that is implemented. What was analysed is class imbalance, per-class performance, robustness and residual errors.
- The CNN output head is confirmed in the code as sized from all unique encoded labels (`num_classes = len(dataset_pl[y].unique())`), and no grouped splitter (`StratifiedGroupKFold` or similar) appears anywhere, so the remap and grouped-split work genuinely remains outstanding.
- The notebooks prove a validated model comparison and a sound research method. They do not prove deployment, live monitoring, user acceptance, accessibility testing or business benefit.

## Evidence gaps: search for `TODO:`

Technical notes under each criterion now include the relevant clarification knowledge from `Z Professional Discussion - from past learners.md` (cleaned of interview fluff and IT-ops-only examples where needed). Items marked **Resolved from code** are backed by `Code/` notebooks; remaining TODOs are still workplace artefacts or unfinished experiments.

### Theme 1

- **T1.1:** Resolved from code: descriptive EDA (counts, word-length distributions, Pareto), inferential distribution tests (`powerlaw` R/p), silhouette embedding checks, supervised NLP comparison and the rejection of vision/RL are now in the STARR. TODO: a verified measure of extra analytical coverage, manual effort avoided or profiling improvement attributable to classification specifically (not extraction generally).
- **T1.2:** TODO: remap the 141 classes and rerun CNN/SEC-BERT on the same grouped split (confirmed outstanding in the code). Resolved from code: statistical comparison design (paired t-tests over five CV folds at 95%; bootstrap holdout CIs); Dummy baseline ~0.007 macro-F1; sqrt-weighting lift; decision-matrix CI-overlap penalty (0.35). TODO: extract exact p-values/effect sizes from saved results if a precise figure is needed. TODO: acceptance-testing record (date, users, criteria, blank-description and dimensional-data changes). TODO: usability-testing record (dashboard task, confusion evidence, change made, retest). TODO: natural-vs-numeric key benchmark status.
- **T1.3:** Resolved from code for Hubble maths STARR: TF-IDF IDF/L2, LinearSVC objective, macro-F1 rationale, MPNet vs TF-IDF significance vs practical cost, power-law/lognormal tests and silhouette scores are quoted from `Code/`. TODO: agent-risk Welch test details (safe sample sizes, statistics, p-value, CI, effect size, confirm the "99% confidence" wording and name the artefact).
- **T1.4:** TODO: artefact showing the R-to-Python and Oracle-output boundary and an integration issue resolved. TODO: a specific commercial-benefit measure from the mixed-language design. (The simulation claim is already kept narrow in the STARR, so that item is done.)
- **T1.5:** TODO: HMRC's classification of enterprise/private/public components plus a nameable architecture or security document. TODO: ODC configuration, volumes, runtimes and stability evidence. TODO: S3 proxy details (dataset, user group, approval flow) and evidence it worked. TODO: auto-scaling cost comparison record. TODO: verify the "days rather than nine months" timeline and name a witness.
- **T1.6:** TODO: the exact workplace interfaces implemented (Oracle driver, `dbplyr`, Solr endpoint, S3 proxy, FSx). Resolved from code: the public Parquet interfaces are Pandas `to_parquet` in the extraction notebook and Polars `read_parquet`/`write_parquet` in the EDA notebook. TODO: what "roughly 128 concurrent" means (workers, cores or documents) and the observed bottleneck. TODO: Oracle/Parquet before-and-after workflow and analyst reuse. TODO: LLM-to-Solr status (built, prototyped or proposed).
- **T1.7:** TODO: wide-to-long challenge details (owner, investigation, approval, improvement, artefact). TODO: tagged-as-supervision baseline and coverage before and after. TODO: calculation-error challenge (safe description, my role, quantified impact, what can be discussed).

### Theme 2

- **T2.1:** TODO: verify DAP growth (1 to 150+ users), the period and the definition, with a report or witness. TODO: one anonymised mentoring outcome. TODO: proof-of-concept model details and how it progressed. TODO: verify the 233% extraction increase and the "millions of pounds" claim separately.
- **T2.2:** TODO: named technical-audience meeting or artefact and an objection addressed. TODO: named non-technical artefact and the plain-language translation used. TODO: the conditions under which SEC-BERT or another assured model would become preferable.
- **T2.3:** TODO: internal dissemination titles, dates, audience, reuse and one changed practice. TODO: where and when Graffiti was shared, the audience, feedback and one concrete reuse.
- **T2.4:** TODO: the specific reports and papers reviewed and the social or public-sector implications drawn. TODO: AI-guidance change record (date, feedback, decision-maker, revised wording). TODO: grounded-LLM justification sources, safeguards and external feedback.
- **T2.5:** TODO: DAP licence and compute decision record. TODO: database-versus-S3 decision record. TODO: Hubble model decision record (stakeholder preferences, pre-agreed weights, corrected matrix, approval route).
- **T2.6:** TODO: engineer contributors and one example where an engineer's input changed the implementation. TODO: the organisational testing, version-control or documentation standard complied with. TODO: test, CI and README evidence and a defect prevented or detected.

### Theme 3

- **T3.1:** TODO: one verified organisational outcome, distinguishing extraction impact from classifier impact. TODO: label industry impact as potential unless demonstrated. TODO: the credible societal link and counter-risks, without over-claiming.
- **T3.2:** TODO: DPIA risk categories, ratings, mitigations, owner and artefact name. TODO: blank-description and dashboard issue discovery, fix, retest and remaining limitation. TODO: distinguish operating controls from proposed drift and performance monitoring.
- **T3.3:** TODO: Graffiti before-and-after or user example. TODO: a measured team-workflow improvement (reproducibility, setup time, defects, review quality).
- **T3.4:** TODO: name the actual HMRC policies, UK GDPR requirements and approvals relevant to Hubble. TODO: who checked compliance, when, and how changes trigger reassessment.

### Theme 4

- TODO: Hubble lawful basis, controller and processor roles, retention, access roles and actual approvals from the DPIA. TODO: which identifiers were canonicalised, what remained identifiable and where processing occurred. TODO: Companies House pipeline status (same or separate, real environment, controls implemented). TODO: WCAG review details (product, date, version and level, findings, my fixes, retest). TODO: Graffiti alternative-install testing and assistive-technology checks. TODO: dashboard user-diversity evidence (roles, task, feedback, change, retest). TODO: licence, IP and contract checks actually completed, otherwise keep as knowledge. TODO: user groups actually consulted, with one need and response each.

### Theme 5

- **T5.1:** TODO: dated CPD record linking the strongest sources to decisions changed. TODO: community or conference evidence (do not imply attendance if it was online reading). TODO: link specific literature to a concrete experiment and decision. TODO: team development process and one before-and-after capability outcome. Describe informal mentoring accurately.
- **T5.2:** Resolved from code for technique-selection narrative: full compare path, holdout scores with CIs, and operational rubric are documented; keep wording as "validated comparison / deployment recommendation" until workplace status is confirmed. TODO: confirm the final model status (deployed, recommended for deployment, or validated prototype) and use one wording throughout. TODO: final production evidence if any (holdout performance, infrastructure, monitoring, acceptance, DPIA). TODO: consistency audit of scores, class counts, split, deployment status and impact claims across this document.

---

# Theme 1: Use and knowledge of computing and statistical foundations of AI and data science

**Theme KSBs:** K7, K16, K18, K19, K22, K25, S1, S16, S19, S20, S26.

**Distinction integration:** the pass answers also identify the norm challenged, the investigation, the proposed solution and its impact where that connection is natural. The standalone distinction answers remain the fullest versions.

## Describes how to use statistical, AI and machine learning methodologies such as data mining, supervised/unsupervised machine learning, natural language processing and machine vision to meet business objectives

**Relevant KSBs:** K19, K22, K25, S26.

### STARR: selecting methodologies for Hubble

**Situation:** Company accounts and tax computations are submitted as iXBRL, but some tax computations had only around 30% of their figures tagged, so conventional extraction omitted much of the available information. Hubble could extract the untagged descriptions, but the same accounting concept could be described in many different ways. That made population profiling through manually maintained regular expressions impractical.

**Task:** I needed to turn inconsistent, untagged descriptions into standard taxonomy concepts so that analysts could profile far more of the data and identify tax risk more efficiently. To do that, I had to decide which statistical, AI and machine learning methodologies actually suited the business objective, rather than assuming a particular model in advance.

**Action:** I worked through the candidate methodologies deliberately instead of selecting a fashionable model, and challenged the assumption that population analysis had to rely on tagged items or matching rules.

I started with descriptive statistics: summary measures of description length, histograms and boxplots of the distributions, and Pareto plots of concept frequency. That showed a long-tailed, heavily imbalanced label set, so accuracy alone would be dominated by common classes and minority-class metrics had to drive selection.

I then used inferential statistics: likelihood-ratio tests on the label-frequency distribution (power law vs lognormal vs exponential), paired t-tests over cross-validation folds to drop significantly worse classical models, and bootstrap confidence intervals on the final holdout comparison so overlapping intervals stopped me treating SEC-BERT's point-estimate advantage as a proven win.

I also mined patterns in the data: frequency ranks, description–concept overlap, cosine similarity between concept tokens, class balance and residual errors. That showed enough labels to train a model, but also ambiguity — generic descriptions such as "Total" mapped to many concepts — and near-duplicate taxonomy groups that would limit any model.

Supervised learning became the core method because correctly tagged items already supplied target concepts. I framed it as multi-class text classification and compared Naive Bayes, tree ensembles, SVC and LinearSVC, SGD-style models, CNN and other neural approaches, SEC-BERT, and MPNet and e5 embeddings.

The NLP pipeline parsed the iXBRL, cleaned and canonicalised the text, built n-gram or embedding features, classified, and retained prediction, score and provenance. Learned transformations were fitted on training data only and reused unchanged in production.

Unsupervised methods stayed exploratory. I used silhouette scores over known concept labels to compare how well different vector spaces separated concepts; that was a representation check, not a clustering product, and I did not deploy K-means or hierarchical clustering.

I ruled out reinforcement learning (no environment or reward signal) and machine vision (text and structure were already extractable from the iXBRL). OCR would only matter if scanned image-only PDFs entered scope.

Finally I assessed every candidate on macro-F1, accuracy, per-class results, cross-validation, bootstrap intervals, speed, infrastructure, explainability, provenance, maintainability and cost. Wider analytical coverage and faster risk profiling mattered more than the highest laboratory score.

**Result:** TF-IDF with LinearSVC was the strongest operational recommendation, even though it did not have the highest point estimate on every metric. Its holdout macro-F1 was 0.800 against 0.808 for the CNN and 0.823 for SEC-BERT, and the confidence intervals overlapped. In exchange it offered far faster CPU-only training, inspectable coefficients and lower lifecycle risk. What made the method suitable was that it met the business objective of widening coverage, reducing manual grouping and supporting faster risk profiling, not that it was technically possible.

**Reflection:** Method selection must begin with the business objective, the availability of labels, the type of data and the deployment constraints. Supervised NLP was appropriate here. Unsupervised methods stayed exploratory, and machine vision and frontier LLMs would have been disproportionate. The best technical score alone does not define the best business solution.

### Technical notes: clarification knowledge

Drawn from past-learner notes on Statistical Methods, Data Mining, Supervised/Unsupervised ML, Types of ML and Why Unsupervised Learning. Aligns to the EPA clarification's methodology list.

#### Statistical methods

Statistical methods collect, summarise, analyse and interpret data to support decisions. They split into descriptive and inferential.

**Descriptive statistics** summarise and describe the main features of a dataset. They organise, simplify and present data, and do not draw conclusions beyond the data itself. Key techniques: measures of central tendency (mean, median, mode); measures of dispersion (range, variance, standard deviation); presentation (tables, histograms, bar charts, box plots). One-liner: descriptive statistics explain *what the data shows*.

**Inferential statistics** draw conclusions or make predictions about a population from a sample, using probability and a stated confidence level. Key techniques: hypothesis testing (t-test, Z-test, chi-square, ANOVA); estimation (confidence intervals); predictive methods (regression, correlation). One-liner: inferential statistics explain *what the data means for a larger population*.

**Common hypothesis tests (interview recall)**

| Test | Use |
| --- | --- |
| t-test | Compare means; small samples / unknown σ. One-sample, independent, or paired. |
| Z-test | Compare means or proportions; large samples (n ≥ 30), known variance or adequate counts. |
| Chi-square (χ²) | Association or independence between categorical variables; also goodness of fit. |
| ANOVA | Compare means across three or more groups (avoids inflated error from many t-tests). |

Paired t-test formula on fold or score differences: `t = mean(d)/(sd(d)/√n)`. Welch's t-test for unequal variances: `t = (m₁−m₂)/√(s₁²/n₁+s₂²/n₂)`. Always pair statistical significance with effect size and practical cost.

#### Data mining

Purpose: discover hidden patterns, trends and relationships in large datasets. Techniques: clustering (group similar points); association-rule mining (items that co-occur, e.g. Apriori with support/confidence/lift); anomaly detection (unusual behaviour). Applications include fraud/risk analysis, customer behaviour, IT anomaly detection and market-basket analysis. One-liner: data mining uncovers patterns that improve performance, reduce risk and support decisions.

#### Supervised machine learning

Purpose: train on labelled data to predict or classify unseen cases. Common techniques: linear regression (continuous); logistic regression (binary); decision trees; random forests; SVM/LinearSVC; neural networks. Applications: churn, fraud, credit scoring, ticket classification, demand forecasting. One-liner: supervised learning uses labelled examples to predict outcomes.

#### Unsupervised machine learning

Purpose: find structure in unlabelled data. Tasks: clustering, pattern discovery, dimensionality reduction, anomaly detection. Algorithms: K-means, hierarchical clustering, DBSCAN, PCA. Use when labels are absent or expensive, for segmentation, exploration or to bootstrap later supervised work. A clustering result still needs domain interpretation before it becomes a business decision. One-liner: unsupervised learning finds hidden patterns without labels.

#### Other learning paradigms (clarification breadth)

- **Semi-supervised:** small labelled set + large unlabelled set (self-training, label propagation, pseudo-labelling).
- **Self-supervised:** model generates its own targets from raw data (masked-word prediction). Underpins BERT and LLM pre-training.
- **Reinforcement learning:** agent learns a policy from rewards in an environment (Q-learning, DQN). Robotics, games, control — not a fixed labelled classification problem.

#### NLP and machine vision

- **NLP:** enable machines to process human language. Techniques: tokenisation, sentiment analysis, NER, topic modelling, text classification, language models (BERT, GPT).
- **Machine vision:** interpret visual information. Techniques: image classification, object detection, segmentation (usually CNN / vision transformer based). Only needed when the signal is in images rather than already-extractable text or structure.

#### Meeting business objectives

Typical objectives these methodologies serve: improving customer retention and experience; optimising operations; increasing sales and marketing effectiveness; fraud detection; risk management; quality control. The right methodology is the one that meets the objective under data, infrastructure, explainability and governance constraints — not the most fashionable model.

## Explains how to solve problems and evaluate software solutions via analysis of test data and results from research, feasibility, acceptance and usability testing in line with organisational requirements

**Relevant KSBs:** K7, S26.

### STARR: evaluating the Hubble classification solution

**Situation:** Analysts could not practically profile the extracted untagged descriptions. The wording was inconsistent, and there were hundreds of taxonomy classes with a long tail of rare examples.

**Task:** I was responsible for defining the problem, researching feasible solutions, testing them objectively, and confirming that the chosen output was usable and met HMRC requirements for security, explainability, infrastructure and analyst adoption.

**Action:** I first defined success more broadly than headline accuracy. The solution had to classify minority concepts as well as common ones, run at operational scale, remain explainable, use supportable technology, protect data and be genuinely usable by analysts.

For research and feasibility, I compared literature, package and model documentation, and empirical results across classical machine learning, neural networks, transformers and embedding approaches. Feasibility covered much more than whether the code ran. I assessed CPU and GPU availability, memory, throughput, cost, package and model provenance, security approval, maintainability, retraining time, and whether the production estate could support the complete pipeline.

For the test design, I created fixed seeded 80/10/10 train, test and holdout flags plus a 10,000-row holdout sample so that comparisons were like for like. I used five-fold `StratifiedKFold` with `GridSearchCV` and `HalvingRandomSearchCV` for the scikit-learn models, and Optuna with MLflow tracking for the neural and transformer runs. During the classical model search I compared candidates with paired t-tests over the cross-validation folds at the 95% confidence level. Many models were significantly worse than the leading configuration, and models that were not significantly worse on the 1% population went forward to the full population, which kept the expensive full-scale runs to the candidates that had earned them. I analysed macro-F1, accuracy, precision and recall, confusion matrices, residual errors, bootstrap intervals, runtime and model size. For production evidence I moved to a chronological or unseen-taxonomy holdout, and fit all learned preprocessing (vocabulary, IDF weights). 

For robustness analysis, I built crafted adversarial, contextual, long-context, OCR-noise, Unicode and typo cases. LinearSVC beat SEC-BERT on most categories, SEC-BERT won on Unicode substitution, and both were weak on abbreviations. These small synthetic groups diagnose failure modes rather than estimate population performance.

I then involved users directly. In acceptance testing, analysts checked whether the extracted dimensions and classifications supported the agreed business use. This exposed predictions being made from blank descriptions using only surrounding headings, so I changed the production logic to return no prediction where the description was missing. It also exposed missing dimensional content, so I generalised the extraction rather than coding a narrow subset. In usability testing, users found the top-five-matches display and the raw scores confusing, so I limited the display to more confident matches and added explanatory text about what the scores meant. One request remains open: analysts asked for numeric rather than natural database keys, and I am treating that as a performance question to benchmark on real Oracle and SAS workloads rather than a preference to accept without evidence.

**Result:** TF-IDF plus LinearSVC balanced model quality with speed, explainability, supportability and security. Its holdout macro-F1 was 0.800, SEC-BERT's higher point estimate was not separated from it by the confidence intervals, and the operational rubric favoured the simpler model. The rubric's interpretability field-name defect means I would not quote its numeric ranking until that is fixed. Acceptance testing changed extraction and prediction behaviour, and usability testing made the dashboard clearer. From the notebooks this is a validated comparison and proof of concept, not proven production deployment.

**Reflection:** I learned to research established tooling before writing bespoke evaluation code. Optuna automated comparison and visualisation that I had partly built myself. I also learned that training, test and production preprocessing need a single controlled implementation so that rules like blank-description handling cannot diverge. In production I monitor extraction failures, the missing-description rate, input and prediction distributions, per-class metrics and analyst overrides, with drift tests flagging when to diagnose, contain, relabel, and retrain or roll back. In future I would agree acceptance criteria earlier, automate pipeline-parity checks and keep a traceable decision log.

### Technical notes: clarification knowledge

Drawn from past-learner notes on The Machine Learning Pipeline, KPIs for Algorithm Accuracy, Poor Data Quality, Model Drift / PSI–Chi-square, and Hyperparameter tuning. Aligns to the EPA clarification on problem solving, testing phases, analysis of test data, and evaluation.

#### Problem solving and research / feasibility

Define the business problem and success criteria first. Research candidate solutions (literature, package docs, empirical runs). Assess feasibility across technical (can it run on the estate?), operational (can the team support it?) and financial (cost, GPU, maintenance) dimensions. Do not force ML if rules or BI would solve the problem at lower risk.

#### Testing phases (software and users)

| Phase | Purpose |
| --- | --- |
| Unit | Individual components correct |
| Integration | Modules / services work together |
| System | Complete system against requirements |
| Acceptance (UAT) | End users confirm the product meets needs |
| Usability | Ease of use via interviews, task tests, surveys |

For ML specifically, also treat train/validate/test and production monitoring as part of evaluation.

#### Analysis of test data

Collect data from all phases. Use statistical methods (means, CIs, paired tests, confusion matrices, residual analysis, bootstrap intervals) to find patterns, trends and anomalies. Document findings and give stakeholders actionable recommendations. Prefer metrics aligned to business risk: F1/AUC and precision/recall under imbalance; MAE/RMSE for regression; latency, throughput and cost for operations.

#### Evaluation and decision-making

Compare solutions on performance, usability and feasibility. Assess risks (wrong predictions, drift, opacity, infrastructure). Decide on the evidence, not preference. A decision matrix with pre-agreed weights and confidence penalties for overlapping intervals is one way to keep the choice impartial.

#### Train / validate / test and overfitting

Training fits parameters; validation tunes hyperparameters; a final untouched holdout evaluates once. Cross-validation folds train and validate: K folds, train on K−1, validate on the held-out fold, rotate and average. Stratify by class under imbalance. Fit learned preprocessing inside each training fold to avoid leakage. Repeatedly peeking at the holdout turns it into another validation set.

**Overfitting:** high train, weak test — learned noise. Mitigate with regularisation, simpler models, more data, dropout, early stopping, CV. **Underfitting:** poor on both — need better features, more capacity or less regularisation. Bias–variance: total error ≈ bias² + variance + irreducible noise.

#### Drift as ongoing evaluation (production)

Data drift (input distribution), concept drift (input→output relationship), prediction drift (output distribution before labels). Detect with PSI (&lt;0.1 none; 0.1–0.25 moderate; &gt;0.25 significant), KS (continuous), chi-square (categorical), and sliding-window performance. Response: confirm type → contain → relabel → retrain → revalidate → redeploy → reset baselines.

#### Poor data quality and KPIs

Raw accuracy and R² mislead when labels or features are poor. Prefer robust signals: MAE / median absolute error, stability trends, drift KPIs, confidence/coverage, override rates, and the cost of wrong predictions. Hyperparameter tuning (grid, random, successive halving, Bayesian/Optuna) belongs inside validation, then confirm once on the holdout.

## Describes the relationship between mathematical principles and core techniques in AI and data science within the organisational context

**Relevant KSBs:** K19, K22.

### STARR: the mathematics behind the Hubble model choice

**Situation:** Hubble needed to classify short, inconsistent accounting descriptions into a large and imbalanced set of standard concepts. Stakeholders needed reliable outputs and an explanation of how the method worked.

**Task:** I needed to select and explain a technique whose mathematical properties suited sparse text, unequal class frequencies and HMRC's need for fast, supportable and interpretable processing.

**Action:** The linear algebra came first. I represented each canonical description as a numeric vector using word TF-IDF over one-to-three-word n-grams. The raw n-gram counts are multiplied by a smoothed inverse document frequency, `IDF(t) = log((1+N)/(1+df(t))) + 1`, and each description vector is then L2-normalised. The effect is that common words are down-weighted while distinctive phrases such as "interest receivable" keep their signal. But since it’s just short phrases plain tf gives similar results. 

The optimisation and geometry came next. LinearSVC finds one-versus-rest separating hyperplanes by convex optimisation. Each class gets a score `w_c·x + b_c` and the prediction is the class with the highest score. The objective is conceptually `||w||₁ + C Σ max(0, 1 − yᵢ(w·xᵢ + b))²`, with `C=2.8` and squared-hinge loss in the final configuration. I chose the L1 penalty deliberately because it drives many feature weights exactly to zero, which produces a sparse and inspectable coefficient set inside a very large feature space. Balanced class weights scaled each class's contribution inversely to its frequency, so errors on minority concepts genuinely mattered during training.

The probability and statistics shaped the evaluation. I challenged the stakeholder preference for accuracy as the headline measure, because with 75 concepts covering about 95% of items, accuracy mostly measures performance on common classes. I made macro-F1, the unweighted mean of per-class F1, the selection metric so that each eligible class contributed equally, and I retained accuracy, per-class precision and recall, support counts and confusion analysis alongside it. Stratified cross-validation estimated generalisation, and bootstrap intervals expressed the uncertainty in the holdout measures.

I also quantified the embedding trade-off in the same mathematical terms, and it is my clearest example of statistical significance not being practical significance. On the standard 1% run, MPNet's advantage over TF-IDF was about 0.003 macro-F1 and it was statistically significant at the 95% level, but it cost roughly 67 times the fit time (9,602 seconds against 143). A statistically real improvement of a third of a percentage point did not justify a GPU dependency and that compute cost, so I rejected it on practical grounds. On the later square-root-weighted run the difference was about 0.0001 and not significant at all. These numbers translated directly into an organisational decision about GPUs, cost and explainability.

**Result:** The mathematics supported an organisationally appropriate choice. The model was fast on existing CPUs, explainable through its coefficients, and better aligned to minority concepts than a selection made on accuracy alone. Reframing the evaluation around macro-F1 made rare-class performance visible and gave stakeholders an impartial basis for comparison.

**Reflection:** Mathematical principles explain why a technique behaves as it does and whether its output is suitable for a decision. I would never present a p-value or a model metric as certainty. Sample size, assumptions, class representation, effect size and business consequences all matter alongside statistical significance.

### STARR: testing whether an agent presented higher risk

**Situation:** In a separate piece of agent-level risk work, a qualitative review suggested that one agent might present higher risk than the wider comparison group.

**Task:** I needed to test that suspicion quantitatively rather than allow an impression to drive the conclusion.

**Action:** I set the null hypothesis that the agent's risk equalled the comparison group's, and then I checked the assumptions before choosing a test. The data was two independent groups measured on a ratio scale, approximately normally distributed, with more than 30 observations and unknown population variances. An F-test indicated that the variances were unequal, so Student's pooled-variance t-test was inappropriate. I therefore selected Welch's t-test, `t = (m₁ − m₂)/√(s₁²/n₁ + s₂²/n₂)`, which uses adjusted degrees of freedom.

**Result:** At a 99% confidence level I rejected the null hypothesis and concluded that the agent presented higher risk than the comparison group. This gave the business quantitative evidence rather than a judgement based only on qualitative review. Rejecting at 99% means the observed difference would be unlikely if the means were truly equal; it does not mean there is a 99% probability that the conclusion is true.

**Reflection:** The test must follow the data and its assumptions. I would present the confidence interval and the practical effect size as well as the p-value, because statistical significance alone does not show how important a difference is operationally.

### Technical notes: clarification knowledge

Drawn from past-learner notes on Statistical Methods, Supervised ML maths (linear regression / trees / forests), Neural networks, Activation functions / Softmax, Clustering maths, Common algorithms / SVM definition. Aligns to the EPA clarification on linear algebra, calculus, probability/statistics, optimisation, and core techniques in organisational context. Full algorithm walkthroughs also sit in the Technical answer bank.

#### Mathematical principles

- **Linear algebra:** vectors and matrices represent data and weights. SVD / eigen-decomposition underpin PCA, recommendations and compression. TF-IDF descriptions are sparse vectors; LinearSVC scores are `w·x + b`.
- **Calculus:** differentiation drives optimisation. Gradient descent minimises loss; partial derivatives + chain rule = backpropagation. Activations introduce non-linearity (ReLU default for hidden layers; sigmoid/tanh; softmax for multi-class outputs).
- **Probability and statistics:** distributions model uncertainty; Bayesian inference updates beliefs; hypothesis tests, CIs and regression infer from samples. Macro-F1, paired t-tests and bootstrap intervals are how uncertainty enters model choice.
- **Optimisation:** convex problems (single global minimum) underpin least squares, logistic regression and SVMs. Stochastic methods (SGD, Adam) scale to large data. Tree splits are greedy local optimisation (Gini / entropy / information gain), not globally optimal.

#### How maths maps to core techniques

| Technique | Core maths idea |
| --- | --- |
| Linear regression | Least squares; normal equation or gradient descent; convex |
| Logistic regression | Sigmoid / log-likelihood; linear decision boundary |
| Decision tree | Gini = 1−Σp² or entropy; information gain; recursive partition |
| Random forest | Bagging + random features → variance reduction |
| SVM / LinearSVC | Max-margin; hinge / squared-hinge; soft-margin C; kernels for non-linear |
| Neural net | Matrix multiplies + activations; backprop; cross-entropy / MSE |
| K-means | Minimise Σ‖x−centroid‖²; silhouette for cohesion vs separation |
| PCA | Eigen / SVD of covariance; max retained variance |
| Transformer | Attention = softmax(QKᵀ/√d_k)V |

#### Key formulas to recall

- Macro-F1 = (1/K) Σ F1_k
- Paired t: `t = mean(d)/(sd(d)/√n)`
- Welch: `t = (m₁−m₂)/√(s₁²/n₁+s₂²/n₂)` (check variances with F-test first)
- SVM: `min ½‖w‖² + C Σ max(0, 1−yᵢ(w·xᵢ+b))` (or squared-hinge / L1 variant)
- Softmax: turns logits into a probability distribution over classes

#### Organisational relevance

Mathematical properties become organisational constraints: compute cost (dense embeddings vs sparse TF-IDF), minority-class coverage (macro-F1 vs accuracy), interpretability (coefficients vs black-box), uncertainty (CIs, overlapping intervals) and auditability (can you defend the choice?).

## Explains how they have used programming languages and modern machine learning libraries for commercially beneficial scientific analysis, simulation and data engineering to meet business needs

**Relevant KSBs:** K18, K25, S26.

### STARR: using R, Python and SQL as one Hubble pipeline

**Situation:** Company returns in XML and accounts in iXBRL/XHTML contained valuable structured and semi-structured data. The analysts who would maintain and use the extraction worked primarily in R, while the strongest documented machine learning ecosystem for the classification experiments was Python.

**Task:** I needed to select languages and libraries for extraction, cleaning, model experimentation and delivery without forcing the whole pipeline into one language or creating an unsupported workflow. That meant challenging the norm that a project stays in the language it started in.

**Action:** I investigated package maturity, team capability, platform support and long-term maintenance rather than choosing a language by preference.

For the data engineering layer in the workplace, I used R for the fuller XML and HTML extraction because it matched the supported analyst workflow and had mature parsing tooling. Keeping extraction in the language its maintainers actually used reduced the support burden. This part needs internal artefacts, because it is not in `Code/`.

At the cross-language boundary, `reticulate` embedded a Python session inside R and converted objects between the two languages. This let the R pipeline call the more mature Python model without rewriting the analyst-facing workflow. I treated its risks as part of the design rather than an afterthought: dependency and environment mismatch, conversion overhead, and error handling across languages were all managed with pinned R, Python and package versions, a reproducible environment and an integration test.

For delivery through SQL and Oracle, `dbplyr` represented remote tables lazily and translated tidyverse verbs into SQL. Filtering, grouping and joins therefore executed inside the database rather than after downloading the whole dataset. I inspected the generated SQL and the query plans for expensive operations rather than assuming the translation was optimal.

The scientific analysis layer in Python is fully code-backed. BeautifulSoup and Pandas parse the filings and save Parquet. Polars and NumPy support the EDA and data engineering. Scikit-learn provides TF-IDF, the classical models, cross-validation and the halving searches. SentenceTransformers supplies MPNet and e5. TensorFlow and Keras implement the neural and CNN experiments. PyTorch and Hugging Face fine-tune SEC-BERT. Optuna runs the hyperparameter searches and MLflow records the experiments.

The feature engineering was empirical throughout. Lower-casing and whitespace and punctuation normalisation reduced accidental vocabulary variation. Typed placeholders such as `hubble_name`, `hubble_date` and `hubble_number` removed high-cardinality identifiers while preserving the information that a name, date or number was present. I tested rather than assumed each choice: replacing forward slashes with spaces reduced performance, so it was not retained. The same tested functions create both training and production features, which prevents skew between the two.

On simulation I treat the claim narrowly. Controlled experiments comparing model and hyperparameter scenarios on fixed splits are experimental analysis, not a physical or Monte Carlo simulation of a real-world process.

**Result:** The code shows a complete experimental path from semi-structured public filings to repeatable model comparisons over millions of rows, and why a CPU-compatible scikit-learn model could beat GPU-heavy alternatives operationally. The commercial benefit was not "using three languages". It was combining their strengths to widen the usable data, reduce manual preparation and deliver through a workflow the organisation could actually support.

**Reflection:** The correct language is contextual. Data format, library maturity, user capability, deployment platform and supportability all matter. Python support is growing in HMRC's AWS lakehouse, so I would reassess the language boundary over time, migrating only where the benefit outweighs the disruption.

### Technical notes: clarification knowledge

Past-learner notes are thin here (only a scikit-learn metrics snippet). Content below follows the EPA clarification points directly, with Hubble-relevant library examples kept as knowledge rather than applied claims.

#### Clarification checklist (hit each point)

1. **Programming languages** — name languages used and why suitable. Python: data analysis/ML, extensive libraries. R: statistics, visualisation, analyst communities. SQL: declarative relational querying. Java/Scala: JVM data engineering (Spark). Mixed-language designs need pinned environments and integration tests (`reticulate`, drivers).
2. **Modern ML libraries** — scikit-learn (classical ML, TF-IDF, CV, searches); TensorFlow/Keras and PyTorch (deep learning); Hugging Face Transformers / SentenceTransformers (pre-trained language models and embeddings); Optuna (hyperparameter search); MLflow (experiment tracking); XGBoost/LightGBM (boosting). Libraries supply tested implementations so effort goes into the problem.
3. **Commercially beneficial scientific analysis** — analysing large datasets for trends, predictions or process optimisation; reproducible and evidence-led.
4. **Simulation** — computational models of real-world scenarios (Monte Carlo, what-if, agent-based). Controlled model/hyperparameter experiments on fixed splits are experimental analysis, not physical simulation — say so honestly.
5. **Data engineering** — collect, clean, transform, prepare; formats such as Parquet; lazy query pushdown (`dbplyr`/SQL); batching and durable writes.
6. **Meeting business needs** — tie skills to efficiency, cost, coverage, revenue or better decisions.

## Uses applied research and data modelling to design and refine the infrastructure and architectures to deliver secure, stable and scalable data products, including enterprise, private and public cloud resources and services

**Relevant KSBs:** K16, S1, S16, S19.

### STARR: refining Hubble's data-product architecture

**Situation:** Hubble processed high-volume, varied data including XML, iXBRL/XHTML and PDFs. The POSIT Data Analytics Platform suited development but not full-volume extraction, and the outputs had to remain secure, stable and accessible to analysts.

**Task:** I needed to define and refine an architecture that could burst for large extraction jobs, recover reliably, and provide queryable outputs without overloading the shared platform.

**Action:** The applied research and data modelling came first. I investigated taxonomy change, Oracle width limits, the shape of the workload and user needs. From that I proposed a long-form data model, storing document, context, concept, description and value as rows, instead of the wide annual-taxonomy tables that created structural change and width pressure every year. The long model costs more rows and occasional pivots for some outputs, but it is taxonomy-independent and removes the annual schema remapping. I consulted analysts before committing, to confirm they could genuinely work with long data.

For scalable compute, I worked with platform engineers to establish On-Demand Compute: temporary EC2 capacity, including large-core or GPU configurations when justified, spun up for a job and shut down afterwards. This isolated heavy workloads from the shared platform and controlled cost. Because document sizes varied widely, static partitioning left some workers idle while stragglers finished, so I used dynamic work allocation in which workers pulled the next document when they became free. I also understood where scaling stops helping: when input and output, database writes, serial setup or credential management becomes the bottleneck. 

For storage, I matched each store to its access pattern. Apache Solr provided distributed, replicated free-text search across servers. Oracle held governed structured outputs for SQL querying and joins. Each store did what it suits rather than one being forced to do both.

For security and stability, the DPIA, data minimisation, controlled-environment processing, model assurance, distribution-list access and controlled Oracle and S3 outputs addressed confidentiality. Replicated Solr, tested code, durable database outputs and workload isolation supported stability.

**Result:** The architecture separated large jobs from the main platform, scaled compute only when needed, and provided fast search plus structured analyst access. The long-form model was taxonomy-independent, removed the wide annual mappings, and supported access to new submissions within days rather than the previous ingestion delay of around nine months.

**Reflection:** Scalability includes operability, workload balance and governance, not just maximum throughput. I would handle token refresh for long-running jobs centrally rather than sharing refreshed S3 credentials between workers through a file. Longer term, Spark on EMR with Redshift or lakehouse-native storage may integrate the processing more effectively, subject to benchmarking and access-control assurance.

### STARR: controlling access to S3 data

**Situation:** Valuable data was held in S3 buckets but should not have been available to every user of the connected analytics system.

**Task:** I needed to define and supervise an access route that allowed authorised users to reach the data without opening the buckets broadly.

**Action:** I created a proxy and controlled access to it through a distribution list. This kept the cloud resource behind an organisationally controlled route and limited access to people with a demonstrated need.

**Result:** Only the intended user group could reach the S3 data. The control met the security requirement, although the extra layer introduced some reliability and performance overhead.

**Reflection:** System-level access is a weaker substitute for direct user-level authorisation. A future lakehouse design should enforce permissions for individual users at the data layer, which would remove the need for a slower proxy workaround.

### STARR: challenging auto-scaling as the default database architecture

**Situation:** For a smaller project, I initially built a database on native AWS auto-scaling services because they were easy to provision and included managed backup and scaling.

**Task:** I needed to determine whether that architecture was technically and financially sustainable for the project's actual workload.

**Action:** I reviewed the charges at low and zero usage and compared the managed auto-scaling design with fixed-price and self-hosted EC2 alternatives. I weighed the total cost of ownership, covering concurrency, storage, idle time, support effort, recovery and expected growth, rather than comparing headline compute prices. The serverless billing was opaque and the baseline cost was disproportionate for a small, intermittent workload. On that evidence I challenged the assumption that cloud-native auto-scaling is automatically the most cost effective choice.

**Result:** Fixed-price or self-hosted capacity was more predictable for this project and could still be resized when demand genuinely grew. The decision separated the technical ability to scale from the commercial question of whether the scaling model was appropriate.

**Reflection:** A scalable service must also be financially sustainable. I would use measured workload profiles and total-cost comparisons before selecting serverless or auto-scaling infrastructure, rather than treating either as a default.

### Technical notes: clarification knowledge

Past-learner notes are thin on cloud architecture (only MLOps/deployment/monitoring). Follow EPA clarification; keep architecture vocabulary ready.

#### Clarification checklist

1. **Applied research and data modelling** — profile sources, prototype schemas, benchmark alternatives before locking the design (e.g. wide annual tables vs long-form taxonomy-independent rows).
2. **Design and refine infrastructure/architectures** — continuously improve systems so they remain robust for required processing (ODC burst compute, dynamic work allocation, matched stores).
3. **Secure, stable, scalable data products**
   - Secure: least privilege, controlled networks, encryption, audit, distribution-list / proxy access
   - Stable: replication, tested code, durable storage, workload isolation, recovery
   - Scalable: horizontal scaling, parallelism, elastic compute — and know when scaling stops helping (Amdahl; I/O, DB writes, serial setup)
4. **Enterprise, private and public cloud** — enterprise = internal platforms; private = dedicated org cloud; public = AWS/Azure/GCP on demand. Public *provider* ≠ public *data*. Know how HMRC classifies the components you used.

#### Architecture options and parallel concepts

Relational DB (governed SQL); search index (Solr — sharding/replication); object store (S3); lake vs lakehouse vs fabric. Embarrassingly parallel workloads; static vs dynamic scheduling; stragglers; total cost of ownership for auto-scaling vs fixed capacity. MLOps link: deployment and drift monitoring are part of a stable data product, not afterthoughts.

## Explains how to design algorithms for accessing and analysing large amounts of data, including Application Programming Interfaces (API) to different databases and data sets

**Relevant KSBs:** K16, S19, S20.

### STARR: moving Hubble from files to scalable data access

**Situation:** The first Hubble workflow saved results to files, which users often exported as CSV or Excel. Runs were slow and usually limited to selected populations, and the repeated file movement made querying, joins and reuse difficult.

**Task:** I needed to redesign the access and processing so that Hubble could handle large document populations without saturating the main platform, exposing results through data stores analysts already used.

**Action:** I challenged the file-based workflow, investigated where time and manual effort were being lost, and designed around data locality, batching, query pushdown, parallelism, storage format and the cost of repeated serialisation.

For the parallel access design, I worked with DevOps to provision On-Demand Compute and used dynamic parallel scheduling. Documents went into a work queue and workers pulled the next one when free, so roughly 128 returns could be processed concurrently without the long tail caused by static batches of differently sized documents. The correct worker count sits just before contention at S3, the network, parsing memory or the Oracle writes removes the benefit of adding cores.

For the API layer I used defined programmatic interfaces rather than ordinary file copies: R database drivers with DBI-style calls to Oracle, `dbplyr` as a higher-level query interface, Solr's query interface, the controlled S3 proxy, and the Parquet-on-FSx storage interfaces. The value of `dbplyr` is its lazy execution: it builds a query representation and only sends the translated SQL when results are collected, so filters, aggregation and joins execute close to the data. That cuts transfer and client memory, and the benefit depends on suitable indexes and predicates the optimiser can push down.

For the storage and format decisions, structured outputs went to Oracle rather than loose files. Where a SAS-writing package proved unreliable, I used a shared FSx route with Parquet, a compressed columnar format in which analytical queries read only the required columns and use metadata for predicate pruning, which is far more efficient than CSV. Batched database writes used sensible transaction boundaries so a failed batch could be retried without creating duplicates. Solr handled fast distributed text retrieval and the S3 proxy controlled object access.

Two design questions are held open deliberately. The analysts' request for numeric surrogate keys over natural keys is a benchmarking question about index size, query plans and end-to-end user effort on representative Oracle and SAS workloads, not a change to make on preference. And a possible future LLM-to-Solr natural-language query route remains clearly proposed rather than built. It would need a controlled schema, syntactic validation, field and operator allow-lists, authorisation in the user's own context, result-size limits, escaping against injection, audit logging and a preview step. The LLM must not become a route around existing access controls.

**Result:** Large extraction jobs ran on isolated temporary capacity without degrading the shared platform. The database and Parquet outputs made results easier to query, join and reuse, while the R analysts kept their familiar syntax and let the database do the heavy work.

**Reflection:** An efficient algorithm is one part of a wider data-access design. Parallelism only helps if the work is balanced, the credentials stay valid and the output does not create a new bottleneck. I would add service interfaces only where they genuinely improve reuse, rather than adding a REST API for its own sake.

### Technical notes: clarification knowledge

Past-learner notes only lightly mention APIs/databases in the ML pipeline. Follow EPA clarification.

#### Clarification checklist

1. **Designing algorithms for large data** — sorting, filtering, aggregating; efficiency and scalability; complexity of the *whole data path* (queueing, parallelism, batching, serialisation), not one function. Dynamic work allocation for uneven document sizes; choose worker count just before contention removes the benefit.
2. **Accessing data via APIs** — an API is a defined programmatic interface, not only a public REST endpoint. Examples: REST/JSON web services; database drivers (ODBC, JDBC, DBI); higher-level query interfaces (`dbplyr` lazy SQL); Solr query API; cloud storage SDKs / controlled proxies; Parquet read/write interfaces. Do not call an ordinary file copy an API.
3. **Analysing data** — statistical analysis, ML and data mining turn raw data into decision-ready information (pushdown filters/aggregations close to the data where possible).
4. **APIs to different databases and datasets** — SQL/relational (structure, joins, transactions); NoSQL (document/key-value/wide-column); search indexes; object stores; columnar formats (Parquet/ORC vs CSV). Seamless integration means the algorithm can use each store for what it suits.

## Distinction: Explains when they have challenged the norm through investigating and proposing a solution and the impact this had

**Relevant KSBs:** K7, S1, S20, S26.

### STARR: replacing annual wide-table ingestion with a taxonomy-independent model

**Situation:** The established approach relied on tagged iXBRL and wide annual Oracle tables. New taxonomies needed manual mapping, the tables approached Oracle width limits, and ingestion could take over nine months. HMRC normally needs to open enquiries within about a year, so that delay left very little time for profiling and case action. Untagged values and free-text descriptions were largely unavailable at scale.

**Task:** I needed to investigate whether a different data model could remove the annual ingestion bottleneck without making the result unusable for analysts.

**Action:** I challenged the assumption that the output needed to be a manually mapped wide table. I profiled the source data, investigated the pattern of taxonomy change and the database limitations, and proposed a long-form, taxonomy-independent representation. Before committing to the change, I consulted analysts to confirm that they could work with long data.

**Result:** New taxonomies could be ingested without annual structural remapping, and analysts could begin profiling submissions within days rather than waiting around nine months.

**Reflection:** Challenging the norm works when it is based on evidence and user validation rather than novelty. The long format traded some immediate human readability for adaptability and scale, which is why consulting analysts was essential. I would retain the benchmarks, acceptance records and before-and-after timings so the impact is readily defensible.

### STARR: reusing tagged descriptions to classify untagged content

**Situation:** The norm was to rely on tagged data or manually maintained matching rules. Inconsistent wording made population-level profiling of untagged descriptions impractical.

**Task:** I needed to investigate whether untagged content could be mapped to the standard taxonomy without analysts maintaining an impossibly large set of regular expressions.

**Action:** I challenged the assumption that tagged and untagged data had to be treated separately. I proposed using the correctly tagged descriptions as supervised training labels for a classifier over the untagged content. I then researched and compared classical machine learning, embeddings, neural networks and transformers, and selected TF-IDF with LinearSVC on the combined basis of quality, speed, explainability, security, infrastructure and maintainability rather than raw score alone.

**Result:** The classifier provided a reusable way to categorise untagged descriptions, extended analytical coverage and reduced the dependence on manual matching rules. Analysts gained access to data they could not previously exploit consistently at scale.

**Reflection:** The novel element was not simply using machine learning. It was recognising that an existing labelled subset could supervise a previously unusable unlabelled subset. I would retain the decision matrix, the experiment record and the user evidence so this impact stays distinguishable from the separate long-format ingestion change.

### STARR: extracting contextual features before a calculation issue emerged

**Situation:** Hubble's original requirement focused on extracting untagged figures, but iXBRL documents also contain headings, table names and positional context, and it was not yet known which of those features future investigations would need.

**Task:** I had to decide whether to meet only the narrow requirement or design a more general extraction that preserved useful context.

**Action:** I challenged the narrow scope and added general support for contextual features in advance. Later, a material issue involving very large incorrect figures produced by software companies required analysts to recreate calculations. Tagged-only data was insufficient because the relevant figures could be mistagged or left untagged, and the volume was far too large for manual checking. I used Hubble's untagged values and contextual features to support the reconstruction.

**Result:** Hubble could extract the information the investigation needed without a new development cycle, allowing calculations to be checked at a scale that manual work and tagged-only data could not support.

**Reflection:** Designing for likely analytical reuse can create significant value, but it must be balanced against unnecessary collection. I would document the original design decision, the exact features used and the verified business outcome, while avoiding sensitive operational detail.

### Technical notes: clarification knowledge

Past-learner notes have little narrative "challenge the norm" content; use their select-and-apply / evidence-vs-accuracy framing as the investigation method. Four elements to hit explicitly:

1. **Norm challenged** — the existing practice, process or belief that needed change (e.g. wide annual tables; tagged-only analysis; accuracy as headline metric; auto-scaling as default).
2. **Investigation** — research, data analysis or expert consultation showing the challenge was informed. Past-learner method: baseline → data readiness → decision matrix → constraints → validate. Use KPIs and poor-data-quality thinking so you do not challenge fashion with fashion.
3. **Proposed solution** — what was innovative and how it differed from the norm (long-form model; supervised reuse of tagged labels; contextual features; fixed-price capacity).
4. **Impact** — measurable benefit (efficiency, cost, performance, coverage, time-to-profile) and how it was validated (before/after timings, user confirmation, experiment record). Keep claims to artefacts you can name.

---

# Theme 2: Professional practice in a commercial environment

**Theme KSBs:** K8, K10, S6, S8, S14, S23, S28, B1, B4, B7.

**Distinction integration:** the pass answers also consider the wider public-sector and social context and current AI trends where that is natural. The standalone distinction answers remain the fullest versions.

## Explains how they have developed their professional working practices and leadership techniques in regard to AI and data science and how this has improved organisational practice

**Relevant KSBs:** K10, S6, B1, B4.

### STARR: leading the growth of the Data Analytics Platform

**Situation:** The Data Analytics Platform began with a single user and needed to support a growing number of analysts using R, Python, data engineering and machine learning.

**Task:** As the platform owner, I needed to keep the service useful and funded, expand its capability, give technical direction and help users develop the skills to use it effectively.

**Action:** I worked with budget holders to justify licence growth, arranged upgrades and new functionality, and collaborated with engineers on On-Demand Compute and GPU access. I supported users directly, mentored project teams and ran discussions about machine learning opportunities. I also created and maintained practical wiki guidance covering virtual environments, secure data access, reproducibility and platform use, and I tailored my communication for analysts, engineers, suppliers and decision-makers rather than giving every audience the same level of detail.

**Result:** DAP grew from one user to more than 250 and supported teams building their own analytical and machine learning tools. Users developed tools and integrations themselves rather than relying on me for every change, which extended organisational capability beyond my own delivery.

**Reflection:** My leadership developed from answering individual technical questions to shaping a service and the practices around it. I would strengthen this with formal skills reviews, succession planning and measured outcomes from mentoring.

### STARR: taking ownership of Hubble's technical direction

**Situation:** No off-the-shelf solution could categorise untagged iXBRL descriptions, and the initial simple NLP approaches performed poorly. Hubble spanned extraction, cleaning, modelling, validation and delivery across several technologies.

**Task:** I needed to take personal responsibility for the technical direction, overcome the infrastructure and modelling problems, and prove that the business problem was tractable.

**Action:** I investigated alternative architectures and model families, rebuilt the training datasets, fine-tuned BERT and tested classical and neural approaches. When GPU and throughput constraints emerged, I adapted the workflow to the infrastructure that was actually available and compared the candidates against operational criteria as well as model quality. I managed the lifecycle end to end, from extraction and cleaning through training, validation and reporting, and I introduced lightweight project controls as the contributor group grew.

**Result:** The work produced a validated classification proof of concept and established the business case for using machine learning in data profiling. The wider Hubble product extracted substantially more data than the previous approach and supported analysts identifying tax risk.

**Reflection:** Ownership meant being accountable for the complete outcome, including its limitations and deployment fit, rather than only producing a model. I would make the prototype-versus-production status and the final performance evidence more explicit in the project record.

### Technical notes: clarification knowledge

Drawn from EPA clarification plus past-learner dissemination / enablement notes (closest available leadership content).

#### Developing professional working practices

Adopt new tools and technologies; stay current with industry trends; continuous learning (courses, workshops, self-study); standardise methods (lifecycle, governance, templates); write reusable guidance (wikis, READMEs); promote reproducibility, testing and proportionate model selection.

#### Leadership techniques

Lead projects; mentor; foster collaboration; make strategic decisions; give technical direction; tailor communication by audience (analysts vs engineers vs budget holders); align senior stakeholders; build capability so others can deliver without you.

#### Impact on organisational practice (clarification examples)

- **Enhanced efficiency** — streamlined processes and workflows
- **Innovation** — new AI/data solutions and competitive capability
- **Improved decision-making** — data-driven insights
- **Team development** — skilled, motivated team through mentorship and enablement

Be ready with a verified organisational measure (users, delivery, mentoring outcome) rather than only describing activity.

## Justifies their choice of techniques, explaining the risks and benefits and offers an alternative to technical and non-technical audiences

**Relevant KSBs:** K8, S6, S8, S28.

### STARR: communicating the LinearSVC decision

**Situation:** Stakeholders had different preferences. Some wanted accuracy as the headline measure, analysts suggested models such as Random Forest, and transformer models attracted interest because they were current and powerful.

**Task:** I needed to make an impartial recommendation, explain the benefits and risks, provide credible alternatives, and communicate the same decision appropriately to technical and non-technical audiences.

**Action:** I consulted the stakeholders first and converted their concerns into a comparison covering macro-F1 and per-class reliability, accuracy, speed, compute cost, explainability, security and provenance, maintainability and deployment fit. The comparison narrowed to LinearSVC, CNN and SEC-BERT on one common holdout, plus rubric-scored operational criteria. SEC-BERT had the highest macro-F1 point estimate at 0.823 against 0.808 and 0.800, but the confidence intervals overlapped. LinearSVC trained in minutes rather than the better part of an hour, ran inference orders of magnitude faster, and was about 8 MB rather than about 1.8 GB, with stronger deployment, maintenance and dependency-risk ratings.

I presented the risks and benefits in both directions. LinearSVC's risks are its linear decision boundary and its lack of contextual understanding. SEC-BERT's risks are its GPU dependency, slower throughput, weaker explainability, provenance and assurance concerns, and lifecycle cost.

For technical audiences, I explained sparse TF-IDF vectors, L1 regularisation, the imbalance handling, cross-validation, bootstrap uncertainty and the CPU and GPU constraints. For non-technical audiences, I described macro-F1 as reliability across rare as well as common concepts, CPU execution as lower cost and easier deployment, and the coefficients as understandable evidence about which phrases influenced a result.

The alternative I offered was SEC-BERT or another assured domain model, in the event that a remapped, grouped evaluation established a worthwhile gain and future infrastructure, assurance and maintenance could support it. The decision matrix itself was designed to be honest about uncertainty: where a model's confidence interval overlapped the best model's on a metric, that metric's score was reduced by a confidence penalty, so an uncertain win could not carry the ranking. Even so I would not quote the current numeric decision score unqualified, because the matrix has a known field-name defect that drops interpretability from the calculation and its weights have not been sensitivity-tested.

**Result:** TF-IDF with LinearSVC was the operational recommendation, offering competitive quality, fast CPU-compatible processing, clearer explanations and lower lifecycle risk.

**Reflection:** Communicating alternatives strengthens a recommendation because it shows the choice was deliberate. In future I would agree metric definitions and risk tolerances even earlier and keep a short decision record containing both the technical comparison and a plain-English version.

### Technical notes: clarification knowledge

Drawn from past-learner notes on "select and apply the most effective/appropriate AI…", KPIs, Poor Data Quality, and Risks of adopting AI. Aligns to justification, risks/benefits, alternatives, and audience tailoring.

#### Justifying a technique (decision process)

1. Start with the business decision and measurable KPIs / constraints (accuracy, latency, interpretability, compliance, cost).
2. Check whether ML is needed at all (rules / BI may be lower risk).
3. Frame the ML task (regression, binary/multi-class, clustering, anomaly, NLP, vision, time series).
4. Assess data readiness (labels, quality, leakage, freshness).
5. Build a fast baseline.
6. Choose with a decision matrix: performance vs interpretability vs latency vs governance — simplest model that meets all constraints.
7. Validate with risk-aligned metrics; productionise with monitoring.

Interview phrasing: "The best model is the one that meets the business outcome reliably under constraints — not the highest laboratory score."

#### Risks and benefits (present both sides)

- **Benefits:** performance, coverage, cost/speed, new capability, explainability where coefficients or SHAP/LIME apply.
- **Risks:** limitations of the decision boundary, errors on edge cases, resource needs (GPU), maintenance and provenance, opacity, drift, over-dependence.
- Use risk vocabulary from AI adoption notes: data, model (bias/opacity), operational (drift), business (wrong decisions), security, compliance, skills, financial, ethical.

#### Offering alternatives

Always name a credible runner-up and the conditions under which it would win (e.g. remapped evaluation shows a material gain *and* infrastructure/assurance can support a transformer). That proves the choice was deliberate.

#### Audience tailoring

| Audience | Emphasise |
| --- | --- |
| Technical | Algorithms, vectors, metrics, CIs, infrastructure, failure modes |
| Non-technical | Problem solved, cost, what could go wrong, decision needed, plain-language metrics (e.g. "reliability across rare as well as common concepts") |

## Explains how they share and disseminate AI and data science practices across organisations to improve industry practice

**Relevant KSBs:** S23, B7.

### STARR: sharing practice internally through DAP guidance and mentoring

**Situation:** DAP users came from different teams and had varying experience with environments, data access, reproducibility, testing and the limitations of machine learning.

**Task:** I needed to make safe, effective practice reusable across the organisation rather than repeatedly solving the same setup and delivery problems for individuals.

**Action:** I shared guidance through Teams channels, direct mentoring, demonstrations and a maintained wiki. The material covered virtual environments, secure data access, reproducibility, testing, model limitations, human-in-the-loop use and proportionate model selection. I also documented Hubble with a full README and detailed design notes so contributors could understand how to run it and why the important choices had been made.

**Result:** Users gained reusable guidance and support, and Hubble contributors adopted more consistent, reproducible workflows. The documentation reduced the reliance on individual knowledge and made it easier for colleagues to build their own tools.

**Reflection:** Internal dissemination requires maintenance, feedback and examples, not just publishing a page. I would track wiki use, mentoring outcomes and reuse by other teams to demonstrate the improvement in organisational practice.

### STARR: sharing grounded-LLM practice through Graffiti

**Situation:** The wider iXBRL community was exploring LLMs, but passing a complete, noisy HTML filing to a model produced poor results and could encourage overconfidence in ungrounded answers.

**Task:** I needed to demonstrate and share a safer, more effective pattern without exposing HMRC data or presenting an experiment as settled best practice.

**Action:** I built Graffiti using public filings. It extracts and structures the iXBRL first, selects the relevant context, and supplies that context together with the user's question to the LLM. I shared the developments with leading iXBRL experts, explaining both the benefit of grounding and the limitations, including hallucination, prompt injection, data leakage, opacity, cost and over-automation.

**Result:** Graffiti provided a practical external demonstration of grounded LLM analysis over iXBRL and a vehicle for discussing responsible use with the professional community.

**Reflection:** External dissemination should distinguish demonstrated behaviour from general claims of industry impact. I would retain the details of the audiences, feedback, reach and any concrete reuse or changed practice that Graffiti prompted.

### Technical notes: clarification knowledge

Drawn nearly in full from past-learner notes: "How do you disseminate AI and Data Science practices?"

#### Internal sharing mechanisms

1. **Standard frameworks and guidelines** — common ML lifecycle, model governance, ethical AI; templates for problem definition, evaluation, KPI dashboards and documentation. Ensures consistency, quality and auditability.
2. **Knowledge sharing** — communities of practice; meetups; wikis (Confluence/SharePoint); playbooks; Git repositories.
3. **Training and enablement** — role-based: business users (awareness), engineers (techniques), leaders (strategy/governance); hands-on workshops.
4. **Reusable assets** — pipelines, feature libraries, prebuilt models/APIs, data-quality and drift tools. Faster delivery, less duplication.
5. **Embedded governance** — validation/approval, bias/fairness checks, privacy compliance, version control and audit trails; MLOps and Responsible AI.
6. **Pilots and use cases** — high-impact PoCs → scaled solutions; showcase cost, SLA or automation benefits.
7. **Dashboards and transparency** — performance, drift and business-impact metrics (Power BI / Tableau) to build trust.
8. **Data-driven culture** — encourage experimentation; reward outcomes; secure senior sponsorship.

**End-to-end flow:** Standards → Training → Tools/Assets → Use Cases → Governance → Scaling → Culture.

#### External dissemination

Conference presentations, publications, professional networks/forums, and open demonstrations on public or synthetic data (never expose organisational data).

#### Improving industry practice

Influencing standards, best practice and guidelines. Be honest: sharing is evidenced by the activity; demonstrated industry change needs reuse, feedback or changed practice as evidence.

**30-second answer:** "I disseminate AI practice by standardising frameworks and governance, enabling teams through training and communities of practice, providing reusable tools, demonstrating value through pilots, and embedding AI into processes with transparent metrics."

## Distinction: Critically analyses the wider social context and current issues and trends, applying the findings with justification and shares these with the wider community

**Relevant KSBs:** K8, S23, B7.

### STARR: challenging overly broad internal AI guidance

**Situation:** New organisational guidance, introduced in response to the risks of generative AI, treated conventional machine learning as if it had the same risk profile. It restricted work to LLM-oriented platforms that did not support ordinary ML development well.

**Task:** I needed to interpret the guidance in its wider public-sector context, protect the organisation from genuine AI risk, and avoid disproportionate restrictions that would block valuable, lower-risk work.

**Action:** I compared the risks of conventional supervised machine learning with those of generative models, including hallucination, prompt injection, ungrounded generation, data leakage and over-automation. I tested the guidance against practical development workflows and showed specifically where it was not implementable or would create substantial business cost without addressing the actual risks. Rather than only objecting, I supplied detailed, usable amendments.

**Result:** The guidance was changed in line with my comments, giving the organisation a more proportionate basis for governing different types of AI work.

**Reflection:** Responsible practice requires the confidence to challenge policy with evidence. Proportional governance protects public trust more effectively than treating every technique as identical, and the guidance should continue to be reviewed as technology, regulation and public expectations change.

### STARR: applying and sharing a grounded-LLM pattern through Graffiti

**Situation:** Foundation models created strong interest in natural-language analysis of company filings. Industry evidence suggested that sending a complete HTML document to an LLM performed poorly, while structured iXBRL context improved grounding. In a public-sector setting, an ungrounded or over-trusted answer could damage confidence and lead to indefensible conclusions.

**Task:** I needed to critically assess the trend, apply it where justified, and share a practical pattern with the wider iXBRL community.

**Action:** I weighed the accessibility and productivity benefits of LLMs against their risks, including hallucination, prompt injection, data leakage, opacity, bias, cost and over-automation. I built Graffiti on public filings, extracting the iXBRL first and supplying the structured context with the user's query. I kept the tool analytical rather than making it an automated decision-maker, made human review explicit, and discussed the pattern and its limitations with iXBRL experts.

**Result:** Graffiti demonstrated a grounded-LLM approach to the wider professional community without exposing HMRC data and without suggesting that model output should replace professional judgement.

**Reflection:** The social licence for AI depends on transparency, accountability and accessible challenge, not simply capability. As MCP and tool use expand, I would keep external demonstrations on public or synthetic data and make the model's limits visible.

### Technical notes: clarification knowledge

Drawn from past-learner notes on identifying AI trends, Will AI remove jobs?, and Impact of AI / Risks. Four distinction elements to hit explicitly.

#### 1. Critically analyse the wider social context

Examine ethics, privacy, economic impact, cultural influence and public perception with evidence. Useful framing for jobs: AI more often **changes tasks** than eliminates whole occupations (displacement vs augmentation). Credible scale figures: WEF ~170m roles created / 92m displaced by 2030; IMF ~40% global employment exposed (~60% advanced economies); ILO — clerical work especially exposed to GenAI. Biggest practical risk is often "people with AI skills vs without", plus loss of accountability if humans rubber-stamp outputs.

#### 2. Current issues and trends

How past learners track trends:
1. Research and publications (arXiv, major labs, Gartner/McKinsey/Forrester)
2. Vendor / ecosystem (AWS, Azure, Google; Hugging Face; copilots; agents)
3. Enterprise adoption patterns (automation, GenAI, predictive analytics, governance)
4. Data-driven signals (job demand, investment)
5. Communities and conferences
6. Use-case evolution (descriptive → predictive → prescriptive; standalone models → platforms)
7. Regulatory/governance (EU AI Act, privacy law, trustworthy/explainable AI)
8. Validate with PoCs; filter hype vs maturity (scalability, cost-benefit, integration, governance)

Example talking points: LLMs/GenAI, copilots, multimodal AI, agents, responsible AI, edge inference.

#### 3. Apply findings with justification

Link action to analysis (e.g. proportionate AI guidance distinguishing conventional ML from GenAI risk; grounded-LLM pattern because unstructured HTML performs poorly). Justify with evidence, not fashion.

#### 4. Share with the wider community

Articles, presentations, forums, demonstrations on public data; keep limitations visible (hallucination, injection, leakage, opacity, cost, over-automation).

## Explains how they have made independent impartial decisions respecting the opinions and views of others in complex, unpredictable and changing circumstances to benefit the business

**Relevant KSBs:** S8, S28, B4.

### STARR: balancing licence, compute and funding priorities for DAP

**Situation:** As DAP owner I received competing demands. Users needed more licences and GPU capability, engineers had platform constraints, and budget holders needed a defensible business case.

**Task:** I needed to respect those perspectives and provide capacity where it benefited the organisation, without committing to unaffordable permanent infrastructure.

**Action:** I gathered evidence of demand and of the work that additional capacity would enable. I justified licence growth with the budget holders, and I worked with the engineers to provide On-Demand Compute, including GPU instances that could be started for specific work and shut down afterwards.

**Result:** DAP grew beyond 150 users with appropriate licences, and ODC provided large CPU and GPU capacity cost-effectively when projects needed it.

**Reflection:** The solution came from separating the underlying need, which was occasional access to high-capacity compute, from the requested implementation of permanent capacity. I would keep short decision records showing the demand, options, cost and outcome.

### STARR: choosing an existing database route over a new S3 path

**Situation:** Some users wanted data written directly to an S3 bucket so POSIT Connect could access it, while an existing controlled database route could already satisfy much of the analytical need.

**Task:** I needed to decide impartially between user convenience and the security, support and maintenance implications of creating another data path.

**Action:** I clarified the outcome the users actually needed, consulted the relevant stakeholders, and compared the proposed S3 route with the existing database connection. I explained the additional access-control, operational and support burden of the new route, and I recommended the existing route where it met the requirement.

**Result:** Avoiding an unnecessary new path limited the security, maintenance and delivery overhead while still giving users access to the data they required.

**Reflection:** Respecting a proposal does not mean accepting its implementation. Impartial decisions start by separating the user's need from their preferred solution and making the trade-off visible.

### STARR: making an impartial Hubble model decision

**Situation:** Hubble stakeholders held different views. Some wanted accuracy as the headline metric, analysts suggested Random Forest, and others favoured transformer models because they were current and powerful.

**Task:** I needed to choose the model that best benefited the business while ensuring those views were heard and tested fairly.

**Action:** I gathered the requested models and metrics, explained why class imbalance made macro-F1 more informative than accuracy alone, and agreed the comparison criteria before the final selection. I then tested the candidates against model quality, speed, explainability, security, maintainability, infrastructure and cost, and documented the trade-offs.

**Result:** TF-IDF with LinearSVC became the evidence-led recommendation rather than the fashionable choice, with competitive macro-F1, much faster training, coefficient-level explanations and lower operational risk.

**Reflection:** Impartiality is easier to demonstrate when the criteria are agreed before the results are known. I would make the decision record routine so stakeholders can challenge it if the evidence or the constraints change.

### Technical notes: clarification knowledge

Past learners cover evidence-led trade-offs more than interpersonal impartiality. Merge EPA clarification with the select-and-apply / stakeholder "value + risk" narrative.

1. **Independent and impartial** — decide on objective analysis and evidence, not personal bias or pressure. Agree criteria and weights *before* seeing final scores where possible.
2. **Respecting others' views** — active listening; value diverse perspectives; incorporate relevant feedback; still decide on the evidence. Separating the user's *need* from their preferred *implementation* is a practical impartiality technique.
3. **Complex, unpredictable, changing circumstances** — unexpected challenges, new information, shifting priorities or funding. Adapt the process; do not drop the evidence standard.
4. **Benefit to the business** — efficiency, conflict resolution, innovation, strategic goals. Name the outcome (capacity provided, path avoided, model chosen) and keep a short decision record (demand, options, cost, outcome).

## Explains how they have worked with software engineers to ensure suitable testing and documentation processes are implemented in line with organisational requirements

**Relevant KSBs:** S14, B1.

### STARR: engineering controls for Hubble

**Situation:** Hubble became a complex tool with varied real-world documents, several contributors and many users. A small change to parsing or preprocessing could silently affect extraction, model inputs or the outputs analysts relied on.

**Task:** I needed to establish, with engineers and contributors, proportionate testing, change control and documentation that supported safe delivery without imposing a heavyweight process on a small team.

**Action:** In the workplace repository I established the principle that changes require tests. If a function had no test, one was written before modifying it, and the suite had to pass before merging to main. Unit tests covered individual functions. Integration-style cases covered complex real documents, because input variation cannot be covered by isolated tests alone. User acceptance came through the analyst testing described under the evaluation criterion.

For traceability and planning, I used GitLab issues, templates, epics and milestones, together with a lightweight Kanban board.

The documentation worked at three levels. A full README covered the multi-system setup, serving as process documentation for new users. Detailed Markdown design notes covered the architecture, the workflows and the reasons behind the key decisions, serving as technical documentation. Analyst guidance explained how to interpret the outputs, serving as user documentation.

I collaborated with platform and DevOps engineers on ODC, data paths and environment constraints, and turned operational findings into tests or documentation wherever possible. In a public-sector context, undocumented behaviour or an unrepeatable result can undermine trust even when a metric looks strong, so reproducibility and traceability were treated as requirements rather than extras.

**Result:** New users could set up the project from the README, contributors could change tested functions with confidence, and the issues and milestones provided an audit trail from requirement to implementation.

**Reflection:** Up-front tests and documentation reduce future change cost and dependency on individual knowledge, and they make AI work more open to review. The largest remaining risk is the diversity of source documents, so I would expand a versioned representative corpus, automate the integration tests in the merge pipeline, and link requirements, tests and release notes explicitly.

### Technical notes: clarification knowledge

Past-learner notes only lightly touch documentation, Git and MLOps. Follow the EPA clarification structure; add pipeline/MLOps vocabulary where useful.

1. **Collaboration with software engineers** — regular communication, joint planning, shared understanding of technical constraints (ODC, data paths, environments), collaborative problem-solving.
2. **Suitable testing processes**
   - Unit — individual components
   - Integration — modules/services together; complex real documents
   - System — complete system against requirements
   - UAT — end users validate functionality and usability
   - Plus MLOps-style checks: schema, missing-rate, ranges; CI before merge
3. **Documentation processes**
   - Technical — architecture, code, APIs, design decisions
   - User — guides and manuals for interpreting outputs
   - Process — development, testing, maintenance, setup (README)
4. **Organisational alignment** — comply with organisational standards, industry best practice, regulatory requirements and QA guidelines. In a public-sector context, undocumented or unrepeatable behaviour undermines trust even when a metric looks strong.

# Theme 3: Awareness of the current and future impact of AI and data science for industry and society

**Theme KSBs:** K11, K17, K21.

## Describes how the potential roles and impact of AI and data science could affect own organisation, industry and society

**Relevant KSBs:** K11.

### STARR: Hubble's organisational and societal impact

**Situation:** Incomplete tagging made large parts of company accounts and tax computations difficult to analyse systematically. Manual interpretation did not scale.

**Task:** I needed to combine data engineering, data science and AI so analysts could exploit more of the information, while considering what wider impact this kind of automation could have.

**Action:** I used data engineering to extract, clean, canonicalise and structure the iXBRL, data science to analyse quality, balance and performance, and supervised NLP to categorise the descriptions. Results were delivered to controlled stores so the model supported analyst judgement rather than replacing it. I also considered where similar methods apply beyond HMRC, such as fraud detection, medical imaging and demand forecasting, and the societal risks: over-trusted outputs, opaque decisions, privacy loss, under-representation of rare classes, deskilling and resistance from staff whose work changes.

**Result:** The approach can reduce repetitive grouping by mapping varied descriptions to consistent concepts. In the workplace, Hubble expanded analytical coverage and supported tax-risk profiling. At industry level, the public notebooks are a reproducible example of the method. At societal level, better evidence may support fairer and more efficient revenue work, but Hubble does not make tax decisions and does not itself prove an increase in public funding.

**Reflection:** A narrow technical pipeline can have material social consequences. Positive impact depends on human oversight, transparent limitations, secure processing and monitoring. The defensible role of AI here is augmenting analysts, not replacing them.

### Technical notes: clarification knowledge

Drawn from past-learner notes on Impact of AI on Industry and Society and Will AI remove jobs? Aligns to organisation / industry / society.

#### Impact on own organisation

- **Operational efficiency** — automate repetitive tasks, optimise workflows, improve decisions
- **Innovation** — new products/services, enhanced customer or analyst experience, competitive capability
- **Data-driven insights** — trends, prediction, strategic decisions
Keep Hubble claims to verified outcomes; distinguish extraction impact from classifier impact.

#### Impact on the industry

- Market dynamics and new business models; disruption of traditional practice
- Regulatory change (privacy, AI regulation)
- Collaboration and integration of AI across sectors
Label industry impact as *potential* unless you can show external reuse or changed practice.

#### Impact on society

- **Ethical** — privacy, bias, fairness, accountability
- **Economic** — job creation and displacement; changed nature of work
- **Social** — healthcare, education, public services (including fairer/more efficient revenue work when used as decision support)

#### AI and jobs (balanced past-learner answer)

AI more often **changes tasks** than eliminates whole occupations. Roles mix routine (automatable), judgement (harder) and accountability (often required by policy). Credible figures: WEF ~170m created / 92m displaced by 2030; IMF ~40% global exposure (~60% advanced economies); ILO — clerical work especially exposed to GenAI. Frame **displacement vs augmentation**. Organisational response: work redesign and reskilling. Biggest risk often "people with AI skills vs without", plus loss of human accountability if outputs are rubber-stamped.

## Explains how they have assessed and addressed the potential business impact of ethical issues relating to AI and data science, the way procedures and methods are selected, and the unintended consequences to the business when they are applied

**Relevant KSBs:** K11, K17. Cross-reference S12 and B3 in Theme 4.

### STARR: ethical impact assessment for Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information. A classifier used in a tax-risk context could create privacy, bias, transparency and accountability risks if its categories were treated as fact or used outside their intended purpose.

**Task:** I needed to assess those ethical issues before and during development, choose proportionate procedures and methods, and reduce the likelihood that unintended model behaviour would cause legal, operational or reputational harm.

**Action:** On the assessment side, I completed a DPIA before work began and reviewed it as the design evolved. I also assessed representation and imbalance quantitatively, using frequency distributions, macro-F1, per-class measures, confusion matrices and residual examples rather than relying on overall accuracy.

On the addressing side, I canonicalised names, companies, dates, postcodes and numbers in the pipeline so that high-cardinality identifiers were not the trained feature. That is feature minimisation, not anonymisation: the source description is retained, so access, retention and purpose controls remain necessary. Processing stayed inside controlled environments. I tested balanced class weights, biased sampling and oversampling. The final LinearSVC used balanced weights, and several of the neural and transformer weighting approaches actually made performance worse. Demographic fairness is still proposed rather than completed. The notebook records the plan: detect bias by checking behaviour across regional names and sexes, assess fairness with demographic parity and equalised odds, and mitigate through re-sampling, re-weighting or a separate model if the classifier proved weaker for smaller companies, whose filings may use different software and wording.

Ethics also shaped the method selection itself. I chose an explainable TF-IDF and LinearSVC pipeline partly so that coefficients, LIME and SHAP could expose feature influence, and model provenance was part of the selection decision.

Unintended consequences were found and fixed through user testing. Acceptance testing found blank descriptions being classified from their surrounding context, so I stopped predictions where the description was absent. Usability feedback showed the top-five display created false confidence, so I simplified it. Both user changes need internal evidence.

**Result:** Identity-like tokens were removed from the modelling feature, minority-class and robustness failures were made visible, and a simpler model enabled direct inspection. Workplace controls kept the model as decision support rather than an automated determinant.

**Reflection:** Ethical assessment must cover the whole sociotechnical process: the data, labels, metrics, model, interface, users and downstream decisions. A technically explainable model can still be misused, so future improvements include monitoring, enforced workflow controls, periodic DPIA review and clearer warnings for low-reliability classes.

### Technical notes: clarification knowledge

Drawn from past-learner Risks of Adopting AI + mitigations, governance bullets, Model Drift / Poor Data Quality. Aligns to assess → address → method selection → unintended consequences → business impact.

#### Assessing ethical issues

Identify privacy, algorithmic bias, transparency, accountability, accuracy. Methods: ethical audits, stakeholder consultation, DPIA / impact assessments; quantitative representation and imbalance analysis (macro-F1, per-class, confusion, residuals) rather than headline accuracy alone.

#### Addressing ethical issues

Data-protection measures; fairness checks (demographic parity, equalised odds — if implemented); transparency/explainability (coefficients, LIME/SHAP); GDPR and ethical AI / Responsible AI principles; human-in-the-loop for significant decisions.

#### Past-learner risk categories (useful vocabulary)

Data (quality, privacy, access); model (bias, opacity); operational (drift, latency, weak monitoring); business (wrong predictions, over-dependence); security (adversarial, poisoning); compliance (audit trails, approval); skills/adoption; financial; ethical/societal.

**Mitigations:** data governance; validation and explainability; continuous monitoring; meaningful human review; security testing; formal approval/audit; training and change management.

#### Method selection

Weigh ethical implications alongside performance (explainability may favour linear models over transformers). Explicit decision criteria. Prefer robust methods and HITL when label quality is poor.

#### Unintended consequences

Anticipate (risk assessment); detect (monitoring, UAT/usability); correct and retest. Examples: blank-description predictions; dashboard false confidence; drift after taxonomy or process change.

#### Business impact of getting ethics right

Public/customer trust; avoided legal issues; protected reputation; defensible decisions. For a public body, legitimacy can outweigh any fine.

#### Reference frameworks

UK responsible-AI principles (safety/security/robustness; transparency/explainability; fairness; accountability/governance; contestability/redress); OECD AI guidelines; EU AI Act risk tiers.

## Describes how they have applied solutions, demonstrated awareness and explained the changes and trends that have led to enhancement of working practices within their organisation and other members of the team

**Relevant KSBs:** K17, K21.

### STARR: testing modern model families before selecting a simpler Hubble model

**Situation:** Transformers, domain-specific BERT models, embeddings and neural networks were prominent developments in text classification, and stakeholders could reasonably expect Hubble to consider them.

**Task:** I needed to test whether those developments improved the classification problem enough to justify their infrastructure, assurance and maintenance costs.

**Action:** I followed the research literature, technical documentation and practical communities, and then implemented real comparisons across classical machine learning, MPNet and e5 embeddings, CNN and neural architectures, and SEC-BERT, all on fixed data flags. I assessed macro-F1 and per-class performance alongside runtime, CPU and GPU needs, provenance, explainability and deployment fit. The evidence was concrete: MPNet's advantage over TF-IDF was small to negligible across the runs, SEC-BERT's higher point estimate came with overlapping intervals, and the robustness categories exposed different failure modes in each model family. I explained the evidence through project documents, demonstrations and stakeholder discussions.

**Result:** The testing showed that the simpler TF-IDF and LinearSVC pipeline was the stronger operational recommendation, and that the recommendation was researched rather than assumed.

**Reflection:** Awareness of a trend does not require adopting it. Applying the trend meant testing it credibly and letting the result improve the team's model-selection practice.

### STARR: applying the grounded-LLM trend in Graffiti

**Situation:** iXBRL International material showed that passing a complete HTML filing to an LLM performed poorly, while extracting the structured iXBRL first gave the model more relevant context.

**Task:** I needed to apply that finding in a usable tool and explain both the opportunity and the risks to colleagues and the wider community.

**Action:** I built Graffiti to extract the iXBRL, select the relevant structured content, and combine it with the user's query. Through demonstrations and discussions I explained hallucination, prompt injection, data leakage, cost, governance and the need for human review.

**Result:** Graffiti provided a clearer route for interrogating public filings and demonstrated how grounding improves LLM analysis without treating the output as an automated decision.

**Reflection:** I would continue monitoring LLM tool use and MCP, applying new capability only after controlled testing and an explicit assessment of what additional systems and data the model could access.

### STARR: converting current practice into reusable team workflows

**Situation:** Colleagues needed practical ways to adopt changing machine learning practice consistently, not just occasional updates about new tools.

**Task:** I needed to turn the relevant developments into working practices that improved reproducibility, review and appropriate use across the team.

**Action:** I promoted experiment tracking, repeatable environments, tests, per-class evaluation, documented limitations and human-in-the-loop use. The channels were Teams, mentoring, the README and design documents, and the DAP wiki.

**Result:** Team members had reusable guidance and a stronger basis for matching model complexity to the evidence, the governance and the business need.

**Reflection:** The next step is measuring the effect on speed, quality and reproducibility, rather than assuming that publishing guidance proves the enhancement.

### Technical notes: clarification knowledge

Drawn from past-learner "How do you identify trends…" plus dissemination (turning awareness into practice).

#### Applied solutions

Concrete implementations: new technologies, methodologies or strategies put into practice (tested model families; grounded-LLM tool; reusable wiki/README workflows) — not just awareness.

#### Demonstrated awareness (how to identify trends)

1. Track research and industry reports
2. Monitor vendor/ecosystem updates
3. Analyse enterprise adoption patterns
4. Use data-driven signals (jobs, investment)
5. Engage communities/networks
6. Observe use-case evolution
7. Track regulatory/governance trends
8. Validate with PoCs; separate hype from maturity (scalability, cost-benefit, governance fit)

Current talking points: GenAI/LLMs, copilots, multimodal AI, agents, responsible AI, edge inference; shift descriptive → predictive → prescriptive.

#### Explaining changes and trends

Communicate significance and impact to the team — demonstrations, docs, stakeholder discussions — not only personal reading.

#### Enhancement of working practices

Tangible improvements: efficiency, collaboration, quality, reproducibility (experiment tracking, environments, tests, per-class evaluation, HITL). Prefer a measured before/after where possible.

## Explains the impact, consequences and risks of non-compliance to the business

**Relevant KSBs:** K11, K17. Cross-reference S12 and B3 in Theme 4.

### STARR: designing to prevent non-compliance in Hubble

**Situation:** Hubble used sensitive data in a regulated public-sector environment. Non-compliance could arise through excessive collection, personal-data leakage, weak access controls, unassured technology, opaque model use, or decisions made without appropriate human review.

**Task:** I needed to understand the impact of those failures and build preventive controls into the pipeline so the product remained legally, ethically and organisationally defensible.

**Action:** I used the DPIA to identify the data-protection and governance risks. I minimised and canonicalised personal information, kept processing in controlled environments, restricted S3 and Oracle access, considered provenance in the model selection, documented lineage and design choices, and retained human review throughout. Hubble's classifications were advisory inputs, which matters because UK GDPR Article 22 restricts solely automated decisions that have legal or similarly significant effects, and a nominal human-in-the-loop is insufficient if the person lacks the time, information or authority to disagree.

I treated compliance as an operational requirement during model and infrastructure selection rather than as a final approval step, and I communicated that classifications were suggestions rather than the defining factor in any action.

I also ran the control lifecycle as a cycle rather than a one-off. Identify the requirements and owners, document the risks in the DPIA, implement minimisation, access controls, assurance and oversight, test the controls, approve the release, monitor use, and review whenever the data, purpose, model, users or infrastructure changes. Compliance evidence stays linked to the same version of the data, code and model that produced the output.

**Result:** The work avoided any known privacy or security incident and proceeded with proportionate controls. Those controls reduced the likelihood of regulatory investigation, legal challenge, invalid decisions, operational rollback, financial loss, reputational damage and loss of public trust.

**Reflection:** For a public body the largest consequence may be the loss of legitimacy and trust, even where a financial penalty is not the immediate outcome. Compliance evidence must remain current as the data, users, models and infrastructure change, so I would schedule formal DPIA and control reviews linked to releases.

### Technical notes: clarification knowledge

Closely linked to the previous ethics criterion. Drawn from EPA clarification plus past-learner compliance/governance risk bullets. Prefer Assessment-criteria figures for UK GDPR fines (past learners mention GDPR but not the UK £ amounts).

1. **Impact on business operations** — delays, interrupted service, forced shutdown, outputs quarantined, decisions reviewed, systems rolled back.
2. **Legal consequences** — penalties, fines, sanctions, enforcement notices, litigation.
3. **GDPR penalty figures** — UK GDPR/DPA 2018: higher max £17.5m or 4% worldwide turnover; standard £8.7m or 2%. EU GDPR: €20m/4% and €10m/2%. UK regulator: ICO.
4. **Financial risks** — remediation, legal fees, incident response, new systems/processes, duplicated analysis, delayed outcomes; also unclear ROI / maintenance costs from past-learner financial-risk list.
5. **Reputational damage** — eroded public/customer trust; stakeholder confidence. For a public body, legitimacy loss can outweigh any fine.
6. **Operational risks** — breaches, security vulnerabilities, inefficiencies; missing audit trails or approval processes (past-learner compliance risks).
7. **Regulatory scrutiny** — increased oversight across programmes after a failure.

Preventive framing: identify requirements → DPIA → controls → test → approve → monitor → reassess on change. Article 22: solely automated significant decisions need valid condition and meaningful human review.

---

# Theme 4: Development of suitable AI and data science solutions with consideration for ethical, legal, regulatory, governance and accessibility issues

**Theme KSBs:** K29, S12, B3.

## Evaluates the regulatory, ethical and legal requirements that affect implementation of solutions, including the need for accessibility for all users and diversity of user needs

**Relevant KSBs:** K29, S12, B3.

### STARR: applying governance and privacy controls to Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information. Its classifications could create privacy, fairness, transparency and accountability risks if used outside their intended purpose.

**Task:** I needed to evaluate the legal, ethical, regulatory and governance requirements across the end-to-end data process and make the pipeline defensible in a public-sector environment.

**Action:** I completed a DPIA before development and reviewed the controls as the design evolved. I then mapped the UK GDPR principles onto the pipeline concretely rather than treating them as abstract labels. Purpose limitation meant using the data only for the defined analytical purpose. Minimisation meant replacing unnecessary names, companies, dates, postcodes and numbers with typed placeholders before training, which reduced the identity signal reaching the model, while recognising that the retained source still needs access, retention and lawful-purpose governance. Security meant controlled environments and controlled output stores. Accountability meant retaining the DPIA, the decision records, the lineage and the tests.

The lawful basis and any statutory power come from the approved DPIA rather than being guessed in discussion. Model provenance formed part of the selection, and I chose an established, explainable TF-IDF and LinearSVC pipeline with classifications documented as advisory under human review. That keeps the solution clear of Article 22's restriction on solely automated significant decisions.

**Result:** The design reduced unnecessary personal-data signal in the model feature and made the model's use easier to explain and challenge. The DPIA, the retention and access controls and the controlled-environment evidence are needed to show that the identifiable source data itself was governed.

**Reflection:** Governance is a lifecycle activity, not a one-off approval. I would link DPIA and control reviews to material changes in the data, purpose, model, users or infrastructure.

### STARR: protecting personal data in a Companies House modelling pipeline

**Situation:** In a pipeline using Companies House filings, otherwise public documents could still contain director names or personal information. Public availability does not stop it being personal data, and it does not supply a lawful basis.

**Task:** I needed to ensure that model development did not unnecessarily retain personal information or create a leakage risk.

**Action:** I applied privacy by design during cleaning, replacing names, company names, dates, postcodes and numbers with typed placeholders so they were not raw model features. The notebooks prove that transformation, though their saved data retains the original description, and they show a local demonstration rather than the controlled AWS and Oracle route. If that route is a separate workplace pipeline, its architecture and access-control artefacts are needed, and the separation should be stated explicitly.

**Result:** The modelling workflow could be demonstrated without raw identifiers as training features. Controlled access to the retained source data is a separate workplace result that the notebooks do not establish.

**Reflection:** Public availability does not remove the need for data minimisation. I would still document the lawful purpose, retention, access roles and any dependency or model-licence checks for the specific implementation.

### STARR: reviewing an existing product with a WCAG specialist

**Situation:** On another project, an existing product lacked evidence that it met the accessibility needs of all users. This is a live issue for a public-sector body, because WCAG conformance at Level AA is a legal requirement for digital services.

**Task:** I needed to identify the gaps with appropriate expertise and establish a practical remediation route.

**Action:** I engaged a WCAG specialist, reviewed the existing product with them, agreed a plan to address the identified issues and began implementing the fixes.

**Result:** The project gained an expert-informed accessibility remediation plan and started moving accessibility work into the delivery process.

**Reflection:** Retrofitting accessibility is harder than designing it in. I would introduce an accessibility checklist, acceptance criteria and representative user testing during discovery, and I would retain the WCAG version, the findings and the retest evidence.

### STARR: providing an accessible installation route for Graffiti

**Situation:** Graffiti was normally installed by dragging a bookmarklet to the browser's bookmarks bar, an interaction that some users cannot perform.

**Task:** I needed to provide another way to install the tool without relying on that drag-and-drop action.

**Action:** I wrote alternative installation guidance that achieved the same outcome without requiring users to drag the bookmarklet.

**Result:** Users who could not use the default interaction had an alternative route to install Graffiti.

**Reflection:** Accessibility includes setup instructions and interaction methods, not only the main user interface. I would validate the alternative with affected users and include keyboard and assistive-technology checks in future releases.

### STARR: reducing cognitive confusion in the Hubble dashboard

**Situation:** The dashboard showed the top five candidate concepts and their raw scores. User testing showed that the weak alternatives and unfamiliar scores confused non-specialist users.

**Task:** I needed to make the output clearer for users with different technical and domain knowledge while avoiding false confidence in the model.

**Action:** I reviewed the feedback, limited the display to more confident matches, and added explanatory wording about what the scores meant and how the predictions should be used. I treated cognitive clarity and plain language as accessibility requirements in their own right, alongside the technical checklist.

**Result:** The dashboard presented less distracting information and gave users clearer context for interpreting the model's suggestions.

**Reflection:** Accessibility includes cognitive clarity and language matched to the audience. I would test the revised presentation with representative analysts, subject-matter experts and accessibility users, and retain the evidence.

### Technical notes: clarification knowledge

Past learners only give high-level privacy/bias/governance vocabulary — the GDPR/WCAG detail below is Assessment-criteria authored and must stay. Structured to the EPA clarification's five points; linked to the compliance criterion in Theme 3.

#### 1. Regulatory requirements

Stay current with laws and standards governing the industry: UK GDPR / DPA 2018, sector rules, accessibility regulations. Incorporate changes into solutions; name owners and reassessment triggers.

**UK GDPR seven principles:** lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability.

**Six lawful bases:** consent, contract, legal obligation, vital interests, public task, legitimate interests.

**Special-category data:** racial/ethnic origin, political opinions, religious/philosophical beliefs, trade-union membership, genetic, biometric, health, sex life, sexual orientation. **Equality Act protected characteristics:** age, disability, gender reassignment, marriage/civil partnership, pregnancy/maternity, race, religion/belief, sex, sexual orientation.

**DPIA:** required where processing is likely high risk. Records nature/scope/context/purpose, necessity/proportionality, risks to people, controls, residual risk, consultation, approval. Start before processing; revisit on material change.

**Article 22:** restricts solely automated decisions with legal or similarly significant effects unless a valid condition and safeguards apply. Meaningful human review = understanding + evidence + authority to override.

**UK vs EU GDPR:** near-identical; differences in scope (national security/immigration), age of consent (13 UK vs default 16 EU), enforcement (ICO vs EDPB/member states). Transfers: adequacy or SCCs/BCRs.

#### 2. Ethical considerations

Fairness, transparency, accountability; bias; privacy; responsible use. Past-learner mitigations: governance, SHAP/LIME, HITL, monitoring. UK responsible-AI principles; OECD; EU AI Act risk tiers (banned / high-risk / transparency / minimal).

#### 3. Legal requirements

IP, contracts, licences (dependencies and models), data-sharing conditions, controller/processor roles, retention, support status, right to audit. Protect stakeholder interests; keep solutions legally sound.

#### 4. Accessibility for all users

WCAG 2.2 (A / AA / AAA). UK public-sector digital services: Level AA under Public Sector Bodies Accessibility Regulations. Practice: keyboard, visible focus, semantics, text alternatives, labels/errors, contrast, zoom/reflow, captions, not colour-only. Test: automated + keyboard + screen reader + representative users. Includes setup routes and cognitive clarity (plain language, not overwhelming alternatives).

#### 5. Diversity of user needs

Cultural, social, economic and ability diversity. Interface diversity (assistive tech, devices, language, confidence) and data diversity (unrepresentative training → biased models). Gather feedback; incorporate diverse perspectives into design and evaluation.

---

# Theme 5: Continuous professional development

**Theme KSBs:** B5, B8.

## Analyses how they take responsibility for their own and their team's currency of knowledge and skills, and their professional and personal growth and development

**Relevant KSBs:** B5, B8.

### STARR: taking responsibility for my own structured development

**Situation:** The apprenticeship provided more material than could be absorbed passively, while AI, NLP, cloud platforms and governance continued to change quickly.

**Task:** I needed to prioritise my learning, develop genuine understanding and maintain the standard required alongside my workplace responsibilities.

**Action:** I completed the structured QA material, made detailed notes, and selected the most relevant recommended books and academic sources for deeper study. Where I did not understand a point, I investigated it properly rather than leaving a superficial explanation. Because reading everything was unrealistic, I prioritised sources by relevance and credibility.

**Result:** My structured study contributed to an assessment result of 80% and strengthened the technical foundation I applied at work.

**Reflection:** CPD requires deliberate prioritisation, curiosity and evidence of understanding. I would keep a dated development log linking each important source to the knowledge or decision it changed.

### STARR: using current research to improve Hubble model selection

**Situation:** Hubble needed a credible text-classification approach while transformers, domain-specific BERT models, embeddings and experimentation tools were developing rapidly.

**Task:** I needed to keep my technical knowledge current enough to test those approaches properly, avoiding both obsolete methods and fashion-driven choices.

**Action:** I used the transformer literature, practical sources, Hugging Face documentation, relevant GitHub repositories, and the documentation for scikit-learn, TensorFlow and Keras, Optuna and MLflow. I applied the learning directly by testing TF-IDF, LinearSVC, embeddings, BERT and SEC-BERT, and CNN, MLP and RNN models, and by improving the experiment comparison and reproducibility.

**Result:** The learning directly informed the evidence-led selection of TF-IDF with LinearSVC and gave the model comparison greater technical credibility.

**Reflection:** Staying current is useful when it changes a real decision. In this case, testing the modern methods credibly strengthened the justification for the simpler operational choice.

### STARR: converting personal learning into team capability

**Situation:** DAP users needed current practical guidance, and useful knowledge has limited organisational value if it stays with one person.

**Task:** I needed to transfer the relevant learning into reusable team practice and support colleagues' development.

**Action:** I recorded the learning in project documentation, setup scripts and the DAP wiki, demonstrated approaches, and mentored teams. The guidance covered virtual environments, reproducibility, testing, secure data access, human oversight, model limitations and technique selection.

**Result:** Team members gained the guidance and support to build their own tools, while DAP grew from one user to more than 150.

**Reflection:** Team development needs stronger evidence than publication counts. I would formalise skills reviews, agree learning goals, check progress, and gather feedback on what colleagues can do independently afterwards.

### Technical notes: clarification knowledge

Drawn from past-learner trend-tracking (own currency) and dissemination (team development), plus EPA clarification.

#### 1. Staying current with knowledge and skills (own)

- Continuous learning: courses, certifications, workshops, seminars (including structured apprenticeship material)
- Reading/research: journals, papers, books; prioritise by relevance and credibility
- Networking: professional groups, conferences, online communities — do not imply physical attendance if it was online reading
- Trend methods from past learners: research tracking, vendor/ecosystem monitoring, adoption patterns, PoCs to separate hype from value

#### 2. Team development

- Training programmes and knowledge-sharing meetings
- Mentorship and guidance (describe informal mentoring accurately)
- Encourage continuous learning and further education
- Dissemination toolkit: standards, CoP, wikis, reusable assets, governance, pilots

#### 3. Professional growth

- Clear development goals and plans
- Regular performance/skills reviews; identify gaps
- Coaching, advancement opportunities, recognition
- Link learning to decisions changed (dated CPD record)

#### 4. Personal growth

- Work-life balance and well-being
- Soft skills: communication, leadership, teamwork
- Support broader interests that aid development

Be ready to name specific courses, books and articles, with a brief reaction to each, and any community membership.

## Explains how they selected and applied the most effective/appropriate AI and data science techniques to solve a complex business problem in line with organisational and regulatory requirements

**Relevant KSBs:** B5, B8. Cross-reference S26.

### STARR: evidence-led selection for a regulated Hubble deployment recommendation

**Situation:** Hubble needed to map inconsistent, often untagged account descriptions to standard taxonomy concepts. The data was large, imbalanced and domain-specific, with 826 engineered labels of which the 141 with sufficient examples were modelled. HMRC required secure, explainable and supportable processing.

**Task:** I needed to choose and apply a technique that solved the business problem at scale while meeting organisational policy, data-protection, security, infrastructure, cost and maintenance requirements.

**Action:** I defined the problem and the success criteria before recommending a model, and I framed the problem deliberately. The required output was a taxonomy classification. Labelled data already existed in the form of tagged items, so supervised classification fitted. The data was unstructured text, which pointed to NLP pipelines.

In applying the techniques, the pipeline extracted and cleaned millions of rows, canonicalised the high-cardinality identifiers and created fixed seeded splits. I established baselines first, then evaluated the classical models, MPNet and e5 embeddings, SEC-BERT and the CNN and neural alternatives. The evaluation used macro-F1, per-class measures, confusion and residual analysis, stratified cross-validation and bootstrap intervals, because accuracy alone hid minority-class performance. Alongside those I compared training and inference time, model size, CPU and GPU needs, explainability, provenance, maintainability and deployment complexity. On the common holdout, LinearSVC recorded 0.800 macro-F1 against 0.808 for the CNN and 0.823 for SEC-BERT, with overlapping intervals. The label-space remap for the neural and transformer heads remains outstanding before the cross-family difference is treated as final.

The organisational and regulatory constraints shaped the choice directly rather than sitting alongside it. The DPIA and the minimisation requirements shaped the features. The explainability expectations favoured inspectable coefficients over a fine-tuned transformer. The infrastructure reality of a CPU estate with scarce GPUs, together with provenance and assurance concerns, weighed against SEC-BERT. Delivery had to fit the supported R workflow with controlled ODC and Oracle delivery. Internal artefacts are needed for the DPIA, the integration and the user changes.

**Result:** The evidence supports an operational recommendation for TF-IDF plus LinearSVC. It is CPU-compatible, directly inspectable, and free of SEC-BERT's lifecycle burden in exchange for an uncertain point-estimate gain. I treat this as a validated comparison and a deployment recommendation rather than proof of live production.

**Reflection:** The most effective technique is the one that meets the complete business and regulatory need, not the model with the highest laboratory score. My CPD let me test the modern methods credibly, while judgement favoured the simpler recommendation. Before formal deployment evidence I would fix the decision-matrix key, group the splits by filing, add time and taxonomy validation, define acceptance thresholds, verify test and production parity, and implement monitored human oversight.

### Technical notes: clarification knowledge

Primary past-learner source: "select and apply the most effective/appropriate AI and data science techniques…". Also Types of ML, ML Pipeline, KPIs / Poor Data Quality, Common algorithms, Model Drift, governance constraints.

#### 1. Start with the business problem (not the model)

Clarify the decision and who uses it. Convert to a measurable objective. Define success KPIs and constraints: accuracy targets, latency, interpretability, regulatory/compliance, cost, operational effort.

#### 2. Diagnose whether AI/ML is needed

- Rules/automation when logic is stable, auditability is high, or labels/data are missing
- Analytics/BI when insight/reporting is enough
- ML/AI when patterns are complex, scale is large, and predictions/segmentation are needed with usable data

#### 3. Frame the ML task type

| Business need | Formulation |
| --- | --- |
| Numerical estimate / forecast | Regression |
| Yes/No | Binary classification |
| Multiple categories | Multi-class classification |
| Group similar items | Clustering |
| Unusual behaviour | Anomaly detection |
| Text / documents | NLP (+ classifier / transformer / RAG as needed) |
| Images/video | CNN / vision transformers |
| Sequential decisions | Reinforcement learning (less common enterprise) |

#### 4. Assess data readiness

Availability, quality, label quality/bias/timeliness, leakage, freshness/drift risk. Poor quality → robust methods, simple baselines, quality/drift KPIs, HITL for high-risk decisions.

#### 5. Build a baseline first

Naïve / rules / simple statistical or tree baseline. Confirms feasibility, sets a floor, helps stakeholders see improvement.

#### 6. Decision matrix (performance vs constraints)

- Interpretability critical → linear/logistic, trees, explainable boosting, SHAP for ensembles
- Tabular performance → RF / gradient boosting
- Text → embeddings + classifier; transformers where justified
- Limited labels → semi/self-supervised, active learning, clustering + human validation
Prefer the simplest model that meets performance, latency, interpretability and governance.

#### 7. Validate with risk-aligned metrics

Classification: F1/AUC under imbalance; precision if FP costly; recall if FN costly. Regression: MAE / RMSE. Operational: latency, throughput, cost, calibration, fairness. Business: SLA, cost, deflection, etc.

#### 8. Production-ready (MLOps)

Feature pipelines; versioning/reproducibility; automated tests; deployment strategy (shadow/A-B/canary); monitoring (PSI/KS/χ², prediction drift, performance drift); retraining triggers and governance approvals.

#### 9. Organisational and regulatory compliance

Data privacy/security (GDPR); ethical concerns (bias, fairness, transparency); documentation and reporting; human override and escalation when confidence is low.

#### 60–90 second answer (past-learner)

"I start by clarifying the business decision and KPIs, and checking whether ML is required. I map the problem to the right technique, assess data readiness, build a baseline, then select models on performance vs interpretability vs latency vs governance. I validate with risk-aligned metrics and productionise with MLOps, drift monitoring and retraining triggers, with stakeholder alignment and operational controls."

---

# Technical answer bank

These are pure revision notes for the "what does that mean?", "how does X work?" and "what are the strengths and weaknesses?" follow-ups. Give a plain-English explanation first, then the formula. Examiner guidance lists the common algorithms to be able to explain as SVM, decision trees, Naive Bayes, neural networks, K-means, PCA and Apriori, and all of them are covered below. The applied Hubble examples live in the STARRs above, not here.

## Learning paradigms

- **Supervised:** learns from labelled examples to predict labels for new cases. Examples include regression, decision trees, SVM and neural networks.
- **Unsupervised:** finds structure without labels. Examples include K-means, hierarchical clustering, PCA, Apriori and anomaly detection.
- **Semi-supervised:** a small labelled set plus a large unlabelled set, using self-training, label propagation or pseudo-labelling. Useful when labelling is expensive.
- **Self-supervised:** the model generates its own targets from raw data, such as masked words. This underpins LLMs and BERT pre-training.
- **Reinforcement:** an agent learns a policy from rewards through interaction with an environment (Q-learning, SARSA, Deep Q-Networks). Used in robotics, game AI and control.
- **Deep learning:** multi-layer neural networks learning hierarchical representations. **Generative AI:** models that produce new content such as text and images from learned distributions.
- **Data mining:** discovering hidden patterns, trends and relationships in large datasets through clustering, association rules and anomaly detection.
- **Data quality dimensions:** accuracy, completeness, consistency, validity, timeliness, uniqueness, lineage and relevance.

## Overfitting, validation and imbalance

- **Overfitting:** the model learns training noise, giving high training performance but weak test performance. Mitigate with regularisation, simpler models, more data, dropout, early stopping, pruning and cross-validation. **Underfitting:** the model is too simple and performs poorly on both. Mitigate with better features, more capacity or less regularisation. The **bias-variance trade-off** frames total error as bias squared (oversimplification) plus variance (sensitivity to the training sample) plus irreducible noise.
- **Train, validate, test:** training fits the parameters, validation tunes the hyperparameters, and the test set is unseen data used once at the end. **Cross-validation** folds train and validate together: K folds, train on K minus 1, validate on the held-out fold, rotate and average. **Stratified** CV keeps class proportions per fold. Fit any data-derived preprocessing inside each training fold to avoid leakage.
- **Imbalance handling:** accuracy misleads, because an always-majority model can score 99%. Use class weighting (weight roughly N/(K·n_k)), oversampling or **SMOTE** (synthetic minority examples created by interpolation), undersampling, and macro-F1, per-class metrics or AUC rather than raw accuracy.

## Classification metrics

Per class, one versus rest: **TP** is predicted and correct. **FP** is predicted and wrong, a Type I error. **FN** is missed, a Type II error and often the dangerous one in safety contexts. **TN** is correctly rejected. The **confusion matrix** tabulates these across the classes.

- **Accuracy** = (TP+TN)/total. Overall correctness, misleading under class imbalance.
- **Precision** = TP/(TP+FP). Of everything predicted positive, how much was right. Use when false positives are costly.
- **Recall (sensitivity)** = TP/(TP+FN). Of all real positives, how many were found. Use when false negatives are costly.
- **F1** = 2PR/(P+R). The harmonic mean of precision and recall, which penalises extreme imbalance between them. High precision with near-zero recall still scores low. *Recall versus F1 (a past question):* recall only measures coverage of the true positives, while F1 balances that coverage against precision.
- **Macro-F1:** the unweighted mean of per-class F1, so every class counts equally and rare classes matter. **Micro-F1** aggregates TP, FP and FN first and is dominated by frequent classes. **Weighted-F1** weights each class by its support.
- **Specificity** = TN/(TN+FP), the true-negative rate.
- **ROC curve and AUC:** the ROC plots recall against the false-positive rate across thresholds. AUC is the probability that a random positive ranks above a random negative, where 1.0 is perfect and 0.5 is random. For heavily imbalanced data, prefer the precision-recall curve and average precision. **Balanced accuracy** = (sensitivity + specificity)/2.

## Regression metrics

- **MAE** = mean(|y−ŷ|). The average absolute error. Robust to outliers and in the same units as the target.
- **MSE** = mean((y−ŷ)²). Penalises large errors and is differentiable, but its units are squared.
- **RMSE** = √MSE. Same units as the target and strongly penalises large errors.
- **R²** = 1 − SS_res/SS_tot. The proportion of variance explained, which can be negative for a poor fit. **Adjusted R²** penalises unnecessary features.
- **Median absolute error:** even more robust than MAE. A good answer for evaluation under poor data quality.

## Classic algorithms: how each works

- **Linear regression:** Y = β₀ + β₁x₁ + … + ε, fitted by least squares. The problem is convex with a single global minimum, solvable by the normal equation or gradient descent. It assumes linearity, independent errors, constant variance, and normal errors for inference.
- **Logistic regression:** the sigmoid P = 1/(1+e^−z) applied to a linear combination, thresholded to classify. Interpretable coefficients and probabilistic output, but a linear boundary.
- **Naive Bayes (a past question):** Bayes' theorem, P(class|features) proportional to P(features|class)·P(class), with the "naive" assumption that features are conditionally independent given the class. The likelihood therefore factorises into a product of per-feature probabilities. It is fast, a strong text baseline, and works with little data, but the independence assumption is unrealistic and calibration is poor. Variants: Multinomial for word counts (the usual text one), Gaussian for continuous features, Bernoulli for binary features. It is generative, modelling the data per class, in contrast to logistic regression's discriminative boundary-learning.
- **Decision tree:** recursively split on the feature and threshold that most reduces impurity. **Gini** = 1 − Σp_k². **Entropy** = −Σp_k·log₂p_k. **Information gain** = parent entropy minus the weighted child entropy. Easy to explain and handles non-linearity, but overfits easily and is unstable. Algorithms include ID3, C4.5 and CART, where CART's binary splits are the basis of random forests and boosting.
- **Random forest:** an ensemble of trees built with bagging (bootstrap samples) plus random feature selection at each split, which decorrelates the trees. Prediction is by majority vote or averaging. It has lower variance than a single tree and gives feature importance, but is less interpretable and heavier to run.
- **Gradient boosting (XGBoost, LightGBM, CatBoost):** trees are built sequentially, with each one correcting the errors of the previous ones by gradient descent in function space. Typically more accurate than a random forest, but easier to overfit and requiring more tuning.
- **SVM and LinearSVC:** finds the maximum-margin separating hyperplane by minimising ½‖w‖² + CΣmax(0, 1−yᵢ(w·xᵢ+b)). The prediction is the sign for binary problems, or the argmax of per-class scores in a one-versus-rest scheme. **C** trades margin width against violations: small C gives a soft margin, large C risks overfitting. The **kernel trick** (RBF, polynomial) implicitly maps the data to a higher-dimensional space to give non-linear boundaries, at a scaling cost. Linear SVMs suit large sparse text.
- **KNN:** a lazy, non-parametric method that classifies a point by majority vote of its K nearest training points. It has no training phase, but is expensive at prediction time, needs feature scaling, and suffers the curse of dimensionality.
- **K-means:** minimises Σ‖x − centroid‖². Assign points to the nearest centroid, recompute centroids as the means, and repeat to convergence. Choose K with the elbow method or the silhouette score, which runs from −1 to 1 and measures cohesion against separation. It is fast and scalable, but needs K in advance, is sensitive to outliers and initialisation (K-means++ helps), and assumes compact clusters. **Hierarchical clustering** builds a dendrogram, agglomerative or divisive, with a linkage rule (single, complete, average or Ward). It needs no K but costs O(n²) or more. **DBSCAN** groups dense regions and labels sparse points as noise, handling irregular shapes well.
- **PCA:** finds orthogonal directions of maximum variance through eigen-decomposition or SVD of the covariance matrix, then projects the data onto the top components ranked by explained variance. It reduces dimensionality and noise and removes correlated features, but the components are linear combinations and not directly interpretable. Standardise the features first.
- **Apriori:** frequent-itemset mining for association rules. **Support**(A) is the fraction of transactions containing A. **Confidence**(A→B) = support(A∩B)/support(A). **Lift**(A→B) = confidence/support(B), where a value above 1 means positive association. The algorithm builds up itemsets, pruning anything below minimum support at each step. Used for market-basket-style analysis.

## Text representation

- **TF-IDF:** TF(t,d) multiplied by IDF(t), where IDF = log(N/df(t)) and smoothed variants add ones. Usually L2-normalised. Common words are down-weighted and distinctive terms up-weighted. It is fast, CPU-friendly, interpretable, and strong with sparse linear models and domain-specific text, but has no synonym or context understanding and suffers vocabulary drift.
- **N-grams:** unigram, bigram and trigram features capture phrase-level meaning at the cost of feature count and sparsity.
- **Embeddings (Word2Vec, MPNet, e5, BERT-style):** dense vectors capturing semantic similarity, so related phrases group together across different wording. They are less interpretable and slower, and generic pre-training can miss specialist domain language. TF-IDF often wins on domain-specific tasks with distinctive vocabulary.

## Neural networks and transformers

- **How a neural network works (a past question):** the input layer takes the feature values, and hidden layers of nodes connect to it by weighted links. Each node computes a weighted sum plus a bias, z = Σwᵢxᵢ + b, then applies a non-linear activation. This is the feed-forward pass. The output layer produces the prediction, using softmax over the classes for classification or a single node for regression. The loss, cross-entropy for classification or MSE for regression, is computed against the labels. Backpropagation applies the chain rule to compute each weight's gradient, and gradient descent updates the weights opposite the gradient, w ← w − η·∂L/∂w, batch by batch. A full pass through the data is an epoch, and training repeats until convergence. The final weights are the model's parameters.
- **Training decisions:** the architecture (number and size of layers), activation functions, loss function, optimiser (SGD, momentum, Adam), learning rate (too large diverges, too small crawls), batch size, number of epochs, early stopping and dropout.
- **Activations:** sigmoid outputs 0 to 1 and suits binary outputs but suffers vanishing gradients. Tanh outputs −1 to 1 and is zero-centred. ReLU = max(0,z) is the hidden-layer default, with a dying-ReLU risk addressed by Leaky ReLU, PReLU or ELU. Softmax produces a multi-class output distribution.
- **CNN:** convolutional filters learn local patterns, whether image regions or phrase-like patterns over token sequences, and pooling downsamples. Fully connected layers do the final classification. **RNN and LSTM:** a sequential hidden state carried through the sequence, with LSTM's input, forget and output gates mitigating vanishing gradients. Both are largely superseded by transformers for NLP.
- **Transformers and BERT:** self-attention, Attention(Q,K,V) = softmax(QKᵀ/√d_k)V, lets every token attend to every other token in parallel. BERT is a bidirectional encoder pre-trained with masked-language modelling and next-sentence prediction, using WordPiece tokenisation and the `[CLS]` token for classification. BERT-Base has 12 layers, 768 dimensions and 12 heads. RoBERTa trains longer without NSP. Domain models such as SEC-BERT add specialist pre-training on financial text. The strengths are context and long-range dependencies. The weaknesses are GPU needs, slow inference, weak explainability, and provenance and supply-chain risk.

## Hyperparameter tuning

Hyperparameters control learning and are set around training: the split ratio, learning rate, optimiser, activation, loss, layers and units, dropout, epochs, K in clustering, kernel or filter size, and batch size. Parameters, the weights, are learned. Techniques: **grid search** is exhaustive. **Random search** samples combinations and is often nearly as good for less cost. **Successive halving** gives more resource to promising candidates. **Bayesian optimisation**, for example Optuna, uses prior trials to choose the next ones. Select on validation or cross-validation performance. Avoid tuning-time overfitting with more data, early stopping, not chasing the single top score, dropout and pruning, then confirm on one final untouched holdout.

## Statistical tests

- **Paired t-test:** `t = mean(d)/(sd(d)/√n)` on paired score differences, for example two models on the same folds. Pairing controls for split difficulty. It assumes roughly normal differences. Statistical significance is not practical significance, so always consider effect size and cost.
- **Welch's t-test:** `t = (m₁−m₂)/√(s₁²/n₁ + s₂²/n₂)`. Compares independent group means with unequal variances, checked first with an F-test. Safer than Student's pooled t-test in that case.
- **Z-test:** compares means or proportions via the normal distribution. It needs large samples (n of 30 or more) and known variance, or adequate counts for proportions.
- **Chi-square:** `Σ((O−E)²/E)`. Tests association between categorical variables or goodness of fit. It needs adequate expected counts and shows association, not causation.
- **ANOVA:** compares means across three or more groups, one-way or two-way, without inflating the error rate that many pairwise t-tests would create.
- **Quick recall:** t-tests and Z-tests compare means (small versus large samples). Chi-square tests categorical relationships. ANOVA compares three or more group means.
- **Bootstrap intervals:** resample to express the uncertainty in a metric. Overlapping intervals between models justify caution about superiority claims. The stronger design bootstraps the paired difference directly.

## Drift and monitoring

- **Types:** data drift, where the input distribution shifts. Concept drift, where the input-to-output relationship changes. Prediction drift, where the output distribution changes before labels arrive. Label or taxonomy drift, where the target's meaning changes. Upstream or extraction drift, where source-format changes alter the fields supplied.
- **Detection:** compare training and production distributions. **PSI** bins both and computes Σ(A−E)·ln(A/E), where below 0.10 means no drift, 0.10 to 0.25 moderate, and above 0.25 significant. It works for numeric and categorical data and is threshold-based. The **KS test** covers continuous features with a significance result, and **chi-square** covers categorical ones. For concept drift, track performance on recent labelled data with a sliding window.
- **Response:** confirm the drift type, contain the risk, collect fresh labels, retrain, re-validate, redeploy and reset the baselines.
- **KPIs under poor data quality:** raw accuracy and R² mislead, hiding garbage-in behind a plausible number. Prefer robust signals such as MAE or median absolute error, stability trends, drift KPIs (PSI, missing-rate), confidence and coverage rates, override and rollback rates, and the cost of wrong predictions.

## Lifecycle, DataOps and MLOps

- **CRISP-DM:** business understanding, data understanding, data preparation, modelling, evaluation, deployment. **SEMMA** is sample, explore, modify, model, assess. The operational pipeline expands to problem definition with KPIs, collection, EDA, cleaning and preprocessing, feature engineering, splitting, model selection, training, evaluation, tuning, deployment, then monitoring and retraining.
- **DataOps:** collaboration, automation, reuse, analytics-as-code, testing, monitoring, short cycles and data-driven improvement.
- **MLOps:** reproducibility, meaning an old model can be retrained with comparable results. Accountability, meaning production output can be traced to the code, data, model and parameters. Versioned collaboration, continuous testing, continuous monitoring and reusable infrastructure.

## Communication by audience

Senior managers want the business problem, value, risk, cost, timescale and the decisions needed, with metrics translated into consequences. Analysts want examples, confusion matrices, per-class reliability and how to use the outputs. Subject-matter experts want domain meaning, edge cases and correctness. DevOps and engineers want infrastructure, dependencies, runtime, tests and monitoring. Governance reviewers want the DPIA, minimisation, security, limitations, human oversight and auditability.

## Generic frameworks for open-ended questions

- **Selecting the right technique:** start with the business decision and KPIs, not the model. Check whether ML is needed at all. Map the question to a task type. Assess data readiness in terms of labels, quality, leakage and freshness. Build a fast, interpretable baseline. Choose through a decision matrix against interpretability, performance, latency and governance, taking the simplest model that meets all the requirements. Validate with risk-aligned metrics, and treat monitoring and retraining as part of the solution.
- **Disseminating practice:** standardise with methodologies, templates and documentation. Enable through communities of practice, wikis and training. Provide reusable assets. Embed governance. Demonstrate value through pilots. Make results visible, and foster the culture with senior sponsorship.
- **Tracking trends:** research and publication tracking (arXiv, the major labs), vendor and ecosystem monitoring, adoption-pattern analysis, community engagement through forums and conferences, and hands-on proof-of-concepts. Then filter hype from value by assessing scalability, cost-benefit and governance fit before recommending adoption.
- **Managing resistance to AI:** understand the concern, whether it is jobs, trust or competence. Involve users early. Show augmentation rather than replacement. Train people. Start with low-risk wins, and keep humans in control of the decisions.

## Risks of adopting AI (and mitigations)

The risk categories: data (quality, privacy, access control), model (bias, opacity), operational (drift, latency, weak monitoring), business (wrong predictions, over-dependence eroding oversight), security (adversarial inputs, data poisoning, supply chain), compliance (missing audit trails, no approval process), skills and adoption (gaps, resistance), financial (cost exceeding unclear benefit), and ethical and societal (unfair impact, loss of accountability).

The mitigations: data governance and quality controls, least privilege, validation and explainability tools such as SHAP and LIME, drift and performance monitoring, meaningful human review, adversarial and security testing, formal approval and audit, and training and change management.

---

# Final evidence and rehearsal checks

**Evidence checks**

- Verify the strongest numerical claims and bring an artefact where possible: 233% more extracted data, DAP growth to 150+ users, days rather than nine months, identified tax risk, the model scores and the 80% assessment result.
- Keep the label counts straight: 826 labels survived preprocessing, 141 met the frequency threshold and were modelled, and 685 were excluded.
- Treat the current scores as proof-of-concept estimates. The split is row-level rather than grouped, and the CNN and SEC-BERT heads need remapping before a final cross-family claim.
- Quote like for like: macro-F1 of 0.800, 0.808 and 0.823 with overlapping intervals, and LinearSVC's minutes-versus-hours training, sub-second-versus-minutes inference, and megabytes-versus-gigabytes size. State the hardware.
- Correct the decision-matrix interpretability key and sensitivity-test the weights before quoting its numeric ranking.
- Be precise about prototype versus production. The code establishes TF-IDF with LinearSVC as an operational recommendation, not proof of deployment. Add the internal release or approval artefact before saying it was deployed.
- Do not imply that Hubble makes tax decisions. It categorises data to support analyst judgement, with a human in the loop.
- Where the evidence is knowledge rather than a completed workplace action, say so clearly and connect it to the decision made. Do not invent a project.
- For each answer, be ready to name the artefact, another person who saw the work, the business outcome, the principal trade-off, the largest risk, and what would be improved next.

**Discussion technique**

- Speak in the first person. Say "I", not "we". The assessment is of my work.
- Replay the question back before answering, and use the KSB language in the answer.
- State my role and responsibilities early, and reference the journal and portfolio artefacts by name.
- Use STARR to structure answers, and always connect the technique to the business value.
- If asked about an algorithm I have not studied in depth, give the high-level view honestly and say I have not explored its mathematical foundations, rather than improvising.
- Cue cards and notes are allowed. The journal is a memory aid, not a submission.
