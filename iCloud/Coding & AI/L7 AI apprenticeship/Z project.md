
Talk about database, 1NF not 2NF or 3NF.  Performance want to just use a single table most of the time. 3NF adds a lot of overhead to analystical work both in terms of having to join them, performance of joins, etc.

Normalise for correctness, denormalised for performance & usability


- ~~Data analysis of the distribution
- Different taxonomies
- Lemmatisation, synonym mapping, embeddings, data augmentation, stemming
	- lemmatisation would also be stuff like deposits -> deposit
	- synonym mapping would be using show_overlap_similarity so map items that are semantically similar but textually different. It reduces noise.
- ~~31 March 1982
- features, table name, description, heading, value type text/numeric
- ~~Rare classes
- TFIDF 1-3 ngrams, word breakdown for  vs SBERT and other embeddings
- SVM, NN, BERT
- Stratified cross-validation
- Random/grid search
- Macro f1
- Confusion matrix
- 
- Maybe graph accuracy over different population sizes, where does it level off.
- 
- weighted balance, over sampling
- Different types of presentations, headline figures, technical terms with illustration and appendix with technical details. Confusion matrixes and errors
- Gitlab instructions

- Select training data that is representative of the whole population
- Check results for bias
- Apply fairness tests
- Continue to monitor ML systems in operational to ensure they continue to perform well and fairly
- 


NN has hyperparameters like the dimension and NN size which would be specific to the input dimension and number of classes, with larger datasets the number of classes could be increased since there would be sufficient population of the minor classes. Also input text size would increase. But it's not possible to do hyperparameter testing on such a large dataset. Which would make it a bit of a guessing game. 

Denormalisation. Where you include redundant copies of data in multiple tables. Means you don't need to join as many tables together. 

TFIDF outperformed BERT when using SVM

[https://aclanthology.org/2020.aespen-1.6/](https://aclanthology.org/2020.aespen-1.6/)