# 1. Introduction and background.

HMRC receives millions of financial documents such as company accounts and tax computations that contain a large amount of information used to provide insight for departmental/government policy and to identify tax risk. They are iXBRL documents; semi-structured (x)HTML documents where key items are tagged with concepts from fixed taxonomies (XBRL International, no date). 

Previous workflows allowed us to reliably extract, structure and analyse fully tagged documents, but a large proportion of figures in some document types are untagged, for various reasons from limitations in accountancy software to people deliberately leaving items they do not want HMRC to review untagged. 

The business priority was to make all the key data items usable analytically promptly after receipt. 

Hubble is a tool I developed that extracts both tagged and untagged items from iXBRL documents and classifies them. I initially worked on Hubble myself, writing the vast majority of the code and all the machine learning, but as the project became bigger and more important to HMRC I arranged for more resource and led a virtual team working on the project.

# 2. Outline of the issue or opportunity and the business problem to be solved.

Initial analysis showed that some document types only have approximately 30% of the figures tagged, so bulk numerical analysis could not use 70% of the figures. Profiles therefore did not have access to billions of figures to properly identify errors and high-risk returns, limiting compliance yield HMRC can bring in by at least tens of millions of pounds (Section 11). We were not always able to provide accurate data or statistics for the department/government to make informed decisions. The previous workflows to extract iXBRL data required complex and long schema updates every year, especially with Oracle's 1,000 column limit being hit, significantly limiting how current the data was.

Initial requirements just included extracting the raw data such as descriptions, but items can be described in lots of different ways with no fixed taxonomy. Analysis showed that some classes had a large variety of descriptions, some with over 23,000 unique descriptions, and subject matter experts (tax professionals) highlighted that many are domain-specific technical terms not all analysts would be familiar with. Existing ad-hoc approaches would take too much subject matter expert time to properly scale.

The 30% of tagged items are tagged by software or accountants so were expected to be reasonable quality training data for supervised learning that could then be applied to the untagged 70%. I recommended creating a supervised multi-class text classification machine learning model to classify the items. This would save significant analyst and subject matter expert time; reduce errors; and improve analysis quality. 

# 3. Methods used and justification

## 3.1. Project management

I selected an agile approach for the overall project (Beck et al., 2001), not strictly adhering to a specific framework, but selecting practices that were appropriate (Atlassian, no date). It was more Kanban focused since the project team was small and the overhead of Scrum would not be appropriate. Competing business demands meant that fixed sprints were not appropriate, but regular Kanban updates ensured progress on this project while other business needs were met. 

## 3.2 CRISP-DM

I used CRISP-DM since it accommodates the cyclical nature of machine learning and provides a clear intuitive structure (Chapman et al., 2000). I worked on the machine learning myself, so CRISP-DM is more appropriate than larger methodologies like TDSP (Microsoft, 2023). Each stage produced documented artefacts, allowing evidence backed decisions in other steps. 

## 3.3 Version control and documentation

While using GitLab to manage projects is not common in HMRC (bespoke spreadsheets are normally used), I decided that the advantages of transparency, auditability and documentation outweighed the costs of learning a new tool. 
- Documentation 
	- Data structures and types. 
	- Oracle tables/credentials setup. 
	- Key decisions and the reason. 
- The issues board worked well as the Kanban board. 
- The epics useful for management and longterm timelines.
- I created templates for issues, tasks and PR, which ensured they were completed to a consistent level by all team members, covering every step required to recreate the issue, expected vs actual, and proposed fixes.
- I encouraged team members to document issues on GitLab, to update project documents, and add comments on why rather than what. 
- Version control, branches and independent review of PR helped ensure changes were of sufficient quality and limit issues. This required training the team to use branches, which I videoed for reference. 

## 3.4 Languages and packages

I initially used R since it was the default language used by analysts at HMRC, so it has better support and maintainability. 
- `aws.s3` AWS S3 access 
- `rvest` and `xml2` for HTML extraction
- `parallel` process hundreds of documents at once
- `dbplyr` allowed Oracle database access using tidyverse syntax analysts are familiar with
- `testthat` for testing

I used Python for machine learning since the machine learning packages are more mature. The `reticulate` package imports Python functions into a R workflow, at the cost of some added setup and coding complexity.
- `mlflow` to track data version, model version, and various metrics
- `scikit-learn` for traditional machine learning models (Pedregosa et al., 2011) 
- `tensorflow`/`keras` to build and train NN
- HuggingFace `transformers` for pre-trained models (Wolf et al., 2020)
- `optuna` for hyperparameters tuning (Akiba et al., 2019)

I used Jupyter notebooks for exploratory work, allowing detailed narrative alongside the code, and SQL for setting up and managing the Oracle database and tables.

## 3.5 Scientific method and testing

I used the scientific method: hypothesis formulation and testing; comparisons against baseline; and statistical testing rather than simply comparing raw values, so the choices were evidence-backed rather than assumed. 

While working with people with more software engineering experience to review the code base, we discussed the scope, coverage, and implementation of unit, integration, and system testing. Constraints included that tests should not contain any customer data, so we used synthetic or anonymised fixtures instead. While we were not using formal test driven development (Beck, 2003), I instructed them to create tests alongside new issues, since it makes it easier to investigate issues and verify fixes. 

# 4. The scope of the project (including key performance indicators).

The scope covered extraction of features such as descriptions, headings, table names, values, structural data (table number, row number, column number) and iXBRL data (concept, dimensional data), machine learning to classify features, and an automated pipeline extracting to Oracle database. Out of scope was any analytical work based on the data, human labelling, and any automated decision making based on the machine learning category. The scope evolved iteratively over time (Section 9).

Working with stakeholders, I established success criteria. 
- Macro-F1 > 0.6, primary performance metric, weighting all classes equally, so common classes do not dominate (Sokolova and Lapalme, 2009).
- Accuracy > 0.7, a secondary metric that is more intuitive to stakeholders and reflects real-world performance.
- Automated extraction coverage > 95%, data automatically extracted and classified
- Timely extraction < 1 week from date of receipt to allow sufficient time to act.
- Interpretability and explainability, we should be able to know why a choice was made and/or provide a human understandable explanation of the factors that drove it.
- Security (dependency risk), should meet HMRC security policy.

Secondary KPIs used were precision; recall; train and inference time; maintainability; reliability; cost control; data protection; AI safeguards; logging; and ability to scale to millions of records quickly.

# 5. Data selection, collection and pre-processing.

## 5.1 Data selection

HMRC's central systems are locked down, without any readily available GPU access, so exploratory work was done using a standalone device with a GPU over 298,461 publicly available iXBRL accounts submitted to Companies House (Companies House, 2026), which avoided using internal customer data. A month of data is sufficiently large to cover account styles, although subject matter experts explained many companies select specific dates like 31 December or 31 March, so it might not be completely representative, but this is unlikely to have any material impact on the analysis. This resulted in 2.8 million lines of data with 956 concepts (labels) (A1 and B15). For the production phase, company accounts and tax computations submitted to HMRC were used. 

The source iXBRL documents are complex with inconsistent HTML structures, iXBRL data and multiple taxonomies (B1, B2, B3). In some situations table names and headings are also important features (B4). I asked subject matter experts about errors where the predicted class was what I expected but the iXBRL concept was slightly different. They explained that some concept names differ between the different taxonomies. A bespoke model for each taxonomy would give the best raw scores, but it would be confusing for analysts, so I recommended training only on the main taxonomy, giving consistent categories.

## 5.2 Exploratory Data Analysis (EDA)

Rank frequency plots of both description and concept had a long tail (B5); with a Pareto chart showing that the 75 most common concepts cover 95% of items (B8); and a distribution closer to a lognormal fit than power-law (B9) (Clauset, Shalizi and Newman, 2009). This motivated using macro-F1 as the primary metric over accuracy. 

The main feature is a description that has various types, from nominal text, dates (temporal), names (nominal) and numeric figures (numeric ratio). Most descriptions are 1-9 words with a mode of 2 (B6 and B7). 

The XBRL concept (label) is a categorical nominal label from a fixed taxonomy, a single CamelCase word that is human readable when splitting into words, with similar concepts normally having similar wording. 

The descriptions and concepts are many-to-many (A2.2.7 and A2.2.8), with cosine similarity analysis identifying situations where some descriptions like "Taxation and social security costs" were used for similar concepts, but other descriptions such as "total" were used for dissimilar concepts. It also highlighted that taxonomy can be specified beyond what could be predicted from the human readable data, which creates a real upper limit on any model. 

Initially I did some classifier-independent analysis, which showed that MPNet (Song et al., 2020) had the best silhouette score (0.467) (Rousseeuw, 1987) suggesting it is able to capture meaning better than plain TF-IDF (0.41) (A2.5 and B16). But this might not carry over to categorisation performance. 

## 5.3 Preprocessing

The text features like description were normalised, lowercasing and replacing special characters with spaces. Not all preprocessing was effective, for example replacing forward slashes with spaces actually reduced performance, so it was dropped (`clean_field`, A2.3). 

I canonicalised the description, so most dates were replaced by a placeholder `hubble_date`, except for 31 March 1982, which subject matter experts explained has a special meaning for tax so that was replaced with `hubble_date_1982_03_31` (`canonicalize_field`, A2.3). 

Similarly company names, individual names, postcodes and numbers were identified using regular expressions and labels, and replaced by placeholders. This helps avoid overfitting and improves generalisation; reduces noise; preserves privacy; and enhances data security through data minimisation. It is more ethical since it treats less common ethnic names the same as more commonly used names. 

Subject matter experts advised that a placeholder by itself would not be enough information to categorise, so I decided to change them to placeholders like `HubbleName` (`target_engineer`, `standardise_names`, A2.3 and B12). So, while we cannot predict the actual concept, knowing it is a name can be useful. 

I implemented data quality controls aligned with HMRC expectations and DAMA UK's quality dimensions (DAMA UK, 2013; Government Data Quality Hub, 2020).
- Completeness improved since untagged data was now extracted. 
- Consistency because the untagged data and tagged data were structured in similar ways on the same tables, with consistent machine learning categories.
- Timeliness. The system architecture and using a long-format structure handles any taxonomy without hitting database column limits, allowing extraction within days of receipt. 
- Validity and accuracy were addressed by removing descriptions shorter than 2 characters, missing, low-quality, or longer than 15 words, which analysis showed were not valid (`filter_data` and `filter_out_labels`, A2.3). 

 This reduced the unique descriptions from 266,178 to 7,795 and labels from 956 to 826 (B15). A limit of 350 examples was added to ensure there were enough samples even with the 1% train population, which reduced labels to 141 while keeping 85% of the rows of data. The effect on the distributions can be seen by comparing the rank frequency, word count and Pareto plots before and after preprocessing (B5-B9 against B10-B14). Along with measures such as restricting access to specific users, this ensured compliance with both HMRC and regulatory requirements, DPIAs and *Data Protection Act 2018*/UK GDPR (Data Protection Act 2018; Regulation (EU) 2016/679; Information Commissioner's Office, no date b). 

Because the data was used over various model architectures and packages, I created stratified splits upfront, 80/10/10, train, test, holdout plus sub splits and square-root weighted splits (`stratified_split`, `sample_split` and `add_sqrt_weight`, A2.6). The holdout ensures the final comparison is over unseen data, so provides a better view of performance against real data.
# 6. Survey of potential alternatives.

This is multi-class text classification with 141 nominal classes and strong class imbalance. I initially used data exploration and theory to limit the solutions to those that would work well with classifying the short domain-specific terminology, reviewed the feasibility within the business context, then evaluated the leading candidates (Sebastiani, 2002).

I considered ways to systemise a rule-based approach, using regular expressions which could have some success but it would use too much subject matter expert time, and would not cover the long tail, so it was not a feasible business solution. 

While the data was tagged, often the specificity was beyond what was required, so unsupervised methods were considered as a way to group similar concepts together. But the cosine similarity analysis highlighted the variety in descriptions for some concepts was too great, so I focused on supervised learning models. 

Traditional machine learning models can perform well with classifying short text, since the feature spaces tend to be linearly separable. Scikit-learn provides various high quality text classification models, such as `SVC`, `LinearSVC`, `SGDClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `MultinomialNB`, `ComplementNB` and `PassiveAggressiveClassifier`. The full search space over these models is at A3.4.1.

There were two main methods used to embed the descriptions, sparse vectorisation (TF, TF-IDF over character and word n-grams) and dense vector embeddings (MPNet, E5) (Sparck Jones, 1972; Cavnar and Trenkle, 1994; Song et al., 2020; Wang et al., 2022). TF-IDF captures domain-specific terminology and phrasing well, and works with a variety of models and is fast. Dense vector embeddings (Reimers and Gurevych, 2019) capture more of the semantic meaning, so should recognise phrases with similar meaning even if the words are different, especially on unseen descriptions (A2.5 and A3.5.2). 

A deep neural network has the advantage of learning patterns beyond a fixed algorithm used in traditional machine learning. Various NN can be used for text classification such as DNN, LSTM, GRU, CNN and BiLSTM, all of which were included in the architecture search (`create_model`, A4.2.2) (Kim, 2014).

Transformer based models are a more advanced architecture with better semantic understanding, especially with pre-training on large amounts of text (Vaswani et al., 2017; Devlin et al., 2019). Various transformer based models were tested: RoBERTa (Liu et al., 2019), SEC-BERT (Loukas et al., 2022), MPNet (Song et al., 2020), and MiniLM (Wang et al., 2020), covering different sizes, architectures, and training data (A5.1 and A5.2). SEC-BERT is a model that was trained on SEC filings (US financial filings), so should have better semantic understanding of accountancy terms.

A frontier LLM, such as ChatGPT, would be expected to have the best semantic understanding, but it would be excessive here since we just have short phrases. At the time it was not possible to send taxpayer data to an external API under the HMRC data security and governance requirements, making this approach unfeasible. 

# 7. Implementation - performance metrics.

## 7.1 Population size validation

Comparing every model and hyperparameter over the full train dataset was not possible, so I initially tested whether smaller populations gave representative results, over 1%, 10% and 100% train populations (A3.3, B17 and B18). The Pearson correlation to the full population for the 1% and 10% samples was 0.971 and 0.998 respectively (B19 and B20). Paired T-tests showed that models that were not significantly worse over the 1% were also not significantly worse at 100%, so I could filter out models and hyperparameters using a smaller sample, and have reliable results from the 10%. 

## 7.2 Traditional machine learning algorithms

To narrow down the initial models and hyperparameters I used HalvingRandomSearchCV over 10,000 candidates, with a DummyClassifier floor to ensure real performance (A3.4.1, A3.4.2, B21 and B37) (Bergstra and Bengio, 2012; Li et al., 2018). Stratified cross validation improved robustness, reduced variance and allowed paired T-tests to indicate which models were not significantly worse at the 5% level, narrowing the field at each stage. Where models could not be separated by macro-F1 I used train times as a secondary measure.

I plotted hyperparameters against scores to help narrow down the ranges to use for subsequent iterations (A3.4.2.1 and A3.5.1.1.1). A 2D graph using colours showed that min_df 1 had clusters with better speed and macro-F1 scores than min_df 2, which was surprising on the speed aspect (B22). 

After fine tuning and training on the full train dataset, LinearSVC beat out the alternatives at a 5% significance level (A3.4.3 and A3.4.4). 

I tried both sparse and dense word embeddings and at the 5% significance level MPNet performed better (macro-F1) than a simple TF-IDF embedding, but it was only by 0.3pp and took 67 times as long (A3.5.2). So I decided to use a simpler TF-IDF word-only embedding, which is faster, easier to maintain and easier to interpret. 

LinearSVC did not fully converge but there was no significant difference in score for max_iter from 5,000 to 20,000, so I selected max_iter of 10,000, since 20,000 was slower for no real gain (A3.6).

The final pipeline used TF-IDF (1-3 word n-grams, min_df 1, norm l2) with LinearSVC (penalty l1, C 2.8, loss squared_hinge, dual False, class_weight balanced, max_iter 10,000) (A3.7). There was a range of similar performance for C, but a lower C was selected to prevent overfitting and enhance model generalisability. 

## 7.3 Conventional and Transformer based Neural Networks 

I used Optuna to compare and find the optimal architecture/model and hyperparameters such as activation, learning rates, dropout rates, embedding dimensions and number of layers (A4.3 and B37). CNN was the best performing conventional neural network, and was then tuned further (A4.4; training curves at B26 and B27). I used dropout hyperparameters as a regularisation technique, limiting overfitting and improving generalisability (Srivastava et al., 2014). SEC-BERT was the best performing transformer based model, with a macro-F1 of 0.754 against 0.743 for RoBERTa, 0.714 for MPNet and 0.681 for MiniLM, demonstrating that domain-based pre-training was beneficial (A5.2, B29 and B30). 

## 7.4 Class imbalance

To deal with the class imbalance (He and Garcia, 2009) and reduce systematic bias towards majority classes, I explored various methods such as: 
- Weighting models worked well with LinearSVC but reduced performance on the NN models (A4.4.1.1 and A5.3.7). 
- Square-root weighted training gave good macro-F1 but sometimes with very small decreases in accuracy, e.g. 1.3pp increase vs 0.0573pp decrease (A3.7.7).
- Random oversampling actually reduced performance on the transformer based models (A5.3.9). 

A smaller modified training dataset improved neural net performance whereas LinearSVC performed best on the full train dataset with a weighted model. 

## 7.5 Model selection

To compare the model architectures I used a decision matrix (A6 and B37), covering various objective and subjective measures.

- Accuracy
- Macro-F1
- Macro-recall
- Macro-precision
- Weighted-F1
- Train time
- Inference time
- Model size
- Interpretability & explainability
- Deployment simplicity
- Maintenance burden
- Domain fit
- Model life cycle
- Dependency risk
- Cost

Each measure was weighted, with a confidence factor of 0.35 for overlapping confidence intervals (B33). A rubric set the standard for the subjective scores with an accompanying narrative (A6.2.5 and B31). 

For fair comparison, and because of memory/time constraints, all models were trained on 10% square-root weighted data and evaluated on the same subset of the holdout data. The 95% confidence intervals were created using the bootstrap method rather than cross validation due to complexity and computational cost (Kohavi, 1995) (B32). 

While SEC-BERT had the best macro-F1 score I chose LinearSVC, trading marginal performance (2.3pp) for a solution that is simpler to maintain, is more explainable (feature coefficients), runs 220x faster, deploys on existing CPU-based infrastructure, scales cost effectively, and relies on well-established, regularly updated packages (B32, B33 and B34).

## 7.6 Production system and governance

Scaling needed additional infrastructure, so I worked with DevOps to set up on-demand-compute, which starts up an EC2 instance running POSIT just for a job and shuts it down when finished, much more cost effective than a large machine running all the time. EC2 instances without a GPU were not only cheaper but also more available. 

The overall system (B35 and B36): 
- Raw iXBRL documents retrieved from AWS S3
- Extracted using `rvest`/`xml2` 
- Structured into long format using R 
- Features are pre-processed using Python
- Embedded and classified by scikit-learn's `Pipeline` with `TfidfVectorizer` and `LinearSVC`
- Output saved to an Oracle database using `dbplyr` 
 
I would work collaboratively with teammates on non-machine learning tasks, partially to share knowledge and up-skill them.

The pipeline now runs automatically daily, so that analysts do not need to run it themselves and just need to query the database. 

Governance is built into the design. Documentation and guidance explain whether an item was tagged by the customer or is a machine learning prediction. Analysts know that the machine learning category can be wrong, that it should never be used in automated decisions, and that there should always be a human in the loop (Information Commissioner's Office, no date a). Per-class performance is available in a dashboard so analysts can check before anything is relied upon. 

# 8. Results.

LinearSVC trained on the full dataset and tested over the full holdout has an accuracy of 0.975 (CI 0.975-0.976) and macro-F1 of 0.785 (CI 0.780-0.788), beating KPIs of 0.7 and 0.6 respectively and a stratified DummyClassifier baseline of 0.007 (A3.7.3 and B38). The production system also meets the remaining KPIs: extracting over 99% of records automatically against a target of 95%; within 3 days against a target of one week; and an interpretable and explainable model. 

Residual analysis identified which classes performed poorly and summaries were created for analysts (A3.10). Per-class results were varied, with a median per-class F1 of 0.966, but 27 of the 141 modelled concepts scored below 0.5 and eight scored zero, pulling down the macro-F1 score. By volume the exposure is smaller, with 94% of holdout records falling in concepts scoring above 0.9 (B40). When I worked with analysts I focused on outcomes, showing confusion matrices for good and poor quality classes and looking at examples (B24), and the dashboard let them check a concept's reliability before using it.

Subject matter experts explained that in some cases there is not enough information in the document to predict the specific concept. For example, the description "cash at bank and in hand" is associated with similar concepts CashBankOnHand 5,670 times and CashOnHand 21 times, so the minority tagging would show as errors (B24).

Sensitivity analysis and model robustness were tested over various categories, abbreviations, adversarial (phrased to be misleading), command (attempts to inject LLM instructions), contextual (semantically the same), long context, OCR issues, synonyms, typos, unicode and variations (Ribeiro et al., 2020) (A3.8, A5.3.5 and B25). Overall LinearSVC outperformed SEC-BERT in robustness testing, scoring equal or better in nine of the eleven categories, which was surprising since the domain-specific training and better theoretical semantic understanding should have favoured SEC-BERT. Also the areas where LinearSVC did worse like typos and variations would be rare over real data, since accountancy documents are primarily generated by software. 

Bias was investigated both against size of companies and software provider (Mehrabi et al., 2021). Large companies had a macro-F1 score of 0.934 vs 0.790 for small companies, which could be explained by smaller companies using cheaper software, with some software providers having a score of 0.184 vs 0.913. Residual analysis showed that while there were some real misclassifications, often they were between very similar classes without enough information to differentiate between them. This suggests that the specificity of the evaluation was too fine-grained. Different software providers do tag things differently, but labels are a training proxy, so such issues would not apply to untagged items or human labels. But it is still a real issue, worth working with providers to make tagging more consistent, since tagged concepts would be considered more reliable than a machine learning category. 

# 9. Discussion and conclusions/recommendations.

An Agile approach worked well with CRISP-DM. Iterating delivered usable products at each stage: basic raw data on file, iXBRL information, machine learning categories, improved architectures and database, with each step evaluated for feasibility, benefits, risk, proving the approach and providing business value. Regular meetings and a workshop helped validate business understanding and get feedback such as the issues dealing with raw descriptions. The iterative approach improved macro-F1 from under 0.50 to 0.785 on the evaluation dataset and adding additional features: table name and heading, improving macro-F1 by 9.8pp on the production dataset. 

While using metrics like macro-F1 works well for comparing similar classes of models, it is important to consider all the business requirements using methods like decision matrices. But some factors like interpretability and security are core requirements that could override a raw score. 

The coefficients of LinearSVC provide real interpretability that could be explained to technical audiences, which was not possible with neural networks (A3.9.1) (Rudin, 2019). But tools like LIME (Ribeiro, Singh and Guestrin, 2016) and SHAP (Lundberg and Lee, 2017) do provide explainability which does partially mitigate such risks with models that are not interpretable (A3.9.2, A3.9.3, B23, B28 and B39). 

Since SEC-BERT is not created by a well-established provider, security aspects may prevent use even if it won the decision matrix. If it was materially superior then we might need to train our own BERT based model. 

TF-IDF creates high dimensional sparse matrices, that capture the short domain-specific descriptions, that work well with LinearSVC, especially with the sparse coefficients from L1 regularisation and dual false (Joachims, 1998). This allowed me to develop the model using existing infrastructure without impacting other users of the platform. 

I worked autonomously where deep focus was required, such as on the coding and modelling, and I would work collaboratively with tax professionals for taxonomy/accountancy advice.

My communication approach evolved based on how stakeholders reacted to early explanations, and methods were tailored for the audience, such as PowerPoint presentations, markdown guides, meetings and workshops. Initial technical descriptions were too detailed for some audiences, so I shifted towards using Problem-Solution-Outcome for non-technical audiences and increased visual and example-based explanations for others. I used a graphed SVM 2D decision boundary; confusion matrices with examples of errors for residual analysis; and a simple example to illustrate the difference between weighted and macro scores rather than relying on formulas. With DevOps I focused on benchmarks, memory usage and future requirements, cost/benefit of specific EC2 instances. 

Repeated questions led me to create an interactive dashboard where users can test the model and see per-concept performance, including where it would be reliable and where it would perform poorly. The dashboard showed the top-5, but some of those were very poor matches, confusing users, so I changed the dashboard to just show the plausible matches. As users' understanding increased so did their use. 

With managers I focused on business level aspects, benefits, outcomes, funding, blockers, and timeframes. In discussions and memos I did cost-benefit analysis covering better timeliness and data coverage, resulting in additional people on the development and funding for infrastructure.  

The project readme utilises markdown to provide clear headings, instructions, links, and code blocks, letting multiple teams use the tool themselves. When users have issues or questions, I updated the relevant documents to be clearer or cover such issues. Further developments resulted in a centralised approach extracting the full population to an Oracle database, so analysts just need to do a database query.

I discovered Optuna while working with neural networks, and fthe built-in visualisations and  hyperparameters search could have replaced a lot of the manual work and code I previously did. So I plan to do wider research on existing packages and functions to solve a problem rather than just jumping straight into coding my own solution.

Recommendations:
- Increase coverage to 100%, to be able to replace existing systems.
- Enhance system robustness, tests moved to a CI pipeline, more reliable scheduling system, move to a fully supported Oracle server.
- Data contracts for data sources and downstream.
- Monitor drift (Gama et al., 2014).
	- Monitoring drift of inputs, check if there are new taxonomies. 
	- Drift on outputs to be detected for both accuracy and macro-F1, using a 2pp drop and for there to be non-overlapping confidence intervals, over two consecutive days. 
	- Automated drift can only check tagged items, there should also be occasional manual check of untagged items. 
- Standard structure for machine learning communications: headline figures first, illustrations and examples, and an appendix with the technical details.
- Human evaluation of tagging.
- Establish the performance ceiling beforehand so time and effort can be budgeted; the most common concept per description gives a hard upper bound, since the same description can be associated with different concepts. 
- Consider a simplified taxonomy, grouping together similar concepts would be more user friendly for analysts.
- Record MLflow version on ouputs, so predictions can be traced back to the exact model and training dataset.

# 10. Summary of findings.

I developed a supervised, multi-class classifier to categorise untagged items in financial iXBRL documents. A variety of models were evaluated using macro-F1, with the final candidate models, LinearSVC, CNN and SEC-BERT, being compared using a decision matrix. While SEC-BERT led on macro-F1 it was rejected because it was not as good on interpretability, deployment simplicity and dependency risk. 

The chosen pipeline was TF-IDF 1-3 word n-gram with LinearSVC.

The biggest factors were actually pre-processing, which increased macro-F1 by 20pp, and adding additional features by 9.8pp. Going forwards I expect the main improvements would come from pre-processing or from simplifying the taxonomy used rather than changing the architectures or tweaking the hyperparameters. 

# 11. Implications.

Hubble helped us meet our quality standards. The machine learning categories reduced the manual regex-style work previously done, improved consistency and reliability of the analysis. 

Hubble is widely used by multiple teams, with data being integrated into various dashboards.

With untagged data now being extracted and classified, we have been able to perform data analysis previously not possible, which has been fed into improving departmental/government policy. 

The data has been used to better identify companies to investigate, and the estimated benefits stored on a spreadsheet are in the tens of millions, but the spreadsheet is incomplete so I arranged for the central management system to have built-in functionality to monitor benefits.

# 12. Caveats and limitations.

The model and evaluation were all based on tagged data, but the main use case is on untagged data, and there is a risk that the untagged data could be different from the tagged data. For example, an item might have been left untagged since there may not be a relevant taxonomy concept. Ideally untagged data would be human tagged, but it would require too much subject matter expert time, so instead experts will feed into a manual evaluation stage. Further evaluation between tagged and untagged descriptions would be useful.

Traditional machine learning model comparisons used 5-fold cross validation, which was a reasonable choice for the initial filtering due to computational cost, but overlapping training data sets can understate variance. Later stages should have used something stronger like 5x2 CV, which uses disjoint training sets within each replication, which limits Type I error (Dietterich, 1998).

LinearSVC has not scaled well on larger datasets. But going from the 10% train data set to 100% saw only a 0.3pp increase in macro-F1, so much larger datasets are unlikely to increase performance much (A3.7.7). 

Increasing data set size while keeping the 350 example threshold, results in more labels, so model performance actually decreased with more data. Also different document types/sources had very different distributions in labels, also resulting in varied performance, making comparison difficult across different populations, document types and sources. So performance varied when implementing on HMRC data.{which was?}

The integration of R and Python, while working well, does add setup  and coding complexity and other teams have had issues with the `reticulate` package. With the long term move to a lakehouse, higher Python use, greater Python ETL support porting should be considered. 



