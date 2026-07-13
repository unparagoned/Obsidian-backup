---
tags:
  - EPA
  - AM3
  - technical-test
  - revision
source: BCS L7 AM3 Sample Paper V2.0 – Vault Reference Links
---

# Z Technical Test Sample – Vault Reference Links

> Quick-reference vault links for each question and sub-part of the BCS AM3 sample paper.
> See also: [[Z Technical Test - sample detailed notes]] for full answer bullet points.

---

## Question 1 – Data Extraction, Linkage & Uncertainty
*KSBs: K4, K24, S21*

### 1a) Types of data to use
- [[Data Science Principles Topic 1 - Intro to Data Science =]] — structured vs. unstructured data types
- [[Data Science Principles Topic 5 - Working with big data =]] — big data characteristics (volume, velocity, variety)
- [[Data Science Principles Topic 6 - Storing your data]] — data formats and storage types
- [[Z Learning - Revision Notes]] — structured vs. semi-structured data definitions
- [[Machine Learning using Cloud Computing Introduction to ML on AWS Course]] — AWS data types and services

### 1b) Process for extracting the data
- [[Data Science Principles Topic 1 - Intro to Data Science =]] — data pipelines, ETL
- [[Data Science Principles Topic 5 - Working with big data =]] — batch vs. streaming ingestion
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — DataOps pipelines, CI/CD
- [[Machine Learning using Cloud Computing Introduction to ML on AWS Course]] — AWS Glue, Kinesis, S3

### 1c) How data from multiple systems can be linked
- [[Disruptive Leadership for Sustainable Strategy - Topic 7 - Data strategy]] — data lakehouse, data fabric, Denodo virtualisation
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — data lake vs. lakehouse
- [[Data Science Principles Topic 6 - Storing your data]] — relational linking, keys
- [[Data Science Principles Topic 5 - Working with big data =]] — data architecture patterns
- [[Machine Learning using Cloud Computing Introduction to ML on AWS Course]] — AWS Athena, Glue catalogue

### 1d) Error, bias and uncertainty in data
- [[AI and Data Science Professional Practice Term 2 Theme 6 Error, bias and uncertainty =]] — full taxonomy of error types (random, systematic, data, model) and bias types (historical, sample, aggregation, coverage, selection, availability)
- [[Disruptive Leadership for Sustainable Strategy - Topic 8 - Error, bias, uncertainty]] — data quality standards (consistency, accuracy, uniqueness, validity, timeliness, completeness); fairness testing methods
- [[Data Science Principles Topic 7 - Data Governance]] — data quality and governance

### 1e) Differences in uncertainty before vs. after analysis
- [[AI and Data Science Professional Practice Term 2 Theme 6 Error, bias and uncertainty =]] — aleatoric, epistemic, ontological, structural uncertainty; Monte Carlo dropout; ensemble methods; confidence intervals
- [[Disruptive Leadership for Sustainable Strategy - Topic 8 - Error, bias, uncertainty]] — uncertainty quantification, fairness metrics
- [[Data Science Principles Topic 3 - Statistical investigations ==]] — standard error, confidence intervals
- [[Data Science Principles Topic 4 - Statistical testing =]] — statistical uncertainty and significance

---

## Question 2 – Storage, Analysis & Machine Learning
*KSBs: K2, K20*

### 2a) How data can be stored, analysed and visualised
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — data lake, lakehouse, data fabric; AWS stack
- [[Data Science Principles Topic 6 - Storing your data]] — storage solutions overview
- [[Programming for AI Topic 8 Visualisation]] — visualisation tools and techniques
- [[Machine Learning using Cloud Computing Introduction to ML on AWS Course]] — AWS QuickSight, Athena, S3

### 2b) Storage requirements
- [[Data Science Principles Topic 6 - Storing your data]] — storage types, retrieval, volume considerations
- [[Data Science Principles Topic 5 - Working with big data =]] — scalable storage, HDFS, object storage
- [[Disruptive Leadership for Sustainable Strategy - Topic 7 - Data strategy]] — AWS Redshift, Athena, S3, data governance in storage design
- [[Machine Learning using Cloud Computing Topic 6 Cloud Architecture and Service Platform Design]] — cloud storage architecture

### 2c) Justification for storage and processing technologies
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — why lakehouse over data warehouse; MLOps infrastructure
- [[Disruptive Leadership for Sustainable Strategy - Topic 7 - Data strategy]] — data strategy alignment, Denodo short-term, lakehouse long-term
- [[Machine Learning using Cloud Computing Topic 2]] — cloud computing models (IaaS, PaaS, SaaS), virtualisation, containers
- [[Machine Learning using Cloud Computing Topic 6 Cloud Architecture and Service Platform Design]] — cloud service design principles

### 2d) ML algorithm comparison (2+ algorithms)
**Demand/stock forecasting:**
- [[Programming for AI Topic 6 Time Series Analysis]] — ARIMA, SARIMA, Holt-Winters, ACF/PACF, ADF stationarity test
- [[Programming for AI Topic 7 Time series modelling with machine learning]] — ML approaches to time series
- [[Machine Learning using Cloud Computing Topic 5 CNN RNN LSTM]] — LSTM and RNN for sequence forecasting

**Customer identification (image/facial recognition):**
- [[Machine Learning using Cloud Computing Topic 5 CNN RNN LSTM]] — CNN architecture, ResNet50/VGG16 transfer learning, Grad-CAM
- [[Machine Learning using Cloud Computing Topic 4 Deep Learning Frameworks]] — deep learning frameworks, model training

**Customer clustering / next-basket prediction:**
- [[Programming for AI Topic 5 Unsupervised learning]] — K-means, DBSCAN, Gaussian mixtures, hierarchical clustering
- [[Programming for AI Topic 1 Machine learning and regression]] — supervised ML pipeline, bias-variance tradeoff, regularisation
- [[Programming for AI Topic 2 Sklearn]] — sklearn model selection, cross-validation, hyperparameter tuning
- [[Data Science Principles Topic 8 - Machine learning]] — ML fundamentals, algorithm comparison framework

**General ML evaluation:**
- [[Programming for AI Topic 1 Machine learning and regression]] — F1-score, precision/recall, confusion matrix, ROC-AUC
- [[Programming for AI Topic 2 Sklearn]] — cross-validation, grid search, SMOTE for imbalanced data

---

## Question 3 – Legal, Ethical & Social Impact
*KSBs: K9, K12*

### Legal constraints
- [[AI and Data Science Professional Practice Term 2 Theme 5 Legal aspects =]] — GDPR/DPA 2018 (all 7 principles, legal bases, special category data, Article 22 automated decision-making, DPIA requirement, data subject rights); Equality Act 2010 (9 protected characteristics, indirect discrimination in algorithms); Human Rights Act 1998 (Article 8 privacy, Article 14 non-discrimination); international data transfers
- [[Data Science Principles Topic 7 - Data Governance]] — data governance frameworks, compliance, regulatory requirements
- [[AI and Data Science Professional Practice Term 2 Theme 4 Ethics and AI =]] — AI-specific regulatory context, government AI strategy

### Ethical impact
- [[AI and Data Science Professional Practice Term 2 Theme 4 Ethics and AI =]] — AI ethics frameworks (Asilomar, OECD, government data ethics framework), transparency, accountability
- [[AI and Digital Innovation Topic 8 Ethics and NLP futures -]] — ethical issues in AI deployment, surveillance, trust, privacy (Facebook Beacon case)
- [[Disruptive Leadership for Sustainable Strategy - Topic 8 - Error, bias, uncertainty]] — fairness testing (statistical parity, equalized odds, counterfactual fairness); bias mitigation approaches

### Social impact (workplace automation)
- [[AI and Digital Innovation Topic 8 Ethics and NLP futures -]] — social context of AI, workplace automation, misuse of data
- [[Disruptive Leadership for Sustainable Strategy - Topic 5 - Culture change and leadership]] — workforce change, resistance, redeployment
- [[Disruptive Leadership for Sustainable Strategy - Topic 4 - Change management]] — change management frameworks (Kotter's 8-step model), managing workforce transitions
- [[AI and Data Science Professional Practice Term 1 Theme 1 -]] — professional responsibility, BCS Code of Conduct

### Internal/external business impact
- [[Disruptive Leadership for Sustainable Strategy - Topic 3 - Data Value]] — business value of data, internal impact of data-driven transformation
- [[Disruptive Leadership for Sustainable Strategy - Topic 2 - Organisation analysis]] — stakeholder analysis, PESTLE/SWOT for external factors
- [[Disruptive Leadership for Sustainable Strategy - Topic 1 - Digital Transformation]] — digital transformation impact, legacy system integration

---

## Question 4 – Design, Development & Deployment
*KSBs: K15, K27, S13*

### 4a) Approach to design, develop and deploy
- [[AI and Data Science Professional Practice Term 4 =]] — CRISP-DM, TDSP, SEMMA, KDD; project management methodologies (Agile, Scrum, Kanban, Data Driven Scrum, PRINCE2, Lean, Six Sigma, Waterfall); phased deployment approaches
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — MLOps principles (reproducible, accountable, collaborative, continuous); CI/CD; continuous training and monitoring; DevOps for ML
- [[Machine Learning using Cloud Computing Topic 6 Cloud Architecture and Service Platform Design]] — cloud-native design patterns, service architecture

### 4b) Resources and architecture required
- [[Machine Learning using Cloud Computing Introduction to ML on AWS Course]] — full AWS service catalogue (S3, Glue, Athena, Kinesis, SageMaker, Redshift, RDS, Lambda, IAM, KMS)
- [[Machine Learning using Cloud Computing Topic 2]] — virtualisation, containers (Docker), orchestration (Kubernetes)
- [[Machine Learning using Cloud Computing Topic 6 Cloud Architecture and Service Platform Design]] — architecture diagrams, service platform design
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — team composition (Data Scientist, Data Engineer, MLOps Engineer, Software Engineer, DevOps, ML Architect)
- [[Machine Learning using Cloud Computing Topic 7 Autoencoders]] — anomaly detection architecture (fraud detection use case)

### 4c) Justification for approach
- [[AI and Data Science Professional Practice Term 4 =]] — justification for CRISP-DM vs. alternatives; when to use Agile vs. waterfall
- [[Disruptive Leadership for Sustainable Strategy - Topic 6 - DataOps and MLOps]] — why MLOps matters; Kaizen/continuous improvement rationale; reproducibility and governance requirements
- [[Disruptive Leadership for Sustainable Strategy - Topic 7 - Data strategy]] — strategic alignment of technology choices; build vs. buy decisions
- [[Machine Learning using Cloud Computing Topic 3]] — model evaluation and validation frameworks

---

## Cross-cutting references (relevant to multiple questions)

- [[Z Technical test]] — additional practice questions and worked examples in same format
- [[Z Overall - EPA notes]] — KSB mapping, assessment criteria, how answers are graded
- [[Misc critical thinking]] — structuring arguments for board-level presentation
- [[Misc Planning and writing assesments]] — assessment writing techniques, covering all parts of multi-part questions
