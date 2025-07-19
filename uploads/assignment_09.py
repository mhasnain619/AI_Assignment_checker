# Assignment 9: PCA for Dimensionality Reduction
# Apply PCA to reduce dimensions of a dataset
from sklearn.decomposition import PCA
import numpy as np

# Synthetic dataset
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Apply PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Error: Accessing undefined attribute
print(pca.explained_variance)  # Should be explained_variance_ratio_
print(X_reduced)