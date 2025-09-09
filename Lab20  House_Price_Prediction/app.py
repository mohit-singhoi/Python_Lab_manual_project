import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample dataset
data = {
    'Area': [1000, 1500, 2000, 2500, 3000, 1300, 1250, 1400, 1600, 1700, 1350, 1450, 1550, 1650, 1750],
    'Price': [150000, 200000, 250000, 300000, 350000, 160000, 150000, 190000, 220000, 240000, 155000, 165000, 175000, 185000, 195000],
    'Bedrooms': [2, 3, 4, 4, 5, 2, 2, 3, 3, 4, 2, 3, 3, 4, 5],
    'Bathrooms': [1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 1, 2, 2, 3, 3],
    'Age': [10, 15, 20, 5, 8, 12, 14, 16, 18, 19, 11, 13, 17, 21, 22]
}
df = pd.DataFrame(data)

# Split data
X = df[['Area', 'Bedrooms', 'Bathrooms', 'Age']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title("🏡 House Price Prediction App")
st.write("Enter the house details to predict the price In Delhi NCR.")

# Input fields
area = st.slider('Area (sq.ft)', 500, 4000,5000, 1500)
bedrooms = st.selectbox('Number of Bedrooms', [1, 2, 3, 4, 5])
bathrooms = st.selectbox('Number of Bathrooms', [1, 2, 3])
age = st.slider('Age of House (years)', 0, 100, 10)

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame([[area, bedrooms, bathrooms, age]], columns=['Area', 'Bedrooms', 'Bathrooms', 'Age'])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Price: ${prediction:,.2f}")

import joblib
joblib.dump(model, 'house_price_model_NCR.pkl')