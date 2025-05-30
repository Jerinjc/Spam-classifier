import numpy as np
import pandas as pd
import re
import string
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv("C:/Users/Lenovo LOQ/OneDrive/Desktop/spam (1).csv", encoding='latin-1')

# Drop unnecessary columns
data = data.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])

# Rename columns
data.columns = ['Label', 'Text']

# Ensure correct label mapping
data['Label'] = data['Label'].map({'spam': 'spam', 'ham': 'ham'})

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    return text

# Apply text preprocessing
data['Clean_Text'] = data['Text'].apply(preprocess_text)

# Balance the dataset (equal number of spam and ham messages)
spam_data = data[data['Label'] == 'spam']
ham_data = data[data['Label'] == 'ham'].sample(len(spam_data), random_state=42)  # Equalizing the classes

balanced_data = pd.concat([spam_data, ham_data])

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    balanced_data['Clean_Text'], balanced_data['Label'], test_size=0.2, random_state=42
)

# Define a pipeline with TF-IDF vectorizer and Naive Bayes classifier
spam_filter = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
spam_filter.fit(X_train, y_train)

# Evaluate the model
y_pred = spam_filter.predict(X_test)
classification_rep = classification_report(y_test, y_pred)
print("Classification Report:\n", classification_rep)

# Save the trained model
with open("spam_classifier.pkl", "wb") as model_file:
    pickle.dump(spam_filter, model_file)

# Save the vectorizer separately
with open("vectorizer.pkl", "wb") as vectorizer_file:
    pickle.dump(spam_filter.named_steps['vectorizer'], vectorizer_file)

print("✅ Model and vectorizer saved successfully!")
