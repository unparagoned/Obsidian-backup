---
tags:
  - EPA
  - AM3
  - technical-test
  - revision
source: BCS L7 AM3 Sample Paper V2.0 – Optimum Answer Notes
---

# Z Technical Test Sample – Detailed Answer Notes

> Scenario: Multi-site grocery retailer moving to a **till-less "lift and leave"** system. Role: recommend an AI solution for customer identification, stock prediction, and seamless checkout.

---

## Question 1 – Data Extraction, Linkage & Uncertainty

### 1a) Types of data you will use

**Internal structured data (databases):**
- MemberTrack: customer personal info, purchase history, membership status, promotional data
- FoodTrack: stock levels per item/store, trigger levels, expiration dates, distribution centre stock
- CheckoutTrack: transaction records, items purchased, payment method, discounts, membership status

**New sensor/device data:**
- Weighted shelf sensor readings (continuous numeric) — item removal/replacement events
- CCTV/camera feeds (unstructured image/video) — existing infrastructure to be augmented
- Mobile app interaction data (semi-structured JSON) — customer ID, basket, payment token

**Biometric data (special category under GDPR):**
- Facial recognition images (biometric identifiers)
- Height estimates (if using overhead cameras)
- Note: biometric data requires explicit consent and DPIA

**External data:**
- Met Office API: weather by location/date → affects footfall and buying patterns
- Office for National Statistics (Owns): demographic profiles per store location
- Consumer Confidence Index (CCI): macro spending trends → stock purchasing and budgeting

**Data classification:**
- Structured: SQL databases (MemberTrack, FoodTrack, CheckoutTrack)
- Semi-structured: JSON from app/API feeds, sensor logs
- Unstructured: CCTV video, camera images

---

### 1b) Process for extracting the data

**Internal systems (MemberTrack, FoodTrack, CheckoutTrack):**
- ETL (Extract, Transform, Load) pipeline via AWS Glue
- SQL queries via JDBC connectors to pull transactional data
- Batch extraction for historical data; event-driven/streaming for real-time updates
- CheckoutTrack currently updates FoodTrack every 90 minutes — real-time streaming (e.g. Kinesis) would be needed for till-less system

**Sensor data:**
- Weighted shelves: IoT data via MQTT/REST API to a message broker (e.g. AWS IoT Core)
- Camera feeds: local edge processing to extract feature vectors; only metadata/embeddings sent to cloud (reduces bandwidth and data volume)

**External APIs:**
- Met Office DataPoint API: scheduled pulls (daily/hourly)
- Owns: batch download, periodic refresh
- CCI: monthly batch ingestion

**Mobile app:**
- Customer-initiated push on app launch and checkout; REST API to cloud data store
- Payment token generated before customer enters store (meets requirement: payment established before goods removed)

---

### 1c) How data from multiple systems can be linked

**Common key fields:**
- `CustomerID` / membership number links MemberTrack ↔ CheckoutTrack ↔ new system
- `ProductID` / barcode links CheckoutTrack ↔ FoodTrack ↔ weighted shelf sensor data
- `StoreID` + timestamp links transaction data ↔ weather data ↔ Owns demographics

**Architecture approach – Data Lakehouse (recommended):**
- Centralise all data into an AWS S3-based lakehouse (raw → processed → curated zones)
- AWS Glue catalogue creates a unified schema across sources
- AWS Athena for ad hoc SQL queries across linked datasets
- Avoids duplication while maintaining lineage

**Short-term – Data virtualisation (Denodo):**
- Federated queries across MemberTrack, FoodTrack, CheckoutTrack without moving data
- Lower disruption to existing systems during transition

**Real-time linkage:**
- Event streaming (AWS Kinesis): customer enters store (app/facial ID) triggers lookup of purchase history in MemberTrack to personalise predictions in real time

---

### 1d) Potential for error, bias, and uncertainty

**Error:**
- *Data error:* FoodTrack updated only every 90 minutes — stock figures may be stale; 15% good-faith delivery means up to 85% of deliveries unchecked (quantity/damage errors undetected)
- *Sensor error:* Weighted shelves may misfire if multiple customers interact simultaneously; calibration drift over time
- *Biometric error:* Facial recognition False Acceptance Rate (FAR) and False Rejection Rate (FRR) — incorrect ID matches
- *Manual data entry error:* Loose items (vegetables) manually entered via touchscreen → transcription errors
- *Model error:* ML model trained on historical CheckoutTrack data may not generalise to new buying patterns post-rollout

**Bias:**
- *Historical bias:* Purchase history skewed by past promotions, delivery gaps, or previous self-scan fraud — models trained on this data inherit those patterns
- *Sample bias:* MemberTrack only covers members (~not all customers); non-members underrepresented in demand predictions
- *Coverage bias:* Facial recognition systems perform worse on non-white faces, faces partially obscured (hats, masks, glasses, scarves) — will disproportionately misidentify certain customer groups
- *Aggregation bias:* Using national CCI averages may not reflect local store demographics (trigger levels already vary by branch — same principle applies to ML models)
- *Selection bias:* If training data is drawn from high-footfall periods, model underperforms in off-peak or seasonal periods

**Uncertainty:**
- *Aleatoric (irreducible):* Inherent randomness in customer behaviour, weather impact on footfall, spontaneous purchasing decisions — cannot be eliminated
- *Epistemic (reducible):* Model uncertainty from insufficient training data for new product lines, new store layouts, or post-COVID behaviour shifts — can be reduced with more/better data
- *Structural uncertainty:* Simplifications in the demand model (e.g. assuming independence between product demand) may not reflect reality of basket correlations

---

### 1e) Differences in uncertainty before and after analysis

**Before analysis (data collection uncertainty):**
- Measurement uncertainty: sensor precision, camera resolution, survey response accuracy (CCI)
- Completeness uncertainty: missing values (non-members, partial delivery records), gaps in CCTV coverage
- Sampling uncertainty: whether collected data is representative of all customer segments and time periods
- Quantified using: standard error (SEM = SD/√n), confidence intervals on data quality metrics

**After analysis (analytical/model output uncertainty):**
- *Aleatoric uncertainty* remains in outputs — inherent noise in predictions (e.g. daily stock demand varies randomly)
- *Epistemic uncertainty* in model: model may be confidently wrong (overconfident outputs from deep learning classifiers — softmax outputs ≠ calibrated probabilities)
- Techniques to quantify model uncertainty:
  - **Monte Carlo Dropout**: run inference multiple times with dropout active; spread of outputs = uncertainty estimate
  - **Ensemble methods**: train multiple models; disagreement between models = uncertainty signal
  - **Calibration curves**: assess whether predicted probabilities match actual outcomes
- *Key distinction:* Pre-analysis uncertainty is about data quality and coverage. Post-analysis uncertainty is about whether the model's conclusions are trustworthy given that data — uncertainty can *increase* after analysis if the model is poorly specified or extrapolating outside its training distribution

---

## Question 2 – Storage, Analysis & Machine Learning

### 2a) How extracted data can be stored, analysed and visualised

**Storage (see 2b/2c for justification):**
- Raw layer: AWS S3 (all formats — structured, semi-structured, unstructured video/images)
- Processed layer: AWS Glue ETL → Parquet/Delta format for query efficiency
- Serving layer: AWS Redshift for BI/reporting; AWS Athena for ad hoc SQL

**Analysis:**
- Descriptive: historical basket analysis, footfall trends, stock velocity per store
- Predictive: demand forecasting (ARIMA/LSTM), customer behaviour clustering, next-basket prediction
- Real-time: streaming anomaly detection (fraud, theft), live stock level updates via Kinesis

**Visualisation:**
- Operational dashboards (Power BI / AWS QuickSight): live stock levels, footfall, alert triggers
- Model performance dashboards: accuracy, F1-score, data drift monitoring
- Heatmaps: store layout foot-traffic patterns from CCTV analysis
- Time series plots: stock levels vs. predicted demand over time

---

### 2b) Storage requirements

| Data Type | Volume | Velocity | Format | Retention |
|---|---|---|---|---|
| Transaction records | High | Batch (90 min) → real-time | Structured SQL | Long-term (regulatory) |
| CCTV/camera | Very high | Continuous stream | Video (MP4) / image embeddings | Short-term raw; embeddings retained |
| Sensor (shelves) | Medium | Near real-time | Time-series JSON | Rolling window |
| Member/stock data | Medium | Batch daily | Structured SQL | Long-term |
| External APIs | Low | Daily/hourly batch | JSON | Medium-term |

- **Scalability:** S3 object storage scales elastically — no pre-provisioning needed
- **Latency:** Real-time checkout requires sub-second lookup → ElastiCache (Redis) for customer profile caching
- **Governance:** Separate storage zones by data sensitivity (biometric data encrypted at rest, strict IAM access control)

---

### 2c) Justification for storage solutions and processing technologies

**AWS S3 + Data Lakehouse:**
- Handles all data types (structured, semi-structured, unstructured) in one place
- Decouples storage from compute — pay only for what you query
- Supports both batch (Glue/Athena) and streaming (Kinesis) pipelines
- Open formats (Parquet/Delta Lake) prevent vendor lock-in
- Native integration with SageMaker for ML training

**AWS Glue (ETL):**
- Serverless — no infrastructure to manage
- Schema discovery, data cataloguing, lineage tracking

**AWS Redshift (warehouse):**
- Columnar storage optimised for analytical queries
- Suitable for BI dashboards and board-level reporting

**AWS SageMaker (ML platform):**
- Managed training, tuning, and deployment
- Built-in MLOps: model registry, pipelines, monitoring for data drift

**Streaming: AWS Kinesis:**
- Required to replace 90-minute batch updates with near real-time stock adjustments
- Feeds live transaction events from till-less system → FoodTrack equivalent

---

### 2d) ML algorithm comparison

#### Task 1: Customer Identification

| Criterion | CNN (custom trained) | Pre-trained Transfer Learning (ResNet50/VGG16) |
|---|---|---|
| Accuracy | High if large labelled dataset available | High even with small dataset (ImageNet weights) |
| Training data needed | Millions of labelled faces | Hundreds of examples per customer (fine-tuning) |
| Speed | Slower to train from scratch | Faster — only fine-tune final layers |
| Explainability | Lower | Lower (Grad-CAM visualisation helps) |
| Bias risk | High — must audit for demographic parity | Same risk — inherited from ImageNet training data |
| **Recommendation** | | **Transfer learning preferred** — practical for deployment timeline |

#### Task 2: Demand / Stock Forecasting

| Criterion | ARIMA / SARIMA | LSTM (Long Short-Term Memory) |
|---|---|---|
| Handles seasonality | SARIMA — yes | Yes (learns automatically) |
| Interpretability | High (explicit parameters p, d, q) | Low (black box) |
| Training data needed | Moderate | Large (sequences of data) |
| Handles external regressors | Limited (ARIMAX) | Yes (multivariate LSTM) |
| Real-time retraining | Feasible | Computationally expensive |
| **Best use** | Individual SKU forecasting where data is regular | Multi-store, multi-product with weather/event features |
| **Recommendation** | | **Hybrid: SARIMA for simple SKUs, LSTM for complex patterns** |

#### Task 3: Personalisation / Next-basket Prediction

| Criterion | Collaborative Filtering | Gradient Boosting (XGBoost) |
|---|---|---|
| Uses purchase history | Yes (matrix factorisation) | Yes (engineered features) |
| Cold start (new customers) | Poor | Better with demographic features |
| Interpretability | Low | Medium (SHAP values) |
| Handles promotions/seasonality | Limited | Yes (include as features) |
| **Recommendation** | | **XGBoost with feature engineering for production; collaborative filtering for member recommendations** |

---

## Question 3 – Legal, Ethical & Social Impact

### 3a) Constraints and internal/external impacts

#### Legal Constraints

**UK GDPR / Data Protection Act 2018:**
- Biometric data (facial recognition, fingerprints) = **special category data** → requires *explicit consent* as the legal basis (not merely legitimate interests)
- **Data minimisation:** only collect what is necessary — full CCTV footage should not be retained longer than necessary; facial embeddings preferred over raw images
- **Purpose limitation:** MemberTrack data collected for promotions cannot be repurposed for surveillance/fraud detection without fresh legal basis
- **Article 22 – Automated decision-making:** Fully automated checkout = automated decision with legal/significant effect → must allow human review or offer opt-out right
- **Data Protection Impact Assessment (DPIA):** Mandatory before deploying facial recognition at scale — high-risk processing
- **Data retention:** Payment card data subject to PCI DSS; biometric data retention period must be defined and enforced

**Equality Act 2010:**
- Facial recognition systems with higher error rates for certain ethnic groups = indirect discrimination on grounds of **race**
- Automated ID verification may disadvantage customers with **disabilities** (e.g. those who cannot use mobile apps or whose faces are obscured for medical reasons)
- Must demonstrate equivalent access for all protected characteristics

**Human Rights Act 1998:**
- **Article 8 (Right to private and family life):** Customer tracking via CCTV/facial recognition must be proportionate and necessary; prominent signage required
- **Article 14 (Non-discrimination):** System must not produce discriminatory outcomes

**Computer Misuse Act 1990 / Payment Card Industry DSS:**
- Payment token storage and transmission must meet PCI DSS standards
- Any breach of stored payment data carries legal liability

#### Ethical Constraints and Impacts

**Facial recognition and surveillance:**
- Even with consent, continuous tracking of customer movement within a store creates a surveillance environment that many customers will find intrusive
- Risk of "function creep" — data collected for checkout repurposed for profiling or marketing without consent
- Alternative: use weighted shelves + mobile app as primary identification (less invasive); facial recognition only as fallback

**Workplace automation (internal social impact):**
- 40% of workforce are checkout operators — full till-less rollout would displace a significant proportion of staff
- Service complaints have *already risen* since self-checkout introduction — suggests customer dissatisfaction with reduced human contact
- Ethical responsibility: phased redundancy with retraining/redeployment programme; union consultation
- Reputational risk if rollout is perceived as exploitative

**Age-restricted goods:**
- Current system requires employee authorisation for alcohol, tobacco etc.
- Automated system must replicate this — requires either facial age estimation (introduces new biometric processing) or mobile app date-of-birth verification linked to customer account
- If system fails to prevent underage sales, there is direct legal liability

**Accessibility:**
- Not all customers can use a mobile app (elderly, visually impaired, those without smartphones or bank accounts)
- Must maintain alternative checkout method — cashless-only system also excludes customers who rely on cash (financial exclusion concern)
- ICO guidance and DWP accessibility standards apply

**Internal impact – organisational:**
- Integration of new system with CheckoutTrack and FoodTrack requires significant change management
- Staff will need retraining for exception handling, fraud detection, customer assistance roles
- Cultural resistance likely; requires leadership support and clear communication (Kotter's 8-step model)

**External impact – reputational:**
- If fraud or misidentification events become public, brand damage can be severe
- Previous trial ended due to fraud concerns — must be addressed explicitly in design
- Community perception of "big brother" surveillance if not carefully communicated

**Professional responsibilities:**
- As an AI Data Specialist, duty to flag ethical risks to the board proactively
- BCS Code of Conduct: public interest, duty to relevant authority, professional competence
- Board has "varying levels of technical knowledge" — must communicate risks in accessible language, not just technical terms

---

## Question 4 – Design, Development & Deployment

### 4a) Approach to design, develop and deploy the solution

**Recommended methodology: CRISP-DM + Data Driven Scrum (DDS)**

**CRISP-DM phases:**
1. **Business Understanding:** Define KPIs (checkout abandonment rate, stock accuracy %, fraud rate, customer satisfaction score). Map to requirements from CI team.
2. **Data Understanding:** Audit existing data quality in MemberTrack, FoodTrack, CheckoutTrack. Identify gaps (non-member data, shelf sensor coverage). Profile external data availability.
3. **Data Preparation:** ETL pipelines (AWS Glue) to clean, standardise, and link data. Feature engineering for demand forecasting (lagged features, weather interaction terms, promotional flags). Anonymisation/pseudonymisation of biometric data.
4. **Modelling:** Train and validate models iteratively (demand forecasting, customer ID, fraud detection). Use stratified k-fold cross-validation; test on held-out store(s) for geographic generalisation.
5. **Evaluation:** Assess against business KPIs and fairness metrics (demographic parity in facial recognition, equal stock availability across branches). Conduct red-team adversarial testing for fraud scenarios.
6. **Deployment:** Phased rollout — pilot in 1–2 stores; monitor; iterate before national rollout.

**Why Data Driven Scrum (DDS) alongside CRISP-DM:**
- CRISP-DM provides the overall process framework; DDS provides sprint-level task management
- Variable-length iterations accommodate uncertainty in data science work (unlike fixed Scrum sprints)
- Kanban board for ongoing monitoring tasks post-deployment

**Phased rollout plan:**
1. Phase 1: Deploy weighted shelves + mobile app payment in pilot stores. No facial recognition. Monitor data quality.
2. Phase 2: Activate demand forecasting models. Begin training customer ID model using consented app users.
3. Phase 3: Full till-less experience with facial recognition as secondary ID method. Monitor for bias, fraud, errors.

---

### 4b) Resources and architecture required

**Team:**
- Data Scientist (model development, evaluation, bias testing)
- Data Engineer (ETL pipelines, lakehouse build)
- MLOps Engineer (SageMaker pipelines, CI/CD, monitoring)
- Software Engineer (mobile app, API integrations)
- DevOps Engineer (infrastructure as code, AWS, containerisation)
- ML Architect (overall design, security, governance)
- Change Management Lead (workforce transition, training)

**Cloud Infrastructure (AWS):**

```
Customer Layer         Store Layer                 Cloud (AWS)
──────────────         ───────────                 ──────────────────────────────
Mobile App       ──►   App Gateway (API GW)   ──►  S3 (raw data lake)
Facial Rec       ──►   Edge processing node   ──►  Kinesis (streaming)
                                                    │
Weighted shelves ──►   IoT Core / MQTT        ──►  Glue (ETL) ──► Athena/Redshift
                                                    │
CCTV cameras     ──►   Rekognition (AWS)      ──►  SageMaker (train/deploy/monitor)
                                                    │
MemberTrack      ──►   RDS / Data connector   ──►  ElastiCache (real-time lookup)
FoodTrack        ──►   RDS / Data connector        │
CheckoutTrack    ──►   Kinesis (CDC)          ──►  QuickSight (dashboards)
```

**Key infrastructure components:**
- **AWS SageMaker:** Training, hyperparameter tuning, model registry, A/B deployment, model monitoring (data drift detection)
- **AWS Kinesis:** Real-time event streaming — replaces 90-minute batch updates
- **AWS Rekognition:** Managed facial analysis service (or custom CNN on SageMaker for more control)
- **ElastiCache (Redis):** Sub-second customer profile lookup at store entry
- **AWS IAM + KMS:** Encryption at rest for biometric data; role-based access control
- **Docker + ECR:** Containerised model serving
- **Terraform / CloudFormation:** Infrastructure as code for reproducible environments

---

### 4c) Justification

**CRISP-DM justification:**
- Industry-standard for ML projects; iterative and non-linear (can return to data prep after modelling)
- Ensures business requirements drive modelling decisions, not the reverse
- Phased rollout reduces risk — fraud concerns from previous trial addressed before national deployment

**AWS cloud justification:**
- Elastic scaling: handles variable store footfall without over-provisioning
- Managed services reduce operational overhead (SageMaker vs. self-hosted ML infrastructure)
- Native integration between services (S3 → Glue → Athena → SageMaker → QuickSight)
- AWS Rekognition and SageMaker have built-in fairness and bias detection tooling

**MLOps justification:**
- Continuous training: demand models must be retrained as buying patterns change (seasonality, economic shifts, new product lines)
- Continuous monitoring: detect model drift before it causes stock-outs or fraud losses
- Reproducible environments: essential for auditability under GDPR (ability to explain automated decisions)
- Rollback capability: if new model version degrades performance, automated rollback to previous version

**Phased deployment justification:**
- Previous mobile-only trial failed due to fraud — iterative approach allows fraud controls to be tested before at-scale deployment
- Minimises workforce disruption — allows staff redeployment/retraining in parallel with rollout
- Builds customer trust gradually rather than forcing immediate behaviour change
- Enables compliance verification (DPIA findings, ICO consultation) before full deployment
