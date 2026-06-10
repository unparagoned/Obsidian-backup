# Z Technical Test - notes

Source notes:
- [[Z Overall - st0763_artificial-intelligence-ai-data-specialist_l7_ap-for-publication_qm]]
- [[Z Technical test]]
- [[Z Technical Test - AM3 BCS_L7_Exam_Prep_Guide]]
- [[Z Technical Test - BCS L7 AI Data Specialist IfATE V1.0 AM3 Technical Test Sample Paper V2.0]]
- [[Z Technical Test - sample detailed notes]]
- [[Z Technical Test - sample draft answers]]
- [[Z Technical Test - sample links]]

## Assessment facts

Assessment method 3 is the technical test.

- 4 long-response scenario-based questions.
- 100 minutes maximum.
- Closed book.
- Calculator, pen, and notepaper are permitted.
- Questions test technical knowledge and skills that cannot be fully tested by the project report or professional discussion.
- To pass, all AM3 pass criteria must be met.
- To get distinction, all pass criteria and all AM3 distinction criteria must be met.

AM3 KSBs:

- K2: Modern data storage solutions, processing technologies, and machine learning methods to maximise organisational impact.
- K4: Extracting data from systems and linking multiple systems to meet business objectives.
- K9: Legal, ethical, professional, and regulatory frameworks for data products/services.
- K12: Wider social context of AI/data science, including workplace automation and misuse of data.
- K15: Engineering principles for design, development, and deployment of new data products.
- K20: Collecting, storing, analysing, and visualising data.
- K24: Sources of error and bias affected by dataset and methodology choice.
- K27: Engineering principles for new instruments and applications for data collection.
- S13: Identifying resources and architectures for a workplace computational problem.
- S21: Identifying and quantifying uncertainty in data collection, experiments, and analyses.

## Answer framework: DELTA

Use DELTA for every substantial answer.

- Define: give the technical definition first.
- Evidence: apply it to the case study with named systems, data sources, and stakeholders.
- Link: connect the technical choice to business impact.
- Trade-offs: compare at least two approaches and justify the chosen option.
- Acknowledge: state risks, assumptions, uncertainty, limitations, and mitigations.

Avoid generic answers. Use the scenario names: MemberTrack, FoodTrack, CheckoutTrack, weighted shelves, CCTV, mobile app, facial recognition, ONS, MetOffice, Consumer Confidence Index, and till-less checkout.

## Distinction strategy

Distinction answers need comparison and judgement, not just description.

- Compare storage options, processing technologies, and ML methods, then conclude which is best and why.
- Explain differences between uncertainty in data collection and uncertainty after analysis.
- Assess the business impact of legal, ethical, professional, and regulatory requirements.
- Justify methodology and architecture with risks, benefits, and alternatives.

Useful phrase:

"The technically strongest option is not automatically the best business option. I would select the option that balances accuracy, latency, explainability, cost, compliance, integration risk, and operational maintainability."

## Time plan

For 100 minutes:

- 5 to 10 minutes: read scenario, mark systems, requirements, constraints, and risks.
- 2 to 3 minutes per question: outline answer with DELTA headings.
- Around 20 minutes per question: write complete answers.
- Last 5 minutes: add missing trade-offs, uncertainty, and business impact.

If time is tight, prioritise all four questions over perfect detail in one answer.

## Question 1: Data extraction, linkage, error, bias, uncertainty

KSBs: K4, K24, S21.

### Types of data

Internal structured data:

- MemberTrack: member identity, personal details, membership status, payment links, offers, purchase history.
- FoodTrack: product, store, stock levels, trigger levels, expiry dates, distribution centre stock.
- CheckoutTrack: transaction records, items, prices, discounts, payment method, membership status.

New operational data:

- Weighted shelf sensor data: item removal/replacement events, weight readings, timestamp, shelf ID.
- CCTV/camera data: images/video for customer identification, movement, basket association, store flow.
- Mobile app data: customer ID, payment token, app check-in, location/event data, basket/receipt.
- Biometric data: facial or fingerprint recognition data. Treat as special category data.

External data:

- MetOffice: weather by geography/time, useful for demand forecasting and delivery planning.
- ONS: local demographics, useful for store-level product ranges and customer/member targeting.
- Consumer Confidence Index: macroeconomic signal for spending, budgeting, and demand assumptions.

Data type language:

- Structured: relational records, transactions, stock tables.
- Semi-structured: JSON app events, API responses, sensor logs.
- Unstructured: CCTV video, images, free-text complaints.
- Time-series: shelf events, stock updates, footfall.
- Personal/special category: member identity, payment data, biometric data.

### Extraction process

For internal systems:

- Use SQL/JDBC or APIs to extract from MemberTrack, FoodTrack, and CheckoutTrack.
- Use batch ETL for historical training data.
- Use streaming/event ingestion for till-less checkout because stock and payment decisions need near real-time updates.
- Keep raw data immutable, then create processed and curated layers.

For sensors:

- Weighted shelves publish events through IoT gateway, MQTT/REST, or message broker.
- Include device ID, shelf ID, product ID, timestamp, measured weight change, and confidence score.
- Cameras should use edge processing where possible, sending metadata or embeddings rather than raw video to reduce bandwidth and privacy risk.

For external APIs:

- Pull MetOffice frequently enough for operational planning.
- Pull ONS periodically because demographics change slowly.
- Pull CCI monthly or on publication schedule.

Controls:

- Validate schema, ranges, missingness, duplicates, timestamps, device IDs, and referential integrity.
- Log lineage from source to curated tables.
- Apply data minimisation, access controls, encryption, retention limits, and audit logs.

### Linking data

Key fields:

- CustomerID/member ID links MemberTrack, CheckoutTrack, app sessions, payment tokens, and recommendations.
- ProductID/barcode/SKU links CheckoutTrack, FoodTrack, shelf sensors, and stock forecasting.
- StoreID plus timestamp links transactions, shelf events, weather, demographics, and footfall.
- SessionID or visitID links customer entry, items removed, basket, and payment event.

Architecture:

- Short-term: data virtualisation/federated queries can reduce disruption while existing systems remain in place.
- Long-term: data lakehouse with raw, processed, and curated zones supports structured, semi-structured, and unstructured data.
- Use a data catalogue and metadata layer for schema discovery and lineage.
- Use event streaming for near real-time stock and checkout.

Business link:

- Accurate linkage enables the till-less store to know who entered, what they removed, how to charge them, and how to update stock.
- Poor linkage creates fraud risk, poor customer experience, stock inaccuracy, and regulatory risk.

### Error

Examples:

- FoodTrack updates only every 90 minutes; stock data may be stale.
- Only 15% of deliveries are manually checked, so delivery errors may remain hidden.
- Shelf sensors may misread if two customers interact with the same shelf or if calibration drifts.
- Camera systems can misidentify customers due to occlusion, lighting, masks, hats, or camera angles.
- Loose produce manually entered through menus can be wrongly classified.
- External API outages or stale weather/demographic data can degrade forecasts.
- Timestamp mismatch across systems can link the wrong customer, product, or event.

Mitigations:

- Sensor calibration, reconciliation, audit sampling, anomaly detection, confidence thresholds, manual review, and fallback checkout path.
- Data validation, monitoring, lineage, and data quality dashboards.

### Bias

Examples:

- MemberTrack covers members more than non-members, so demand predictions may overrepresent loyal customers.
- Historical promotions and stockouts distort purchase history.
- Facial recognition may perform worse across protected characteristics or under different lighting/occlusion conditions.
- Store-level demographic data may stereotype areas or fail to capture individuals.
- Training data from high-footfall periods may not represent quiet periods.
- Algorithms optimised for shrinkage/fraud reduction may create unfair suspicion patterns.

Mitigations:

- Evaluate performance by relevant groups and stores.
- Use fairness metrics such as demographic parity, equal opportunity, equalised odds, and false positive/false negative rates.
- Provide non-biometric alternatives.
- Keep human escalation routes.
- Monitor drift and complaints after deployment.

### Uncertainty

Key definitions:

- Aleatoric uncertainty: irreducible randomness, such as spontaneous customer behaviour or noisy sensor readings.
- Epistemic uncertainty: reducible uncertainty from limited data, poor model knowledge, or insufficient examples.
- Measurement uncertainty: sensor precision, camera quality, timestamp accuracy.
- Sampling uncertainty: whether collected data represents all customers, products, stores, and time periods.
- Model uncertainty: uncertainty due to algorithm choice, parameter estimation, or extrapolation.
- Structural uncertainty: uncertainty from simplifications in the model, such as assuming past demand patterns will continue.

Before analysis:

- Focus is on data collection quality: missingness, measurement error, sampling bias, timeliness, coverage, and representativeness.
- Quantify using data quality percentages, error rates, confidence intervals, standard error, missingness rates, and sensor calibration results.

After analysis:

- Focus is on whether model outputs are trustworthy.
- Quantify using prediction intervals, calibrated probabilities, confidence intervals, model ensembles, Monte Carlo dropout, cross-validation variance, and drift metrics.

Good distinction point:

"Analysis does not automatically reduce uncertainty. It can reveal uncertainty that was hidden, and a model can add new uncertainty through assumptions, feature choices, and extrapolation outside the training distribution."

## Question 2: Storage, analysis, visualisation, ML comparison

KSBs: K2, K20.

### Storage

Recommended pattern: cloud lakehouse.

- Raw layer: store source extracts/events in original form.
- Processed layer: cleaned/standardised data in Parquet/Delta/Iceberg.
- Curated layer: business-ready feature tables, model inputs, BI tables.
- Warehouse/serving layer: Redshift/Snowflake/BigQuery/Athena/SQL warehouse for dashboards and reporting.
- Low-latency layer: Redis/ElastiCache or operational database for live customer/session lookup.
- Object storage: S3 or equivalent for scalable storage of mixed formats.
- Time-series/event store: useful for shelf sensors and live stock events.

Storage requirements:

- CCTV/video: very high volume, high velocity, short raw retention, strong access control.
- Biometric embeddings: sensitive, encrypted, tightly governed, short retention where possible.
- Transactions: high volume, structured, long retention for audit/regulatory purposes.
- Shelf sensors: high velocity, medium volume, time-series.
- Member data: personal data, structured, strict access and purpose control.
- External data: lower volume, periodic refresh, lineage needed.

### Processing

- Batch ETL: historical data, reporting, retraining datasets.
- Streaming: till-less checkout events, stock updates, fraud/anomaly alerts.
- Feature engineering: basket history, store/time features, weather, promotions, demographics.
- MLOps: model registry, training pipelines, evaluation gates, deployment pipelines, monitoring.
- Edge processing: computer vision metadata extraction near cameras to reduce latency/privacy risk.

### Analysis

- Descriptive: sales trends, stock movement, footfall, complaints, shrinkage.
- Diagnostic: why stockouts happen, where misidentification occurs, why complaints rose.
- Predictive: demand forecasting, next-basket prediction, replenishment, customer identity matching.
- Prescriptive: reorder quantities, store-level product range changes, staffing changes.

### Visualisation

- Board dashboards: business KPIs, implementation risk, service impact, fraud/shrinkage, cost.
- Store dashboards: live stock, replenishment alerts, sensor health, customer flow.
- Model dashboards: precision, recall, F1, false accept/reject, calibration, drift, fairness metrics.
- Operational visualisations: heatmaps, time-series, confusion matrices, anomaly charts.

### ML algorithm comparisons

Customer identification:

- Facial recognition CNN/transfer learning: fast and convenient but high privacy, bias, and consent risk.
- Mobile app QR/NFC/check-in: more transparent and consent-based, but excludes customers without smartphones and may add friction.
- Fingerprint recognition: strong identity signal but highly intrusive and special category data.

Likely recommendation:

- Prefer mobile app/payment-token check-in as primary ID, with optional biometric only where explicit consent and alternative access routes exist.

Demand forecasting:

- ARIMA/SARIMA: interpretable and good for stable univariate time series; weaker with many external features.
- Gradient boosting/XGBoost: handles tabular features, non-linear interactions, promotions, weather, store variables; reasonably explainable with SHAP.
- LSTM/deep learning: useful for complex sequences at scale but more data-hungry and less interpretable.

Likely recommendation:

- Use gradient boosting or hybrid models for store/SKU demand forecasting because they handle mixed internal/external features and offer better explainability than LSTM.

Basket/personalisation:

- Collaborative filtering: good for recommendation from purchase history but poor cold start.
- Association rules: explainable market-basket analysis but less personalised.
- XGBoost/ranking model: handles customer/product/store/time features; better cold-start with demographics/context.

Stock/event anomaly detection:

- Rule thresholds: simple and explainable but brittle.
- Isolation forest/autoencoder: better anomaly detection but needs monitoring and explanation.

## Question 3: Legal, ethical, social, professional impact

KSBs: K9, K12.

### Legal constraints

UK GDPR / Data Protection Act 2018:

- Personal data: member details, payments, app identifiers, CCTV.
- Special category data: biometrics used for identification.
- Lawful basis required for processing.
- Explicit consent likely required for biometric identification.
- Data minimisation: collect only what is needed.
- Purpose limitation: do not reuse MemberTrack data for incompatible surveillance without lawful basis.
- Storage limitation: define retention periods.
- Accuracy: avoid wrongly charging or identifying customers.
- Security: encryption, IAM, audit logs, secure payment handling.
- DPIA required for high-risk processing such as biometric surveillance at scale.
- Automated decision-making rights may apply if customers are charged or blocked by automated systems.

Equality Act 2010:

- Avoid indirect discrimination if identification or access performs worse for protected groups.
- Provide accessible alternatives for disabled users and those unable/unwilling to use biometrics or smartphones.

Human Rights Act:

- Privacy and proportionality matter, especially around CCTV and tracking.

PCI DSS:

- Payment tokenisation and card processing must be handled securely.

### Ethical constraints

- Transparency: clear signage and customer explanations.
- Consent: meaningful choice, especially for biometrics.
- Fairness: evaluate error rates by relevant groups and stores.
- Accountability: human review for disputes and failed identification.
- Explainability: customers and staff need understandable reasons for actions.
- Data minimisation: do not store raw video or biometrics longer than necessary.
- Proportionality: fraud reduction and convenience must be balanced against surveillance risk.

### Social impact

- 40% of workforce are checkout operators or related roles, so automation has substantial workforce impact.
- Benefits may include reduced queues, improved stock availability, and redeployment to customer support.
- Risks include job displacement, deskilling, customer exclusion, trust erosion, and increased complaints.
- Service complaints have already risen after self-checkout/self-scan, so further automation could worsen customer experience unless designed carefully.

### Professional impact

- Follow BCS-style professional responsibilities: public interest, integrity, competence, duty to relevant authority.
- Be honest about limitations, failure modes, and uncertainty.
- Do not overclaim accuracy.
- Ensure governance, documentation, and incident handling.

### Business impact of compliance

Compliance may increase cost and implementation time through DPIA, accessibility design, testing, security controls, retention systems, and staff training.

Non-compliance risks are larger: fines, legal challenge, reputational damage, loss of customer trust, exclusion of customer groups, incorrect charging, and failed rollout.

Distinction phrasing:

"The business case should include compliance as a delivery requirement, not as an optional constraint. A till-less store that is accurate but unlawful, inaccessible, or distrusted is not a successful business solution."

## Question 4: Design, development, deployment, resources, architecture

KSBs: K15, K27, S13.

### Approach

Use CRISP-DM or a hybrid CRISP-DM plus Agile/MLOps approach.

1. Business understanding: define till-less objectives, KPIs, risk appetite, customer journeys, and constraints.
2. Data understanding: profile MemberTrack, FoodTrack, CheckoutTrack, CCTV, shelves, app, and external data.
3. Data preparation: clean, link, validate, create features, and handle PII/biometrics.
4. Modelling: compare candidate approaches for ID, stock forecasting, recommendations, and anomaly detection.
5. Evaluation: accuracy, latency, false accept/reject, stock error, fairness, usability, and business impact.
6. Deployment: phased pilot, shadow mode, limited stores, human fallback, then scale.
7. Monitoring: drift, data quality, model performance, fairness, customer complaints, stock variance, payment disputes.

### Engineering principles

- Modular architecture with clear interfaces.
- APIs between systems.
- Event-driven design for real-time checkout and stock updates.
- Security by design.
- Privacy by design.
- Observability: logs, metrics, traces, alerts.
- Reproducibility: version data, code, models, and configurations.
- CI/CD for software and ML pipelines.
- Rollback and fallback processes.
- Human-in-the-loop for exceptions.

### Resources

People:

- Product owner/business sponsor.
- Data scientist/ML engineer.
- Data engineer.
- Software engineer.
- MLOps/DevOps engineer.
- Cloud/infrastructure architect.
- Security specialist.
- Data protection officer/legal advisor.
- UX/accessibility specialist.
- Store operations representatives.
- Change manager/HR representative.

Technology:

- Cloud storage/lakehouse.
- Stream processing/message broker.
- IoT gateway for shelves.
- Camera/edge processing.
- Operational database/cache.
- ML platform/model registry.
- BI dashboards.
- Monitoring/alerting.
- IAM, KMS/encryption, audit logging.
- Test environments and synthetic data.

### Architecture sketch

- Store sensors/app/cameras produce events.
- Edge processing extracts low-latency signals.
- Events flow into streaming platform.
- Operational service links customer, product, store, timestamp, and payment token.
- Stock service updates inventory and triggers replenishment.
- Data lakehouse stores raw/processed/curated data.
- ML training pipelines use curated historical data.
- Model serving provides identity confidence, basket prediction, demand forecasts, and anomaly flags.
- Dashboards expose operational and governance metrics.

### Justification

- Agile/CRISP-DM supports iterative delivery because requirements, data quality, and customer behaviour are uncertain.
- Pilot deployment reduces risk before nationwide rollout.
- Event-driven architecture supports near real-time stock and checkout.
- Lakehouse supports multiple data formats and future analytics.
- Edge processing reduces latency and privacy risk.
- MLOps is required because models drift and must be monitored/retrained.

Alternative:

- Big-bang waterfall rollout is risky because identity accuracy, customer acceptance, and operational impact are uncertain.
- Pure batch architecture is insufficient because till-less checkout needs real-time linkage and stock/payment events.

## Quick revision checklist

- Always name at least one alternative and reject it with a reason.
- Always include legal/ethical/professional constraints when biometrics or customer data appear.
- Always quantify or describe uncertainty.
- Always connect architecture choices to business outcomes.
- Always mention monitoring, retraining, fallback, and human review.
- Avoid saying "AI will solve it"; say what data, model, system, and control makes it work.
