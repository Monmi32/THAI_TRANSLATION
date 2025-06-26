import os
import json
from googletrans import Translator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

MEMORY_FILE = "memory.json"
translator = Translator()
vectorizer = TfidfVectorizer()
model = MultinomialNB()
is_model_trained = False

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        learned_translations = json.load(f)
else:
    learned_translations = {}

def save_learned_translations():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(learned_translations, f, ensure_ascii=False, indent=2)

def train_learning_model():
    global is_model_trained
    if not learned_translations:
        is_model_trained = False
        return
    X = vectorizer.fit_transform(learned_translations.keys())
    y = list(learned_translations.values())
    model.fit(X, y)
    is_model_trained = True

train_learning_model()
