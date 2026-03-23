Journal when due not set

Part 2 should be end of Term 4 not Term 3

Choose course, maybe choose AWS or maybe Azure

Do some internet search on the provider. Cover ML and include deep learning. Facilities on the cloud and why it's useful.

Our own organisation and whether that cloud would be useful there as well.

Propose application that would be of benefit to you, needs to have deep learning on it.

Using different processing unit's CPU/GPU/TPU, might need to do just that bit on google colab.

Raw data doesn't need to be provided, but they like some samples.

Error, bias and uncertainty will be on the final test, so it's important to cover

How to deploy and how it would fit in with everything else. Does it feed into another system.

Deep learning is more than one hidden layer

2.2

Data sourcing

Your data for analysis may reside in various underlying systems in your infrastructure or may include external data such as social media. You may use APIs or languages like SQL to source individual records or you may bulk extract files via down/up loading.

Data preparation

This stage usually takes the longest. You need to decide which elements of the data to use, then dice, slice and/or link, to make your analytics data set. You may need to clean the data, sort out anomalies, handle missing values and scale the data fields you will be using. Typical preparation tasks can include:

- Removing outliers
- Handling missing values
- Scaling
- One-hot encoding

Training

The data set following preparation needs to be split into training and testing sets. You can decide what percentage of records to use for training and what percentage for testing – packages provide simple functions for splitting the data.

Training refers to the process of using the training dataset to teach an algorithm to make predictions or decisions by adjusting its internal parameters.

Validation/optimisation

When training the model, it is good practice to keep some records back for the final test, i.e., split the data three ways to have a training set, validation set, and final testing set. The training set is used to train the model, the validation set is used to tune the model's hyperparameters and make decisions about model selection, and the test set is used to provide an unbiased evaluation of the final model's performance.

This split ensures that the model is properly trained, tuned, and tested on separate subsets of data, enhancing its ability to generalise to new, unseen data. The Python functions for splitting data however assume a one-way split (training and testing sets) so the keeping back of the final test data would need to be done at the start before entering the main testing and training phase.

Testing

Testing involves evaluating the trained model's performance using the testing dataset, which also contains input-output pairs but was not used during training. This helps to assess how well the model generalises to new, unseen data.

Various hyperparameters can also be experimented with, with the aim of improving results.

Deployment

Following training and testing, if you have satisfactory results, you can deploy the model. Deployment might involve developing suitable interfaces for the intended users and training the users. This phase might be passed to a delivery team, although the data scientist is likely to be needed for consultation.

Review

From time to time, the model needs to be reviewed. As the world changes, the model may no longer be suitable, and therefore the model will need to be updated by repeating the whole process.

The existence of such a clear pipeline has led to the development of high-level interfaces for machine learning solution development. Deep learning frameworks are an example of this, and they are quite plentiful – single functions or commands can often be used for many of the operations in the pipeline.

From <[https://app.qa.com/course/topic-4-deep-learning-frameworks-ai-1698/machine-learning-pipelines/?context_id=15077&context_resource=lp](https://app.qa.com/course/topic-4-deep-learning-frameworks-ai-1698/machine-learning-pipelines/?context_id=15077&context_resource=lp)>

from sklearn.metrics import classification_report

print(classification_report(y_test_class, y_pred_class))

confusion_matrix(y_test_class, y_pred_class)

kernel_initializer='he_normal'

So in plain terms: he_normal initializes weights with random values from a normal distribution, scaled in a way that works best for ReLU-like activations.