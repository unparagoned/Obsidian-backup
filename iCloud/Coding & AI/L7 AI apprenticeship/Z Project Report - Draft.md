# Categorising Data in Financial Documents
*Draft — for review and refinement*

---

## 1. Introduction and Background

HMRC processes approximately 12 million company tax returns annually, a significant proportion of which are submitted as iXBRL (inline eXtensible Business Reporting Language) documents. iXBRL is a semi-structured format: it is fundamentally an (x)HTML document in which financial items are optionally tagged with concepts drawn from a fixed taxonomy, providing machine-readable metadata alongside the human-readable presentation. The iXBRL taxonomy concept associated with a tagged item — for example, `CalledUpShareCapital` or `ProfitLoss` — provides a consistent, structured label that enables automated extraction and analysis of financial data at scale.

Where tagging is comprehensive, existing HMRC workflows reliably extract, structure, and analyse tagged figures for profiling, policy analysis, and risk identification. However, tagging quality varies significantly across document types. For some critical document categories — including certain tax computation formats — an average of only 30% of figures are tagged, meaning the majority of the data in these important documents has historically been unavailable for automated analysis. Analysts working with these documents have been limited to the tagged minority of figures, or have had to engage in labour-intensive manual review of untagged descriptions, which is time-consuming, inconsistent across analysts, and requires specialist domain knowledge that is not uniformly distributed across teams.

This report describes the development of Hubble, an internal tool I built at HMRC to address this capability gap. Hubble extracts both tagged and untagged items from iXBRL documents and uses supervised machine learning to classify untagged items into the appropriate taxonomy concept. The central technical challenge is that while tagged items have precise, structured labels assigned at submission by the preparer, untagged items carry only a free-text description. There is no fixed taxonomy or required format for these descriptions; items of the same conceptual class can therefore have many different textual representations. Financial documents also use domain-specific terminology — terms such as "deferred consideration", "amounts owed to group undertakings", or "called up share capital not paid" — that data analysts may not be familiar with, making it difficult to work directly with raw descriptions at the scale required for population analysis.

I led the technical implementation across all stages of the project, from initial data understanding through to production deployment. The project followed the CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology, with a Kanban-based agile approach managing delivery through iterative increments using GitLab. The project addressed a genuine gap in HMRC's analytical capability and has since been adopted by multiple analyst teams across the organisation, including teams engaged in population profiling, policy analysis, and tax risk identification.

---

## 2. Outline of the Issue and Business Problem

The business problem is clearly defined: a significant portion of the financial data submitted to HMRC in iXBRL format cannot be reliably used for analysis because it lacks machine-readable categorisation. Analysts who wish to work with this data must either manually review free-text descriptions — which is slow, inconsistent, and requires specialist domain knowledge — or restrict their analysis to the tagged subset, which is incomplete and potentially unrepresentative of the full population.

This gap has real analytical and compliance consequences. Population-level profiling of financial data informs government policy decisions and the allocation of compliance resources. An analysis restricted to the 30% of figures that are tagged will systematically under-represent or miss entire categories of financial data — particularly data in sections of company accounts that preparers have not prioritised for iXBRL tagging. Risk indicators embedded in untagged items may go undetected, representing a direct cost in terms of compliance yield and policy accuracy.

The opportunity identified was that the existing tagged figures within the same documents provide high-quality, authoritative supervision signal — iXBRL concepts assigned by the preparer at submission — that could be used as training labels for a supervised machine learning classifier. By learning the relationship between free-text descriptions and their corresponding taxonomy concepts from tagged examples, a model could then predict concepts for untagged items, extending coverage from 30% to close to 100% of figures in affected document types.

To validate the recommendation to use machine learning rather than a manual or rule-based approach, I worked with subject matter experts (SMEs) and analysts during initial stakeholder engagement workshops. An examination of key taxonomy classes revealed that the variety of descriptions used for a single concept was extremely high: some classes had over 23,000 unique descriptions in the dataset, including domain-specific technical terms and abbreviations that even experienced analysts struggled to consistently identify. Manual classification at this scale was not feasible, and a rule-based system would require ongoing expert maintenance and would still fail to handle the long tail of novel descriptions. This analysis confirmed that machine learning was the appropriate approach and formed the basis of the recommendation to stakeholders.

---

## 3. Methods Used and Justification

**CRISP-DM methodology**

The project was structured using the CRISP-DM methodology, which provides an established, documented framework for iterative data mining projects. CRISP-DM was appropriate because it explicitly accommodates the cyclical nature of applied ML development: discoveries at the modelling stage frequently prompt revisions to data preparation, and evaluation findings may require revisiting the business understanding. Each phase produced documented artefacts — data quality reports, EDA notebooks, experiment logs, and model evaluation summaries — providing an evidence base for all decisions made.

Across multiple CRISP-DM iterations, the project evolved significantly. The first iteration used raw descriptions as the sole feature and achieved macro-F1 scores below 50%, revealing that noise from dates, names, and numeric values was substantially degrading model performance. The second iteration introduced canonicalization — replacing PII, dates, and numeric values with typed placeholder tokens — which raised macro-F1 above 70%. A third iteration added heading and table name as supplementary features, further improving performance for classes where the description alone was ambiguous. This structured iteration, grounded in error analysis at each cycle, is the mechanism through which CRISP-DM produces robust, progressively better solutions.

**Project management**

A Kanban approach was selected over more heavyweight frameworks such as SCRUM, which would have introduced unnecessary overhead for a small technical team. GitLab was used to manage epics, issues, tasks, and milestones, providing visibility of progress and a documented audit trail of technical decisions and rationale. Regular stakeholder engagement sessions — workshops with analysts, SMEs, and DevOps — ensured that the solution remained aligned with operational requirements and that feedback was incorporated systematically across iterations.

**Programming languages and tools**

R was used for the primary extraction and pre-processing pipeline, as it is the organisational default at HMRC, is widely used by analysts, and has strong HTML parsing libraries. This made outputs maintainable and accessible to the broader team, reducing the risk of single-person dependency. Python was used for all machine learning components, where the library ecosystem — scikit-learn, TensorFlow/Keras, HuggingFace Transformers, Optuna, and MLflow — is considerably more mature than equivalent R packages for text classification and hyperparameter optimisation. The two components were integrated via the reticulate package. Jupyter notebooks were used throughout the experimental work to provide a reproducible, narrative record of the methodology. MLflow tracked all experiments, logging hyperparameters, metrics, and artefacts for every run.

**Scientific methodology**

All experiments were designed with explicit hypotheses and a controlled baseline. A DummyClassifier was used at every experimental phase to establish the minimum performance floor and confirm that models were providing genuine predictive signal. Macro-F1 was chosen as the primary evaluation metric, providing equal weight to all 826 classes and directly addressing the requirement that the model performs well across the full taxonomy, not just the most common concepts. Stratified k-fold cross-validation (k=5) was used throughout, ensuring all classes were represented in each fold and reducing evaluation variance. Statistical significance of differences between model configurations was assessed using paired t-tests, identifying configurations that were not statistically distinguishable from the best-performing run at the 95% confidence level.

---

## 4. Scope of the Project and Key Performance Indicators

The scope covered the complete pipeline from data extraction through to production deployment for one key document type, with the architecture designed for extensibility to additional document types. Success criteria were defined in collaboration with analysts and managers at the outset and agreed as measurable targets:

- **Macro-F1 ≥ 0.70**: the primary ML performance indicator, reflecting equal-weight performance across all taxonomy concepts including minority classes. Chosen over accuracy to directly address the class imbalance problem.
- **Inference latency < 10μs per record**: enabling daily batch processing of millions of records on existing CPU-based infrastructure, avoiding the need for specialist GPU compute.
- **Coverage ≥ 95%**: the proportion of extracted figures that can be assigned a taxonomy concept.
- **Accuracy ≥ 95%** on majority classes, monitored as a secondary metric to ensure practical usability for common concepts.
- **Short-term milestone**: sub-population outputs to file within an initial phase to demonstrate value and gather analyst feedback early in the project.
- **Long-term milestone**: full daily population ingestion to Oracle database within the agreed project timeline.

These KPIs balanced ML performance with operational feasibility, and were explicitly reviewed against infrastructure and cost constraints to ensure they were achievable within HMRC's existing environment.

---

## 5. Data Selection, Collection, and Pre-Processing

**Data collection**

Training data was derived directly from iXBRL documents processed through HMRC's existing systems. Tagged figures in these documents provide authoritative supervision: the iXBRL concept assigned at submission by the preparer constitutes the ground truth label, without requiring additional human annotation. This is a significant methodological advantage — the labels reflect expert human judgement applied at the point of document creation, with no additional annotation cost or inter-annotator variability.

Different iXBRL document types use different taxonomies — for example, the FRC taxonomy for company accounts and the HMRC CT600 taxonomy for tax computations — which use different concept names for semantically similar items. Training a single model across all taxonomies would introduce label noise, since the same description could correctly map to different concept names depending on document context. Following SME consultation, the decision was made to train a separate model per document type using only the main taxonomy for that document type, applying those labels universally across all documents of that type. This provided consistent, standardised class names that improved analytical usability at a modest cost to theoretical precision for documents using secondary taxonomies.

**Exploratory data analysis**

EDA on the extracted dataset revealed several structural characteristics with direct implications for modelling:

- The label distribution was approximately lognormal — confirmed by statistical comparison against power-law and exponential distributions. The top 75 concepts accounted for 95% of all items, with a long tail extending beyond 900 concepts. This power-law-like structure directly motivated the use of macro-F1 as the primary metric: a naive model predicting only the most common classes would achieve high accuracy but would be useless for the analytical purposes that motivated the project.
- Many descriptions mapped to multiple XBRL concepts, creating genuine ambiguity. Cosine similarity analysis of concept groups showed that some co-occurring concepts were semantically related (e.g., variants of "amounts owed to group undertakings"), while others were genuinely different concepts sharing a generic description such as "total" or "additions". This ambiguity represents an irreducible performance ceiling for models using description as the sole feature.
- Descriptions spanned multiple types: nominal financial terms, personal names, company names, numeric values, dates, and free-text extracts. This heterogeneity required differentiated treatment during pre-processing rather than a uniform approach.

**Pre-processing and canonicalization**

Pre-processing was designed to reduce noise, standardise the feature representation, and ensure compliance with the Data Protection Act 2018 and UK GDPR, in accordance with the Data Protection Impact Assessment (DPIA) completed prior to work involving personally identifiable information. The following steps were applied:

1. **Text cleaning**: all descriptions were lowercased and punctuation normalised. EDA revealed highly inconsistent casing across documents.
2. **Date handling**: the date 31 March 1982 — which has specific capital gains tax significance — was replaced with a dedicated semantic token. All other dates were replaced with a generic `hubble_date` token, as specific dates carry no predictive signal for concept classification but would otherwise create spurious vocabulary entries.
3. **PII removal and tokenisation**: personal names, company names, addresses, and postcodes were identified using regular expressions and, where applicable, by detecting taxonomy concepts known to contain PII (such as `NameEntityOfficer` and `AdvancesCreditsDirectors`). Identified PII was replaced with typed canonical tokens (`hubble_name`, `hubble_company`). This simultaneously addressed privacy compliance and reduced noise from high-cardinality free-text fields that would otherwise inflate vocabulary size and reduce model generalisation.
4. **Numeric canonicalization**: numeric and monetary values were replaced with a `hubble_number` token.
5. **Label engineering**: records whose descriptions reduced entirely to a name, date, or number after canonicalization were assigned a canonical label (e.g., `HubbleName`), since the description alone cannot distinguish between the original taxonomy concepts for these items, but knowing it was a name would be useful.

The cumulative effect of canonicalization was substantial: unique descriptions reduced from 266,178 to 10,591 (a 96% reduction), the number of active labels reduced from 956 to 826, and 86% of original rows were retained. The dramatic reduction in vocabulary size significantly improved signal-to-noise ratio and model generalisation.

**Stratified splitting and training subsets**

Data was split 80/10/10 into training, test, and holdout sets using stratified sampling to ensure proportional representation of all 826 classes in every split. Stratified training subsets were created at 1%, 10%, 50%, and 100% of the training data to enable efficient experimentation. Population correlation analysis validated this approach: Pearson r between macro-F1 scores on the 1% and 100% subsets was 0.971; between 10% and 100% it was 0.998, confirming that the 10% subset could be used reliably for hyperparameter search without full-dataset training runs. Sqrt-weighted training populations were also created, applying a square root transformation to class frequencies to amplify minority class representation while preserving some majority class signal.

---

## 6. Survey of Potential Alternatives

The classification task is multi-class text classification across 826 nominal categories with strong class imbalance. Four broad approaches were systematically evaluated:

**Baseline (DummyClassifier)**: stratified and most-frequent strategies established minimum performance bounds and confirmed that all substantive models were providing genuine predictive signal above chance.

**TF-IDF with scikit-learn classifiers**: TF-IDF n-gram vectorisation captures the occurrence and distinctiveness of word sequences. For short, domain-specific text, n-gram features are effective because key vocabulary is highly discriminative — terms such as "deferred consideration" or "share premium account" provide strong signal for specific taxonomy concepts. Multiple classifier families were evaluated: LinearSVC, SVC, PassiveAggressiveClassifier, LogisticRegression, RandomForestClassifier, and GradientBoostingClassifier. A two-stage search was used — HalvingRandomSearchCV over 10,000 candidates on the 10% training subset for initial screening, followed by GridSearchCV over refined parameter ranges for the top candidates. This efficiently explored a large search space while concentrating computational budget on the most promising regions.

**Convolutional neural network (CNN)**: a convolutional neural network with a trainable embedding layer was evaluated as an approach that captures richer local sequential structure than bag-of-words methods. Optuna's TPE sampler with HyperbandPruner was used for architecture and hyperparameter search over 200+ trials. The best architecture used a trainable embedding layer (dimension 518), convolutional filters with ELU activation, and a dense layer with GELU activation. The CNN was trained with sqrt-weighted data to address class imbalance.

**Transformer-based models**: four pre-trained transformer models were evaluated: `nlpaueb/sec-bert-base` (pre-trained on financial SEC filings, providing domain-relevant pre-training), `roberta-base`, `all-mpnet-base-v2`, and `all-MiniLM-L6-v2`. These models capture contextual semantic meaning and have strong performance on many NLP benchmarks. Optuna's MedianPruner allowed under-performing trials to be terminated early. Different training population sizes (1%, 10%, 50%, 100%) and batch sizes were systematically explored.

**Embedding comparison**: independently of the classifier, silhouette scores were computed for five vectorisation approaches on a 50,000-record sample: TF-IDF word n-grams, TF word n-grams, combined word and character n-grams, SBERT mpnet, and E5-large. Scores ranged from 0.419 to 0.477. A grid-searched combination of word and character n-grams achieved 0.477, marginally better than the mpnet sentence transformer (0.467), indicating that the domain-specific vocabulary was well-captured by n-gram methods — consistent with TF-IDF being a strong approach for this problem type.

Model selection criteria were defined prior to evaluation and reflected HMRC's organisational priorities: macro-F1 performance; inference latency; training time; interpretability and explainability; computational cost; infrastructure requirements; and long-term maintainability. These criteria were used to construct a multi-factor comparison for the final model selection decision.

---

## 7. Implementation and Performance Metrics

**Population size validation**

A key methodological contribution was validating smaller training subsets as reliable proxies for full-dataset model ranking. Pearson correlation between macro-F1 scores on 1% and 100% training subsets was 0.971; between 10% and 100% it was 0.998. This allowed the 10% subset to be used reliably for the majority of hyperparameter search, reducing experimental compute time by a factor of ten while maintaining confident model ranking.

**LinearSVC hyperparameter optimisation**

HalvingRandomSearchCV over 10,000 candidates identified LinearSVC as consistently among the top-ranked models. Refined GridSearchCV identified the optimal configuration: C=2.0, balanced class weighting, l1 penalty, squared hinge loss, max_iter=5,000. The l1 penalty applies implicit feature selection during training, producing a sparser weight matrix and improving inference efficiency. Paired t-tests confirmed the top configuration was statistically distinguishable from lower-ranked alternatives at the 95% confidence level.

**Neural network optimisation**

Optuna explored architecture choices and training hyperparameters over 200+ trials. Architecture type was the most important factor for F1 performance — CNN outperformed MLP and RNN architectures. Batch size was the most important factor for training time. The optimal CNN configuration used gelu activation in the dense layer, elu in the convolutional layer, embedding dimension 518, and batch size 16 with dropout 0.254. For class imbalance, sqrt-weighted training data with an unweighted model (macro-F1 0.776) outperformed both fully balanced weighting (0.721) and the unweighted baseline (0.757).

**Transformer evaluation**

Among transformer models, sec-bert-base outperformed alternatives on the 1% training subset (F1 0.754), consistent with its domain-relevant financial pre-training. Scaling to the full training population with batch size 16 improved this to 0.782, requiring 14.3 hours of GPU training. The 10% sqrt-weighted training configuration achieved 0.779 — approximately 14 times faster — demonstrating that sqrt-weighted sampling provides an effective efficiency gain for transformer models as well as for simpler classifiers.

**Final model comparison**

| Model | Training Data | Macro-F1 | Accuracy | Training Time | Inference |
|---|---|---|---|---|---|
| LinearSVC | 100% | 0.787 | 0.971 | ~2 hours (CPU) | 2.7μs/record |
| CNN | 10% sqrt-weighted | 0.776 | 0.973 | ~44 minutes (CPU) | ~15μs/record |
| SEC-BERT | 100%, batch=16 | 0.782 | 0.977 | 14.3 hours (GPU) | >1ms/record (CPU) |

The multi-factor evaluation, incorporating interpretability, deployment complexity, maintenance burden, and operational cost alongside the ML metrics, favoured LinearSVC. Crucially, LinearSVC's macro-F1 of 0.787 is not lower than SEC-BERT's 0.782 — it is marginally better — while requiring no GPU infrastructure and operating 370 times faster at inference. At HMRC scale, processing millions of records per daily batch, the operational cost difference is very large. LinearSVC's feature coefficients also provide direct interpretability: the n-gram weights for each class correspond intuitively to the vocabulary used in practice, enabling explainability and facilitating error analysis.

---

## 8. Results

The deployed model — LinearSVC with TF-IDF 1-2 word n-grams, l2 normalisation, C=2.0, balanced class weighting, and l1 penalty — achieved a macro-F1 of 0.787 and an accuracy of 97.1% on the holdout test set. This exceeds the target macro-F1 of ≥0.70 by 8.7 percentage points. Inference latency of 2.7μs per record on a standard CPU enables daily processing of millions of records within the required operational window on existing infrastructure.

The iterative CRISP-DM process produced measurable, documented improvement at each cycle:
- **Iteration 1** (raw descriptions, no pre-processing): macro-F1 <0.50.
- **Iteration 2** (canonicalization — typed tokens for dates, names, numbers): macro-F1 >0.70.
- **Iteration 3** (supplementary features — heading and table name added): further improvement for ambiguous classes.
- **Final** (full hyperparameter optimisation, balanced class weighting): macro-F1 0.787.

Error analysis using confusion matrices revealed systematic patterns in misclassifications: the majority of errors occurred between semantically similar concepts (e.g., different variants of "amounts owed to group undertakings"), confirming that the residual errors reflect genuine ambiguity in the descriptions rather than model deficiencies. This finding was communicated to analysts with examples, enabling them to understand where to apply additional scrutiny and when to inspect the raw description rather than relying solely on the ML classification.

The TF-IDF feature weights directly revealed which vocabulary drove predictions for each class, providing the interpretability required for HMRC's AI governance requirements. The model was integrated into the R production pipeline via reticulate, with outputs ingested to an Oracle database. On-demand compute on an EC2 instance was set up to handle the daily batch volume, firing up the required resources only for the duration of the job and shutting down on completion, keeping infrastructure costs controlled.

---

## 9. Discussion and Conclusions

The results demonstrate that supervised machine learning can reliably extend taxonomy classification in iXBRL financial documents from 30% to close to 100% coverage, meeting all defined KPIs. The macro-F1 of 0.787 reflects strong performance across a highly imbalanced, 826-class problem with genuine ambiguity in a significant proportion of cases.

The decision to select LinearSVC over transformer-based models illustrates the importance of evaluating solutions against the full set of operational requirements rather than optimising on a single metric. SEC-BERT achieves a macro-F1 of 0.782 — 0.5 percentage points below LinearSVC — while requiring GPU infrastructure, 14 hours of training, and significantly more complex deployment and maintenance. The marginal performance difference does not justify the operational cost at HMRC's scale and within HMRC's infrastructure constraints. This decision also reflects the broader principle that explainability is a first-order requirement, not a secondary consideration: LinearSVC's interpretable feature weights enabled error analysis, stakeholder communication, and the analyst-facing dashboard that supports informed use of the ML classifications.

The CRISP-DM methodology provided a clear structure that produced documented evidence at each stage and enabled disciplined iteration. The Kanban project management approach, supported by GitLab tooling, provided transparency, accountability, and a knowledge-transfer-ready audit trail. Regular stakeholder engagement at each stage — analysts providing feedback on outputs, SMEs clarifying taxonomy edge cases, DevOps collaborating on infrastructure design — was essential for keeping the solution aligned with operational requirements.

Communication required deliberate adaptation across stakeholder groups. With analysts, explanations centred on concrete examples and confusion matrices showing where the model worked well and where it made mistakes, rather than abstract performance statistics. This approach — presenting model behaviour in terms that analysts could act on, rather than metrics they could not evaluate — improved uptake and helped analysts develop accurate intuitions about the model's limitations. With DevOps, discussions focused on benchmarks, memory usage, and scalability. With managers, communications were structured around business outcomes, resource requirements, and funding needs, with formal memos used to request additional infrastructure investment. This communication approach, adapted to each audience, was effective in securing the stakeholder buy-in needed to complete the project.

**Recommendations**

1. Extend the methodology to additional iXBRL document types using the established pipeline and validated methodology.
2. Implement ongoing performance monitoring against the fixed holdout set, with retraining triggered when macro-F1 falls below the operational threshold.
3. Explore targeted active learning for the lowest-performing classes, using analyst feedback on uncertain predictions to improve training data quality.
4. Maintain and enforce the human-in-the-loop requirement: the ML classification should not be used for automated decisions, and per-class performance documentation should accompany all analytical output that relies on it.

---

## 10. Summary of Findings

A supervised machine learning classifier was developed and deployed to categorise untagged items in iXBRL financial documents at HMRC. The selected model — LinearSVC with TF-IDF 1-2 n-gram vectorisation — achieved macro-F1 0.787 and accuracy 97.1%, exceeding the target KPI of ≥0.70 macro-F1. Inference latency of 2.7μs per record enables large-scale batch processing on existing CPU infrastructure. The model was selected over CNN and BERT-based alternatives on the basis of its combined performance, interpretability, computational efficiency, and operational fit with HMRC's infrastructure and governance requirements. The project followed CRISP-DM with Kanban project management and has been successfully deployed, with the tool adopted by multiple analyst teams for population profiling, policy analysis, and risk identification work that was previously unavailable.

---

## 11. Implications

**Analytical capability**: the tool extends analyst access from approximately 30% to close to 100% of figures in affected document types, enabling more complete and representative population-level analysis. Teams that previously relied on the tagged minority of data can now work with the full population, improving the statistical basis for policy recommendations and the completeness of risk identification.

**Organisational pattern**: the project establishes a validated methodology for applying supervised ML to semi-structured tax data. The key methodological contributions — using existing iXBRL labels as training supervision, iterative CRISP-DM development with documented error analysis, population-scaled evaluation using sub-population correlation validation, and sqrt-weighted sampling for class imbalance — are directly reusable for other document types and similar classification problems across HMRC's data estate.

**Deployment architecture**: the on-demand compute (ODC) approach, spinning up an EC2 instance for daily batch processing and shutting down on completion, provides a cost-effective and scalable deployment model for ML pipelines requiring periodic high-volume processing without dedicated infrastructure. Developed in collaboration with DevOps, this architecture is a reusable template for future ML deployments.

**Governance**: the project demonstrates that operationally useful ML can be deployed within HMRC's data governance framework. The completed DPIA, PII canonicalization approach, human-in-the-loop requirement, per-class performance documentation, and analyst-facing performance dashboard collectively provide a governance model that is proportionate to the risk profile and HMRC's AI safeguard requirements.

---

## 12. Caveats and Limitations

**Minority class performance**: despite balanced class weighting, taxonomy concepts with very few training examples achieve lower individual F1 scores. The aggregate macro-F1 of 0.787 reflects average performance across all 826 classes; concepts with fewer than approximately 350 training examples perform below this average. A per-class performance dashboard was created to enable analysts to assess model reliability for specific concepts before using ML classifications in analytical outputs.

**Irreducible ambiguity**: for some concepts, the description alone is genuinely insufficient to determine the correct classification — generic terms such as "total" or "additions" can correspond to multiple different concepts depending on their document context. The addition of table name and heading as supplementary features partially mitigated this issue, but a residual portion of items remains intrinsically ambiguous from the extracted features. Further improvement would require richer contextual features, such as surrounding rows or document section context, which are more complex to extract reliably.

**Taxonomy evolution**: the model is trained on the main taxonomy for each document type. Taxonomy updates introducing new concepts, and documents using secondary taxonomies with different concept names for the same items, will not be correctly classified. Periodic retraining is required to maintain performance as taxonomies evolve and as document preparation practices change over time.

**Extraction coverage**: approximately 15% of documents use non-standard HTML structures that do not use standard table nodes, requiring bespoke positional extraction logic. This logic was implemented in R and processes these documents separately. Full coverage of all document structures remains an ongoing development area.

**PII handling edge cases**: the canonicalization approach handles the majority of PII using regular expressions and taxonomy-label-based detection. Edge cases remain — for example, directors' names without common salutation prefixes that fall outside the regular expression patterns. These cases were identified during exploratory data analysis and are documented in the DPIA with a committed mitigation plan for subsequent iterations.

**Production data versus demonstration notebooks**: the Jupyter notebooks presented as supplementary evidence for this report use publicly available Companies House data to demonstrate the methodology without disclosing sensitive HMRC data. The methodology, preprocessing approach, model configurations, and performance results are consistent between the public demonstration and the production system.

---

## Appendices

*The following appendices support this report and are not included in the 5,000-word count.*

**Appendix A — Code and documentation**
Jupyter notebooks 00–06 covering data extraction, exploratory data analysis and preprocessing, scikit-learn model experiments, neural network experiments, transformer experiments, and final model comparison. All experiments tracked in MLflow.

**Appendix B — Statistical rigour**
Confidence intervals and paired t-test results from GridSearchCV and HalvingRandomSearchCV experiments. Population correlation analysis (Pearson r for 1%, 10%, 100% subset scores). Silhouette score comparison across vectorisation approaches.

**Appendix C — Figures and visualisations**
Pareto chart of XBRL concept frequency distribution; frequency-rank plots; word count distributions; confusion matrices for final LinearSVC model; Optuna hyperparameter importance and optimisation history plots; model comparison table.

**Appendix D — KSB mapping**
Mapping of this report to the KSBs for Assessment Method 1: K1, K3, K5, K6, K13, K14, K23, K26, K28; S2, S3, S4, S5, S7, S9, S10, S11, S15, S17, S18, S22, S24, S25, S27; B2, B6.

**Appendix E — Employer verification**
Verification by HMRC that this project report is a true reflection of Jesse Karadia's involvement and is their own work.
