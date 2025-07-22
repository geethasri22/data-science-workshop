# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Step 2: Load Dataset
df = pd.read_csv("output_students.csv")

# Step 3: Initial Data Overview
print("Original Shape:", df.shape)
print("\nColumn Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nNumber of Duplicate Rows:", df.duplicated().sum())

# Step 4: Drop Duplicate Rows
df.drop_duplicates(inplace=True)

# Step 5: Handle Missing Values
# Fill numerical columns with mean
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Step 6: Encode Categorical Columns using One-Hot Encoding
df = pd.get_dummies(df, drop_first=True)

# Step 7: Standardize Numerical Features
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

# Step 8: Final Output
print("\nCleaned Data Shape:", df.shape)
print(df.head())

# Step 9: Save Preprocessed Dataset
df.to_csv("cleaned_output_students.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_output_students.csv'")
