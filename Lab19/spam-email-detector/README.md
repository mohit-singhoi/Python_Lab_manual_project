# 📧 Spam Email Detection with Machine Learning

This project is an end-to-end machine learning solution for detecting spam SMS messages using natural language processing (NLP) techniques and a Naive Bayes classifier. It includes data preprocessing, model training, and a user-friendly Streamlit web interface for prediction.

---

## 🔍 Features

- Preprocessing of SMS text data
- TF-IDF vectorization
- Naive Bayes classification model
- Model saving/loading with `joblib`
- Streamlit web app for real-time prediction

---

## 📁 Project Structure

spam-email-detector/
├── data/
│ └── spam.csv # Dataset (2000 rows of ham/spam)
├── model/
│ ├── spam_model.pkl # Trained model
│ └── vectorizer.pkl # TF-IDF vectorizer
├── utils/
│ └── train_model.py # Model training script
├── app.py # Streamlit app for prediction
├── requirements.txt # Dependencies
└── README.md # Project 

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python utils/train_model.py
streamlit run app.py



---

### ✅ 6. **How to Run the App**

```bash
# Step 1: Train the model
python utils/train_model.py

# Step 2: Launch the Streamlit app
streamlit run app.py

