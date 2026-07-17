**Artificial Intelligence Data Specialist, Level 7 Apprenticeship**
**Learner:** Jesse Karadia
**Organisation:** HMRC

This document organises professional-discussion preparation around the EPA assessment criteria. Each criterion has the relevant KSBs, one or more STARR answers containing all the applied evidence (what I did, with the technical specifics), and a short block of technical notes covering the pure knowledge that the criterion's clarification expects. The technical notes hold definitions, techniques and frameworks only, with no applied content mixed in.

Use the STARRs as speaking notes rather than a script. Speak in the first person ("I", not "we"), adapt the depth to the question, and be ready to name supporting artefacts such as test results, decision matrices, GitLab issues, dashboards, DPIAs, stakeholder feedback, wiki guidance and experiment records. The grading table assesses KSBs collectively within each theme, so the per-criterion KSB lists are a practical evidence map rather than official marking units.

## Evidence boundary and status

The EPA clarification repeatedly requires my own practical application in my current role and organisation. The notebooks in `Code/` are technical artefacts, not a substitute for workplace evidence about deployment, users, governance or business impact. Three evidence categories are used throughout this document.

- **Code-backed:** directly demonstrated by source code or saved output in `Code/`.
- **Workplace evidence:** statements about internal Hubble, HMRC systems, stakeholders, deployment or impact. These need an approved artefact or witness as well as my explanation.
- **Proposed/future:** a control or improvement that I can justify but must not describe as implemented.

The public notebooks use Companies House accounts and deliberately simplify the internal implementation. The public version is a Python/BeautifulSoup extraction of description and concept only, whereas the internal extraction is R-led, integrates R, Python and SQL, and captures contextual features such as table name and heading. I should present the notebooks as reproducible corroboration of the methodology and experiments, then use separate workplace artefacts to prove the internal architecture, operational scale, user changes and business outcome.

### Code artefact map

| Artefact | Demonstrates |
|---|---|
| `00_ixbrl_data_extraction.ipynb` | Python parser over a Companies House monthly accounts archive. Table descriptions and iXBRL concept labels saved to Parquet. |
| `01_ixbrl_eda_preprocessing.ipynb` | EDA, ambiguity and imbalance analysis, text cleaning, canonicalisation, label engineering, embedding comparisons and fixed seeded splits. |
| `03_ixbrl_experiment_models.ipynb` | Classical-model search, stratified CV, TF-IDF and embedding comparisons, bootstrap intervals, robustness cases, LIME/SHAP and the final LinearSVC configuration. |
| `04_ixbrl_nn.ipynb` | Optuna-led neural-network and CNN experimentation, class-weighting tests and robustness testing. |
| `05_xbrl_transformers.ipynb` | Hugging Face and PyTorch transformer comparison, SEC-BERT tuning, sampling and weighting experiments, explainability and resource trade-offs. |
| `06_compare_models.ipynb` | Three-model comparison using objective measures, confidence intervals and an operational rubric. |

### Key figures to quote

- Corpus: around 2.9 million extracted rows across 956 raw concepts, reducing to around 2.5 million rows and 826 engineered labels after cleaning. Modelling used the 141 labels with at least 350 examples each, and the 685 rarer labels were excluded.
- A fixed seeded 80/10/10 train/test/holdout split was used, with a 10,000-row holdout sample for like-for-like model comparisons.
- The top 75 raw concepts cover about 95% of items, and generic descriptions such as "Total" map to many different concepts. This ambiguity and long tail is what motivated contextual features and macro-F1.
- The final classical pipeline was word TF-IDF with 1-to-3-word n-grams, IDF weighting and L2 normalisation, feeding a LinearSVC with `C=2.8`, an L1 penalty, squared-hinge loss and balanced class weights.
- Holdout comparison (accuracy and macro-F1): LinearSVC **0.975 and 0.800**, CNN **0.977 and 0.808**, SEC-BERT **0.977 and 0.823**. The 95% bootstrap intervals overlap, so SEC-BERT's roughly two-point macro-F1 advantage is a point-estimate difference, not a statistically established improvement.
- Operational measures (training time, full-test inference time, model size): LinearSVC about 2.5 minutes, 0.6 seconds and 8 MB. CNN about 44 minutes, 24 seconds and 30 MB. SEC-BERT about 67 minutes, 143 seconds and 1.8 GB. State the hardware before generalising these.
- Embeddings: on one 1% run MPNet beat TF-IDF by about 0.003 macro-F1 at roughly 67 times the fit time. A later 1% run showed a difference of about 0.0001, which was not significant at 95%. Keep the two runs separate when quoting them.

### Limitations to state rather than hide

- The split stratifies individual rows rather than filings or descriptions, so related rows can cross partitions and the saved metrics may be optimistic. Production evidence needs a grouped (filing or company level) or temporal holdout.
- The CNN and transformer output layers cover all 826 labels even though only 141 have training examples. They should be remapped to the 141 classes and rerun before the cross-family ranking is treated as final.
- The decision matrix has a field-name mismatch that omits interpretability from its calculated score, and its subjective ratings and min-max scaling over only three candidates are sensitive to the weights. Correct it and run a sensitivity test before quoting the numeric ranking. The qualitative conclusion, that LinearSVC is favoured operationally, still stands.
- Canonicalisation reduces identity signal in the model feature. It does not anonymise the source data, and it does not replace access, retention and lawful-purpose controls.
- Fairness metrics (demographic parity, equalised odds) and live drift monitoring are proposed work, not implemented controls. What was analysed is class imbalance, per-class performance, robustness and residual errors.
- The notebooks prove a validated model comparison and a sound research method. They do not prove deployment, live monitoring, user acceptance, accessibility testing or business benefit.

## Evidence gaps: search for `TODO:`

### Theme 1

- **T1.1:** TODO: a verified measure of extra analytical coverage, manual effort avoided or profiling improvement attributable to classification specifically (not extraction generally).
- **T1.2:** TODO: remap the 141 classes and rerun CNN/SEC-BERT on the same grouped split. TODO: the exact statistical comparison (test, folds, assumptions, p-value, CI, effect size). TODO: acceptance-testing record (date, users, criteria, blank-description and dimensional-data changes). TODO: usability-testing record (dashboard task, confusion evidence, change made, retest). TODO: natural-vs-numeric key benchmark status.
- **T1.3:** TODO: agent-risk Welch test details (safe sample sizes, statistics, p-value, CI, effect size, confirm the "99% confidence" wording and name the artefact).
- **T1.4:** TODO: artefact showing the R-to-Python and Oracle-output boundary and an integration issue resolved. TODO: keep the simulation claim narrow (controlled computational experiments, not Monte Carlo). TODO: a specific commercial-benefit measure from the mixed-language design.
- **T1.5:** TODO: HMRC's classification of enterprise/private/public components plus a nameable architecture or security document. TODO: ODC configuration, volumes, runtimes and stability evidence. TODO: S3 proxy details (dataset, user group, approval flow) and evidence it worked. TODO: auto-scaling cost comparison record. TODO: verify the "days rather than nine months" timeline and name a witness.
- **T1.6:** TODO: the exact interfaces implemented (Oracle driver, `dbplyr`, Solr endpoint, S3 proxy, FSx, Parquet library). TODO: what "roughly 128 concurrent" means (workers, cores or documents) and the observed bottleneck. TODO: Oracle/Parquet before-and-after workflow and analyst reuse. TODO: LLM-to-Solr status (built, prototyped or proposed).
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
- **T5.2:** TODO: confirm the final model status (deployed, recommended for deployment, or validated prototype) and use one wording throughout. TODO: final production evidence if any (holdout performance, infrastructure, monitoring, acceptance, DPIA). TODO: consistency audit of scores, class counts, split, deployment status and impact claims across this document.

---

# Theme 1: Use and knowledge of computing and statistical foundations of AI and data science

**Theme KSBs:** K7, K16, K18, K19, K22, K25, S1, S16, S19, S20, S26.

**Distinction integration:** the pass answers also identify the norm challenged, the investigation, the proposed solution and its impact where that connection is natural. The standalone distinction answers remain the fullest versions.

## Describes how to use statistical, AI and machine learning methodologies such as data mining, supervised/unsupervised machine learning, natural language processing and machine vision to meet business objectives

**Relevant KSBs:** K19, K22, K25, S26.

### STARR: selecting methodologies for Hubble

**Situation:** Company accounts and tax computations are submitted as iXBRL, but some tax computations had only around 30% of their figures tagged, so conventional extraction omitted much of the available information. Hubble could extract the untagged descriptions, but the same accounting concept could be described in many different ways. That made population profiling through manually maintained regular expressions impractical.

**Task:** I needed to turn inconsistent, untagged descriptions into standard taxonomy concepts so that analysts could profile far more of the data and identify tax risk more efficiently. To do that, I had to decide which statistical, AI and machine learning methodologies actually suited the business objective, rather than assuming a particular model in advance.

**Action:** I worked through the candidate methodologies deliberately instead of selecting a fashionable model, and in doing so I challenged the assumption that population analysis had to rely on tagged items or matching rules.

I started with data mining. On the roughly 2.5 million cleaned rows I analysed frequency ranks, Pareto concentration, the overlap between descriptions and concepts, cosine similarity, class balance and residual errors. This established that sufficient labels existed to train a model. It also revealed a long-tailed and ambiguous problem: the top 75 raw concepts covered about 95% of items, while generic descriptions such as "Total" mapped to many different concepts. Just as importantly, it showed me where taxonomy quality and source-data quality would limit what any model could achieve.

Supervised learning became the core method because correctly tagged items already supplied target concepts. I framed the work as multi-class text classification and compared a wide range of model families: Naive Bayes, tree ensembles, SVC and LinearSVC, SGD-style models, CNN and other neural approaches, SEC-BERT, and MPNet and e5 embeddings.

The NLP pipeline I built ran as follows. Parse the iXBRL or XHTML, select the relevant descriptions and context, lower-case the text, normalise whitespace and punctuation, canonicalise names, companies, dates, postcodes and numbers into typed tokens, tokenise into word n-grams of one to three words, vectorise with TF-IDF or embeddings, classify, and retain the prediction, its score and its provenance. Every learned transformation was fitted on training data only and reused unchanged in production, which prevents leakage and pipeline divergence.

Unsupervised methods stayed exploratory. I compared vector spaces using silhouette scores calculated over the known concept labels, but that is a representation test rather than an operationalised clustering model. A genuine clustering result would still need a subject-matter expert to interpret whether the discovered groups meant anything useful to the business.

I also rejected some methods explicitly, with reasons. Reinforcement learning did not fit because this was a fixed, labelled classification problem with no environment or reward signal to learn from. Machine vision was unnecessary because the text and structure were already extractable from the iXBRL itself. OCR would only become relevant if scanned, image-only PDFs entered scope, and it would add an error-producing stage that would need its own accuracy and usability testing.

Finally, I assessed every candidate on macro-F1, accuracy, per-class results, stratified cross-validation, bootstrap intervals, speed, infrastructure requirements, explainability, provenance, maintainability and cost.

**Result:** TF-IDF with LinearSVC was the strongest operational recommendation, even though it did not have the highest point estimate on every metric. Its holdout macro-F1 was 0.800 against 0.808 for the CNN and 0.823 for SEC-BERT, and the confidence intervals overlapped. In exchange it offered far faster CPU-only training, inspectable coefficients and lower lifecycle risk. What made the method suitable was that it met the business objective of widening coverage, reducing manual grouping and supporting faster risk profiling, not that it was technically possible. The business-impact claim itself still requires a workplace artefact and is kept separate from the technical result.

**Reflection:** Method selection must begin with the business objective, the availability of labels, the type of data and the deployment constraints. Supervised NLP was appropriate here. Unsupervised methods stayed exploratory, and machine vision and frontier LLMs would have been disproportionate. The best technical score alone does not define the best business solution.

### Technical notes: clarification knowledge

- **Statistical methods:** descriptive statistics summarise data (mean, median, spread, distributions). Inferential statistics generalise from samples through hypothesis testing, confidence intervals and regression analysis.
- **Data mining:** discovering patterns and relationships in large datasets. Techniques include clustering, association rule mining and anomaly detection.
- **Supervised ML:** trains on labelled data to predict or classify. Techniques include linear regression, logistic regression, decision trees, random forests, support vector machines and neural networks.
- **Unsupervised ML:** finds hidden structure in unlabelled data. Techniques include K-means clustering, hierarchical clustering, PCA and anomaly detection.
- **Semi-supervised learning:** a small labelled set plus a large unlabelled set, using self-training, label propagation or pseudo-labelling.
- **Self-supervised learning:** the model generates its own targets from raw data, for example masked-word prediction. This underpins BERT and LLM pre-training.
- **Reinforcement learning:** an agent learns a policy from rewards through interaction with an environment (Q-learning, Deep Q-Networks). Used in robotics, game AI and control problems.
- **NLP:** enabling machines to process human language. Techniques include tokenisation, sentiment analysis, named entity recognition, topic modelling and text classification.
- **Machine vision:** interpreting visual information. Techniques include image classification, object detection and segmentation, usually CNN-based.
- **Business objectives these serve:** customer retention and experience, operational efficiency, sales and marketing effectiveness, fraud detection, risk management and quality control.

## Explains how to solve problems and evaluate software solutions via analysis of test data and results from research, feasibility, acceptance and usability testing in line with organisational requirements

**Relevant KSBs:** K7, S26.

### STARR: evaluating the Hubble classification solution

**Situation:** Analysts could not practically profile the extracted untagged descriptions. The wording was inconsistent, and there were hundreds of taxonomy classes with a long tail of rare examples.

**Task:** I was responsible for defining the problem, researching feasible solutions, testing them objectively, and confirming that the chosen output was usable and met HMRC requirements for security, explainability, infrastructure and analyst adoption.

**Action:** I first defined success more broadly than headline accuracy. The solution had to classify minority concepts as well as common ones, run at operational scale, remain explainable, use supportable technology, protect data and be genuinely usable by analysts.

For research and feasibility, I compared literature, package and model documentation, and empirical results across classical machine learning, neural networks, transformers and embedding approaches. Feasibility covered much more than whether the code ran. I assessed CPU and GPU availability, memory, throughput, cost, package and model provenance, security approval, maintainability, retraining time, and whether the production estate could support the complete pipeline.

For the test design, I created fixed seeded 80/10/10 train, test and holdout flags plus a 10,000-row holdout sample so that comparisons were like for like. I used five-fold `StratifiedKFold` with `GridSearchCV` and `HalvingRandomSearchCV` for the scikit-learn models, and Optuna with MLflow tracking for the neural and transformer runs. I analysed macro-F1, accuracy, precision and recall, confusion matrices, residual errors, bootstrap intervals, runtime and model size. I also understood the split's weakness and can defend it openly: it stratifies rows rather than filings, so related descriptions can cross partitions. For production evidence I would move to `StratifiedGroupKFold` or a grouped split by filing or company, add a chronological or unseen-taxonomy holdout, and fit all learned preprocessing (vocabulary, IDF weights) inside each fold.

For robustness analysis, I built crafted adversarial, contextual, long-context, OCR-noise, Unicode and typo cases. LinearSVC beat SEC-BERT on most categories, SEC-BERT won on Unicode substitution, and both were weak on abbreviations. These small synthetic groups diagnose failure modes, and I am careful not to present them as population performance estimates.

I then involved users directly. In acceptance testing, analysts checked whether the extracted dimensions and classifications supported the agreed business use. This exposed predictions being made from blank descriptions using only surrounding headings, so I changed the production logic to return no prediction where the description was missing. It also exposed missing dimensional content, so I generalised the extraction rather than coding a narrow subset. In usability testing, users found the top-five-matches display and the raw scores confusing, so I limited the display to more confident matches and added explanatory text about what the scores meant. One request remains open: analysts asked for numeric rather than natural database keys, and I am treating that as a performance question to benchmark on real Oracle and SAS workloads rather than a preference to accept without evidence.

**Result:** TF-IDF plus LinearSVC balanced model quality with speed, explainability, supportability and security. Its holdout macro-F1 was 0.800, SEC-BERT's higher point estimate was not separated from it by the confidence intervals, and the operational rubric favoured the simpler model. I note that the rubric's interpretability-key defect must be fixed before its numeric ranking is quoted. Acceptance testing changed extraction and prediction behaviour, and usability testing made the dashboard clearer, though both user outcomes need named internal artefacts. The defensible status from the notebooks is a validated comparison and proof of concept, not proven production deployment.

**Reflection:** I learned to research established tooling before writing bespoke evaluation code. Optuna automated comparison and visualisation that I had partly built myself. I also learned that training, test and production preprocessing need a single controlled implementation so that rules like blank-description handling cannot diverge. If this went to production I would monitor extraction failures, the missing-description rate, input and prediction distributions, per-class metrics and analyst overrides, with drift tests flagging when to diagnose, contain, relabel, and retrain or roll back. In future I would agree acceptance criteria earlier, automate pipeline-parity checks and keep a traceable decision log.

### Technical notes: clarification knowledge

- **Problem solving:** define the business problem clearly, research potential solutions, and assess feasibility across technical, operational and financial dimensions.
- **Testing phases:** unit testing checks individual components. Integration testing checks that modules work together. System testing checks the complete system against requirements. Acceptance testing (UAT) involves end users confirming the software meets their needs. Usability testing evaluates ease of use and user experience through interviews, task testing and surveys.
- **Analysis of test data:** collect data from all testing phases, use statistical methods to identify patterns, trends and anomalies, then document findings and report actionable insights to stakeholders.
- **Evaluation and decision-making:** compare solutions on performance, usability and feasibility, assess the risks of each, and decide on the evidence.
- **Train, validate, test (the gold standard):** training data fits the parameters, validation data tunes the hyperparameters, and a final untouched test or holdout set evaluates the finished model. Cross-validation folds the train and validate phases together: split into K folds, train on K minus 1, validate on the held-out fold, rotate and average. Repeatedly checking the holdout while tuning turns it into another validation set.
- **Overfitting:** high training performance with weak test performance, meaning the model learned noise. Mitigate with regularisation, simpler models, more data, dropout, early stopping and cross-validation. **Underfitting:** poor performance on both, mitigated with better features, more capacity or less regularisation. The bias-variance trade-off frames total error as bias squared plus variance plus irreducible noise.

## Describes the relationship between mathematical principles and core techniques in AI and data science within the organisational context

**Relevant KSBs:** K19, K22.

### STARR: the mathematics behind the Hubble model choice

**Situation:** Hubble needed to classify short, inconsistent accounting descriptions into a large and imbalanced set of standard concepts. Stakeholders needed reliable outputs and an explanation of how the method worked.

**Task:** I needed to select and explain a technique whose mathematical properties suited sparse text, unequal class frequencies and HMRC's need for fast, supportable and interpretable processing.

**Action:** The linear algebra came first. I represented each canonical description as a numeric vector using word TF-IDF over one-to-three-word n-grams. The raw n-gram counts are multiplied by a smoothed inverse document frequency, `IDF(t) = log((1+N)/(1+df(t))) + 1`, and each description vector is then L2-normalised. The effect is that common words are down-weighted while distinctive phrases such as "interest receivable" keep their signal.

The optimisation and geometry came next. LinearSVC finds one-versus-rest separating hyperplanes by convex optimisation. Each class gets a score `w_c·x + b_c` and the prediction is the class with the highest score. The objective is conceptually `||w||₁ + C Σ max(0, 1 − yᵢ(w·xᵢ + b))²`, with `C=2.8` and squared-hinge loss in the final configuration. I chose the L1 penalty deliberately because it drives many feature weights exactly to zero, which produces a sparse and inspectable coefficient set inside a very large feature space. Balanced class weights scaled each class's contribution inversely to its frequency, so errors on minority concepts genuinely mattered during training.

The probability and statistics shaped the evaluation. I challenged the stakeholder preference for accuracy as the headline measure, because with 75 concepts covering about 95% of items, accuracy mostly measures performance on common classes. I made macro-F1, the unweighted mean of per-class F1, the selection metric so that each eligible class contributed equally, and I retained accuracy, per-class precision and recall, support counts and confusion analysis alongside it. Stratified cross-validation estimated generalisation, and bootstrap intervals expressed the uncertainty in the holdout measures. That uncertainty is exactly why I would not claim SEC-BERT's 0.823 beat LinearSVC's 0.800: the intervals overlap.

I also quantified the embedding trade-off in the same mathematical terms. MPNet's advantage over TF-IDF was about 0.003 macro-F1 at roughly 67 times the fit time on one run, and a later run showed a difference of about 0.0001 that was not significant at 95% confidence. These are mathematically real numbers that translated directly into an organisational decision about GPUs, cost and explainability.

**Result:** The mathematics supported an organisationally appropriate choice. The model was fast on existing CPUs, explainable through its coefficients, and better aligned to minority concepts than a selection made on accuracy alone. Reframing the evaluation around macro-F1 made rare-class performance visible and gave stakeholders an impartial basis for comparison.

**Reflection:** Mathematical principles explain why a technique behaves as it does and whether its output is suitable for a decision. I would never present a p-value or a model metric as certainty. Sample size, assumptions, class representation, effect size and business consequences all matter alongside statistical significance.

### STARR: testing whether an agent presented higher risk

**Situation:** In a separate piece of agent-level risk work, a qualitative review suggested that one agent might present higher risk than the wider comparison group.

**Task:** I needed to test that suspicion quantitatively rather than allow an impression to drive the conclusion.

**Action:** I set the null hypothesis that the agent's risk equalled the comparison group's, and then I checked the assumptions before choosing a test. The data was two independent groups measured on a ratio scale, approximately normally distributed, with more than 30 observations and unknown population variances. An F-test indicated that the variances were unequal, so Student's pooled-variance t-test was inappropriate. I therefore selected Welch's t-test, `t = (m₁ − m₂)/√(s₁²/n₁ + s₂²/n₂)`, which uses adjusted degrees of freedom.

**Result:** At a 99% confidence level I rejected the null hypothesis and concluded that the agent presented higher risk than the comparison group. This gave the business quantitative evidence rather than a judgement based only on qualitative review. Rejecting at 99% means the observed difference would be unlikely if the means were truly equal. It does not mean there is a 99% probability that the conclusion is true, and I am careful to keep that distinction.

**Reflection:** The test must follow the data and its assumptions. I would present the confidence interval and the practical effect size as well as the p-value, because statistical significance alone does not show how important a difference is operationally.

### Technical notes: clarification knowledge

- **Linear algebra:** vectors and matrices represent data and model weights. Matrix decompositions such as SVD underpin PCA, recommendation systems and compression.
- **Calculus:** differentiation drives optimisation. Gradient descent minimises the loss function, and partial derivatives with the chain rule are the machinery of backpropagation.
- **Probability and statistics:** probability distributions model uncertainty. Bayesian inference updates beliefs from evidence. Hypothesis testing, confidence intervals and regression infer patterns from samples.
- **Optimisation:** convex optimisation, which has a single global minimum, underpins SVMs and linear models. Stochastic optimisation (SGD, Adam) handles large datasets efficiently.
- **How the maths maps to core techniques:** regression and classification rest on least squares, maximum likelihood and hinge loss. Neural networks are matrix multiplications with non-linear activations, trained by gradient descent. Clustering minimises distances, for example K-means minimises the sum of squared distances to centroids. Dimensionality reduction maximises retained variance via eigen-decomposition. Transformers compute attention as scaled dot-products, `softmax(QKᵀ/√d_k)V`.
- **Key formulas to recall:** macro-F1 = (1/K)ΣF1_k. Paired t-test `t = mean(d)/(sd(d)/√n)`. Welch's `t = (m₁−m₂)/√(s₁²/n₁+s₂²/n₂)` for unequal variances, checked first with an F-test. SVM objective `min ½‖w‖² + CΣmax(0, 1−yᵢ(w·xᵢ+b))`.
- **Organisational relevance:** mathematical properties translate into compute cost, minority-class coverage, interpretability, uncertainty quantification and the ability to defend a decision to stakeholders and auditors.

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

On simulation I keep the claim narrow and honest. Controlled computational experiments comparing model and hyperparameter scenarios on fixed splits are a defensible form of experimental analysis, but they are not a physical or Monte Carlo simulation, and I say so explicitly rather than implying a separate simulation project.

**Result:** The code demonstrates a complete experimental path from semi-structured public filings to repeatable model comparisons over millions of rows, and it demonstrates why a CPU-compatible scikit-learn model could beat GPU-heavy alternatives operationally. The commercial benefit was not "using three languages". It was combining their strengths to widen the usable data, reduce manual preparation and deliver through a workflow the organisation could actually support. The workplace claims about coverage and adoption still need internal measures.

**Reflection:** The correct language is contextual. Data format, library maturity, user capability, deployment platform and supportability all matter. Python support is growing in HMRC's AWS lakehouse, so I would reassess the language boundary over time, migrating only where the benefit outweighs the disruption.

### Technical notes: clarification knowledge

- **Programming languages:** Python is dominant for data analysis and ML because of its extensive libraries and easy syntax. R is strong for statistical analysis and visualisation and in analyst communities. SQL provides declarative querying of relational data. Java and Scala serve JVM data engineering, for example Spark.
- **ML libraries:** scikit-learn for classical ML, preprocessing and model selection. TensorFlow/Keras and PyTorch for deep learning. Hugging Face Transformers for pre-trained language models. XGBoost and LightGBM for gradient boosting. Libraries provide tested implementations, so effort goes into the problem rather than reimplementing algorithms.
- **Scientific analysis:** analysing large datasets to identify trends, make predictions and optimise processes. Results must be reproducible and evidence-led.
- **Simulation:** modelling real-world scenarios computationally so outcomes can be explored before committing. Examples include Monte Carlo methods, what-if scenario modelling and agent-based models.
- **Data engineering:** the collection, cleaning, transformation and preparation of data. Reliable pipelines and formats such as Parquet ensure analysis and models receive accurate, consistent input.
- **Meeting business needs:** the test of the technical work is business impact, such as efficiency gained, cost reduced, revenue or coverage increased, and decisions improved.

## Uses applied research and data modelling to design and refine the infrastructure and architectures to deliver secure, stable and scalable data products, including enterprise, private and public cloud resources and services

**Relevant KSBs:** K16, S1, S16, S19.

### STARR: refining Hubble's data-product architecture

**Situation:** Hubble processed high-volume, varied data including XML, iXBRL/XHTML and PDFs. The POSIT Data Analytics Platform suited development but not full-volume extraction, and the outputs had to remain secure, stable and accessible to analysts.

**Task:** I needed to define and refine an architecture that could burst for large extraction jobs, recover reliably, and provide queryable outputs without overloading the shared platform.

**Action:** The applied research and data modelling came first. I investigated taxonomy change, Oracle width limits, the shape of the workload and user needs. From that I proposed a long-form data model, storing document, context, concept, description and value as rows, instead of the wide annual-taxonomy tables that created structural change and width pressure every year. The long model costs more rows and occasional pivots for some outputs, but it is taxonomy-independent and removes the annual schema remapping. I consulted analysts before committing, to confirm they could genuinely work with long data.

For scalable compute, I worked with platform engineers to establish On-Demand Compute: temporary EC2 capacity, including large-core or GPU configurations when justified, spun up for a job and shut down afterwards. This isolated heavy workloads from the shared platform and controlled cost. Because document sizes varied widely, static partitioning left some workers idle while stragglers finished, so I used dynamic work allocation in which workers pulled the next document when they became free. I also understood where scaling stops helping: when input and output, database writes, serial setup or credential management becomes the bottleneck. That is Amdahl's law showing up in practice.

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

**Action:** I reviewed the charges at low and zero usage and compared the managed auto-scaling design with fixed-price and self-hosted EC2 alternatives. I weighed the total cost of ownership, covering concurrency, storage, idle time, support effort, recovery and expected growth, rather than comparing headline compute prices. The serverless billing was opaque and the baseline cost was disproportionate for a small, intermittent workload. On that evidence I challenged the assumption that cloud-native auto-scaling is automatically the most scalable choice.

**Result:** Fixed-price or self-hosted capacity was more predictable for this project and could still be resized when demand genuinely grew. The decision separated the technical ability to scale from the commercial question of whether the scaling model was appropriate.

**Reflection:** A scalable service must also be financially sustainable. I would use measured workload profiles and total-cost comparisons before selecting serverless or auto-scaling infrastructure, rather than treating either as a default.

### Technical notes: clarification knowledge

- **Applied research and data modelling:** using research methods and modelling techniques to understand a problem before designing the solution. This includes profiling sources, prototyping schemas and benchmarking alternatives.
- **Secure, stable and scalable:** secure means protected from unauthorised access through least privilege, controlled networks, encryption and audit. Stable means reliable, consistent performance with recovery from failure, supported by replication, tested code and durable storage. Scalable means handling growing data and users through horizontal scaling, parallelism and elastic compute.
- **Enterprise, private and public cloud:** enterprise refers to an organisation's own internal platforms and services. Private cloud is dedicated cloud resources for a single organisation. Public cloud is third-party provider services (AWS, Azure, GCP) consumed on demand. Using a public provider does not make the data public. It stays within organisational accounts, networks and governance.
- **Data architecture options:** relational databases give governed structured querying, joins and access control. Document and text search engines give distributed indexes with sharding and replication. A data lake gives cheap native-format storage but risks becoming a swamp without metadata and governance. A lakehouse adds transactions, schema enforcement and warehouse-style analytics on lake storage. A data fabric is a metadata-driven virtual layer, powerful but complex.
- **Parallel-processing concepts:** embarrassingly parallel workloads, static versus dynamic scheduling, stragglers, and Amdahl's law, under which serial fractions and shared bottlenecks cap the achievable speed-up.

## Explains how to design algorithms for accessing and analysing large amounts of data, including Application Programming Interfaces (API) to different databases and data sets

**Relevant KSBs:** K16, S19, S20.

### STARR: moving Hubble from files to scalable data access

**Situation:** The first Hubble workflow saved results to files, which users often exported as CSV or Excel. Runs were slow and usually limited to selected populations, and the repeated file movement made querying, joins and reuse difficult.

**Task:** I needed to redesign the access and processing so that Hubble could handle large document populations without saturating the main platform, exposing results through data stores analysts already used.

**Action:** I challenged the file-based workflow, investigated where time and manual effort were being lost, and designed around data locality, batching, query pushdown, parallelism, storage format and the cost of repeated serialisation.

For the parallel access design, I worked with DevOps to provision On-Demand Compute and used dynamic parallel scheduling. Documents went into a work queue and workers pulled the next one when free, so roughly 128 returns could be processed concurrently without the long tail caused by static batches of differently sized documents. The correct worker count sits just before contention at S3, the network, parsing memory or the Oracle writes removes the benefit of adding cores.

For the API layer, my starting point is that an API is a defined programmatic interface, not necessarily a public REST endpoint. The interfaces I actually used were R database drivers with DBI-style calls to Oracle, `dbplyr` as a higher-level query interface, Solr's query interface, the controlled S3 proxy, and the Parquet-on-FSx storage interfaces. I am careful not to describe an ordinary file copy as an API. The value of `dbplyr` is its lazy execution: it builds a query representation and only sends the translated SQL when results are collected, so filters, aggregation and joins execute close to the data. That cuts transfer and client memory, and the benefit depends on suitable indexes and predicates the optimiser can push down.

For the storage and format decisions, structured outputs went to Oracle rather than loose files. Where a SAS-writing package proved unreliable, I used a shared FSx route with Parquet, a compressed columnar format in which analytical queries read only the required columns and use metadata for predicate pruning, which is far more efficient than CSV. Batched database writes used sensible transaction boundaries so a failed batch could be retried without creating duplicates. Solr handled fast distributed text retrieval and the S3 proxy controlled object access.

Two design questions are held open deliberately. The analysts' request for numeric surrogate keys over natural keys is a benchmarking question about index size, query plans and end-to-end user effort on representative Oracle and SAS workloads, not a change to make on preference. And a possible future LLM-to-Solr natural-language query route remains clearly proposed rather than built. It would need a controlled schema, syntactic validation, field and operator allow-lists, authorisation in the user's own context, result-size limits, escaping against injection, audit logging and a preview step. The LLM must not become a route around existing access controls.

**Result:** Large extraction jobs ran on isolated temporary capacity without degrading the shared platform. The database and Parquet outputs made results easier to query, join and reuse, while the R analysts kept their familiar syntax and let the database do the heavy work.

**Reflection:** An efficient algorithm is one part of a wider data-access design. Parallelism only helps if the work is balanced, the credentials stay valid and the output does not create a new bottleneck. I would add service interfaces only where they genuinely improve reuse, rather than adding a REST API for its own sake.

### Technical notes: clarification knowledge

- **Designing algorithms for large data:** choose methods suited to processing at scale, such as sorting, filtering and aggregating. Efficiency and scalability matter more as volumes grow, and complexity is about the whole data path rather than one function.
- **Accessing data via APIs:** APIs let algorithms retrieve data from external sources. Examples include web services (REST and JSON), database drivers (ODBC, JDBC, DBI), cloud storage SDKs and query endpoints. They abstract the storage details behind a defined interface.
- **Analysing data:** statistical analysis, machine learning and data mining turn raw data into information that can inform business decisions.
- **Different databases and data sets:** SQL and relational databases offer structure, joins and transactions. NoSQL stores (document, key-value, wide-column) offer flexible schemas at scale. Search indexes, object stores and file formats (CSV versus columnar Parquet or ORC) each serve different access patterns. Integration means algorithms can work seamlessly across these sources.

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

The distinction criterion has four elements to hit explicitly. First, the norm challenged: the existing practice, process or belief that needed change. Second, the investigation: the research, data analysis or expert consultation showing the challenge was informed rather than assumed. Third, the proposed solution: what was innovative about it and how it differed from the norm. Fourth, the impact: the measurable benefit in efficiency, cost or performance, and how it was validated.

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

**Result:** DAP grew from one user to more than 150 and supported teams building their own analytical and machine learning tools. Users developed tools and integrations themselves rather than relying on me for every change, which extended organisational capability beyond my own delivery.

**Reflection:** My leadership developed from answering individual technical questions to shaping a service and the practices around it. I would strengthen this with formal skills reviews, succession planning and measured outcomes from mentoring.

### STARR: taking ownership of Hubble's technical direction

**Situation:** No off-the-shelf solution could categorise untagged iXBRL descriptions, and the initial simple NLP approaches performed poorly. Hubble spanned extraction, cleaning, modelling, validation and delivery across several technologies.

**Task:** I needed to take personal responsibility for the technical direction, overcome the infrastructure and modelling problems, and prove that the business problem was tractable.

**Action:** I investigated alternative architectures and model families, rebuilt the training datasets, fine-tuned BERT and tested classical and neural approaches. When GPU and throughput constraints emerged, I adapted the workflow to the infrastructure that was actually available and compared the candidates against operational criteria as well as model quality. I managed the lifecycle end to end, from extraction and cleaning through training, validation and reporting, and I introduced lightweight project controls as the contributor group grew.

**Result:** The work produced a validated classification proof of concept and established the business case for using machine learning in data profiling. The wider Hubble product extracted substantially more data than the previous approach and supported analysts identifying tax risk.

**Reflection:** Ownership meant being accountable for the complete outcome, including its limitations and deployment fit, rather than only producing a model. I would make the prototype-versus-production status and the final performance evidence more explicit in the project record.

### Technical notes: clarification knowledge

- **Developing working practices:** adopting new tools and technologies, staying current with industry trends, and continuous learning through courses, workshops and self-study.
- **Leadership techniques:** leading projects, mentoring, fostering collaboration, making strategic decisions, giving technical direction and tailoring communication to the audience.
- **Organisational impact categories:** enhanced efficiency through streamlined processes, innovation through new AI and data solutions, improved decision-making through data-driven insights, and team development through effective mentorship.

## Justifies their choice of techniques, explaining the risks and benefits and offers an alternative to technical and non-technical audiences

**Relevant KSBs:** K8, S6, S8, S28.

### STARR: communicating the LinearSVC decision

**Situation:** Stakeholders had different preferences. Some wanted accuracy as the headline measure, analysts suggested models such as Random Forest, and transformer models attracted interest because they were current and powerful.

**Task:** I needed to make an impartial recommendation, explain the benefits and risks, provide credible alternatives, and communicate the same decision appropriately to technical and non-technical audiences.

**Action:** I consulted the stakeholders first and converted their concerns into a comparison covering macro-F1 and per-class reliability, accuracy, speed, compute cost, explainability, security and provenance, maintainability and deployment fit. The comparison narrowed to LinearSVC, CNN and SEC-BERT on one common holdout, plus rubric-scored operational criteria. SEC-BERT had the highest macro-F1 point estimate at 0.823 against 0.808 and 0.800, but the confidence intervals overlapped. LinearSVC trained in minutes rather than the better part of an hour, ran inference orders of magnitude faster, and was about 8 MB rather than about 1.8 GB, with stronger deployment, maintenance and dependency-risk ratings.

I presented the risks and benefits in both directions. LinearSVC's risks are its linear decision boundary and its lack of contextual understanding. SEC-BERT's risks are its GPU dependency, slower throughput, weaker explainability, provenance and assurance concerns, and lifecycle cost.

For technical audiences, I explained sparse TF-IDF vectors, L1 regularisation, the imbalance handling, cross-validation, bootstrap uncertainty and the CPU and GPU constraints. For non-technical audiences, I described macro-F1 as reliability across rare as well as common concepts, CPU execution as lower cost and easier deployment, and the coefficients as understandable evidence about which phrases influenced a result.

The alternative I offered was SEC-BERT or another assured domain model, in the event that a remapped, grouped evaluation established a worthwhile gain and future infrastructure, assurance and maintenance could support it. I would not present the current numeric decision score unqualified, because the matrix has a known field-name defect and untested weights. Explaining that defect openly is itself part of impartial, evidence-led decision making.

**Result:** TF-IDF with LinearSVC was the operational recommendation, offering competitive quality, fast CPU-compatible processing, clearer explanations and lower lifecycle risk. A named meeting, decision paper or approval is still needed to prove how technical and non-technical stakeholders received it.

**Reflection:** Communicating alternatives strengthens a recommendation because it shows the choice was deliberate. In future I would agree metric definitions and risk tolerances even earlier and keep a short decision record containing both the technical comparison and a plain-English version.

### Technical notes: clarification knowledge

- **Justifying a technique:** show its suitability against the problem in terms of efficiency, accuracy, scalability, relevance and cost.
- **Risks and benefits:** risks include limitations, potential errors, resource requirements and maintenance burden. Benefits include performance, cost savings and new capability. Present both sides rather than a sales pitch.
- **Offering alternatives:** show the choice was deliberate by presenting credible alternatives and the conditions under which they would win.
- **Audience tailoring:** technical audiences want algorithms, data structures, metrics and infrastructure. Non-technical audiences want the practical implications, meaning what problem it solves, what it costs, what could go wrong and what decision is needed.

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

- **Sharing internally:** training sessions, workshops, demonstrations, wikis, communities of practice and mentoring.
- **Disseminating externally:** conference presentations, publications, professional networks and forums, and open demonstrations on public data.
- **Improving industry practice:** influencing standards and best practice and contributing to guidelines. Be honest about the difference between sharing, which has been done, and demonstrated industry change, which needs evidence.

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

Four elements to hit explicitly. First, critical analysis of the wider social context, covering ethics, privacy, economic impact and public perception, supported by evidence rather than assertion. Second, current issues and trends, covering technology advances, regulatory change and emerging debates. Third, applying the findings with justification, meaning the action taken links back to the analysis. Fourth, sharing with the wider community through articles, presentations, forums or demonstrations.

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

**Result:** TF-IDF with LinearSVC became the evidence-led recommendation rather than the fashionable choice, with competitive macro-F1, much faster training, coefficient-level explanations and lower operational risk. The workplace decision and approval still need to be named.

**Reflection:** Impartiality is easier to demonstrate when the criteria are agreed before the results are known. I would make the decision record routine so stakeholders can challenge it if the evidence or the constraints change.

### Technical notes: clarification knowledge

- **Independent and impartial:** decisions based on objective analysis and evidence rather than personal bias or external pressure.
- **Respecting others' views:** active listening, valuing diverse perspectives, and incorporating relevant feedback into the decision process while still deciding on the evidence.
- **Complex, unpredictable and changing circumstances:** unexpected challenges, new information and shifting priorities. Adapt the decision process, not the standard of evidence.
- **Business benefit:** efficiency, conflict resolution, innovation and strategic goals. Be specific about the outcome achieved.

## Explains how they have worked with software engineers to ensure suitable testing and documentation processes are implemented in line with organisational requirements

**Relevant KSBs:** S14, B1.

### STARR: engineering controls for Hubble

**Situation:** Hubble became a complex tool with varied real-world documents, several contributors and many users. A small change to parsing or preprocessing could silently affect extraction, model inputs or the outputs analysts relied on.

**Task:** I needed to establish, with engineers and contributors, proportionate testing, change control and documentation that supported safe delivery without imposing a heavyweight process on a small team.

**Action:** In the workplace repository I established the principle that changes require tests. If a function had no test, one was written before modifying it, and the suite had to pass before merging to main. Unit tests covered individual functions. Integration-style cases covered complex real documents, because input variation cannot be covered by isolated tests alone. User acceptance came through the analyst testing described under the evaluation criterion.

For traceability and planning, I used GitLab issues, templates, epics and milestones, together with a lightweight Kanban board.

The documentation worked at three levels. A full README covered the multi-system setup, serving as process documentation for new users. Detailed Markdown design notes covered the architecture, the workflows and the reasons behind the key decisions, serving as technical documentation. Analyst guidance explained how to interpret the outputs, serving as user documentation.

I collaborated with platform and DevOps engineers on ODC, data paths and environment constraints, and turned operational findings into tests or documentation wherever possible. In a public-sector context, undocumented behaviour or an unrepeatable result can undermine trust even when a metric looks strong, so reproducibility and traceability were treated as requirements rather than extras. `Code/` contains research notebooks only, which means the internal test suite, the CI gates, the README and the reviews all need workplace artefacts.

**Result:** New users could set up the project from the README, contributors could change tested functions with confidence, and the issues and milestones provided an audit trail from requirement to implementation. This should be evidenced with a test report or CI result, the README, a representative merge request and an engineer witness.

**Reflection:** Up-front tests and documentation reduce future change cost and dependency on individual knowledge, and they make AI work more open to review. The largest remaining risk is the diversity of source documents, so I would expand a versioned representative corpus, automate the integration tests in the merge pipeline, and link requirements, tests and release notes explicitly.

### Technical notes: clarification knowledge

- **Collaboration with engineers:** regular communication, joint planning and collaborative problem-solving on requirements and constraints.
- **Testing levels:** unit testing for individual components, integration testing for modules working together, system testing for the complete system against requirements, and user acceptance testing where end users validate functionality and usability.
- **Documentation types:** technical documentation covers architecture, code and APIs. User documentation covers guides and manuals. Process documentation covers development, testing and maintenance procedures.
- **Organisational alignment:** testing and documentation must comply with organisational standards, industry best practice, regulatory requirements and quality-assurance guidelines.

---

# Theme 3: Awareness of the current and future impact of AI and data science for industry and society

**Theme KSBs:** K11, K17, K21.

## Describes how the potential roles and impact of AI and data science could affect own organisation, industry and society

**Relevant KSBs:** K11.

### STARR: Hubble's organisational and societal impact

**Situation:** Incomplete tagging made large parts of company accounts and tax computations difficult to analyse systematically. Manual interpretation did not scale.

**Task:** I needed to combine data engineering, data science and AI so analysts could exploit more of the information, while considering what wider impact this kind of automation could have.

**Action:** I used data engineering to extract, clean, canonicalise and structure the iXBRL, data science to analyse quality, balance and performance, and supervised NLP to categorise the descriptions. Results were delivered to controlled stores so the model supported analyst judgement rather than replacing it. I also considered where similar methods apply beyond HMRC, such as fraud detection, medical imaging and demand forecasting, and the societal risks: over-trusted outputs, opaque decisions, privacy loss, under-representation of rare classes, deskilling and resistance from staff whose work changes.

**Result:** The code demonstrates the potential to reduce repetitive grouping by mapping varied descriptions to consistent concepts. The workplace account is that Hubble expanded analytical coverage and supported tax-risk profiling, which needs an internal measure or witness. At the industry level the notebooks are a reproducible example rather than proof that practice changed. At the societal level, better evidence may support fairer and more efficient revenue work, but Hubble does not make tax decisions and does not directly prove an increase in public funding.

**Reflection:** A narrow technical pipeline can have material social consequences. Positive impact depends on human oversight, transparent limitations, secure processing and monitoring. The defensible role of AI here is augmenting analysts, not replacing them.

### Technical notes: clarification knowledge

- **Organisational impact:** operational efficiency through automation and optimised workflows, innovation through new products and services, and data-driven insight through trend discovery, prediction and strategic decisions.
- **Industry impact:** changed market dynamics and business models, disruption of traditional practice, new regulation and standards, and cross-sector partnerships and integration.
- **Societal impact:** ethical considerations around privacy, bias and fairness, economic change through job creation and displacement and the changed nature of work, and social change in healthcare, education and public services.
- **AI and jobs (balanced answer):** AI more often changes jobs than eliminates them, because most roles mix routine tasks that can be automated, judgement tasks that are harder, and accountability tasks that policy often requires a person to hold. On scale, the WEF projects large churn by 2030 (around 170 million roles created, 92 million displaced), the IMF estimates about 40% of global employment is exposed (around 60% in advanced economies), and the ILO finds clerical work particularly exposed. The useful framing is displacement versus augmentation, and the organisational response is work redesign and reskilling rather than automation for its own sake.

## Explains how they have assessed and addressed the potential business impact of ethical issues relating to AI and data science, the way procedures and methods are selected, and the unintended consequences to the business when they are applied

**Relevant KSBs:** K11, K17. Cross-reference S12 and B3 in Theme 4.

### STARR: ethical impact assessment for Hubble

**Situation:** Hubble processed accounts and tax computations containing names, references and detailed financial information. A classifier used in a tax-risk context could create privacy, bias, transparency and accountability risks if its categories were treated as fact or used outside their intended purpose.

**Task:** I needed to assess those ethical issues before and during development, choose proportionate procedures and methods, and reduce the likelihood that unintended model behaviour would cause legal, operational or reputational harm.

**Action:** On the assessment side, I completed a DPIA before work began and reviewed it as the design evolved. I also assessed representation and imbalance quantitatively, using frequency distributions, macro-F1, per-class measures, confusion matrices and residual examples rather than relying on overall accuracy.

On the addressing side, I canonicalised names, companies, dates, postcodes and numbers in the pipeline so that high-cardinality identifiers were not the trained feature. I am precise about what this achieves: it is feature minimisation, not anonymisation, because the source description is retained, and access, retention and purpose controls remain necessary. Processing stayed inside controlled environments. I tested balanced class weights, biased sampling and oversampling. The final LinearSVC used balanced weights, and several of the neural and transformer weighting approaches actually made performance worse. Demographic fairness, meaning parity and equalised odds, remains proposed rather than completed, and I say so plainly.

Ethics also shaped the method selection itself. I chose an explainable TF-IDF and LinearSVC pipeline partly so that coefficients, LIME and SHAP could expose feature influence, and model provenance was part of the selection decision.

Unintended consequences were found and fixed through user testing. Acceptance testing found blank descriptions being classified from their surrounding context, so I stopped predictions where the description was absent. Usability feedback showed the top-five display created false confidence, so I simplified it. Both user changes need internal evidence.

**Result:** The code supports the narrower conclusions: identity-like tokens were removed from the modelling feature, minority-class and robustness failures were made visible, and a simpler model enabled direct inspection. The workplace controls kept the model as decision support rather than an automated determinant. The DPIA, the human-oversight instruction and the user evidence should be named to substantiate that result.

**Reflection:** Ethical assessment must cover the whole sociotechnical process: the data, labels, metrics, model, interface, users and downstream decisions. A technically explainable model can still be misused, so future improvements include monitoring, enforced workflow controls, periodic DPIA review and clearer warnings for low-reliability classes.

### Technical notes: clarification knowledge

- **Assessing ethical issues:** identify concerns such as privacy, algorithmic bias, transparency and accountability through ethical audits, stakeholder consultation and impact assessments such as a DPIA.
- **Addressing them:** data-protection measures, fairness checks, transparency and explainability, and documented frameworks such as GDPR and ethical AI principles.
- **Method selection:** weigh the ethical implications of alternative approaches alongside performance, with explicit decision criteria.
- **Unintended consequences:** anticipate them through risk assessment, detect them through monitoring and user testing, and correct and retest when they are found.
- **Business impact of getting it right:** customer and public trust, avoided legal issues and protected reputation.
- **Ethical concern areas for AI generally:** transparency, accountability, bias, accuracy and privacy. Reference frameworks include the UK responsible-AI principles (safety, security and robustness, appropriate transparency and explainability, fairness, accountability and governance, contestability and redress), the OECD AI guidelines and the EU AI Act.

## Describes how they have applied solutions, demonstrated awareness and explained the changes and trends that have led to enhancement of working practices within their organisation and other members of the team

**Relevant KSBs:** K17, K21.

### STARR: testing modern model families before selecting a simpler Hubble model

**Situation:** Transformers, domain-specific BERT models, embeddings and neural networks were prominent developments in text classification, and stakeholders could reasonably expect Hubble to consider them.

**Task:** I needed to test whether those developments improved the classification problem enough to justify their infrastructure, assurance and maintenance costs.

**Action:** I followed the research literature, technical documentation and practical communities, and then implemented real comparisons across classical machine learning, MPNet and e5 embeddings, CNN and neural architectures, and SEC-BERT, all on fixed data flags. I assessed macro-F1 and per-class performance alongside runtime, CPU and GPU needs, provenance, explainability and deployment fit. The evidence was concrete: MPNet's advantage over TF-IDF was small to negligible across the runs, SEC-BERT's higher point estimate came with overlapping intervals, and the robustness categories exposed different failure modes in each model family. I explained the evidence through project documents, demonstrations and stakeholder discussions.

**Result:** The testing showed that the simpler TF-IDF and LinearSVC pipeline was the stronger operational recommendation. The code proves that the recommendation was researched. An internal approval or user measure is still needed to show the deployed benefit.

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

- **Applied solutions:** concrete implementations addressing organisational challenges, meaning new technologies, methodologies or strategies actually put into practice.
- **Demonstrated awareness:** staying informed through courses, conferences, publications, professional networks, research tracking, vendor and ecosystem monitoring, and hands-on proof-of-concepts.
- **Explaining changes and trends:** communicating the significance and potential impact of developments to the team and organisation, not just knowing about them.
- **Enhancement of working practices:** tangible improvements in efficiency, collaboration, quality and reproducibility, with measurable examples.

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

- **Impact on operations:** disrupted activities, interrupted service delivery, forced shutdown of processing, outputs quarantined, decisions reviewed and systems rolled back.
- **Legal consequences:** penalties, fines, sanctions, enforcement notices and litigation.
- **GDPR penalty figures (a past-learner question):** under UK GDPR and the DPA 2018, the higher maximum is £17.5 million or 4% of annual worldwide turnover, whichever is higher. The standard maximum is £8.7 million or 2%. Under EU GDPR the figures are €20 million or 4%, and €10 million or 2%. The UK enforcement body is the ICO.
- **Financial risks:** beyond fines, there is remediation, legal fees, incident response, new systems and processes, duplicated analysis and delayed outcomes.
- **Reputational damage:** eroded customer and public trust and reduced investor and stakeholder confidence. For a public body, the loss of legitimacy can outweigh any fine.
- **Operational risks:** data breaches, security vulnerabilities and inefficiencies from uncontrolled processes.
- **Regulatory scrutiny:** increased oversight across otherwise unrelated programmes after a failure.

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

- **UK GDPR principles (seven):** lawfulness, fairness and transparency. Purpose limitation. Data minimisation. Accuracy. Storage limitation. Integrity and confidentiality. Accountability.
- **Lawful bases (six):** consent, contract, legal obligation, vital interests, public task and legitimate interests.
- **Special-category data:** racial or ethnic origin, political opinions, religious or philosophical beliefs, trade-union membership, genetic data, biometric data, health, sex life and sexual orientation. **Equality Act protected characteristics:** age, disability, gender reassignment, marriage and civil partnership, pregnancy and maternity, race, religion or belief, sex and sexual orientation.
- **DPIA:** required where processing is likely to be high risk. It records the nature, scope, context and purpose, necessity and proportionality, risks to people, controls, residual risk, consultation and approval. It starts before processing and is revisited on material change.
- **Article 22:** restricts solely automated decisions with legal or similarly significant effects unless a valid condition and safeguards apply. Meaningful human review requires understanding, evidence and the authority to override.
- **UK versus EU GDPR:** the UK incorporated EU GDPR into law as UK GDPR and the DPA 2018 on leaving the EU. They are near-identical, with differences in scope (national security and immigration), age of consent (13 in the UK versus a default of 16 in the EU) and enforcement (the ICO versus the EDPB and member-state authorities). International transfers rely on adequacy regulations or appropriate safeguards such as standard contractual clauses and binding corporate rules.
- **Wider frameworks:** the UK responsible-AI principles (safety, security and robustness, appropriate transparency and explainability, fairness, accountability and governance, contestability and redress), the OECD AI guidelines, and the EU AI Act with its risk-based tiers (banned, high-risk regulated, transparency duties, minimal).
- **Legal and commercial checks:** dependency and model licences, intellectual property, supplier contracts, data-sharing conditions, processing roles, retention duties, support status and the right to audit.
- **Accessibility and WCAG:** WCAG 2.2 is the current W3C standard, with conformance levels A, AA and AAA. UK public-sector websites and apps are legally required to meet Level AA under the Public Sector Bodies Accessibility Regulations. Core practice covers keyboard operation, visible focus, semantic structure, text alternatives, labels and error messages, contrast, zoom and reflow, captions, and avoiding colour as the only signal. Testing combines automated checks with keyboard, screen-reader and representative-user testing. WCAG 2.2 adds criteria for cognitive and learning disabilities, low vision, mobile use and input methods.
- **Diversity of user needs:** users differ in cultural, social, economic and ability backgrounds. This covers interface diversity, meaning assistive technology, devices, language and technical confidence, and it also covers data diversity. Unrepresentative training sets produce biased models, as when facial recognition systems misclassify dark-skinned women. Diverse data improves generalisation and equity. Gather user feedback and incorporate diverse perspectives into the design.

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

- **Own currency:** continuous learning through courses, certifications and workshops, reading and research across journals, papers and articles, and networking through professional groups, conferences and online communities.
- **Team development:** training programmes, mentorship, knowledge-sharing sessions and encouraging a learning culture.
- **Professional growth:** set development goals with plans, hold regular performance and skills reviews, and provide coaching and recognition.
- **Personal growth:** work-life balance, soft-skills development in communication, leadership and teamwork, and supporting broader interests.
- Be ready to name specific courses, books and articles read, with a brief reaction to each, and any professional-community membership.

## Explains how they selected and applied the most effective/appropriate AI and data science techniques to solve a complex business problem in line with organisational and regulatory requirements

**Relevant KSBs:** B5, B8. Cross-reference S26.

### STARR: evidence-led selection for a regulated Hubble deployment recommendation

**Situation:** Hubble needed to map inconsistent, often untagged account descriptions to standard taxonomy concepts. The data was large, imbalanced and domain-specific, with 826 engineered labels of which the 141 with sufficient examples were modelled. HMRC required secure, explainable and supportable processing.

**Task:** I needed to choose and apply a technique that solved the business problem at scale while meeting organisational policy, data-protection, security, infrastructure, cost and maintenance requirements.

**Action:** I defined the problem and the success criteria before recommending a model, and I framed the problem deliberately. The required output was a taxonomy classification. Labelled data already existed in the form of tagged items, so supervised classification fitted. The data was unstructured text, which pointed to NLP pipelines.

In applying the techniques, the pipeline extracted and cleaned millions of rows, canonicalised the high-cardinality identifiers and created fixed seeded splits. I established baselines first, then evaluated the classical models, MPNet and e5 embeddings, SEC-BERT and the CNN and neural alternatives. The evaluation used macro-F1, per-class measures, confusion and residual analysis, stratified cross-validation and bootstrap intervals, because accuracy alone hid minority-class performance. Alongside those I compared training and inference time, model size, CPU and GPU needs, explainability, provenance, maintainability and deployment complexity. On the common holdout, LinearSVC recorded 0.800 macro-F1 against 0.808 for the CNN and 0.823 for SEC-BERT, with overlapping intervals. The label-space remap for the neural and transformer heads remains outstanding before the cross-family difference is treated as final.

The organisational and regulatory constraints shaped the choice directly rather than sitting alongside it. The DPIA and the minimisation requirements shaped the features. The explainability expectations favoured inspectable coefficients over a fine-tuned transformer. The infrastructure reality of a CPU estate with scarce GPUs, together with provenance and assurance concerns, weighed against SEC-BERT. Delivery had to fit the supported R workflow with controlled ODC and Oracle delivery. Internal artefacts are needed for the DPIA, the integration and the user changes.

**Result:** The evidence supports an operational recommendation for TF-IDF plus LinearSVC. It is CPU-compatible, directly inspectable, and free of SEC-BERT's lifecycle burden in exchange for an uncertain point-estimate gain. Until the workplace status is confirmed, I call this a validated comparison and a deployment recommendation, and I would describe any internal production outcome separately, with evidence.

**Reflection:** The most effective technique is the one that meets the complete business and regulatory need, not the model with the highest laboratory score. My CPD let me test the modern methods credibly, while judgement favoured the simpler recommendation. Before formal deployment evidence I would fix the decision-matrix key, group the splits by filing, add time and taxonomy validation, define acceptance thresholds, verify test and production parity, and implement monitored human oversight.

### Technical notes: clarification knowledge

- **Framing a problem to select a technique:** ask, in order, what output is wanted, what input data that needs and whether it exists, whether ML is needed at all or rules and statistics suffice, whether the problem is supervised (prediction or classification with labels) or unsupervised (pattern discovery, anomaly detection), whether the prediction is a continuous value (regression) or a category (classification), and whether the data is structured or unstructured. Answering these in order narrows the algorithm choice.
- **Then apply the constraints:** platform restrictions, GDPR lawful basis and PII handling, explainability requirements (which can rule out deep learning), cost and infrastructure. Only after that, experiment across the remaining candidates with appropriate metrics.
- **Application steps:** data preparation (collect, clean, preprocess), model development (build and train with appropriate tools), and validation and testing on unseen data against agreed performance standards.
- **Compliance:** data privacy and security measures, handling of bias, fairness and transparency, and documentation and reporting for accountability.

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
