#Q.17 Apply k-Means clustering on an unlabeled dataset and visualize cluster formation.

# Step 1: Import Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# Step 2: Generate or Load an Unlabeled Dataset

# Create sample data with 3 centers
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)

# X is unlabeled data (we ignore the labels returned by make_blobs)


# Step 3: Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Get cluster labels for each point
labels = kmeans.labels_

# Get coordinates of cluster centers
centroids = kmeans.cluster_centers_


# Step 4: Visualize Cluster Formation
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o')
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X')  # Cluster centers
plt.title("k-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
