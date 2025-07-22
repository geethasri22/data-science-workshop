import pandas as pd
import numpy as np

# --- 1. Create a Sample DataFrame ---
# Let's create a DataFrame to simulate some real-world data.
# It will include numerical, categorical, and missing data.
print("--- Initial DataFrame ---")
data = {
    'ProductID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Clothing',
                 'Electronics', 'Books', 'Clothing', 'Electronics', 'Books'],
    'Price': [1200.50, 45.99, 899.00, 15.75, 60.00,
              np.nan, 22.50, 55.50, 1500.00, 18.25],
    'Quantity': [10, 25, 5, 50, 15,
                 8, np.nan, 30, 3, 40],
    'Rating': [4.5, 3.8, 4.7, 4.0, 3.5,
               4.2, 3.9, 4.1, 4.8, 3.7],
    'LastUpdated': pd.to_datetime([
        '2023-01-15', '2023-02-20', '2023-01-25', '2023-03-01', '2023-02-10',
        '2023-01-30', '2023-03-05', '2023-02-28', '2023-01-20', '2023-03-10'
    ])
}
df = pd.DataFrame(data)
print(df)
print("\nDataFrame Info:")
df.info()
print("\nDataFrame Description:")
print(df.describe())

# --- 2. Data Cleaning and Preprocessing ---

# Handling Missing Values:
# Option 1: Fill missing 'Price' with the mean price of its category
print("\n--- Handling Missing Values (Filling Price by Category Mean) ---")
df['Price'] = df.groupby('Category')['Price'].transform(lambda x: x.fillna(x.mean()))
print("Missing values after filling Price:\n", df.isnull().sum())

# Option 2: Fill missing 'Quantity' with the median (or 0 if it makes sense for inventory)
print("\n--- Handling Missing Values (Filling Quantity with Median) ---")
df['Quantity'].fillna(df['Quantity'].median(), inplace=True)
print("Missing values after filling Quantity:\n", df.isnull().sum())

# Ensure 'Quantity' is an integer type after filling NaNs
df['Quantity'] = df['Quantity'].astype(int)
print("\nDataFrame Info after type conversion:")
df.info()

# Creating a new feature: 'TotalPrice'
print("\n--- Creating New Feature: TotalPrice ---")
df['TotalPrice'] = df['Price'] * df['Quantity']
print(df[['Price', 'Quantity', 'TotalPrice']].head())

# --- 3. Data Aggregation and Analysis ---

# Group by 'Category' and calculate aggregate statistics
print("\n--- Aggregated Statistics by Category ---")
category_summary = df.groupby('Category').agg(
    Average_Price=('Price', 'mean'),
    Total_Quantity=('Quantity', 'sum'),
    Max_Rating=('Rating', 'max'),
    Count=('ProductID', 'count')
).reset_index()
print(category_summary)

# Find the product with the highest rating
print("\n--- Product with Highest Rating ---")
highest_rating_product = df.loc[df['Rating'].idxmax()]
print(highest_rating_product)

# Filter data: Products with Price > 500
print("\n--- Products with Price > 500 ---")
high_value_products = df[df['Price'] > 500]
print(high_value_products)

# --- 4. NumPy Operations on Pandas Data ---

# Using NumPy for conditional selection (e.g., mark products as 'High' or 'Low' value)
print("\n--- Adding 'Value_Segment' using NumPy's where ---")
df['Value_Segment'] = np.where(df['Price'] > df['Price'].median(), 'High', 'Low')
print(df[['ProductID', 'Price', 'Value_Segment']].head())

# Applying a NumPy function (e.g., log transformation on Price)
print("\n--- Log Transformation of Price using NumPy's log ---")
df['Price_Log'] = np.log(df['Price'])
print(df[['Price', 'Price_Log']].head())

# Calculating correlation matrix for numerical columns
print("\n--- Correlation Matrix of Numerical Columns ---")
numerical_cols = df.select_dtypes(include=np.number)
print(numerical_cols.corr())

print("\n--- Final DataFrame after processing ---")
print(df)