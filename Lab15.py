#Q15. Train and visualize a Decision Tree model for classification tasks.

# Step 1: Import Required Libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Step 2: Load the Iris Dataset 

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Step 3: Split the Dataset into Training and Testing 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train the Decision Tree Classifier

clf = DecisionTreeClassifier(criterion='entropy', random_state=42)  # or use criterion='gini'
clf.fit(X_train, y_train)

#  Step 5: Make Predictions (Optional)

y_pred = clf.predict(X_test)

# Step 6: Visualize the Decision Tree
plt.figure(figsize=(12,8))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.title("Decision Tree Visualization")
plt.show()



# Step 7: Evaluate the Model (Optional)
accuracy = clf.score(X_test, y_test)
print(f"Accuracy of the Decision Tree Classifier: {accuracy:.2f}")

