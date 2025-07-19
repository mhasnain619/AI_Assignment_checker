# Assignment 4: Linear Regression on Synthetic Data
# Build a linear regression model to predict house prices
import numpy as np
from sklearn.linear_model import LinearRegression

# Synthetic dataset
X = np.array([[1, 2], [2, 4], [3, 6], [4, 8]])  # Features: size, rooms
y = np.array([100, 200, 300, 400])  # Prices

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict on new data
new_data = np.array([5, 10])  # Error: Shape mismatch, should be [[5, 10]]
print(f"Predicted price: {model.predict(new_data)}")