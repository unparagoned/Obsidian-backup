# Project Report - Review and To Do

## Project Overview

**Task:** iXBRL concept classification from UK Companies House accounts (298,461 filings, 18.5GB). Multi-class text classification: given a financial line-item description, predict the XBRL taxonomy concept (826 classes).

---

## Notebook-by-Notebook Summary

**00 — Data Extraction**
BeautifulSoup-based extraction of `ix:nonfraction`/`ix:nonnumeric` tags. Handles multiple encodings. Saves description + XBRL concept label to parquet. Simple and functional but knowingly incomplete — the notebook notes that more extensive code for additional features (table name, heading, non-table-node documents) exists but isn't included. For EPA purposes, this is a credible limitation to discuss explicitly rather than gloss over.

**01 — EDA & Preprocessing**
The strongest notebook. Key work:
- Distribution analysis: 956 labels, lognormal distribution, top 75 concepts cover 95% of items — this justifies macro-F1 as your primary metric.
- Ambiguity analysis: many-to-many mapping between descriptions and concepts, cosine similarity of concept groups.
- Canonicalization: lowercasing, 1982-03-31 date substitution (tax significance), name/company/number/date/postcode replacement with canonical tokens (`hubble_name`, `hubble_date`, etc.), label engineering for canonical labels.
- Result: reduced from 266,178 unique descriptions to 10,591; 956 → 826 labels; 2.86M → 2.47M rows.
- Silhouette score comparison across TFIDF, TF, word+char n-grams, SBERT, E5 (0.419–0.477).
- Stratified 80/10/10 split, sqrt-weighted training subsets.

**03 — Scikit-learn Models**
Very methodical:
- Population size validation: Pearson correlation 1% vs 100% = 0.971; 10% vs 100% = 0.998 — justifies using 10% for most experiments.
- Paired t-test for statistical significance of model differences.
- HalvingRandomSearchCV (10,000 candidates) → refined GridSearchCV.
- Winner: **LinearSVC** with TF-IDF (1-2 ngrams), C=2, balanced class weight, l1 penalty — F1-macro **0.787**.
- MLflow tracking throughout.

**04 — Neural Networks (CNN/TensorFlow)**
- Custom CNN: TextVectorization → Embedding (dim=518) → CNN (elu) → Dense (88 units, gelu) → output.
- Optuna (200+ trials) for architecture search; CNN beat RNN/LSTM/MLP.
- Best config: batch=16, dropout=0.254, learning_rate=1e-4.
- sqrt-weighted data with unweighted model was optimal — F1-macro **~0.776** (10% subset).
- Has robustness test suite (`IXBRL_TEXT_CLASSIFICATION_TEST_CASES`) — good for EPA.
- Known issue: Optuna memory leak causing >120GB RAM use, documented but not fully resolved.

**05 — Transformers (HuggingFace sec-bert)**
- Models compared: `sec-bert-base`, `roberta-base`, `all-mpnet-base-v2`, `all-MiniLM-L6-v2`.
- sec-bert-base won (pre-trained on financial/SEC text) — F1-macro **0.782** on 100% population, batch=16 (14.3h training).
- 10% sqrt-weighted (15 epochs, batch=16) reached **0.7785** — 14× faster, near-equivalent.
- Weighted loss (`WeightedTrainer`) performed worse.
- Issue: full test set requires 150GB RAM, used `test_5_pct` as proxy throughout.

**06 — Compare Models (Final)**
Loads LinearSVC, CNN, and SEC-BERT results from MLflow. Has a subjective rubric for interpretability/explainability, deployment simplicity, and maintenance burden for LinearSVC. Only 7 cells total — this is the sparsest notebook and appears incomplete as a comparison artifact.

---

## Issues Found

### Technical / Code Issues

| Notebook | Issue | Impact |
|---|---|---|
| **00** | `analyze_table` starts table iteration at index 1, silently skipping table 0 — rationale unexplained | May miss data from single-table documents |
| **00** | `map()` is lazy; on file read failure, the entire `pd.concat` will fail rather than skip bad files | Silent data loss risk |
| **01** | `AdvancesCreditsDirectors` — directors' names not fully caught by canonicalization (noted as TODO, cell 89) | PII leakage into training data; unreachable labels |
| **01** | `MAX_WORDS = 15` used as a constant but its origin/justification isn't stated | Unclear if this is a data observation or an assumption |
| **03** | `tf.random.set_seed(SEED)` in cell 3 but TensorFlow isn't imported in the visible import block | Potential runtime error if run fresh |
| **03** | Training data is `v13`, test data is `v16` — version difference unexplained | Reproducibility concern; could introduce subtle differences |
| **04** | Optuna memory leak (>120GB) documented but not resolved; `load_if_exists=True` allows resumption but not clean reruns | Reproducibility / infrastructure concern |
| **04** | `vectorize` layer adapted once — unclear whether it's adapted on the full dataset or just the training subset | Could cause OOV tokens at test time |
| **05** | Full test set requires 150GB RAM; `test_5_pct` used as a proxy without validating it's consistently representative | Potential evaluation bias |
| **06** | `subjective_inputs` defined for LinearSVC but CNN and SEC-BERT entries appear incomplete | Comparison rubric is one-sided |

---

## Gaps Against EPA Criteria

**Bias and fairness analysis** (K23, S3, S17 — required for Pass; key for Distinction)
There's no analysis of whether the model performs worse on specific subgroups — e.g., micro vs. macro accounts, specific industries, or rare concepts. The class imbalance is addressed through weighting and macro-F1, but no demographic/fairness parity testing is done. For the report, add at minimum a per-class F1 breakdown with commentary on which concepts are hardest to classify and why.

**Data governance narrative** (S17)
Companies House data is public, but company officer names are PII under GDPR. The `AdvancesCreditsDirectors` TODO means names are leaking into training data. The report needs a section explicitly addressing this — even if the conclusion is "data is public and no individual is identified in model outputs."

**Statistical significance on final comparisons** (K23)
Notebook 03 uses paired t-tests throughout, which is excellent. But the final comparison in notebook 06 doesn't appear to include confidence intervals or significance tests across the three final models. The report should state whether the difference between LinearSVC (0.787) and SEC-BERT (0.782) on the 10% subset is statistically significant.

**Notebook 06 is incomplete**
The final comparison notebook has only 7 cells. It loads results and defines the rubric, but the actual comparison table, final recommendation, and business case aren't visible. This is the notebook that maps most directly to "demonstrates how they contributed to identifying the optimal solution" — it needs to show the full decision matrix, not just the inputs.

**CRISP-DM or methodology framing**
The work follows CRISP-DM closely but this is never named explicitly. The report should explicitly reference this, especially under the "AI project and development management" (K6, S24) criteria.

**Scalability and deployment** (K13, K14 — Distinction level)
LinearSVC is the obvious production candidate — small model, fast inference, interpretable. But there's no notebook discussing deployment architecture (how would this run against incoming Companies House filings?), latency benchmarks, or retraining triggers. Cell 114-115 in notebook 04 logs inference time to MLflow, which is a start. The report needs to articulate the operational model explicitly.

---

## Strongest Assets for the Report

1. **Population size validation** (notebook 03, cells 26–36) — the correlation analysis proving 10% subsets are representative is publication-quality methodology.
2. **Canonicalization design** (notebook 01, section 3) — replacing PII-adjacent fields with typed canonical tokens is both a data quality measure and an implicit feature engineering insight.
3. **Lognormal distribution analysis** — justifies macro-F1 over accuracy concisely and with statistical backing.
4. **MLflow experiment tracking** — every model run is logged; this is directly citable as evidence of systematic methodology.
5. **Robustness test cases** (notebook 04, cell 122–126 and notebook 05, cell 90–95) — the `IXBRL_TEXT_CLASSIFICATION_TEST_CASES` suite directly addresses "robustness of decisions at all stages."

---

## To Do (Priority Order)

- [ ] **Complete notebook 06** — add confusion matrices, side-by-side metrics with confidence intervals, and a decision matrix for all three models (LinearSVC, CNN, SEC-BERT).
- [ ] **Resolve the `AdvancesCreditsDirectors` TODO** — or document it explicitly as a known limitation with a mitigation plan.
- [ ] **Add per-class error analysis** — identify the top 10–20 misclassified classes and explain why (ambiguous descriptions, overlapping concepts, etc.).
- [ ] **Add a data governance section** to notebook 01 — acknowledge PII handling even briefly (public data, no individual identified in outputs).
- [ ] **Explain the v13 vs v16 dataset version difference** — add a markdown cell in notebook 03 or 04.
- [ ] **Add statistical significance testing to notebook 06** — confirm whether differences between final models are significant.
- [ ] **Add CRISP-DM framing** to notebook 01 or a new intro notebook — reference it explicitly for K6/S24 evidence.
- [ ] **Add deployment architecture discussion** — even a brief section on how LinearSVC would run operationally, retraining triggers, monitoring approach.
- [ ] **Explain `MAX_WORDS = 15`** — add a comment or markdown cell showing where this value comes from.
- [ ] **Explain table index 0 skip** in notebook 00 — add a comment explaining why iteration starts at index 1.
