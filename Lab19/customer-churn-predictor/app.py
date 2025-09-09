import streamlit as st
import pandas as pd
import joblib

# Load model and feature columns
model = joblib.load('./model/churn_model.pkl')
feature_names = joblib.load('./model/feature_names.pkl')

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📉 Customer Churn Prediction App")
st.markdown("Provide customer info to predict churn likelihood.")

# UI Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges")
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

# Preprocess inputs
input_data = {
    'gender': [gender],
    'SeniorCitizen': [1 if senior == "Yes" else 0],
    'tenure': [tenure],
    'MonthlyCharges': [monthly],
    'Contract': [contract],
    # Add all required features
}

df = pd.DataFrame(input_data)
df = pd.get_dummies(df)
df = df.reindex(columns=feature_names, fill_value=0)

if st.button("Predict Churn"):
    prediction = model.predict(df)[0]
    label = "❌ Will Churn" if prediction == 1 else "✅ Will Stay"
    st.success(f"Prediction: {label}")
