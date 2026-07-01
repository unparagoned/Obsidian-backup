# Z Technical Test - notes

These notes are for revising the 60 minute technical test. They are deliberately generic, not tied to the mock scenario. The mock test is still useful because it shows the question style, but the real test can use a different business context.

Use these notes as a menu of approaches. In the exam, pick the approach that best fits the scenario, explain why it fits, and briefly reject one or two weaker alternatives.

## Source notes used

- [[Z Overall - st0763_artificial-intelligence-ai-data-specialist_l7_ap-for-publication_qm]]
- [[Z Technical test]]
- [[Z Technical Test - AM3 BCS_L7_Exam_Prep_Guide]]
- [[Z Technical Test - BCS L7 AI Data Specialist IfATE V1.0 AM3 Technical Test Sample Paper V2.0]]
- [[Z Technical Test - sample detailed notes]]
- [[Z Technical Test - sample draft answers]]
- [[Z Technical Test - sample links]]
- [[AI and Data Science Professional Practice Term 2 Theme 4 Ethics and AI =]]
- [[AI and Data Science Professional Practice Term 2 Theme 5 Legal aspects =]]
- [[AI and Data Science Professional Practice Term 2 Theme 6 Error, bias and uncertainty =]]
- [[AI and Data Science Professional Practice Term 4 =]]
- [[Data Science Principles Topic 4 - Statistical testing]]
- [[Data Science Principles Topic 6 - Storing your data]]
- [[Data Science Principles Topic 8 - Machine learning]]
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]]
- [[Disruptive Leadership for Sustainable Strategy - Topic 7 - Data strategy]]
- [[Disruptive Leadership for Sustainable Strategy - Topic 8 - Error, bias, uncertainty]]
- [[Programming for AI Topic 4]]
- [[Programming for AI Topic 6 Time Series Analysis]]
- [[Programming for AI Topic 7 Time series modelling with machine learning]]

## Assessment facts

- 60 minute controlled technical test.
- Four questions.
- Weighting is 25% of the EPA.
- Questions are scenario-based and test whether you can apply technical judgement, not just define terms.
- Question 1 usually covers data sources, data extraction, linking, error, bias and uncertainty.
- Question 2 usually covers storage, analysis, visualisation, algorithms and technical justification.
- Question 3 usually covers legal, ethical, social and professional impacts.
- Question 4 usually covers how to design, develop and deploy an AI or data science system, including methodologies, architecture and resources.

## Exam answer pattern

Use DELTA:

1. **Define** the issue or choice in the scenario.
2. **Explain** why it matters technically, legally, ethically, operationally or commercially.
3. **Link** it to the scenario and the evidence available.
4. **Trade off** strengths, weaknesses and alternatives.
5. **Action** with concrete controls, methods, metrics or next steps.

Good technical test answers usually do all of the following:

- name the technique or method;
- explain why it is appropriate;
- identify a limitation or risk;
- state a mitigation;
- mention measurement, monitoring or validation.

Bad answers usually only list tools without showing why they fit the context.

## Quick Question Map

| Question | Core topic | What the marker is likely looking for |
|---|---|---|
| Q1 | Data extraction, linkage, error, bias and uncertainty | Appropriate data sources, integration logic, data quality controls, uncertainty handling, awareness of bias |
| Q2 | Storage, processing, visualisation and algorithms | Architecture choices, algorithm selection, metrics, scalability, interpretability, operational constraints |
| Q3 | Legal, ethical, social and professional issues | UK GDPR/Data Protection Act, Equality Act, DPIA, fairness, transparency, accountability, public trust |
| Q4 | Methodology, development, deployment and resources | CRISP-DM/TDSP/KDD/SEMMA/Agile/MLOps comparison, architecture, team roles, monitoring, deployment strategy |

# Question 1 - Data Extraction, Linkage, Error, Bias and Uncertainty

## What Q1 is really asking

Q1 is normally about how to get usable data from multiple sources and turn it into something reliable enough for analysis or modelling.

You need to cover:

- what data is needed;
- where it might come from;
- how it will be extracted;
- how sources will be linked;
- what could go wrong with quality, bias and uncertainty;
- how those problems will be measured or mitigated.

## Generic data source categories

| Source type | Examples | Strengths | Weaknesses | Use when |
|---|---|---|---|---|
| Transactional systems | Sales, orders, claims, bookings, payments, CRM | High business relevance, structured, timestamped, often complete for recorded events | Only shows recorded activity, can miss context, may be siloed | Need objective records of what happened |
| Operational systems | ERP, HR, inventory, manufacturing, service desk, logistics | Good for process performance and resource use | Data definitions can vary by department | Need to improve internal operations |
| Sensor or IoT data | Temperature, movement, machine telemetry, wearables, store sensors | High frequency, useful for real-time decisions | Noisy, missing packets, calibration drift, high volume | Need physical-world measurement or automation |
| Application logs | Clickstream, API logs, app events, web analytics | Good for behavioural journeys and funnel analysis | Can overrepresent digitally active users, tracking gaps | Need to understand digital behaviour |
| Text and documents | Emails, forms, PDFs, support tickets, reports, social media | Rich context and sentiment | Unstructured, harder to validate, privacy risks | Need qualitative insight or NLP |
| Images/video/audio | CCTV, inspection photos, calls, medical scans, product images | Captures information not available in tables | High storage, privacy, annotation and explainability issues | Need computer vision or speech analysis |
| Public/open data | Owns, weather, transport, economic, demographic, geographic | Adds external context, often low cost | Granularity and update frequency may not match | Need contextual features or benchmarking |
| Third-party commercial data | Credit, market, demographic, geospatial, enrichment data | Can fill gaps quickly | Licensing, bias, provenance, and quality risks | Value justifies cost and legal basis is clear |
| Surveys and interviews | Customer surveys, staff feedback, expert elicitation | Captures motivation, perception and missing context | Response bias, small samples, subjective | Need "why", not just "what" |

## Extraction approaches

| Approach | Strengths | Weaknesses | Use when | Avoid when |
|---|---|---|---|---|
| Batch ETL | Mature, controllable, good for stable reporting, easy to audit | Latency, duplicated data, pipelines can become rigid | Daily/weekly reporting or stable warehouse loads | Decisions need real-time freshness |
| ELT into data lake/lakehouse | Keeps raw data, flexible transformation, good for varied data | Requires governance or the lake becomes messy | Data science, experimentation, large/varied sources | Organisation lacks data catalogue or ownership |
| Streaming ingestion | Low latency, enables real-time alerts and personalisation | More complex, needs event schemas and monitoring | Fraud detection, IoT, live recommendations, safety alerts | Batch freshness is enough |
| API integration | Controlled, documented, supports external services | Rate limits, authentication, schema changes | Need repeatable access to SaaS or partner systems | API is unreliable or lacks required fields |
| Change Data Capture (CDC) | Efficiently captures database changes, supports near-real-time sync | Needs careful ordering, replay and deletion handling | Replicating operational DB changes to analytics | Source system cannot support CDC safely |
| Web scraping | Can gather data where no API exists | Fragile, legal/terms-of-use risks, quality issues | Public low-risk data with permission | API or licensed source exists |
| Manual upload | Simple, low technical barrier | Error-prone, weak auditability, not scalable | One-off pilots or small controlled datasets | Production pipelines |
| Edge extraction | Reduces latency and data transfer, can preserve privacy | Harder deployment and device management | IoT, cameras, remote sites, privacy-sensitive sensing | Models need central compute or frequent retraining |

## Data linking and integration approaches

| Method | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Deterministic key join | Simple, explainable, reproducible | Fails when IDs are missing, duplicated or inconsistent | Shared reliable IDs exist, such as customer ID/order ID |
| Composite key matching | More robust than one key | Still brittle if source formats vary | Match on combinations such as name + postcode + date |
| Probabilistic record linkage | Handles messy data and partial matches | False matches, needs thresholds and validation | Linking people/entities across imperfect systems |
| Master Data Management (MDM) | Creates governed "golden record" | Requires organisational ownership and stewardship | Repeated cross-system entity matching is business critical |
| Data warehouse integration | Structured, audited, consistent definitions | Less flexible for raw/semi-structured data | Stable BI, regulatory reporting, repeatable KPIs |
| Data lake/lakehouse integration | Handles structured, semi-structured and unstructured data | Needs metadata, access control and quality rules | AI/ML needs raw and curated data in one platform |
| Data virtualisation/federation | Avoids moving data, quick access across systems | Performance and governance can be harder | Data cannot be copied or systems are highly distributed |
| Knowledge graph/graph integration | Good for relationships and lineage | Requires modelling effort | Entity relationships are central to the task |

## Data quality checks

Use these as a checklist:

- **Accuracy** - values represent reality.
- **Completeness** - required fields are present.
- **Consistency** - definitions match across sources.
- **Uniqueness** - no duplicate records unless expected.
- **Timeliness** - data is recent enough.
- **Validity** - values fit expected formats and ranges.
- **Lineage** - source and transformations are traceable.
- **Relevance** - fields actually support the business problem.

Example controls:

- schema validation;
- range checks;
- duplicate detection;
- referential integrity checks;
- missingness reports;
- outlier detection;
- source reconciliation against known totals;
- data quality dashboards;
- data contracts between producers and consumers.

## Error types

| Error type | Meaning | Examples | Mitigation |
|---|---|---|---|
| Random error | Unpredictable variation or noise | Sensor noise, manual typing mistakes, natural fluctuation | Larger samples, repeated measurement, smoothing, confidence intervals |
| Systematic error | Consistent skew in one direction | Miscalibrated sensor, biased sample, under-reporting | Calibration, audit, representative sampling, process redesign |
| Data collection error | Problem at source | Missing fields, transcription error, tracking failure | Validation at entry, source monitoring, data contracts |
| Model error | Problem from analysis/model | Overfitting, bad assumptions, poor features | Train/validation/test split, cross-validation, model diagnostics |
| Measurement error | Proxy does not measure intended concept | Using clicks as satisfaction | Better proxy, triangulate multiple measures, user research |

## Bias types

| Bias type | Meaning | Example | Mitigation |
|---|---|---|---|
| Sample bias | Data sample is not representative | Survey only includes active app users | Stratified sampling, weighting, collect missing groups |
| Selection bias | Inclusion depends on behaviour/outcome | Only analysing approved loan applicants | Include rejected cases or use correction methods |
| Historical bias | Past unfairness is embedded in data | Hiring model learns past underrepresentation | Fairness testing, feature review, outcome monitoring |
| Coverage bias | Some populations or events are not captured | Rural users excluded from urban sensor network | Add sources, assess coverage gaps |
| Aggregation bias | One model/rule hides subgroup differences | Global model performs poorly for minority group | Segment analysis, subgroup metrics, tailored models |
| Confirmation bias | Analysts look for expected result | Choosing charts that support a preferred view | Pre-register tests, peer review, challenge assumptions |
| Label bias | Target variable is flawed | "High performer" based on manager rating only | Improve labels, use multiple evidence sources |
| Feature bias | Predictors encode protected characteristics or proxies | Postcode acting as ethnicity/income proxy | Feature audit, fairness metrics, remove or control proxies |

## Uncertainty types

| Uncertainty type | Meaning | Example | How to handle |
|---|---|---|---|
| Aleatoric | Irreducible randomness in the world or data | Weather variability, noisy human behaviour | Quantify with prediction intervals, use robust decisions |
| Epistemic | Lack of knowledge or insufficient data | New product with little history | Collect more data, Bayesian methods, model ensembles |
| Ontological | Unknown unknowns, problem framing uncertainty | New market behaviour after a shock | Scenario planning, human review, adaptive monitoring |
| Structural | Model/system assumptions may be wrong | Linear model used for nonlinear process | Compare model families, residual analysis |
| Deep uncertainty | No agreed probabilities or future states | Long-term social or regulatory change | Stress testing, robust strategy, governance review |

## Quantifying uncertainty

| Method | Use | Strengths | Weaknesses |
|---|---|---|---|
| Confidence interval | Estimate uncertainty around a statistic | Easy to explain, standard in reporting | Assumptions can be misunderstood |
| Prediction interval | Range for future observation | Better for forecasting decisions | Wider and harder to communicate |
| Standard error | Uncertainty of a sample estimate | Good for survey/sample statistics | Only covers sampling variability |
| Sensitivity analysis | Test effect of assumptions | Good for business decisions | Can miss untested assumptions |
| Monte Carlo simulation | Propagate uncertainty through a model | Handles complex uncertainty | Needs distributions and compute |
| Ensemble models | Compare variation across models | Useful for epistemic uncertainty | More complex to explain |
| Calibration curves | Check predicted probabilities | Important for risk scores | Needs enough labelled data |

## Q1 answer structure

Use this pattern:

1. Identify primary internal sources and relevant external sources.
2. Explain extraction method: batch, API, streaming, CDC, manual pilot.
3. Explain linking method: key join, MDM, probabilistic matching, lakehouse.
4. State data quality checks.
5. Discuss error, bias and uncertainty.
6. Add controls: validation, governance, monitoring, human review.

# Question 2 - Storage, Processing, Visualisation and Algorithms

## What Q2 is really asking

Q2 is about technical choices. You need to choose suitable data storage, analysis, visualisation and modelling methods for the scenario.

Do not just say "use AI" or "use cloud". Say:

- what storage pattern you would use;
- what processing pattern you would use;
- what analytics or algorithm fits the task;
- what metric proves it works;
- what trade-offs exist.

## Storage options

| Storage option | Strengths | Weaknesses | Use when | Avoid when |
|---|---|---|---|---|
| Relational database | ACID transactions, structured schema, SQL, mature | Less flexible for unstructured data and huge analytical workloads | Operational apps, structured data, transactional integrity | Storing raw video/text/logs at scale |
| Data warehouse | Consistent BI, governed reporting, performance for SQL analytics | Less flexible, schema-on-write, can be costly | KPIs, dashboards, regulatory reporting | Exploratory ML on raw varied data |
| Enterprise Data Warehouse (EDW) | Single governed store across organisation | Slow to change, high modelling effort | Organisation-wide trusted reporting | Fast experimental data science |
| Data mart | Focused departmental reporting | Can create silos and inconsistent definitions | Department-specific analytics | Cross-business single truth needed |
| Data lake | Stores raw structured/unstructured data cheaply | Can become a data swamp without governance | Large varied data, exploration, AI/ML raw inputs | Need strict curated reporting only |
| Lakehouse | Combines lake flexibility with warehouse governance | Platform complexity, needs strong metadata and access controls | Mixed BI and ML, structured and unstructured data | Small simple reporting use case |
| Document database | Flexible JSON-like records, good for changing schemas | Harder joins and consistency | Product catalogues, user profiles, semi-structured records | Complex relational reporting |
| Key-value store | Very fast lookup, simple scale | Limited querying | Sessions, caching, feature lookup | Complex analytics |
| Wide-column store | Scales for large sparse/high-write data | Query patterns must be designed upfront | IoT, logs, high-volume event data | Ad hoc relational queries |
| Graph database | Relationship queries, path analysis, network patterns | Requires graph modelling skills | Fraud rings, recommendations, entity relationships | Simple tabular reporting |
| Time-series database | Optimised for timestamped metrics | Less suited to non-time-series joins | Sensors, monitoring, telemetry, forecasting features | General enterprise data store |
| Search index | Full text search, ranking, filtering | Not source of truth | Document search, logs, support tickets | Financial records or transaction truth |
| Vector database | Similarity search over embeddings | Needs embedding quality and governance | Semantic search, RAG, recommendation, image/text similarity | Exact BI reporting |
| Data fabric | Connects distributed data through metadata/semantic layer | Organisational and technical complexity | Many distributed sources, need governed access | Simple single-platform data estate |

## Storage decision rules

- If the question is about stable dashboards and KPIs, choose **data warehouse** or **lakehouse curated layer**.
- If the question is about raw varied data for AI/ML, choose **data lake** or **lakehouse**.
- If the question is about relationships, choose **graph database** or graph features.
- If the question is about real-time events, use **streaming platform + event store/time-series store**.
- If the question is about semantic search, use **embeddings + vector database**.
- If the question is about operational app state, use **relational/document/key-value** depending on structure and latency.

## Processing options

| Processing option | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Batch processing | Simple, auditable, cost-efficient | Not real-time | Reports, periodic model retraining, large historical jobs |
| Micro-batch | Near-real-time with simpler operations than pure streaming | Still has latency | Frequent updates every few minutes |
| Streaming | Real-time decisions and alerts | Complex state, ordering, replay, monitoring | Fraud, IoT, live personalisation, safety |
| Edge processing | Low latency, privacy, less bandwidth | Harder deployment, device drift | Cameras, sensors, remote or privacy-sensitive sites |
| Distributed processing | Handles large volume | More engineering overhead | Big data transformations, large feature generation |
| Serverless processing | Low ops, scales on demand | Vendor constraints, cold starts, cost surprises | Event-driven pipelines, irregular workloads |

## Visualisation approaches

| Visualisation | Use when | Strengths | Watch out for |
|---|---|---|---|
| KPI dashboard | Executives or operational teams need repeated monitoring | Clear, standardised, track targets | Too many metrics, vanity KPIs |
| Drill-down BI dashboard | Users need to investigate drivers | Interactive, good for root cause | Requires governed dimensions |
| Time-series chart | Trends, seasonality, anomalies | Natural for temporal data | Avoid misleading axes or over-smoothing |
| Heatmap | Location/time/product intensity | Easy pattern spotting | Colour scales can distort |
| Geospatial map | Spatial patterns matter | Communicates location effects | Privacy and aggregation risk |
| Confusion matrix | Classification model errors | Shows false positives/negatives | Needs business cost interpretation |
| ROC/PR curve | Classifier threshold selection | Helps compare models | PR curve better for imbalanced data |
| SHAP/feature importance | Model explanation | Supports transparency | Can be misinterpreted as causal |
| Control chart | Process monitoring | Distinguishes normal variation from special cause | Needs stable process assumptions |

## Algorithm selection by task

### Classification

Use when the target is a category, such as churn yes/no, fraud/not fraud, defect type, risk class.

| Algorithm | Strengths | Weaknesses | Use when | Avoid when |
|---|---|---|---|---|
| Logistic regression | Simple, interpretable, fast, good baseline | Linear decision boundary, limited interactions | Need explainability, regulated decision, small/medium structured data | Complex nonlinear patterns dominate |
| Decision tree | Easy to explain, handles nonlinear rules | Overfits if deep, unstable | Need transparent rules or quick prototype | Need highest accuracy on noisy data |
| Random forest | Strong general accuracy, handles nonlinear data, robust | Less interpretable than one tree, larger model | Structured tabular classification/regression | Need simple explanation or very low latency |
| Gradient boosting / XGBoost / LightGBM | Often excellent on tabular data | Tuning, overfitting risk, less transparent | High-performance structured prediction | Very small data or strict interpretability |
| SVM | Effective in high-dimensional spaces | Scaling and tuning can be hard, less interpretable | Medium-sized high-dimensional data | Very large datasets or probability calibration needed |
| Naive Bayes | Fast, works well for text baselines | Strong independence assumption | Spam/text classification baseline | Correlated features dominate |
| Neural network | Learns complex patterns | Data hungry, less explainable, needs compute | Images, audio, complex nonlinear data | Small tabular data with explanation needs |
| Transformer/BERT-style model | Strong NLP contextual understanding | Compute intensive, needs careful fine-tuning and privacy checks | Text classification, semantic matching, entity extraction | Simple keyword/rule task is enough |

### Regression and prediction

Use when the target is numeric, such as price, demand, cost, waiting time, energy use.

| Algorithm | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Linear regression | Interpretable, fast, good baseline | Assumes linearity, sensitive to outliers | Need simple numeric prediction and coefficients |
| Regularised regression (Ridge/Lasso/Elastic Net) | Reduces overfitting, handles many features | Still mostly linear | Many correlated features, need stable baseline |
| Decision tree regression | Captures nonlinear splits | Overfits, step-like predictions | Explainable segmentation of numeric target |
| Random forest regression | Strong robust tabular model | Less interpretable, can be slow | Nonlinear structured data |
| Gradient boosting regression | High performance on tabular data | Tuning and monitoring needed | Accuracy is important and data is structured |
| Neural network regression | Flexible | Needs data, compute and tuning | Complex patterns or unstructured inputs |

### Time-series forecasting

Use when order in time matters and future values depend on previous values.

| Method | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Naive/seasonal naive baseline | Simple, strong benchmark | No complex relationships | Always use as a baseline |
| Moving average/exponential smoothing | Smooths noise, simple | Limited with complex drivers | Short-term stable series |
| Holt-Winters | Handles level, trend and seasonality | Assumes stable seasonal patterns | Forecasts with clear trend/seasonality |
| ARIMA | Combines autoregression, differencing and moving average | Needs stationarity, tuning p/d/q, weaker with external drivers | Single series with autocorrelation and trend handled by differencing |
| SARIMA | Adds seasonal ARIMA terms | More parameters, needs enough history | Seasonal series, e.g. weekly/yearly cycles |
| SARIMAX | Adds external variables | Requires future values of external variables | Forecast affected by promotions, weather, economic indicators |
| STL decomposition | Separates trend, seasonality and residual | More complex than differencing | Need to understand changing seasonality |
| Tree/boosting with lag features | Handles nonlinear drivers and many features | Feature engineering and time-aware validation needed | Rich exogenous data and multiple series |
| LSTM/sequence model | Captures complex temporal dependencies | Data hungry, less explainable, harder to maintain | Large sequential datasets, complex patterns |

Time-series notes:

- Trend can be handled by differencing, detrending, or models that include trend.
- Seasonality can be handled by seasonal differencing, seasonal dummy variables, SARIMA/SARIMAX, or STL.
- First-order differencing subtracts the previous value from the current value to remove a linear trend.
- Seasonal differencing subtracts the value from the same season in a previous cycle.
- Use rolling-origin or time-based validation, not random train/test split, because random splitting leaks future information.

### Clustering and segmentation

Use when there is no target label and you need groups.

| Algorithm | Strengths | Weaknesses | Use when |
|---|---|---|---|
| K-means | Simple, scalable, good baseline | Must choose k, assumes roughly spherical clusters, sensitive to scaling | Customer/product segmentation with numeric features |
| K-means++ | Better initial centre selection | Still has k-means assumptions | Same as k-means but want more stable starts |
| Hierarchical clustering | Dendrogram, no need to pre-set k initially | Does not scale well to very large data | Explore small/medium datasets |
| DBSCAN | Finds arbitrary shapes, identifies noise | Struggles with varying density and high dimensions | Geospatial/anomaly-like clusters |
| Gaussian Mixture Model | Soft membership probabilities | Assumes distributional form | Overlapping clusters and probabilistic assignment |
| PCA + clustering | Reduces dimensions before clustering | PCA can hide interpretability | High-dimensional numeric data |

### Anomaly detection

Use when rare unusual cases matter, such as fraud, defects, safety events or system faults.

| Method | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Rule-based detection | Explainable, quick, uses expert knowledge | Misses novel patterns, many false alerts | Known risk patterns and compliance rules |
| Statistical thresholds | Simple, transparent | Fails with seasonal/non-normal data | Stable metrics with clear outliers |
| Isolation Forest | Good general anomaly method for tabular data | Less transparent, tuning contamination | Multivariate outliers without many labels |
| One-class SVM | Learns boundary of normal class | Scaling/tuning difficult | Small/medium high-dimensional normal data |
| Autoencoder | Learns complex normal patterns | Data/compute heavy, less explainable | Complex sensor, image or sequence anomaly detection |
| Clustering-based anomaly | Finds points far from clusters | Sensitive to scaling and cluster assumptions | Need exploratory anomaly detection |

### Association and recommendation

| Method | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Association rules | Explainable "if X then Y" patterns | Can produce many trivial rules | Basket analysis, co-occurrence patterns |
| Collaborative filtering | Learns from similar users/items | Cold-start problem, sparse data | Recommending items with enough interaction history |
| Content-based filtering | Works with item/user attributes | Can over-specialise | New items or limited interaction data |
| Matrix factorisation | Good latent preference modelling | Less transparent, cold-start | Large user-item interaction matrix |
| Learning-to-rank | Optimises ranking directly | Needs labelled ranking/click data | Search/recommendation ranking |

### NLP and text analytics

| Method | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Keyword/rules | Transparent and quick | Brittle, misses context | Compliance flags, simple routing |
| TF-IDF + linear model | Strong baseline, interpretable features | Limited semantics | Text classification with modest data |
| Topic modelling | Finds themes without labels | Topics can be unstable/hard to name | Explore document collections |
| Embeddings | Captures semantic similarity | Needs model governance, can encode bias | Semantic search, clustering, matching |
| BERT/transformer | Context-aware, strong NLP performance | Compute, privacy, explainability | Complex classification, NER, question answering |

### Computer vision

| Method | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Traditional image processing | Fast, explainable | Sensitive to lighting and variation | Simple controlled inspection |
| CNN | Learns visual features | Needs labelled images and compute | Classification/detection in images |
| Transfer learning | Reduces data needs | Domain mismatch risk | Limited labelled data but similar pre-trained domain |
| Object detection model | Locates and classifies objects | Annotation effort, latency | Need bounding boxes/counting |
| OCR | Extracts text from images/docs | Accuracy depends on image quality | Forms, receipts, scanned documents |

## Metrics

| Task | Useful metrics | Notes |
|---|---|---|
| Balanced classification | Accuracy, F1, confusion matrix | Accuracy is acceptable only if classes are balanced |
| Imbalanced classification | Precision, recall, F1, PR-AUC | Optimise threshold for business cost |
| Risk scoring | ROC-AUC, calibration, Brier score | Probabilities must be calibrated |
| Regression | MAE, MSE, RMSE, R2 | MAE is interpretable; RMSE penalises large errors |
| Forecasting | MAE, RMSE, Map/sMAPE, backtesting | Use time-aware validation |
| Clustering | Silhouette, Davies-Bouldin, domain validation | Metrics are not enough; clusters must make business sense |
| Ranking | NDCG, MAP, precision@k, recall@k | Evaluate the top results users actually see |
| Anomaly detection | Precision@k, recall, false positive rate | Labels may be limited; human review matters |
| Fairness | Disparate impact, equal opportunity, subgroup performance | Use protected characteristic analysis where lawful and ethical |

## Model selection trade-offs

| Need | Prefer | Why |
|---|---|---|
| Interpretability | Logistic regression, decision tree, rule-based, linear model | Easier to explain and govern |
| Highest tabular accuracy | Gradient boosting, random forest | Strong for structured data |
| Real-time low latency | Linear/logistic model, rules, compact tree, cached features | Predictable speed |
| Small labelled dataset | Simpler models, transfer learning, expert rules | Avoid overfitting |
| Complex text | Transformer/BERT or embeddings | Captures context |
| Complex images | CNN/transfer learning | Learns visual features |
| Unlabelled segmentation | K-means, hierarchical, DBSCAN | No target label required |
| Rare event detection | Anomaly methods, imbalanced classifiers | Handles scarce positives |
| Regulated decisions | Interpretable model + governance + human review | Accountability and Article 22 risk |

## Q2 answer structure

1. State the storage architecture.
2. Explain processing pattern.
3. Pick visualisation/reporting outputs.
4. Pick algorithms by task.
5. Compare at least one alternative.
6. Give validation metrics.
7. Mention deployment/monitoring constraints.

# Question 3 - Legal, Ethical, Social and Professional Impacts

## What Q3 is really asking

Q3 tests whether you can see beyond the model and consider real-world consequences.

Cover four layers:

- legal compliance;
- ethical quality and fairness;
- social impact;
- professional accountability.

## UK GDPR and Data Protection Act 2018

Core principles:

- **Lawfulness, fairness and transparency** - people should know what is happening and processing must have a legal basis.
- **Purpose limitation** - use data for specified purposes.
- **Data minimisation** - collect only what is needed.
- **Accuracy** - keep data correct.
- **Storage limitation** - do not keep data longer than needed.
- **Integrity and confidentiality** - protect data.
- **Accountability** - be able to demonstrate compliance.

Lawful bases:

- consent;
- contract;
- legal obligation;
- vital interests;
- public task;
- legitimate interests.

When discussing lawful basis:

- consent must be freely given, specific, informed and withdrawable;
- legitimate interests needs a legitimate interest assessment: purpose, necessity and balancing test;
- contract applies only where processing is necessary for the contract, not merely useful;
- public task applies mainly to public authority or official functions.

## Special category data

Special category data includes:

- race or ethnicity;
- political opinions;
- religion or philosophical beliefs;
- trade union membership;
- genetic data;
- biometric data for identification;
- health data;
- sex life or sexual orientation.

For special category data, you need:

- a normal lawful basis under Article 6;
- a separate Article 9 condition;
- stronger safeguards;
- clear documentation.

Biometric, health, location, behavioural and CCTV-like data can be high risk even when not all of it is special category.

## DPIA

A Data Protection Impact Assessment is needed when processing is likely to create high risk to individuals.

High-risk indicators:

- large-scale monitoring;
- biometric identification;
- profiling or automated decisions;
- vulnerable people;
- combining datasets;
- location tracking;
- new technology;
- sensitive or special category data.

DPIA should cover:

- processing purpose;
- necessity and proportionality;
- risks to individuals;
- mitigations;
- residual risk;
- consultation with DPO/stakeholders where needed.

## Article 22 and automated decisions

UK GDPR Article 22 is relevant where there is solely automated decision-making with legal or similarly significant effects.

Risks:

- unfair denial of services;
- opaque decisions;
- inability to contest;
- hidden discrimination.

Mitigations:

- human review for significant decisions;
- clear explanation;
- route to appeal;
- model documentation;
- fairness testing;
- avoid fully automated decisions where not necessary.

## Equality Act 2010

Protected characteristics:

- age;
- disability;
- gender reassignment;
- marriage and civil partnership;
- pregnancy and maternity;
- race;
- religion or belief;
- sex;
- sexual orientation.

In technical answers:

- test subgroup performance where lawful and appropriate;
- avoid proxy discrimination;
- ensure reasonable adjustments and accessibility;
- document fairness trade-offs;
- monitor outcomes after deployment.

## Human Rights Act and privacy

Article 8 privacy is often relevant where surveillance, monitoring, personal data or profiling is involved.

Use proportionality:

- Is the objective legitimate?
- Is the data necessary?
- Is there a less intrusive alternative?
- Are safeguards strong enough?

## AI Act and AI governance

Use this generically:

- classify risk level;
- document system purpose and limitations;
- maintain human oversight;
- ensure transparency;
- manage data quality and bias;
- keep logs and technical documentation;
- monitor post-deployment performance.

High-risk AI requires stronger governance, documentation, risk management, human oversight and data quality controls.

## Ethical frameworks

| Framework | Useful points |
|---|---|
| OECD AI principles | Human-centred values, fairness, transparency, robustness, accountability |
| Asilomar principles | Safety, failure transparency, judicial transparency, value alignment, responsibility |
| UK Data Ethics Framework | Clear public benefit, transparency, accountability, proportionality |
| EU trustworthy AI themes | Human agency, technical robustness, privacy, transparency, fairness, societal wellbeing, accountability |
| Professional code of conduct | Competence, integrity, public interest, confidentiality, avoid harm |

## Ethical issue checklist

| Issue | Why it matters | Mitigation |
|---|---|---|
| Fairness and bias | Harm to protected or vulnerable groups | Bias audit, subgroup metrics, representative data, monitoring |
| Transparency | Users may not understand automated use of data | Clear notices, model cards, explainable outputs |
| Accountability | No one owns failures | Named owner, governance board, audit trail |
| Privacy | Intrusive collection or re-identification | Minimisation, pseudonymisation, access control, DPIA |
| Security | Breach or misuse | Encryption, least privilege, logging, incident response |
| Explainability | Decisions cannot be challenged | Use interpretable models or explanation tools |
| Human oversight | Automation can scale harm | Human-in-the-loop for high-impact decisions |
| Sustainability | Compute and storage have environmental cost | Efficient models, right-sized infrastructure, lifecycle review |
| Misuse | Model used beyond intended purpose | Access control, policy, monitoring, purpose limitation |
| Data ownership/IP | Unclear rights to data/models | Licensing review, contracts, provenance |

## Social impacts

Consider:

- job displacement or deskilling;
- worker monitoring and autonomy;
- customer trust;
- exclusion of digitally disadvantaged groups;
- accessibility;
- impact on vulnerable people;
- chilling effects from surveillance;
- overreliance on automated decisions;
- environmental cost;
- public legitimacy.

## Professional responsibilities

An AI data specialist should:

- work within competence;
- document assumptions;
- be honest about limitations;
- challenge unsafe or unethical uses;
- maintain confidentiality;
- follow security policies;
- validate models properly;
- monitor drift and performance;
- escalate high-risk issues;
- keep evidence for audit.

## Q3 answer structure

Use this pattern:

1. Identify legal basis and data protection principles.
2. State whether DPIA is needed.
3. Discuss special category/profiling/Article 22 if relevant.
4. Cover Equality Act and fairness.
5. Cover ethics: transparency, accountability, privacy, human oversight.
6. Cover social impact.
7. Give controls: governance, documentation, testing, monitoring, appeal process.

# Question 4 - Methodologies, Design, Development, Deployment and Resources

## What Q4 is really asking

Q4 asks how you would deliver the system or project, not just which model you would use.

You need to show:

- project methodology;
- data science process;
- engineering and deployment process;
- architecture;
- resources and roles;
- monitoring and governance.

The user mentioned "TSPS". The method usually referenced in AI/data project notes is **TDSP**, the Microsoft Team Data Science Process. If the exam wording says TSPS, answer the wording used, but revise TDSP as the common framework.

## Methodology selection table

| Method | Phases / idea | Strengths | Weaknesses | Best use |
|---|---|---|---|---|
| CRISP-DM | Business understanding, data understanding, data preparation, modelling, evaluation, deployment | Very strong generic data science lifecycle, business-led, iterative, widely recognised | Does not prescribe modern software/MLOps practices in detail | Most ML/data science exam answers, especially when problem definition and modelling are central |
| TDSP | Business understanding, data acquisition/understanding, modelling, deployment, customer acceptance; includes team roles and artefacts | More operational/team-focused than CRISP-DM, fits cloud and collaborative delivery | Less universally known than CRISP-DM | Enterprise team delivery, cloud ML, repeatable artefacts |
| KDD | Selection, preprocessing, transformation, data mining, interpretation/evaluation | Strong for knowledge discovery and data mining | Less focused on deployment and business change | Exploratory pattern discovery, research-like analysis |
| SEMMA | Sample, Explore, Modify, Model, Assess | Clear modelling workflow, good for SAS/data mining style projects | Starts with data rather than business problem, weak deployment focus | Model-building workflow when data already exists |
| Agile | Iterative delivery, backlog, customer collaboration, respond to change | Flexible, frequent feedback, good when requirements evolve | Can underplay data uncertainty unless combined with CRISP-DM/TDSP | Product development around data/AI capability |
| Scrum | Roles, sprints, sprint planning, review, retrospective | Cadence, accountability, stakeholder demos | Fixed sprint commitments can clash with uncertain research tasks | Cross-functional product team with regular increments |
| Kanban | Visualise work, limit WIP, optimise flow | Good for variable-length tasks, support work, data science uncertainty | Less structured planning than Scrum | Data science teams with uneven task sizes |
| Scrumban | Scrum planning plus Kanban flow/WIP limits | Combines cadence with flexibility | Can become vague without discipline | AI teams needing sprint goals and flexible discovery |
| Waterfall | Sequential requirements, design, build, test, deploy | Clear governance and documentation | Poor for uncertain data/model discovery | Stable regulatory or infrastructure work with fixed requirements |
| DevOps | Collaboration, automation, CI/CD, monitoring | Strong for reliable software delivery | Does not cover data/model drift by itself | Software components, APIs, deployment pipelines |
| DataOps | Agile, automated, governed data pipelines and analytics | Improves data quality, lineage, testing and collaboration | Needs cultural and tooling maturity | Production data pipelines feeding analytics/ML |
| MLOps | CI/CD/CT/CM for ML: delivery, training, testing, monitoring | Handles reproducibility, drift, deployment and retraining | More complex than one-off modelling | Any production ML model |
| Lean/Kaizen | Reduce waste, continuous improvement | Good for process optimisation and measurable value | Not a full ML lifecycle | Operational improvement and reducing process waste |
| PRINCE2 / stage-gate | Controlled stages, business case, governance | Strong governance and risk control | Can be slow/rigid | Large organisation projects needing formal approvals |

## How to choose the right methodology

| Scenario clue | Strong answer |
|---|---|
| Data science problem, uncertain features/model | CRISP-DM as core lifecycle |
| Team/cloud enterprise delivery | TDSP plus Agile/MLOps |
| Discovery of unknown patterns | KDD or CRISP-DM data understanding/exploration |
| Model building from prepared data | SEMMA |
| Fast changing stakeholder requirements | Agile/Scrum/Scrumban |
| Variable data science tasks and support requests | Kanban or Scrumban |
| Production pipelines | DataOps |
| Production model | MLOps |
| Software/API deployment | DevOps |
| Fixed regulated deliverable | Waterfall/stage-gate plus governance |

## CRISP-DM detailed notes

| Phase | What to do | Outputs | Risks |
|---|---|---|---|
| Business understanding | Define business objectives, success criteria, constraints, stakeholders | Problem statement, KPI, risk log | Building the wrong thing |
| Data understanding | Identify sources, collect initial data, explore quality and bias | Data inventory, EDA, quality report | Hidden gaps or biased samples |
| Data preparation | Clean, transform, link, label, feature engineer | Training dataset, feature pipeline, documentation | Leakage, inconsistent definitions |
| Modelling | Select algorithms, train, tune, compare baselines | Candidate models, metrics, experiments | Overfitting, chasing accuracy |
| Evaluation | Check model against business objectives, ethics, legal and operational constraints | Evaluation report, go/no-go decision | Good metric but poor real-world value |
| Deployment | Implement model, dashboard, decision support or process change | Production service/report/process | No monitoring, no adoption |

CRISP-DM strengths:

- business-led;
- iterative;
- easy to explain;
- fits most data science problems;
- encourages evaluation before deployment.

CRISP-DM weaknesses:

- older framework;
- weak on CI/CD, monitoring, data contracts and infrastructure;
- needs pairing with Agile/DataOps/MLOps for production.

Good exam phrasing:

> I would use CRISP-DM as the core data science lifecycle because the problem requires iterative movement between business understanding, data understanding, preparation, modelling and evaluation. I would combine it with Kanban/Scrumban for delivery management and MLOps for production deployment and monitoring.

## TDSP detailed notes

TDSP is useful when the question asks about team delivery, enterprise repeatability or cloud-based ML.

Typical phases:

- business understanding;
- data acquisition and understanding;
- modelling;
- deployment;
- customer acceptance.

Strengths:

- includes team roles and artefacts;
- better fit for collaborative delivery than pure CRISP-DM;
- supports repeatable project structure;
- aligns well with cloud ML platforms.

Weaknesses:

- less widely recognised than CRISP-DM;
- can feel heavyweight for a small one-off analysis;
- still needs organisation-specific governance and MLOps.

Use TDSP when:

- multiple people are involved;
- deliverables need to be repeatable;
- cloud resources and shared repositories are used;
- customer acceptance and operational handover matter.

## KDD detailed notes

KDD means Knowledge Discovery in Databases.

Typical stages:

- selection;
- preprocessing;
- transformation;
- data mining;
- interpretation/evaluation.

Strengths:

- strong for exploratory pattern discovery;
- emphasises preprocessing and transformation;
- useful for unsupervised discovery and data mining.

Weaknesses:

- weaker on business deployment and product operation;
- can become data-led rather than problem-led;
- does not define MLOps or governance practices.

Use KDD when:

- the task is to discover hidden patterns;
- labels are unavailable;
- the business does not yet know what signals exist.

## SEMMA detailed notes

SEMMA means Sample, Explore, Modify, Model, Assess.

Strengths:

- simple and memorable;
- practical for model-building;
- good when data already exists and the task is analytical.

Weaknesses:

- not business-first;
- weak on deployment;
- associated with data mining tooling rather than end-to-end AI delivery.

Use SEMMA when:

- the question is focused on modelling workflow;
- you need a quick structure for data mining;
- data is already available and the aim is model comparison.

## Agile, Scrum, Kanban and Scrumban

| Method | Strengths | Weaknesses | Good fit |
|---|---|---|---|
| Agile | Adapts to change, frequent feedback, incremental delivery | Can become unstructured if not managed | Product and stakeholder-driven AI projects |
| Scrum | Clear ceremonies, sprint goals, demos, retrospectives | Research tasks may not fit neat sprint estimates | Cross-functional team building a product increment |
| Kanban | Visual workflow, WIP limits, continuous delivery | Less long-term planning | Data science tasks with variable uncertainty |
| Scrumban | Combines sprint planning with flexible flow | Needs discipline to avoid process confusion | AI delivery where discovery and production tasks coexist |

For data science, Kanban often fits because some tasks are unpredictable: data cleaning could take hours or weeks depending on quality. Scrum can still help when there are clear sprint demos, product increments or stakeholder deadlines.

## DataOps, MLOps and DevOps

| Practice | Focus | Key controls | Use when |
|---|---|---|---|
| DevOps | Software delivery | CI/CD, infrastructure as code, automated tests, monitoring | APIs, apps, dashboards, deployment automation |
| DataOps | Data pipeline delivery | Data tests, orchestration, lineage, data quality monitoring, analytics as code | ETL/ELT, warehouses, lakehouses, production datasets |
| MLOps | Model lifecycle | Experiment tracking, model registry, CI/CD/CT, drift monitoring, retraining, rollback | Production ML models |

MLOps should cover:

- reproducible environments;
- versioned data/features/code/models;
- experiment tracking;
- model registry;
- automated testing;
- deployment pipelines;
- continuous monitoring;
- drift detection;
- retraining triggers;
- rollback plan.

DataOps should cover:

- pipeline orchestration;
- data quality tests;
- metadata and lineage;
- access control;
- monitoring and alerting;
- reusable components;
- data contracts;
- collaboration between data engineers, scientists and users.

## Architecture patterns

| Pattern | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Batch analytics pipeline | Simple, auditable, cost-efficient | Latency | Periodic reporting and retraining |
| Streaming/event-driven architecture | Real-time, responsive | Operational complexity | Live alerts, IoT, fraud, operational automation |
| Lakehouse ML platform | Supports raw and curated data, BI and ML | Governance and platform complexity | Organisation needs both analytics and ML |
| Microservices/API model serving | Scalable, integrates with apps | Requires DevOps, monitoring and versioning | Model predictions needed by applications |
| Edge AI | Low latency, privacy, bandwidth saving | Device management, model update complexity | Sensors, cameras, remote locations |
| Serverless pipeline | Low operations and event-driven scaling | Vendor lock-in and cold starts | Irregular jobs or small event-driven workloads |
| Hybrid/on-prem/cloud | Balances control and scalability | Integration complexity | Sensitive data, legacy systems, cloud scaling needs |
| Data fabric | Unified access over distributed sources | Heavy governance and metadata needs | Large distributed organisation |

## Generic target architecture

A strong generic AI/data architecture often includes:

1. **Source systems** - operational DBs, APIs, sensors, documents, external data.
2. **Ingestion** - batch ETL/ELT, streaming, CDC, API connectors.
3. **Raw zone** - immutable raw data with metadata and access controls.
4. **Curated zone** - cleaned, linked, standardised data.
5. **Feature layer** - reusable model features with definitions and lineage.
6. **Model development** - notebooks/IDE, experiment tracking, version control.
7. **Model registry** - approved model versions and metadata.
8. **Serving layer** - API, batch scoring, dashboard, decision support or edge device.
9. **Monitoring** - data quality, drift, performance, fairness, latency, cost.
10. **Governance** - DPIA, access control, audit logs, documentation, approvals.

## Development lifecycle for a production model

1. Define problem, users, risks and success metric.
2. Confirm legal basis and DPIA need.
3. Acquire and profile data.
4. Build baseline model.
5. Engineer features and compare candidate models.
6. Validate on holdout/time-aware test set.
7. Check fairness, explainability and robustness.
8. Package model with reproducible environment.
9. Deploy first to offline, shadow or pilot mode.
10. Monitor, retrain, improve or retire.

## Deployment strategies

| Strategy | Strengths | Weaknesses | Use when |
|---|---|---|---|
| Proof of concept | Fast learning | Not production quality | Test feasibility |
| Pilot | Real-world limited test | Limited scale | Validate with controlled users/sites |
| Shadow mode | Model runs without affecting decisions | Needs parallel operation | High-risk decisions where safety matters |
| A/B test | Measures business impact | Ethical/statistical design needed | Compare model/process variants |
| Canary release | Limits blast radius | Needs monitoring and rollback | Gradual production rollout |
| Blue-green deployment | Fast rollback | Duplicate environments | Critical systems |
| Phased rollout | Lower adoption risk | Slower benefits | Large organisation/process change |
| Human-in-the-loop | Adds oversight | Slower, possible inconsistency | High-impact or uncertain predictions |

## Monitoring

Monitor all of these:

- data freshness;
- missingness and schema changes;
- input distribution drift;
- concept drift;
- model accuracy/performance;
- subgroup fairness;
- calibration;
- latency;
- cost;
- uptime;
- user feedback;
- incidents and overrides.

Retraining triggers:

- performance drops below threshold;
- input distribution changes;
- new labelled data arrives;
- business process changes;
- regulatory or policy change;
- seasonal update needed.

## Resources and roles

| Role | Responsibility |
|---|---|
| Product owner / business sponsor | Defines value, prioritises backlog, accepts deliverables |
| Domain expert | Explains process, validates assumptions, interprets outputs |
| Data owner | Accountable for data use and access decisions |
| Data steward | Maintains definitions, quality rules and governance |
| Data engineer | Builds ingestion, pipelines, storage, data quality checks |
| Data scientist | EDA, feature engineering, modelling, evaluation |
| ML engineer | Packages model, model serving, performance engineering |
| MLOps/DevOps engineer | CI/CD, infrastructure, monitoring, deployment automation |
| Software engineer | Integrates model into app/API/workflow |
| Security engineer | Access control, threat modelling, secure deployment |
| DPO/legal/compliance | GDPR, DPIA, contracts, high-risk review |
| UX/service designer | Human workflow, explainability, adoption |
| QA/test engineer | Test strategy and automation |
| Change manager/trainer | Adoption, training, process change |

## Infrastructure resources

- cloud or on-prem compute;
- secure storage;
- data warehouse/lake/lakehouse;
- orchestration tool;
- version control;
- CI/CD pipeline;
- container registry;
- experiment tracking;
- feature store where useful;
- model registry;
- monitoring/alerting;
- secrets management;
- identity and access management;
- backup and disaster recovery;
- logging and audit trail.

## Testing checklist

| Test type | What it checks |
|---|---|
| Unit tests | Code functions behave correctly |
| Data validation tests | Schema, ranges, missingness, duplicates |
| Pipeline tests | ETL/ELT works end to end |
| Model validation | Accuracy, robustness, calibration |
| Fairness tests | Subgroup performance and proxy bias |
| Security tests | Access, secrets, vulnerabilities |
| Performance tests | Latency, throughput, scale |
| User acceptance tests | Users can interpret and act on outputs |
| Monitoring tests | Alerts fire when data/model issues occur |

## Q4 answer structure

1. Select methodology and justify it.
2. Explain phases from problem definition to deployment.
3. Add Agile/Kanban/Scrum if delivery management is needed.
4. Add DataOps/MLOps for production data/model management.
5. Describe architecture.
6. List people and technical resources.
7. Explain deployment strategy.
8. Explain monitoring, retraining and governance.

# Quick Selection Guide

## If asked "what method should be used?"

- Use **CRISP-DM** for most generic AI/data science lifecycle questions.
- Use **TDSP** where team, cloud, artefacts and customer acceptance matter.
- Use **KDD** for discovering hidden patterns from data.
- Use **SEMMA** for model-building from available data.
- Use **Agile/Kanban/Scrumban** for managing changing work.
- Use **DataOps** for reliable data pipelines.
- Use **MLOps** for production ML lifecycle.
- Use **DevOps** for software/API deployment.

## If asked "which storage?"

- Structured reporting: data warehouse.
- Mixed BI + ML: lakehouse.
- Raw varied data: data lake.
- Relationships: graph database.
- Fast lookups/cache: key-value store.
- Semi-structured documents: document DB.
- High-volume time events: wide-column or time-series store.
- Semantic search: vector database.

## If asked "which algorithm?"

- Explainable binary decision: logistic regression or decision tree.
- Strong tabular prediction: gradient boosting or random forest.
- Forecast with seasonality: SARIMA/SARIMAX or Holt-Winters.
- Forecast with many drivers: tree/boosting with lag features or SARIMAX.
- Text classification: TF-IDF + linear baseline, then BERT/transformer if complexity justifies it.
- Image task: CNN/transfer learning.
- Segmentation: k-means, hierarchical or DBSCAN depending on shape/scale.
- Anomaly detection: rules for known patterns, Isolation Forest/autoencoder for unknown patterns.
- Recommendation: association rules for explainable co-occurrence, collaborative/content-based/matrix factorisation for personalisation.

## If asked "what are the risks?"

- Data quality risk: missing, inconsistent, biased, stale data.
- Legal risk: no lawful basis, excessive data, Article 22, special category data.
- Ethical risk: unfairness, opacity, lack of accountability, intrusive surveillance.
- Technical risk: overfitting, drift, leakage, poor calibration, weak monitoring.
- Operational risk: no owner, no adoption, no rollback, poor integration.
- Security risk: unauthorised access, data leakage, model misuse.

## If asked "how would you make it production ready?"

- Version code, data, features and models.
- Automate tests and deployment.
- Use a model registry.
- Monitor data quality, drift and model performance.
- Add fairness and explainability checks.
- Define retraining triggers.
- Use staged rollout and rollback.
- Document decisions, assumptions and limitations.
- Assign owners for data, model and business process.

## Final exam reminder

For every choice, write:

- **Use this because...**
- **It is stronger than X because...**
- **The weakness is...**
- **I would mitigate it by...**
- **I would measure success with...**
