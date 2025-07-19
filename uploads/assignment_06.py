# Assignment 6: Missing Value Imputation
# Impute missing values in a dataset using mean strategy
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# Synthetic dataset
data = {
    'feature1': [1, 2, np.nan, 4],
    'feature2': [10, np.nan, 30, 40]
}
df = pd.DataFrame(data)

# Impute missing values
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df)

# Error: Incorrectly printing DataFrame as array
print(df_imputed['feature1'])  # Should use pd.DataFrame(df_imputed)