# Assignment 3: EDA on Synthetic Dataset
# Perform EDA on a dataset of student scores
import pandas as pd
import numpy as np

# Synthetic dataset
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'math_score': [85, 90, 78, 92],
    'science_score': [88, 95, 80, 90]
}
df = pd.DataFrame(data)

# Calculate average scores
avg_math = df['math_score'].mean()
avg_science = df['science_score'].mean()
print(f"Average Math Score: {avg_math}")
print(f"Average Science Score: {avg_science}")

# Plot histogram of math scores
import matplotlib.pyplot as plt
plt.hist(df['math_score'], bins=5)
plt.title('Math Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()  # Error: May not display in non-interactive environments
print(df['english_score'])  # Error: 'english_score' column doesn't exist