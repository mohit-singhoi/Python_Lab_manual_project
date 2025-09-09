#Q. 11 Use visualization techniques (heatmaps) to explore dataset patterns.

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# from sklearn.datasets import load_iris

# # Load Iris dataset
# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)

# # Compute correlation matrix
# correlation = df.corr()

# # Plot heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Heatmap of Feature Correlations - Iris Dataset")
# plt.show()





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Area': [1200, 1500, 2000, 1000],
    'Bedrooms': [2, 3, 4, 2],
    'Bathrooms': [1, 2, 3, 1],
    'Price': [180, 220, 300, 160]
}

df = pd.DataFrame(data)

# Create a correlation matrix
corr_matrix = df.corr()

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

