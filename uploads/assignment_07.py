# Assignment 7: Feature Engineering - Polynomial Features
# Create polynomial features for a regression model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Synthetic dataset
X = np.array([[1], [2], [3], [4]])

# Create polynomial features
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Error: Incorrectly accessing feature names
print(poly.feature_names)  # Error: Should use get_feature_names_out()
print(X_poly)