# app.py
import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('./model/spam_model.pkl')
vectorizer = joblib.load('./model/vectorizer.pkl')

st.set_page_config(page_title="📧 Spam Email Detector")
st.title("📧 Spam Email Classifier")
st.markdown("Enter a message to classify it as spam or not.")

# User input
user_input = st.text_area("✉️ Enter your message:")

if st.button("Predict"):
    if user_input.strip():
        # Transform input
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        label = "❌ Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: **{label}**")
    else:
        st.warning("Please enter a message.")
# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [A Developer]")
