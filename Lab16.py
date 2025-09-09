#Q.16 Implement k-NN for classification problems and find the optimal k value.

# Step 1: Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load the Iris Dataset

iris = load_iris()
X = iris.data
y = iris.target


# Step 3: Split the Dataset into Training and Testing Sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Step 4: Train the K-Nearest Neighbors Classifier
# Train and Test with Different k values

k_values = range(1, 21)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)


# Step 5: Plot the Accuracy vs. k Values

plt.figure(figsize=(10,6))
plt.plot(k_values, accuracies, marker='o', linestyle='--', color='b')
plt.title("Accuracy vs. K Value")
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.xticks(k_values)
plt.grid(True)
plt.show()


# Step 6: Find the Best k Value
# Find optimal k value based on accuracy

optimal_k = k_values[np.argmax(accuracies)]
print("Optimal k value:", optimal_k)
print("Highest Accuracy:", max(accuracies))


