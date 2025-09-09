# Q.14 Implement Logistic Regression to classify a dataset (e.g., predicting student pass/fail).

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Create the Dataset
data = {
    'StudyHours': [1, 2, 1.5, 3, 5, 6, 1, 4, 2.5, 3.5, 5.5, 6.5, 0.5, 3, 4.5],
    'Attendance': [60, 65, 55, 75, 90, 95, 50, 85, 70, 80, 92, 96, 45, 78, 88],
    'Pass':       [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
}
df = pd.DataFrame(data)

# Step 3: Feature and Target
X = df[['StudyHours', 'Attendance']]
y = df['Pass']

# Step 4: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 5: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", report)

# Step 8: Visualization (optional for 2D)
plt.figure(figsize=(8,6))
plt.scatter(df['StudyHours'], df['Attendance'], c=df['Pass'], cmap='bwr', edgecolors='k')
plt.xlabel('Study Hours')
plt.ylabel('Attendance (%)')
plt.title('Pass/Fail Classification')
plt.grid(True)
plt.show()


#🔵 Blue points = Students who failed

#🔴 Red points = Students who passed
