#Q.13 Train a Linear Regression model on a dataset (e.g., house price prediction) and evaluate performance.

#Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Create or Load the Dataset
data = {
    'Area': [1000, 1500, 2000, 2500, 3000,1300,1250, 1400, 1600, 1700,1350, 1450, 1550, 1650, 1750],
    'Price': [150000, 200000, 250000, 300000, 350000, 160000, 150000, 190000, 220000, 240000,155000, 165000, 175000, 185000, 195000],
    'Bedrooms': [2, 3, 4, 4, 5, 2, 2, 3, 3, 4, 2, 3, 3, 4, 5],
    'Bathrooms': [1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 1, 2, 2, 3, 3],
    'Age': [10, 15, 20, 5, 8, 12, 14, 16, 18, 19, 11, 13, 17, 21, 22]  # Age of the house
}

df = pd.DataFrame(data)

# Step 3: Data Preprocessing
# Check for missing values
if df.isnull().values.any():
    print("Missing values found. Filling missing values with mean.")
    df.fillna(df.mean(), inplace=True)
    
# Convert categorical variables to numerical if necessary

# Step 4: Feature Selection
X = df[['Area', 'Bedrooms', 'Bathrooms', 'Age']]  # Features
y = df['Price']  # Target variable

# Step 5: Split the Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Create and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# step 9: Plot actual vs predicted prices
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Ideal Fit')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.grid(True)
plt.show()

# Step 11: Save the Model (Optional)
import joblib
joblib.dump(model, 'house_price_modelQ13.pkl')

