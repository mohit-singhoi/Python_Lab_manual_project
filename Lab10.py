#Q. 10 Use visualization techniques (histograms to explore dataset patterns.

# import pandas as pd
# import matplotlib.pyplot as plt

# # Sample dataset
# data = {
#     'Age': [22, 25, 27, 25, 29, 30, 32, 35, 40, 45, 50, 55, 60, 65, 70]
# }
# df = pd.DataFrame(data)

# # Create histogram
# plt.hist(df['Age'], bins=8, color='skyblue', edgecolor='black')

# # Add titles and labels
# plt.title('Histogram of Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Plot histogram for all features
df.hist(bins=10, figsize=(10, 6), color='lightgreen', edgecolor='black')
plt.suptitle("Histogram of Iris Dataset Features")
plt.show()

