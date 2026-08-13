
# 1. Introduction and background.

HMRC receives millions of financial documents such as company accounts and tax computations that contain a large amount of information used to provide insight for operational/government policy and to identify tax risk. They are iXBRL documents; semi-structured (x)HTML documents where key items are tagged with concepts from fixed taxonomies. 

For fully tagged documents, previous workflows allowed us to reliably extract, structure and analyse the data in those documents. Initial analysis showed that some document types only have approximately 30% of the figures tagged, which means that previous workflows could not utilise 70% of the figures. There are various reasons for this, ranging from limitations in software used to create the documents to people deliberately leaving items they don't want HMRC to review untagged. 

The previous workflows to extract iXBRL data, require complex and long schema updates to processes new taxonomies every year. The wide database format was also hitting the column limits of the Oracle database complicating things further. It can take up to 9 months for the updates, but HMRC only have 12 months to open an enquiry, leaving little time for profiling and opening an enquiry in time. {move this to the problem bit}

Hubble is a tool I developed that extracts both tagged and untagged items; and uses supervised multi-class text classification to categorise the untagged items. The system scales with workload and uses a long format for the Oracle database, allowing it to deal with any taxonomy, resulting in data being ingested within days of receipt. 

I initially worked on Hubble myself, writing the vast majority of the code and doing all the ML elements myself, but as the project became bigger and more important to HMRC I arranged for more resource and lead a virtual team working on the project.

{Maybe some of this should be moved to impact}

# 2. Outline of the issue or opportunity and the business problem to be solved.

The business problem was that a significant amount of data submitted to HMRC couldn't be used in bulk analysis, since previous workflows didn't extract untagged data. So bulk numerical analysis was restricted the tagged figures, which could be missing 70% of the numerical data in those documents. This means profiles using such data don't have the data to properly identify high tax risk returns limiting compliance yield HMRC can bring in. Also we were unable to provide accurate data or statistics for the department/government to make informed decisions. This combined with the 9 month taxonomy lag was creating serious operational issues. 

The initial requirements just included extracting the raw data such as descriptions, but items can be described in lots of different ways with no fixed taxonomy. Analysis of the descriptions showed that some classes had a large variety of descriptions, some with over 23,000 unique descriptions, and SME highlighted that many are domain-specific technical terms that not all analysts would be familiar with. Graphs and stats showed a very long tail, beyond anything that could practically be investigated in depth. 

Initial usage required lots of complex regular expressions and working with SME due to the domain-specific terminology, which was error prone, incomplete and time-consuming. I considered ways to systemise a rule-based system which would help with some of the issues but it would be too resource intensive, especially of the SME time, and wouldn't cover the long tail. It wasn't a feasible business solution, so I investigated alternatives. 

While 70% of items may be untagged, 30% of figures are tagged, and they are tagged by software or accountants so should be good quality training data for supervised learning that could then be applied to the 70%. So, I recommended creating a supervised multi-class text classification ML model to classify the descriptions. 

# 3. Methods used and justification.

## 3.1. Project management

I selected an agile approach for the overall project(https://agilemanifesto.org/principles.html). I didn't strictly adhere to a specific framework, selecting features that were appropriate("Teams tailor Agile practices to their needs, blending frameworks like Scrum and Kanban for optimal results" https://www.atlassian.com/agile), with it being more Kanban focused since the project team was small and the overhead of SCRUM wouldn't be appropriate. The competing business demands on the team meant that fixed sprints weren't appropriate but regular Kanban updates ensured progress on this project while other business needs were accommodated. 

The agile approach allowed us to iterate quickly delivering usable pieces of work, with basic raw data initially delivered on file, then in additional steps more data, iXBRL information, ML categories, improved architectures and database. Regular meetings and a workshop with stakeholders helped get feedback such as the issues dealing with raw descriptions; validate business understanding and planned approaches. With each step evaluated for feasibility, benefits and risks. The customer requirements at the beginning wouldn't have foreseen the way the project developed, highlighting the benefit of an agile approach opposed to a more fixed waterfall approach. {should this second paragraph be in discussion?, there is a bit of overlap}

## 3.2 CRISP-DM

I used CRISP-DM since it accommodates the cyclical nature of ML and provides a clear intuitive structure. I working on the ML aspect myself, so CRISP-DM is more appropriate than larger more complex methodologies like TDSP. Each stage produced documented artefacts, allowing evidence backed decisions in other steps. 

## 3.3 Languages and Tools

### 3.3.1 Gitlab

While using GitLab to manage project isn't common in HMRC, I decided that the advantages of transparency, audibility and documentation outweighed the costs of learning a new tool. 
- Documentation 
	- {Readme stuff?}
	- Data structures and types, 
	- Guide to setup Oracle tables/credentials, 
	- Details of key decisions and the reason why they were made. 
- The issues board worked well as the Kanban board helping us track issues and tasks. 
- The epics were useful for working with management who were focused on longer term timelines. 
- I created templates for issues, tasks and PR, which ensured they were completed to a consistent level by all team members. Covering details such as details of every step required to recreate the issue, expected vs actual and proposed fixes.
- Team members were encouraged to document issues in detail on GitLab, to update project markdown documents, and guided that code comments should be why code does what it does rather than just describing what it does. 
- Version control, branches and independent review of PR helped ensure changes were of sufficient quality and limit issues. This required training the team how to use branches, which I videoed for reference. 

### 3.3.2 Languages and packages

I used R due to its relevant packages and because it is the default coding language used by analysts at HMRC, so has much greater support and maintainability. 
- `aws.s3` to access iXBRL documents from AWS S3 buckets. 
- `rvest` and `xml2` for html extraction.
- `parallel` to allow processing hundreds of documents at the same time.
- `dbplyr` allowed Oracle database access using familiar tidyverse syntax analysts are used to.
- `testthat` for testing

I used python for the ML aspects since the classification packages are more mature and have more support. The reticulate package in R allows importing python function into a R workflow, which made integrating it work well. 
- `mlflow` to track tracks data version, model version, performance and various other metrics
- `scikit-learn` for traditional ML models 
- `tensorflow`/`keras` to build and train NN
- HuggingFace `transformers` to utilise pre-trained transformer based models
- `optuna` to fine tune parameters and hyperparameters. 

Jupyter notebooks for exploratory work allowing for detailed narrative alongside the code. The exploratory notebooks are reproduced in Appendix A: extraction (A1), EDA and preprocessing (A2), traditional ML experiments (A3), neural networks (A4), transformers (A5) and the model comparison (A6).  

SQL was also used for setting up and managing the Oracle database and tables.

## 3.4 Testing

While working with others to review the code base, we discussed the scope, coverage and implementation of unit, integration and system testing. Constraints such as that the tests shouldn’t contain any customer data, so to use synthetic or anonymised fixtures instead. While we weren't using formal test driven development, I did explain to the team how it can be useful and instructed them to create a tests alongside new issues, since it makes it easier to investigate, fix and verify the fixes. 

With user acceptance testing, it highlighted that users might prefer numeric primary keys for joining rather than natural keys for join performance reasons. They also suggested structuring data in a way they are more familiar with. {maybe move this second paragraph to dicussion}

## 3.5 Scientific method and statistical analysis

I used hypothesis formulation; controlled experimentation including DummyClassifier baselines; stratified cross validation with paired t-tests at the 95% confidence level to determine if models were statistically different from the top model (`compare_to_top` and `add_confidence_interval`, Appendix A3.2). Challenges included class imbalance which required using score like macro-F1 which gives equal weighting to each class, stopping common classes from dominating the scores. On the modelling side different approaches were tested such as balanced weights and/or square-root weighted training samples.

# 4. The scope of the project (including key performance indicators).

The project scope evolved over time, from pure extraction of core data like descriptions and values to file; to extracting and formatting other relevant data such as headings, table names, structural data(table number, row number, column number) and iXBRL data(concept, dimensional data); adding ML capabilities; and an automated pipeline extracting to Oracle database. 

Working with stakeholders success criteria were established. 
- Macro-F1 > 0.6, primary performance metric, weighing all classes equally, so common classes don't dominate.
- Accuracy > 0.7, a secondary metric metric that is more intuitive and easier top understand by stakeholders and does give real world performance.
- Automated extraction coverage > 95%, data automatically extracted and classified
- Timely extraction < 1 week from date of receipt. 
- Interpretability and explainability, we should be able to know why a choice was made and/or provide a human understandable explanation of the factors that drove the choice.
- Security(dependency risk)

Secondary KPIs used were precision; recall, train time, inference time, interpretability, explainability, maintainability, reliability, cost control, data protection, AI safeguards, logging, and ability to scale to millions of records quickly.

# 5. Data selection, collection and pre-processing.

## 5.1 Data selection

HMRC's systems are locked down, without any readily available GPU access making it difficult to do exploratory work with complex models, so exploratory work was done using a standalone device with a GPU over 298,461 publicly available iXBRL accounts submitted to Companies House. It was a a month of data making it more representative, although many companies select specific dates like 31 December or 31 March, so the data might not be completely representative but that shouldn't have any material impact for my analysis. This resulted in 2.8m lines of data with 956 concepts(labels)(extraction code Appendix A1; dataset characteristics Appendix B15). For the implementation phase company accounts and tax computations submitted to HMRC were used. 

The source iXBRL documents were complex with inconsistent HTML structures, iXBRL data and multiple taxonomies. Appendix B1 shows how tagged and untagged values sit in the document, Appendix B2 and B3 the two structural variants (with and without HTML table nodes, ~85%/~15% of documents), and Appendix B4 the table name and headings that later became additional features. I asked SME about errors where the predicted class was what I expected but the iXBRL concept was slightly different, they explained that some concept names differ between the different taxonomies. A bespoke model for each taxonomy would give the best raw scores, but it would be confusing for analysts, so it was recommended to train only using the main taxonomy giving consistent categories.

## 5.2 Exploratory Data Analysis(EDA)

Rank frequency plots of both description and concept had a long tail(Appendix B5). With a Pareto chart showing that the 75 most common concepts cover 95% of items(Appendix B8); with a distribution closer to a lognormal fit than power-law(Appendix B9). Motivating the use of macro-F1 over accuracy so that common classes don't dominate the metrics. {I say this lots of times all over the place, maybe just say it here}

The main feature is a description that has various types, from nominal text, dates(temporal), names(nominal) and numeric figures(numeric ratio). Most descriptions are 1-9 words with a mode of 2(Appendix B6), and the five most common concepts all have interquartile ranges of 2-7 words(Appendix B7). 

The xbrl concept(label) is a categorical nominal label from a fixed taxonomy. It's a single CammelCase word, but splitting into words make it human readable with similar concepts normally having similar wording. 

The descriptions and concepts are many-to-many(Appendix A2.2.7 and A2.2.8), with cosine similarity analysis identifying situations where some descriptions like "Taxation and social security costs" were used for very similar concepts, but other descriptions such as "total" were used for lots of different concepts. It also highlighted that taxonomy goes into a great deal of specificity, beyond what is generally required or could be predicted based on the human readable data in the accounts. Creating a real upper limit to any model. {Isn't this said elsewhere?}

Initially I did some classifier independent analysis, which showed that MPNet had the best silhouette score(0.467) suggesting it is able to capture meaning of the different descriptions better than plain TFIDF(0.41)(Appendix A2.5, full scores at Appendix B16). 
## 5.3 Preprocessing

The text features like description were normalised, lowercasing and replacing special characters with spaces. Not all preprocessing was effective, for example replacing forward slashes with spaces actually reduced performance, so it was dropped(`clean_field`, Appendix A2.3). 

I canonicalised the description, so most dates were replaced by a placeholder "hubble_date", except for 31 March 1982, which subject matter experts explained has a special meaning for tax so that was replaced with "hubble_date_1982_03_31"(`canonicalize_field`, Appendix A2.3). 

Similarly company names, individual names, postcodes and numbers were identified using regular expressions and labels replaced by placeholders. This helps avoid overfitting and makes the model more generalisable; improves model performance since it reduces a lot of the noise;  preserves privacy; and enhances data security through data minimisation. It is more ethical since it would treat less common ethnic names the same as more commonly used names. 

Subject matter experts advised that where there was a placeholder by itself, then that would not be enough information to categorise, so we agreed to do label engineering and changing them to similar placeholders like HubbleName(`target_engineer` and `standardise_names`, Appendix A2.3; effect on the label distribution at Appendix B12). So while we can't predict the actual concept the placeholder is related to, knowing it is a name can be useful in analysis. 

I implemented data quality controls aligned with HMRC expectation and broadly in line with DAMA UK’s quality dimensions(https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework)(https://www.dama-uk.org/resources/the-six-primary-dimensions-for-data-quality-assessment).
- Completeness improved since untagged data was now extracted. 
- Consistency because the untagged data and iXBRL tagged data was structured and formatted in similar ways on the same tables. 
- Timeliness, the system architecture and structuring the data in a long format allowes extraction and categorised within days. 
- Validity and accuracy were addressed by removing descriptions less than 2 characters, missing; low-quality; or longer than 16 words which analysis showed weren't valid descriptions(`filter_data` and `filter_out_labels`, Appendix A2.3). 

This reduced the unique descriptions from 266,178 to 10,591 and labels from 956 to 826, while keeping 86% of the rows of data(Appendix B15). The effect on the distributions can be seen by comparing the rank frequency, word count and Pareto plots before and after preprocessing(Appendix B5-B9 against B10-B14). These measures and preprocessing improved model macro-F1 scores from under 0.5 to over 0.7. Along with measure like restricting access to systems and data to specific users ensured I was complying with both HMRC and regulatory requirements, DPIAs and Data Protection Act 2018/UK GDPR. 

Because the data was going to be used over various model architectures and packages, I created stratified splits upfront, 80/10/10, test, train, holdout plus sub splits and square-root weighted splits(`stratified_split`, `sample_split` and `add_sqrt_weight`, Appendix A2.6). The holdout ensures that the final comparison is over unseen data, so provides a better view of performance against real data.


# 6. Survey of potential alternatives.

This is multi-class text classification with over 826 nominal classes with strong class imbalance. I initially used data exploration and theory to limit the solutions to those that would work well with classifying the short domain-specific terminology, reviewed the feasibility within the business context then and then evaluated the leading candidates. 

Systematising the existing regular expression process wasn't a feasible business solution, so various ML approaches were considered. 

While the data was tagged, often the specificity was beyond what was required, so unsupervised methods were considered as a way to group similar concepts together. But initial analysis using cosine similarity highlighted that the great variety in descriptions for some concepts meant that it wasn't feasible. So I focused on supervised learning models. 

Traditional ML models can perform well with classifying short simple text, especially since descriptions in the accounts will normally have less variety and more domain-specific terminology than generic free text. {Isn't this more about TFIDF than traditional ML algorithms}. Scikit-learn is a package that provides various high quality models that can be used for text classification, such as `SVC`, `LinearSVC`, `SGDClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `MultinomialNB`, `ComplementNB` and `PassiveAgressiveClassifier`. The full search space over these models is at Appendix A3.4.1.

There were two main methods used to embed the descriptions for the traditional ML models, sparse vectorisation(TF, TFIDF) and dense vector embeddings(MPNet, E5). TFIDF over character and word n-grams can perform well since it captures domain specific terminology and phrasing well and works well with a variety of models with good speeds and performance. Dense vector embeddings capture more of the semantic meaning of phrases so should capture phrases that have similar meaning even if the words are different, which should improve classification especially on unseen descriptions(Appendix A2.5 and A3.5.2). 

A deep neural network can be trained to categorise descriptions, and has the advantage of being able to learn patterns beyond that of a fixed algorithm used in transitional ML. Various NN can be used for text classification such as DNN, LSTM, GRU, CNN and BI, all of which were included in the architecture search(`create_model`, Appendix A4.2.2).

Transformer based models are a more advanced architecture that results in better semantic understanding of text that often outperforms other neural network architectures. Pre-trained models are trained over large amounts of text so have a lot of semantic understanding baked in. Various transformer based models were tested, RoBERTa, SEC-BERT, MPNet, and MiniLM, covering different sizes, architectures and training data(Appendix A5.1 and A5.2). SEC-BERT is a model that was trained on SEC filing(financial filings), so should have better semantic understanding of accountancy terms and concepts.

It is expected that a frontier LLM, such as Chat GPT would have better semantic understanding of text, but it is likely to be excessive for this use case. A LLM would be good at understanding lots of text, but we just have short phrases. There are additional technical, data security and governance issues around using an API, which made this approach unfeasible from a business perspective. 


# 7. Implementation - performance metrics.

## 7.1 Population size validation

It wasn't possible to compare every model and hyperparameter over the full train dataset. So initially I tested a few smaller models over 1%, 10% and 100% train populations, to see if results using the smaller populations were representative of larger populations(Appendix A3.3). The 1% population had a fairly high score of Pearson correlation of 0.971 to the full train population and 10% had a very high score of 0.998(Appendix B19 and B20). Paired T-tests showed that models that weren't not significantly worse over the 1% population were the same at 100% population. So this meant that it was reasonable to filter out models and hyperparameters using a smaller populations, and that the 10% train population was large enough for reliable results. 

Initially I focused on macro-F1 scores for within-class comparison.

## 7.2 Traditional ML algorithms

To narrow down the initial models and hyperparameters I used HalvingRandomSearchCV over 10,000 candidates, which let me cover many models and hyperparameters in an efficient way, while using a DummyClassifier floor to ensure real performance. Robustness was improved through stratified cross validation which reduced variance and allowed paired T-test to indicate which models were not significantly worse at the 5% level, which was used to narrow down the models used at each stage. 

To get a better handle of the hyperparameters I plotted them against against scores, helping narrow down the ranges to use for subsequent iterations. A 2D graph using colours showed that min_df 1 had clusters with better speed and macro-F1 scores over min_df 2, which was surprising on the speed aspect. 

After fine tuning the hyper parameters and training on the full train dataset, LinearSVC was the best performing model beating out the alternatives at a 5% confidence level. 

To deal with the class imbalance and reduce systematic bias towards majority classes, I used explored both using balanced class weight as part of the model hyperparameters and square-root weighted training data. The 10% square-root weighted vs strait 10% train population resulted in 1.3pp better macro-F1 score but 0.0573pp lower accuracy. But training on the full 100% population using a balanced hyperparameter resulted in the best f1-macro and accuracy, and would have the simplest pipeline. 

I tried both sparse and dense word embeddings and at the 5% significance level MPNet performed better(macro-F1) than a simple TFIDF embedding, but it was only by 0.3pp and took 76 times as long. So I decided to stick with a simpler TFIDF word only embeddings, which would be faster, easier to maintain and would make it easier to interpret models using them.  

The final pipelines used TFIDF(1-3 word n-grams, min_df 1, norm l2) with LinearSVC(penalty l1, C 2.8, loss squared_hinge, dual False, class_weight balanced, max_iter 10000). There was a range of similar performance for C, but a lower C was selected to prevent overfitting and enhance model generalisability. 

## 7.3 Conventional and Transformer based Neural Networks 

I used Optuna to compare and find the optimal architecture/model and hyperparameters such as activation, learning rates, dropout rates, embeddings dimensions, dense dimension size and number of layers. CNN was the best performing conventional neural network. It used dropout hyperparameters used as regularisation technique, limiting overfitting and improving generalisability. SEC-BERT was the best performing transformer based model, demonstrating that the domain based pre-training was beneficial. 

## 7.4 Class imbalance

To deal with the class imbalance and reduce systematic bias towards majority classes, I used explored various methods such as: 
- Weighting models worked well with LinearSVC but reduced performance on the NN models. 
- Square-root weighted training data over various models provided good increases in macro-F1 but sometimes with a very small decreases in accuracy, e.g. 1.3pp macro-F1 increase vs 0.0573pp accuracy decrease.
- Random oversampling, actually reduced performance on the transformer based models. 

While for the NN based models making a smaller modified training dataset improved performance compared to the full train dataset, LinearSVC performed best on the full train dataset, using a weighted model. 

## 7.5 Model selection

To compare the model architectures a decision matrix was used, covering various objective and subjective measures.

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
- Model Lifecycle
- Dependency risk
- Cost

Each measure was weighted and adjustments were made if there were overlapping confidence intervals. With a rubric setting the standard/scores for the the subjective scores with an accompanying narrative. 

To make comparison fair and due to memory/time constraints, all models were all trained on 10% square-root weighted data and evaluated on the same subset of the holdout data. The 5% confidence intervals were created using the bootstrap method over using cross validation due to complexity and computational time constraint reasons. 

While SEC-BERT had the best macro-F1 score I chose LinearSVC, trading marginal performance(2.3pp) for a solution that is simpler(more maintainable), more explainable(feature coefficients), quicker(13x), allows development on existing infrastructure(CPU based), with the ability to scale cost effectively, relies on well-established packages that are regularly updated.

## 7.5 Wider system

To scale we would need additional infrastructure, I worked dev-ops to setup on-demand-compute, which allows us to fire up an EC2 instance running POSIT just for a job and shuts it down when finished, which is much more cost effective than having a large machine running all the time. EC2 instances without a GPU were not only cheaper but also have better availability. 

The overall system consisted of the raw iXBRL documents in AWS S3, with ODC creating a dedicated EC2 instance running POSIT, where iXBRL document are accessed using `aws.s3`, then extracted using `rvest`/`xml2` and structured using bespoke R code, then `reticulate` allows the running of python function to canonicalise the features and use scikit-learn's `Pipeline` with `TfidfVectorizer` to embed the text features and `LinearSVC` to classify the features, with the output save to an Oracle database via `dbplyr`.  The scope of the project meant that others were working on non-ML aspects, where  I would often work collaboratively with them, partially to share knowledge and also up-skill them.

# 8. Results.

LinearSVC trained on the full dataset and tested over the full holdout has an accuracy of 0.975(CI 0.975-0.976) and macro-F1 of 0.785(CI 0.780-0.788) beating KPIs of 0.7 and 0.6 respectively. The system also meets the KPIs by extracting over 99% of records; within 3 days; and has an interpretable and explainable ML model. 

Residual analysis helped identify which classes performed poorly and summaries were created for analysts. I worked closely with analysts where I focused on outcomes, showing confusion matrices for good and poor quality classes and looking at examples, so they understood where it would be good, situations where it would make mistakes and the kind of mistake they should expect. I got similar questions about the ML, so I also created an an interactive dashboard where users can test the model and also see details on how well it performs with certain concepts, which is much more user friendly than just having a large dataset they would have to filter/process themselves. The dashboard had a top-k, some of those were very poor matches confusing users, so I changed the dashboard to just show the plausible matches. As users understanding of how the ML worked their use increased.

Subject matter experts also provided input explaining how that in some cases there simply isn't enough information at all in the document to predict the specific concept used. For example the description "amounts owed to group undertakings" is associated with multiple but similar concepts. So the data is in the form of multi-label, but multi-class analysis is being used. This  highlights that maybe a simplified list of categories could actually be beneficial, especially on the evaluation aspect. 

Sensitivity analysis and model robustness was tested over various categories, abbreviations, adversarial(So phrased to be misleading), scenario planning, command(command to inject LLM), contextual(semantically the same), long context, OCR issues, synonyms, typos, unicode and variations. Overall LinearSVC outperformed SEC-BERT in robustness testing, which was unexpected since I would have expected the domain-specific training and theoretical better semantic understanding would have SEC-BERT doing better overall. Also the areas where LinearSVC did worse like typos and variations would be rare over real data, since accountancy documents are primarily generated by computers, rather than people typing every description. 

Bias was investigated both against size of companies and software provider. So large companies had a macro-F1 score of 0.9343 vs 0.789835 for small companies. Which could be explained by smaller companies using cheaper software, with some software providers having a score of 0.184061 vs 0.913292. On residual analysis often the misclassifications were for very similar classes and there was not enough information to differentiate between them. This highlights an issues one that maybe the specificity of the model and testing to too high. Also it is highlighting just how different software tags items, but it's a training proxy, and such issues wouldn't apply to untagged items, or if we had human labelled classes this issue wouldn't show up. 

# 9. Discussion and conclusions/recommendations.

An Agile approach worked well with CRISP-DM, allowing us to create initial version initial products that proved the approach and provided business value, then future iterations improved the both extraction and the ML aspects providing even more value to the business both in quality and completeness of data, increased scale of operation, and more streamlined access to data. The iterative improved macro-F1 from under 0.50 to 0.787.  In later iterations using additional features, table name and heading, improved macro-F1 by 9.8pp. 

While using metrics like macro-F1 works well for comparing similar classes of models, it's important to consider all the business requirements using method like decision matrixes. But some factors like interpretability are core requirements that could override a raw score. The coefficients of LinearSVC provide real interpretability that could be explained to technical audiences that was not available with neural networks. But tools like LIME and SHAP do provide explainability which does partially mitigate such risks with models that aren't interpretable. 

Since SEC-BERT is not created by a well established provider, even if it was the winner of the decision matrix, security aspects may prevent use. If it was clearly superior then it might be that we would need to invest in training our own BERT based model.  

My communication approach evolved based on how stakeholders reacted to early explanations, and methods tailored for the use case, such as powerpoint presentations, markdown guides, interactive dashboards, meeting, dashboards. Initial technical descriptions were too detailed for some audiences, so I shifted towards visual and example-based explanations. So very simple visual decision trees showing what attribute was split on, or graphed SVM 2D decision boundary.  I used a simple example to helped illustrate the difference between weighted and macro scores rather than going into in depth formulas.



With DevOps I focused on benchmarks, memory usage and future requirements, cost/benefit of specific EC2 instances. 


Future requirements include scaling to millions of documents with fast inference speeds(2.7ms), on low cost infrastructure. This ruled out the larger transformer based models that would need to be run on expensive GPUs, and still be significantly slower to train and run. SVM based models that can be developed on existing CPU based infrastructure, have good performance and are very fast.

The coefficients from LinearSVC helps interpreting how the model arrived at what it did, something not possible with CNN or SEC-BERT. But there are tools like LIME and SHAP which do work help with the explainability with all the models and provide some insights beyond the coefficients alone. 

The selection of TF-IDF and LinearSVC was selected. The short domain-specific descriptions led itself well to TF-IDF(1-3 n-grams) with domain-specific vocabulary captured as their own feature. LinearSVC works well with sparse matrices like those created by TF-IDF and using L1 regularisation which removes irrelevant features, resulted in even sparser matrices, allowing inner products to be done very efficiently. This allowed me to test and develop the model using existing infrastructure without disturbing other users.


I recommended that communications should have the headline figures and results, with a section that explains any technical terms with illustrations and examples, and an appendix with the technical details.

Presentations to non-technical audiences roughly follows the Problem-Solution-Outcome structure. Trying to explain complex concepts even step by step was still confusing for non-technical audiences, so I moved over to using simple concepts like confusion matrixes with examples. The solution is at a very high level without going into the technical detail, with the focus on the outcomes each slide focused on a separate benefit/functionality with clear examples they could understand explaining what it does without going into unnecessary detail. 

With managers I focused less on the technical development and focused on the business level, so benefits and outcomes, funding, blockers timeframes, and the benefits of more people working on the project, which resulted in additional people to help with development. I created a memos with a cost benefit analysis highlighting both improved timeliness and also extracting new untagged data, resulting in additional funding for infrastructure. Further funding will be required. 

The project readme utilises markdown to provide clear headings and sections, with instructions, links and code blocks, which has been successfully used by many analysts to setup the tool. This means many analysts are now running the tool allowing me to focus on development. But further developments resulted in a centralised approach extracting the full population and storing the data in an Oracle database streamlining the process with users just needing to do a database query rather than running the tool themselves. When users have issues or questions, I updated the relevant documents to be clearer or cover such issues. 

Monitoring drift of inputs, are there new taxonomies. Drift on outputs is detected for both accuracy and f1-macro, using a 2pp drop and for there to be non-overlapping confidence intervals, over two consecutive days. 

While a single command runs all the the tests, I would like to also add a CI pipeline in the future. 

Optuna has built in visualisations and automatically tunes the hyperparameters. This automated the more manual process I used with scikit-learn, so I plan on trying Optuna with scikit-learn in the future.
# 10. Summary of findings.

I developed a supervised classifier, multi-class, to categorise untagged items in financial iXBRL documents. A variety of models were evaluated using macro-F1, with the final candidate models, LinearSVC, CNN and SEC-BERT being compared using a decision matrix.  The chosen pipeline was TF-IDF 1-3 word n-gram with LinearSVC with accuracy of 0.975(CI 0.975-0.976) and macro-F1 of 0.785(CI 0.780-0.788). {beating KPI by}. 

# 11. Implications.

The result is a dataset that reduces manual effort 

Hubble being widely used in by multiple teams

Hubble helped us meet our quality standards, such as completeness and consistency since we can extract all of the figures and have consistent ML classes. Enabling analyssts to more easily and robustly use the data.

The business value is that it reduces manual effort, allows us to better create statistics that informs and drives government policy and better identify risks. 

Manual spreadsheet to record benefits showed tens of millions in estimated benefits, but completion was incomplete so I arranged for the central management system to have built in functionality to monitor benefits. 

# 12. Caveats and limitations.

The model and evaluation were all based on tagged data. But the main use case would be on untagged data, and there is a risk that the untagged data could be different than the tagged data. e.g. An item might have been left untagged since there aren't any relevant taxonomy concepts for that item. Ideally untagged data would be human tagged by SME, but it requires tax trained experts, who while do not have time to fully tag enough items themselves, will be feeding into a manual evaluation stage. 

Analysts were educated that the ML category can be wrong and shouldn’t be used for automated decisions. There should always be a human in the loop before any action on it happens. 

LinearSVC has very good train times on smaller dataset sizes but doesn't scale as well on larger datasets, so it's not practical to train it on larger datasets. But going from 10% train data set to 100% saw only a 0.4pp increase in f1-macro, so much larger datasets are unlikely to increase performance much. 

Increasing data set size while keeping a fixed numeric cutoff, results in more labels, so model performance actually decreased, also different document types had different distributions in labels, also resulting in varied performance, making comparison across different document types and sources difficult. 

The integration of R and python while working well, does add more complexity to setting up the project and other teams have had issues with the reticulate package. With the the long term move to a lakehouse, initial investigations suggest like python has more support for the ETL stage where Hubble would fit. With higher python use in HMRC now, it might be worth considering porting in the future. 

# 13. Appendices.
## Code and documentation used for the project.
## Statistical rigour: uncertainty, bias, and error estimates where appropriate.
## Figures, tables, and visualisations.
## Mapping of the project report to AM1 KSBs.
## Employer verification that the report reflects my own involvement and work.