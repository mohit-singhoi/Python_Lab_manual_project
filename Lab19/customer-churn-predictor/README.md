# 📉 Customer Churn Prediction

This project is an end-to-end machine learning web application that predicts whether a telecom customer is likely to churn (leave the service) based on their profile and service usage details. It includes data preprocessing, model training using `RandomForestClassifier`, and a user-friendly web interface built with Streamlit.

---

## 🚀 Features

- Clean and efficient preprocessing pipeline
- Binary classification model (Will Churn / Will Stay)
- Streamlit-based interactive web app
- Real-time prediction using user inputs
- Feature engineering and one-hot encoding
- Model and feature persistence using `joblib`

---

## 🗂️ Project Structure

customer-churn-predictor/
├── data/
│ └── Telco-Customer-Churn.csv
├── model/
│ ├── churn_model.pkl
│ └── feature_names.pkl
├── utiles/
│ └── preprocessing.py
├── app.py
└── README.md



💡 How It Works
The user provides customer details in the web form.

The input is preprocessed and transformed to match the training format.

The trained model makes a prediction.

The result is displayed as:

✅ Will Stay

❌ Will Churn



🧠 Technologies Used
Python 🐍

Pandas

Scikit-learn

Joblib

Streamlit 🎈