# Spam Classifier

## Dataset

My dataset is a CSV file containing SMS messages labeled as either **Spam** or **Ham**.  
It has two important columns:  
- **Label**: Indicates whether the message is spam or ham  
- **Text**: Contains the actual SMS message  

I dropped irrelevant columns named `Unnamed: 2`, `Unnamed: 3`, and `Unnamed: 4`,  
then renamed the remaining columns to `Label` and `Text`.

---

## Preprocessing

- Converted all characters to **lowercase**  
- Removed all **digits** using regular expressions  
- Removed all **punctuation symbols**  
- Balanced the dataset by equalizing the number of spam and ham messages to avoid model bias toward one class

---

## Model

- **TF-IDF Vectorizer**: Converts text into numerical features based on the frequency of words in a message relative to the entire dataset  
- **Multinomial Naive Bayes Classifier**: A fast and effective algorithm used for text classification  

The dataset was split into:  
- **80% for training**  
- **20% for testing**

---

## Performance Metrics

The model was evaluated using:  
- **Precision**  
- **Recall**  
- **F1-Score**  
- **Accuracy**  

These metrics help us understand how well the model identifies spam and non-spam messages.

---

## Author

**Jerin John Chacko**  
MSc Data Analytics  
Digital University Kerala  

GitHub: [@jerinjc](https://github.com/jerinjc)
