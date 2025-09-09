import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

def preprocess_and_train():
    # Load dataset
    df = pd.read_csv('customer-churn-predictor\data\Telco_Customer.csv')

    # df = pd.read_csv('Telco-Customer-Churn.csv')


    # Drop customerID column
    df.drop(['customerID'], axis=1, inplace=True)

    # Handle missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.fillna(method='ffill', inplace=True)

    # Encode target variable
    df['Churn'] = LabelEncoder().fit_transform(df['Churn'])

    # One-hot encoding for categorical features
    df = pd.get_dummies(df)

    # Features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Ensure model directory exists
    os.makedirs('./model', exist_ok=True)

    # Save model and features
    joblib.dump(model, './model/churn_model.pkl')
    joblib.dump(X.columns.tolist(), './model/feature_names.pkl')

    print("✅ Model and feature names saved successfully.")

# Run function
if __name__ == "__main__":
    preprocess_and_train()
