
# Introduction and background.


# Outline of the issue or opportunity and the business problem to be solved.

HMRC receives company accounts and tax computations which are in iXBRL format, which are semi-structured (x)HTML documents. The key items in those document are tagged with a concept from a fixed taxonomy, which makes it easy for software to extract and structure tagged items. 

Tax computations have only about 30% of the figures tagged, which means that existing workflows can't profile across 70% of the figures in these documents. There are various reasons for this, ranging from poor software support to people deliberately leaving items related to fraud untagged. 

The data in these documents is crucial for creating profiles to identify customers where there is a higher risk that they owe more tax than declared. The data is also used to form statistics used to inform government policy. Having most of the data in the tax computations untagged means that profiles don't have the data to properly identify high tax risk return. We were also unable to provide accurate data or statistics for policy or the government to make informed decisions. 

The existing systems to extract iXBRL data, require complex and long updates to processes and schemas every year when new taxonomies come out. The wide database format is also hitting the limits of the Oracle database. It can take up to 9 months for the updates, but HMRC only have 12 months to open an enquiry, leaving little time for profiling and opening an enquiry in time. 

Hubble is a tool I develop that initially extracted untagged figures and their associated descriptions. People can describe items in lots of different ways with no fixed taxonomy. Initial data analysis required lots of complex regular expressions and working with SME due to the domain-specific terminology, which was error prone, incomplete and time-consuming. 

We wanted to make the output data easier to profile across in a more reliable way. Can we categorise those items using ML, allowing analysts to use those ML categories to select the items they are interested in. 
# Methods used and justification.

The primary feature is a free text "description". So this is text classification problem. While most figures are untagged, 30% of figures are tagged and due to the volume of the total data, this means that we can train the model on the 30% of tagged data, so it is a supervised multi-class classification problem.  

The descriptions are normally just a word or a short phrase, but are have domain-specific terminology. There were two main methods used to embed the descriptions, TFIDF and vector embeddings. TFIDF extracts character and word n-grams, this can work well since it captures domain specific terminology and phrasing well and works well with a variety of models with good speeds and performance. Vector embeddings capture more of the semantic meaning of phrases so should capture phrases that have similar meaning even if the words are different, which should improve classification especially on unseen descriptions. 

There are a range of possible models that deal with text such as using traditional ML such as Naive Bayes and SVM; training a deep neural network from scratch; fine tuning a larger transformer based model locally; using a frontier LLM and fine tuning it via an API. 

Traditional ML models can perform well with classifying short simple text, especially since descriptions in the accounts will normally have less variety than generic free text.

A deep neural network can be trained to categorise descriptions, and has the advantage of being able to learn patterns beyond that of a fixed algorithm used in transitional ML. 

There are a number of BERT based models. These models have been pre-trained, so have a lot of semantic understanding baked in. But many BERT models are trained on generic text,  SEC-BERT is a model that was trained on SEC filing(financial filings), so should have better semantic understanding of accountancy terms and concepts, which is very appropriate here in this use case where we are classifying descriptions in financial documents. 

It is expected that a frontier LLM would have the best semantic understanding, but it is likely to be excessive for this use case. A LLM would be good at understanding lots of text, but we just have short phrases and small sentences at most. There are additional technical, data security and governance issues around using an API. So a LLM based approach was not used.

# The scope of the project (including key performance indicators).

The project covers understanding the business issue and what they would like to do. 

Understanding current issues with iXBRL extraction and storage. 

Extracting relevant data such as description, headings, table names, structural data(table number, row number, column number), iXBRL data(concept, dimensional data) and value. 

Processing and formatting data.

Developing ML model to categorise the data. 

Saving the data into an Oracle database to allow analysts to profile across it in bulk.

Setup a reliable architecture that would automate the end extraction, categorisation and storing of data. 

Key performance indicators would be f1-macro, accuracy, precision, recall, train time, inference time, explainability and interpretability. 


# Data selection, collection and pre-processing.

HMRC's systems are locked down, making doing exploratory work trying different models difficult. Also there isn't quick easy access to a GPU device for more the more complex models. 

So the public company accounts submitted at companies house, which are iXBRL format were used for the exploratory phase since that could be done on a standalone device with a GPU. The  accounts submitted in November 2015 were used. Using all the returns submitted in a month makes the data more representative. 

For the implementation phase the company accounts and tax computations submitted to HMRC were used. 

I extracted key data such as the description, heading, table name, iXBRL concept, iXBRL dimensional data, references, footnotes and structural data. 

The text features like description were cleaned, lowercasing and replacing special characters with spaces. But testing showed that replacing forward slashes with spaces actually reduced performance, so it was dropped. 

I canonicalised the feature, so most dates were replaced by a placeholder "hubble_date", except for 31 March 1982, which subject matter experts explained has a special meaning for tax so that was replaced with "hubble_date_1982_03_31". Similarly company names, individual names, postcodes and numbers were replaced by placeholders. This improves model performance, since it reduces a lot of the noise. Removing personal data like individual names enhances data security since personal data is removed and not used in latter steps.

Then there was some label engineering, where the feature a placeholder by itself, then the label was changed to reflect that. e.g. if a description is just hubble_number, then the label would be changed to be HubbleNumber. The reason for this is that placeholders by themself don't contain enough information to predict a category, but knowing the type could be useful to know. 

Then filtered for where there is at least 2 characters and less than 16 words in the description.

I removed data that had concepts related to names or addresses. 



# Survey of potential alternatives.

Regex. 

Manual deterministic flow

LLM.

Does this include stuff like CNN/SEC-BERT which I tried but didn't select? - Yeh probably, wouldn't fit elsewher.
# Implementation - performance metrics.
# Results.
# Discussion and conclusions/recommendations.
# Summary of findings.
# Implications.
# Caveats and limitations.

# Appendices.
## Code and documentation used for the project.
## Statistical rigour: uncertainty, bias, and error estimates where appropriate.
## Figures, tables, and visualisations.
## Mapping of the project report to AM1 KSBs.
## Employer verification that the report reflects my own involvement and work.