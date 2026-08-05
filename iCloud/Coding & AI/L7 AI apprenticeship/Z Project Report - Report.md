
# Introduction and background.


# Outline of the issue or opportunity and the business problem to be solved.

HMRC receive financial documents such as company accounts and tax computations that contain a large amount of useful information, that are used to provide insight for operational/government policy and to identify tax risk. They are iXBRL documents; semi-structured (x)HTML documents where key items are tagged with a concepts from fixed taxonomies. 

For fully tagged documents, existing workflows allows us to reliably extract, structure and analyse the data in those documents. But some documents only have approximately 30% of the figures tagged, which means that existing workflows can't utilise 70% of the figures. There are various reasons for this, ranging from limitations in software used to create the documents to people deliberately leaving items they don't want HMRC to review untagged. 

Having most of the data in the some documents untagged means that profiles don't have the data to properly identify high tax risk return. We were also unable to provide accurate data or statistics for the department/government to make informed decisions. 

The existing systems to extract iXBRL data, require complex and long updates to processes the schemas every year when new taxonomies come out. The wide database format is also hitting the column limits of the Oracle database. It can take up to 9 months for the updates, but HMRC only have 12 months to open an enquiry, leaving little time for profiling and opening an enquiry in time. 

Hubble is a tool I develop that initially extracted untagged figures and their associated descriptions. People can describe items in lots of different ways with no fixed taxonomy. Initial data analysis required lots of complex regular expressions and working with SME due to the domain-specific terminology, which was error prone, incomplete and time-consuming. 

I investigated and implemented a solution that extracted additional data and used ML to categorise items increasing consistency so that analysts could more easily and robustly use the data.

# Methods used and justification.

I selected an agile approach for the overall project(https://agilemanifesto.org/principles.html). I didn't strictly adhere to a specific framework, selecting features that were appropriate, with it being more Kanban focused since the project team was small and the overhead of SCRUM wouldn't be appropriate.("Teams tailor Agile practices to their needs, blending frameworks like Scrum and Kanban for optimal results" https://www.atlassian.com/agile). 

While using GitLab to manage project isn't common in HMRC, I decided that the advantages of transparency, audibility and documentation outweighed the costs of learning a new tool. 

The agile approach allowed us to iterate quickly delivering usable pieces of work, so initially just extracting descriptions and values, then extracting iXBRL data, which then opened up having a ML category, then extracting more data such as headings and table names, allowing improved ML, then storing the data in a database increasing availability. The customer requirements at the beginning wouldn't have foreseen the way the project developed, highlighting the benefit of an agile approach opposed to a more fixed waterfall approach. But regular contact with stakeholders ensured that the project stayed aligned with their needs. 

A focus on collaboration meant that I got lots of feedback from analysts who use the data to create profiles, such as the difficulty working with raw descriptions, errors with extracts. 

Before expanding the project workshops were held with a variety of users, validated the need for the tool. 

The epics in GitLab were useful for working with management on the longer term plans and timelines they were more focused on. 

The issues board in GitLab was used as the Kanban board which formed the core the development team regular meetings, helping us track issues and tasks. 

I used CRISP-DM since it works well on ML projects like this and provides a clear intuitive structure. 

I used R for the extraction work since it has strong HTML parsing packages and is the default coding language used by analysts, so has much greater support and more people that would be able to take over. I used python for the ML aspects since the packages are more mature and have more support. The reticulate package in R allows importing python function into a R workflow, which made integrating it work well. The python ML packages used included MLflow, sci-kit learn, TensorFlow/Keras, HuggingFace Transformers and Optuna. The exploratory work was done in Jupyter notebooks to allow for detailed narrative alongside the code. 




# The scope of the project (including key performance indicators).

The project covers understanding the business issue and what they would like to do. 

Understanding current issues with iXBRL extraction and storage. 

Extracting relevant data such as description, headings, table names, structural data(table number, row number, column number), iXBRL data(concept, dimensional data) and value. 

Processing and formatting data.

Developing ML model to categorise the data. 

Saving the data into an Oracle database to allow analysts to profile across it in bulk.

Setup a reliable architecture that would automate the end extraction, categorisation and storing of data. 

Key performance indicators would be f1-macro, accuracy, precision, recall, train time, inference time, interpretability/explainability. 

I designed a solution around HMRC’s priorities of maintainability, reliability, cost control, data protection, AI safeguards, security and ability to scale to millions of records quickly.

# Data selection, collection and pre-processing.

HMRC's systems are locked down, making doing exploratory work trying different models difficult. Also there wasn't quick easy access to a GPU device for more the more complex models. 

So the public company accounts submitted at companies house, which are iXBRL format were used for the exploratory phase since that could be done on a standalone device with a GPU. From the 298,461 accounts submitted in November 2015 I used the html accounts that had html tables. Selecting the data submitted in a month makes it more representative, although many companies select specific dates like 31 December or 31 March for various reasons, so the data might not be completely representative but it shouldn't have any material impact for our analysis.

This resulted in 2.8m lines of data with 956 concepts(labels). With rank frequency plots of both description and concept having a long tail. With a pareto chart showing that the most used 75 concepts cover 95% of items. Powerlaw analysis showed it was closer to a lognormal fit than powerlaw. 

For the implementation phase the company accounts and tax computations submitted to HMRC were used. 

I extracted key data such as the description, heading, table name, iXBRL concept, iXBRL dimensional data, references, footnotes and structural data. 

There are various types of description, from nominal text, dates(temporal different formats), names(nominal) and figures(numeric ratio). 

The xbrl concept is a categorical nominal label from a fixed taxonomy. It's a single CammelCase word, but splitting into words make it human readable with similar concepts have similar wording. 

The text features like description were cleaned, lowercasing and replacing special characters with spaces. Not all cleaning was effective, for example replacing forward slashes with spaces actually reduced performance, so it was dropped. 

I canonicalised the feature, so most dates were replaced by a placeholder "hubble_date", except for 31 March 1982, which subject matter experts explained has a special meaning for tax so that was replaced with "hubble_date_1982_03_31". Similarly company names, individual names, postcodes and numbers were replaced by placeholders. This improves model performance, since it reduces a lot of the noise. Removing personal data like individual names enhances data security since personal data is removed and not used in latter steps.

Using cosine similarity analysis, it identified situations where some descriptions like "Taxation and social security costs" were used for very similar concepts, but other descriptions such as pure dates were used for lots of different concepts.  Creating a real upper limit to any model.  It also highlighted that taxonomy goes into a great deal of specificity, beyond what is generally required or could be predicted based on the visual data in the accounts. Maybe in future iterations grouping similar groups together would make a model perform better but also outputs easier to use for non-tax technical analysts. 

Cosine similarity analysis also highlighted that while some concepts had descriptions that were very similar, other concepts had descriptions which were very varied, meaning there would be fundamental limits if any unsupervised methods were used, if say we wanted to create a simplified number of categories. 

Then there was some label engineering, where the feature a placeholder by itself, then the label was changed to reflect that. e.g. if a description is just hubble_number, then the label would be changed to be HubbleNumber. The reason for this is that placeholders by themself don't contain enough information to predict a category, but knowing the type could be useful to know. 

The interquartile range for the number of words was between 2 and 5 words. A review of the data showed that some descriptions were just a single special character, which wouldn't have enough information to categorise on, so anything 2 or less characters was filtered out. Reviewing descriptions of 16 words or more showed that they weren't descriptions of the kind I was interested in, and there were very few over that length so were filtered out.

I removed data that had concepts related to names or addresses. 

Various approaches were used to embed the words, from TF word and character ngrams, all-mpnet-base-v2 and infloat/e5-large-v2. The silhouette score was used to see how well the models embedded the descriptions for each concept. MPNET has the best silhouette score, suggesting it's able to capture the different descriptions which have the similar meaning better than just TF. 

Because the data was going to be used over various model architectures and packages, test/train/holdout including sub splits and sqrt weighted splits were created upfront so they could be read out of the source data file. 

The work on preprocessing significantly improved the performance of the model going form a macro-f1 of 50% to over 70%.

# Survey of potential alternatives.

The primary feature is a free text "description". So this is text classification problem. While most figures are untagged, 30% of figures are tagged and due to the volume of the total data, this means that we can train the model on the 30% of tagged data, so it is a supervised multi-class classification problem.  

The descriptions are normally just a word or a short phrase, but  have domain-specific terminology. There were two main methods used to embed the descriptions, TFIDF and dense vector embeddings. TFIDF extracts character and word n-grams, this can work well since it captures domain specific terminology and phrasing well and works well with a variety of models with good speeds and performance. Dense vector embeddings capture more of the semantic meaning of phrases so should capture phrases that have similar meaning even if the words are different, which should improve classification especially on unseen descriptions. 

There are a range of possible models that deal with text such as using traditional ML such as Naive Bayes and SVM; training a deep neural network from scratch; fine tuning a larger transformer based model locally; using a frontier LLM and fine tuning it via an API. 

Traditional ML models can perform well with classifying short simple text, especially since descriptions in the accounts will normally have less variety than generic free text.

A deep neural network can be trained to categorise descriptions, and has the advantage of being able to learn patterns beyond that of a fixed algorithm used in transitional ML. 

There are a number of BERT based models. These models have been pre-trained, so have a lot of semantic understanding baked in. But many BERT models are trained on generic text,  SEC-BERT is a model that was trained on SEC filing(financial filings), so should have better semantic understanding of accountancy terms and concepts, which is very appropriate here.

It is expected that a frontier LLM would have the best semantic understanding, but it is likely to be excessive for this use case. A LLM would be good at understanding lots of text, but we just have short phrases and small sentences at most. There are additional technical, data security and governance issues around using an API. So a LLM based approach was not used.

The existing approach of using regex's could could be systemised, creating a repository of concepts and the associated regular expressions that could be used to identify them from the description. This would be a very labour intensive approach, that would require large input from SME, would be incomplete and error prone. So this approach wasn't used. 

Exploratory analysis showed that unsupervised methods around the words used would be insufficient. 

The primary feature is a free text "description". So this is text classification problem. While most figures are untagged, 30% of figures are tagged and due to the volume of the total data, this means that we can train the model on the 30% of tagged data, so it is a supervised multi-class classification problem.  

The descriptions are normally just a word or a short phrase, but are have domain-specific terminology. There were two main methods used to embed the descriptions, TFIDF and dense vector embeddings. TFIDF extracts character and word n-grams, this can work well since it captures domain specific terminology and phrasing well and works well with a variety of models with good speeds and performance. Vector embeddings capture more of the semantic meaning of phrases so should capture phrases that have similar meaning even if the words are different, which should improve classification especially on unseen descriptions. 

There are a range of possible models that deal with text such as using traditional ML such as Naive Bayes and SVM; training a deep neural network from scratch; fine tuning a larger transformer based model locally; using a frontier LLM and fine tuning it via an API. 

It wasn't possible to test every model and hyperparameter over the full train dataset. So initially I tested a few smaller models over 1%, 10% and 100% train populations, to see if results using the smaller populations were representative of larger populations. I checked the Pearson correlation of the f1-macro scores for those models to the various populations. The 1% population had a fairly high score of 0.971 and 10% had a very high scores of 0.998. Using a paired T-test models that weren't not significantly worse over the 1% population were the same at 100% population. So this meant that it was reasonable to filter out models and hyperparameters using a smaller populations, and that the 10% train population was large enough for reliable results. 

To narrow down the initial models and hyperparameters I used HalvingRandomSearchCV, which let's me cover many models and hyperparameters in an efficient way. Since there were cross validation scores, I used this with a paired t-test to show which models were not significantly worse at the 95% level. This narrowed down the models to LinearSVC, SVC(linear) and PassiveAggressiveClassifier. 

To get a better handle of the hyperparameters I plotted them against against scores, this helped narrow down the ranges to use in more in the next iteration using the full train population size.  A 2D graph using colour showed that min_df 1 had clusters with better speed and scores over min_df 2. 

Here LinearSVC had the best f1-macro score and was significantly better than the other models at the 95% confidence level. 

I then tried different embeddings, such as mpnet, e5, various tfidf word and character embeddings. Complex tfidf with a complicated combination of word and character ngrams, performed significantly better than a simple tfidf word embedding,  the difference was very small ~0.003 and it took 2.46 times longer than simpler word only embeddings. mpnet also was significantly better but also by only 0.003 but took 76 times as long. So the choice was to stick with a simpler tfidf word only embeddings, which would be faster, easier to maintain and would make it easier to interpret models over the them.  



Traditional ML models can perform well with classifying short simple text, especially since descriptions in the accounts will normally have less variety than generic free text. 

A deep neural network can be trained to categorise descriptions, and has the advantage of being able to learn patterns beyond that of a fixed algorithm used in transitional ML. 

There are a number of BERT based models. These models have been pre-trained, so have a lot of semantic understanding baked in. But many BERT models are trained on generic text,  SEC-BERT is a model that was trained on SEC filing(financial filings), so should have better semantic understanding of accountancy terms and concepts, which is very appropriate here in this use case where we are classifying descriptions in financial documents. 

It is expected that a frontier LLM would have the best semantic understanding, but it is likely to be excessive for this use case. A LLM would be good at understanding lots of text, but we just have short phrases and small sentences at most. There are additional technical, data security and governance issues around using an API. So a LLM based approach was not used.


# Implementation - performance metrics.

The final pipelines used TFIDF(1-3 word ngrasms, min_df 1, norm l2) with LinearSVC(penalty l1, C 2.8, loss squared_hinge, dual False, class_weight balanced, max_iter 10000) from scikit-learn. 

I calculated confidence intervals using a bootstrap method. 

The model was trained across a 1%, 10%, 100% train population plus also 10% square root weighted population. The 10% sqrt weighted train population resulted in 1.3pp better f1-macro score but 0.0573pp lower accuracy, compared to 10% population. But training on the full 100% population resulted in the best f1-macro and accuracy, and would have the simplest pipeline. 

Optuna was used with NN and transformer based models. This has the benefit over the fairly manual approach used with scikit-learn. Optuna has built in visualisation around hyper parameters and automatically tuns the hyperparameters. In the future I will also use Optuna with sci-kit learn models. 

DNN, LSTM, GRU, CNN, BI neural networks were tested, with CNN doing best. 

Various transformer based models were tested, roberta-base, nlpaueb/sec-bert-base, sentence-transformers/all-mpnet-base-v2, and sentence-transformers/all-MiniLM-L6-v2. Various combinations of using weighted models, sqrt weighted training data and random oversampling were tried. Using sqrt weighted training data has the best f1-macro score. 

# Results.

Model robustness was tested over various categories, abbreviations, adversarial(So phrased to be misleading), command(command to inject LLM), contextual(semantically the same), long context, ocr issues, synonyms, typos, unicode and variations. 

Overall LinearSVC outperformed SEC-BERT in robustness testing, which was unexpected since I would have expected the domain specific training and better semantic meaning would it would have done better overall. Also the areas where LinearSVC did worse like typos and variations would be rare over real data, since accountancy documents are primarily generated by computers, rather than people typing every description. 

Looking at the coefficients of the LinearSVC helps interpreting how the model arrived at what it did, but it's not possible to do anything similar with SEC-BERT. 

But there are tools like LIME and SHAP which do work on SEC-BERT and help with the explainability with both CNN and FFSEC-BERT but also LinearSVC. They can provide insights beyond the coefficients alone. 

Residual analysis, confusion matrix is useful to see what kinds of mistakes the model is making for the different concepts.  Many issues relate to there not being enough distinguishing information in the description, so it would classify based on the most common concept associated with that description, but the testing dataset has example of that description being associated with different concepts. So this isn't a limit of the model. In some situations it means the description alone isn't enough data to categorise the item, so in later iterations additional features of the table name and heading were also included which improved f1-macro from x to y. 

Performance was balanced by infrastructure/costs, where selecting faster models that could run quickly on a CPU were prioritised allowing development on existing infrastructure.

SME also provided input explaining how that in some cases there simply isn't enough information at all in the accounts to predict the specific concept used. 

To compare the model architectures a decision matrix was used. This covered 8 objective measures such as f1-macro and train time and 6 subjective measures such as interpretability and deployment simplicity. Each measure was weighted and adjustments were made if there were overlapping confidence intervals. With a rubric setting the standard/scores for the the subjective scores with an accompanying narrative. So factors like simplicity, interpretability, maintenance burden, deployment simplicity, model size, train time outweighed pure f1-macro scores. 

Performance was balanced by infrastructure/costs, where selecting faster models that could run quickly on a CPU were prioritised allowing development on existing infrastructure.

I chose LinearSVC over transformer based models, trading marginal performance gains(2.3pp) for a solution that is simpler(more maintainable), more explainable(feature coefficients), quicker(13x), allows development on existing infrastructure, with the ability to scale cost effectively.

The result is a dataset that reduces manual effort 
# Discussion and conclusions/recommendations.

Separate models for every taxonomy would give the best raw performance, but I used a single taxonomy for each document type, resulting in consistent class names, to increase analyst usability.

To scale we would need additional infrastructure, but to be cost effective we setup on-demand-compute, which allows us to fire up an EC2 instance just for a job and close it when finished.
# Summary of findings.
# Implications.

Hubble helped us meet our quality standards, such as completeness and consistency since we can extract all of the figures and have consistent ML classes.

The business value is that it reduces manual effort, allows us to better create statistics that informs and drives government policy and better identify risks. It's been used in projects where hundreds of billions of pounds of incorrect figures in returns have been identified. 

# Caveats and limitations.

# Appendices.
## Code and documentation used for the project.
## Statistical rigour: uncertainty, bias, and error estimates where appropriate.
## Figures, tables, and visualisations.
## Mapping of the project report to AM1 KSBs.
## Employer verification that the report reflects my own involvement and work.