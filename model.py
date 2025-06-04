import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("faq.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

df["question_clean"] = df["question"].apply(clean_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["question_clean"])

model = NearestNeighbors(n_neighbors=1, metric="cosine")
model.fit(X)

def get_response(user_question):
    user_clean = clean_text(user_question)

    # Salutations simples
    greetings = ["bonjour", "salut", "coucou", "bonsoir", "hello", "hey"]
    wellbeing = [
        "comment ça va", "ça va", "tu vas bien", "vous allez bien",
        "quoi de neuf", "bien ou quoi"
    ]

    if any(greet in user_clean.split() for greet in greetings):
        return "Bonjour ! Comment puis-je vous aider ? 😊"

    if any(phrase in user_clean for phrase in wellbeing):
        return "Je vais bien, merci ! Et vous ? 😊"

    user_vec = vectorizer.transform([user_clean])
    distance, index = model.kneighbors(user_vec)
    return df.iloc[index[0][0]]["answer"]
