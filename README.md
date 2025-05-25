# Spam-classifier
Dataset

My dataset is a CSV file, which contains SMS messages labeled as either Spam or Ham. There are two columns, one is label which represent, whether the message is spam or ham and the other one is texxt, which contains the SMS message.

I dropped the irrelevant columns named, Unnamed: 2, Unnamed: 3 and Unnamed: 4 and then renamed the remaining columns to Label and Text.



Preprocessing

All the characters where first converted to lowercase. All digits were removed using the regular expression. All punctuation symbols were also removed.

The dataset was balanced, as one label was more then the other, so that we can avoid the bias of the model towards that class.



Model

TF-IDF Vectorizer: Converts text into numbers based on how often those words appear in a message vs. across the entire messages.

Multinomial Naive Bayes Classifier: A fast machine learning algorithm which is used for text classification.

The dataset was split into two parts: 80% for training and 20% for testing



Performance Metrics

Precision,Recall,F1-Score and Accuracy were used to evaluate the model. These metrics helps us to understand how well the model is in identifying spam and non-spam messages.

