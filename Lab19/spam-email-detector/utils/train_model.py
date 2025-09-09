# utils/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

def train_spam_detector():
    # Load dataset
    data_path = os.path.join('Q.19\spam-email-detector\data\spam.csv')
    try:
        df = pd.read_csv(data_path, encoding='latin-1')[['v1', 'v2']]
    except FileNotFoundError:
        print(f"❌ Error: Dataset not found at '{data_path}'. Make sure the CSV file exists.")
        return
    except Exception as e:
        print(f"❌ Unexpected error while loading dataset: {e}")
        return

    # Rename columns
    df.columns = ['label', 'message']

    # Encode labels: ham = 0, spam = 1
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], df['label'], test_size=0.2, random_state=42
    )

    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train Naive Bayes classifier
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # Save model and vectorizer
    model_dir = os.path.join('model')
    os.makedirs(model_dir, exist_ok=True)

    joblib.dump(model, os.path.join(model_dir, 'spam_model.pkl'))
    joblib.dump(vectorizer, os.path.join(model_dir, 'vectorizer.pkl'))

    print("✅ Model and vectorizer saved successfully in ./model/")

# Run script directly
if __name__ == "__main__":
    train_spam_detector()
