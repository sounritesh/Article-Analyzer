import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from re import sub
import pickle5 as pickle

data_set = pd.read_csv("Language Detection.csv")

## splitting samples and labels
samples = data_set["Text"]
labels = data_set["Language"]

## encoding labels
encoder = LabelEncoder()
enc = encoder.fit(labels)
y = enc.transform(labels)

print(enc.classes_)

## print dist
y_df = pd.DataFrame(y)

sample_text_list = []
## cleaning text samples
for text in samples:
    text = sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    text = sub(r'[[]]', ' ', text)
    text = text.lower()
    sample_text_list.append(text)

## vectorizing samples
vectorizer = CountVectorizer()
vect = vectorizer.fit(sample_text_list)
X = vect.transform(sample_text_list).toarray()

## splitting testing and training  data
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model training
model = MultinomialNB()
model.fit(x_train, y_train)

# prediction and model evaluation (testing)
test_predictions = model.predict(x_test)

accuracy = accuracy_score(y_test, test_predictions)
pickle.dump(vect, open('language_detection_dict.sav', 'wb'))
pickle.dump(model, open('language_detection_model.sav', 'wb'))
pickle.dump(enc, open('language_detection_classes.sav', 'wb'))