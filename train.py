# ---------------------- IMPORTS ----------------------
import pandas as pd
import re, string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import pickle
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# ---------------------- LOAD DATA ----------------------
df = pd.read_csv("../data/spam_ham_emails_fr_500.csv")  # dataset

df = df[['label', 'emails']].rename(columns={'emails':'text'})

encoder = LabelEncoder()
df['label'] = encoder.fit_transform(df['label'])

# ---------------------- CLEAN TEXT FUNCTION ----------------------
def clean_text(t):
    t = t.lower()
    t = re.sub(r"http\S+", " ", t)
    t = t.translate(str.maketrans("", "", string.punctuation))
    t = re.sub(r"\d+", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()

df['text'] = df['text'].apply(clean_text)

# ---------------------- SPLIT ----------------------
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# ---------------------- PIPELINE TF-IDF + LOGISTIC ----------------------
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words=stopwords.words('french'))),
    ('clf', LogisticRegression(max_iter=200))
])

model.fit(X_train, y_train)

# ---------------------- SAVE ARTIFACTS ----------------------
import os
os.makedirs("../artifacts", exist_ok=True)

with open("../artifacts/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("../artifacts/encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("✅ Model and encoder saved in artifacts/")