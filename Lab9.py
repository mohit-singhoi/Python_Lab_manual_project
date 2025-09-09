# Q.9 Normalize and regularize numerical features.

# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# # Sample data
# data = {'Height': [150, 160, 170, 180, 190],
#         'Weight': [50, 65, 80, 90, 100]}
# df = pd.DataFrame(data)

# # Min-Max Normalization
# min_max_scaler = MinMaxScaler()
# normalized = min_max_scaler.fit_transform(df)
# normalized_df = pd.DataFrame(normalized, columns=['Height', 'Weight'])

# print("Min-Max Normalized Data:")
# print(normalized_df)

# # Z-Score Standardization
# standard_scaler = StandardScaler()
# standardized = standard_scaler.fit_transform(df)
# standardized_df = pd.DataFrame(standardized, columns=['Height', 'Weight'])

# print("\nZ-Score Standardized Data:")
# print(standardized_df)


from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
import numpy as np

# Simple synthetic data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 1.3, 3.75, 2.25])

# Ridge Regression (L2)
ridge = Ridge(alpha=1.0)
ridge.fit(X, y)
print("\nRidge Coefficient:", ridge.coef_)

# Lasso Regression (L1)
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)
print("Lasso Coefficient:", lasso.coef_)
