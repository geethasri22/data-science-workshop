import pandas as pd
import numpy as np

print("--- Demonstrating 50 Pandas Operations ---")
print("-" * 50)

# --- I. DataFrame/Series Creation and Basic Info ---

print("\n--- I. DataFrame/Series Creation and Basic Info ---")

# 1. pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}): Create a DataFrame from a dictionary of lists.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [24, 27, 22, 32, 29, 35, 26],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York', 'Los Angeles'],
    'Score': [85, 92, 78, 95, 88, 70, 81],
    'IsStudent': [True, False, True, False, True, False, True],
    'EnrollmentDate': pd.to_datetime(['2022-01-15', '2021-03-20', '2023-09-01', '2020-05-10', '2022-11-25', '2019-07-01', '2023-02-14']),
    'MissingValueCol': [1, np.nan, 3, np.nan, 5, 6, np.nan]
}
df = pd.DataFrame(data)
print(f"\n1. Initial DataFrame created from dict:\n{df.head(3)}")

# 2. pd.Series([10, 20, 30]): Create a Series from a list.
s = pd.Series([10, 20, 30, 40, 50], name="MySeries")
print(f"\n2. pd.Series([10, 20, 30, 40, 50]):\n{s}")

# Create dummy CSV and Excel files for demonstration of read operations
df.to_csv('temp_data.csv', index=False)
df.to_excel('temp_data.xlsx', index=False, sheet_name='Students')
df.to_json('temp_data.json', orient='records', lines=True)

# 3. pd.read_csv('data.csv'): Read data from a CSV file.
try:
    df_csv = pd.read_csv('temp_data.csv')
    print(f"\n3. pd.read_csv('temp_data.csv') - First 2 rows:\n{df_csv.head(2)}")
except FileNotFoundError:
    print("\n3. temp_data.csv not found. Skipping this operation.")

# 4. pd.read_excel('data.xlsx'): Read data from an Excel file.
try:
    df_excel = pd.read_excel('temp_data.xlsx', sheet_name='Students')
    print(f"\n4. pd.read_excel('temp_data.xlsx') - First 2 rows:\n{df_excel.head(2)}")
except FileNotFoundError:
    print("\n4. temp_data.xlsx not found. Skipping this operation.")

# 5. pd.read_json('data.json'): Read data from a JSON file.
try:
    df_json = pd.read_json('temp_data.json', orient='records', lines=True)
    print(f"\n5. pd.read_json('temp_data.json') - First 2 rows:\n{df_json.head(2)}")
except FileNotFoundError:
    print("\n5. temp_data.json not found. Skipping this operation.")


# 6. df.head(): View the first 5 rows of the DataFrame.
print(f"\n6. df.head():\n{df.head()}")

# 7. df.tail(): View the last 5 rows of the DataFrame.
print(f"\n7. df.tail():\n{df.tail()}")

# 8. df.info(): Get a summary of the DataFrame.
print(f"\n8. df.info():")
df.info()

# 9. df.shape: Get the number of rows and columns as a tuple.
print(f"\n9. df.shape: {df.shape}")

# 10. df.columns: Get a list of column names.
print(f"\n10. df.columns: {list(df.columns)}")

# 11. df.index: Get the index of the DataFrame.
print(f"\n11. df.index: {df.index}")

# 12. df.dtypes: Get the data type of each column.
print(f"\n12. df.dtypes:\n{df.dtypes}")

# 13. df.describe(): Generate descriptive statistics of numerical columns.
print(f"\n13. df.describe():\n{df.describe()}")


# --- II. Data Selection and Indexing ---

print("\n\n--- II. Data Selection and Indexing ---")

# 14. df['col_name']: Select a single column as a Series.
names_series = df['Name']
print(f"\n14. df['Name'] (Series):\n{names_series.head(3)}")

# 15. df[['col1', 'col2']]: Select multiple columns as a DataFrame.
name_age_df = df[['Name', 'Age']]
print(f"\n15. df[['Name', 'Age']] (DataFrame):\n{name_age_df.head(3)}")

# 16. df.loc[0]: Select a row by label (index).
first_row_loc = df.loc[0]
print(f"\n16. df.loc[0]:\n{first_row_loc}")

# 17. df.loc[0, 'Name']: Select a single cell by row and column labels.
cell_loc = df.loc[0, 'Name']
print(f"\n17. df.loc[0, 'Name']: {cell_loc}")

# 18. df.loc[0:2, 'Name':'City']: Select a slice of rows and columns by labels.
slice_loc = df.loc[0:2, 'Name':'City']
print(f"\n18. df.loc[0:2, 'Name':'City']:\n{slice_loc}")

# 19. df.iloc[0]: Select a row by integer position.
first_row_iloc = df.iloc[0]
print(f"\n19. df.iloc[0]:\n{first_row_iloc}")

# 20. df.iloc[0, 1]: Select a single cell by integer row and column positions.
cell_iloc = df.iloc[0, 1] # Age of first person
print(f"\n20. df.iloc[0, 1]: {cell_iloc}")

# 21. df.iloc[0:2, 0:3]: Select a slice of rows and columns by integer positions.
slice_iloc = df.iloc[0:2, 0:3]
print(f"\n21. df.iloc[0:2, 0:3]:\n{slice_iloc}")

# 22. df[df['col_name'] > 5]: Boolean indexing (filter rows based on a condition).
high_score_students = df[df['Score'] > 90]
print(f"\n22. df[df['Score'] > 90]:\n{high_score_students}")

# 23. df.filter(like='ol', axis=1): Select columns based on a pattern in their names.
filtered_cols = df.filter(like='ol', axis=1) # Will match 'col' if we had one, for now, demonstration
print(f"\n23. df.filter(like='Score', axis=1):\n{df.filter(like='Score', axis=1).head(2)}")
print(f"    df.filter(like='Date', axis=1):\n{df.filter(like='Date', axis=1).head(2)}")

# 24. df.isin([1, 2]): Check if elements are contained in a list.
isin_check = df[['Age', 'Score']].isin([24, 78])
print(f"\n24. df[['Age', 'Score']].isin([24, 78]) (partial output):\n{isin_check.head(3)}")


# --- III. Data Cleaning and Handling Missing Data ---

print("\n\n--- III. Data Cleaning and Handling Missing Data ---")

# 25. df.isnull(): Check for missing values (returns boolean DataFrame).
print(f"\n25. df.isnull() (head):\n{df.isnull().head()}")

# 26. df.isna().sum(): Count missing values per column.
print(f"\n26. df.isna().sum():\n{df.isna().sum()}")

# 27. df.dropna(): Remove rows with any missing values.
df_dropna_rows = df.dropna()
print(f"\n27. df.dropna() (rows with NaNs removed):\n{df_dropna_rows}")

# 28. df.dropna(axis=1): Remove columns with any missing values.
df_dropna_cols = df.dropna(axis=1)
print(f"\n28. df.dropna(axis=1) (cols with NaNs removed):\n{df_dropna_cols.head()}")

# 29. df.fillna(0): Fill missing values with a specific value (e.g., 0).
df_fillna_zero = df.fillna(0)
print(f"\n29. df.fillna(0) (MissingValueCol):\n{df_fillna_zero['MissingValueCol']}")

# 30. df.fillna(df.mean()): Fill missing numerical values with the mean of their column.
# Note: .mean() will ignore NaNs by default for numeric columns
df_fillna_mean = df.copy() # Work on a copy
df_fillna_mean['MissingValueCol'] = df_fillna_mean['MissingValueCol'].fillna(df_fillna_mean['MissingValueCol'].mean())
print(f"\n30. df.fillna(df.mean()) for 'MissingValueCol':\n{df_fillna_mean['MissingValueCol']}")

# Add a duplicate row for demonstration
df_with_duplicates = pd.concat([df, df.iloc[0:1]], ignore_index=True)
print(f"\nOriginal df with duplicates:\n{df_with_duplicates.tail(2)}")

# 31. df.drop_duplicates(): Remove duplicate rows.
df_no_duplicates = df_with_duplicates.drop_duplicates()
print(f"\n31. df.drop_duplicates():\n{df_no_duplicates.tail(2)}") # Shows the duplicate is gone

# 32. df.rename(columns={'old_name': 'new_name'}): Rename columns.
df_renamed = df.rename(columns={'Name': 'Full_Name', 'Age': 'Years_Old'})
print(f"\n32. df.rename(columns={{'Name': 'Full_Name'}}):\n{df_renamed.head(2)}")

# 33. df['col'].astype(str): Change the data type of a column.
df_copy_for_type = df.copy()
df_copy_for_type['Score_Str'] = df_copy_for_type['Score'].astype(str)
print(f"\n33. df['Score'].astype(str) - dtypes:\n{df_copy_for_type[['Score', 'Score_Str']].dtypes}")


# --- IV. Data Manipulation and Transformation ---

print("\n\n--- IV. Data Manipulation and Transformation ---")

# 34. df['new_col'] = df['col1'] + df['col2']: Create a new column.
df['Age_Plus_Score'] = df['Age'] + df['Score']
print(f"\n34. df['Age_Plus_Score'] = df['Age'] + df['Score']:\n{df[['Age', 'Score', 'Age_Plus_Score']].head(3)}")

# 35. df['col'].apply(lambda x: x*2): Apply a function to each element in a Series.
df['Age_Doubled'] = df['Age'].apply(lambda x: x * 2)
print(f"\n35. df['Age'].apply(lambda x: x * 2):\n{df[['Age', 'Age_Doubled']].head(3)}")

# 36. df.groupby('category_col').sum(): Group data by a column and perform an aggregation.
grouped_by_city_score = df.groupby('City')['Score'].mean().reset_index()
print(f"\n36. df.groupby('City')['Score'].mean():\n{grouped_by_city_score}")

# 37. df.pivot_table(index='col1', columns='col2', values='col3', aggfunc='mean'): Create a pivot table.
pivot_table_df = df.pivot_table(index='City', values='Score', aggfunc='mean')
print(f"\n37. df.pivot_table(index='City', values='Score', aggfunc='mean'):\n{pivot_table_df}")

# 38. df.sort_values(by='col_name', ascending=False): Sort DataFrame by a column's values.
df_sorted = df.sort_values(by='Score', ascending=False)
print(f"\n38. df.sort_values(by='Score', ascending=False):\n{df_sorted.head(3)}")

# 39. df.set_index('col_name'): Set a column as the DataFrame index.
df_indexed = df.set_index('Name')
print(f"\n39. df.set_index('Name'):\n{df_indexed.head(3)}")

# 40. df.reset_index(): Reset the DataFrame index to default integers.
df_reset = df_indexed.reset_index()
print(f"\n40. df_indexed.reset_index():\n{df_reset.head(3)}")

# Create two dataframes for merge and concat
df_merge1 = pd.DataFrame({'ID': [1, 2, 3], 'Value1': ['A', 'B', 'C']})
df_merge2 = pd.DataFrame({'ID': [2, 3, 4], 'Value2': ['X', 'Y', 'Z']})

# 41. pd.merge(df1, df2, on='key_col'): Merge two DataFrames.
merged_df = pd.merge(df_merge1, df_merge2, on='ID', how='inner')
print(f"\n41. pd.merge(df_merge1, df_merge2, on='ID'):\n{merged_df}")

# 42. pd.concat([df1, df2]): Concatenate DataFrames (row-wise by default).
concatenated_df = pd.concat([df_merge1, df_merge2], ignore_index=True)
print(f"\n42. pd.concat([df_merge1, df_merge2]):\n{concatenated_df}")

# 43. df.drop('col_name', axis=1): Drop a column.
df_dropped_col = df.drop('Age_Doubled', axis=1)
print(f"\n43. df.drop('Age_Doubled', axis=1) (columns):\n{df_dropped_col.columns}")

# 44. df.drop([0, 1], axis=0): Drop rows by index label.
df_dropped_rows = df.drop([0, 1], axis=0)
print(f"\n44. df.drop([0, 1], axis=0) (first 2 rows dropped):\n{df_dropped_rows.head(3)}")

# 45. df.sample(n=3): Select a random sample of n rows.
sampled_df = df.sample(n=3, random_state=42) # random_state for reproducibility
print(f"\n45. df.sample(n=3):\n{sampled_df}")

# 46. df.value_counts(): Count unique values in a Series.
city_counts = df['City'].value_counts()
print(f"\n46. df['City'].value_counts():\n{city_counts}")

# 47. df.replace({'old_val': 'new_val'}): Replace specific values in a DataFrame.
df_replaced = df.replace({'New York': 'NYC', True: 'Yes'})
print(f"\n47. df.replace(): 'New York' to 'NYC', True to 'Yes' (head):\n{df_replaced[['City', 'IsStudent']].head()}")


# --- V. Data Aggregation and Output ---

print("\n\n--- V. Data Aggregation and Output ---")

# 48. df['col'].mean(): Calculate the mean of a Series.
mean_score = df['Score'].mean()
print(f"\n48. df['Score'].mean(): {mean_score:.2f}")

# 49. df.to_csv('output.csv', index=False): Write DataFrame to a CSV file.
output_csv_path = 'output_students.csv'
df.to_csv(output_csv_path, index=False)
print(f"\n49. df.to_csv('{output_csv_path}', index=False): File created.")

# 50. df.to_excel('output.xlsx', sheet_name='Sheet1', index=False): Write DataFrame to an Excel file.
output_excel_path = 'output_students.xlsx'
df.to_excel(output_excel_path, sheet_name='StudentData', index=False)
print(f"\n50. df.to_excel('{output_excel_path}', sheet_name='StudentData', index=False): File created.")

# Clean up temporary files
import os
for temp_file in ['temp_data.csv', 'temp_data.xlsx', 'temp_data.json']:
    if os.path.exists(temp_file):
        os.remove(temp_file)
print("\nCleaned up temporary files: temp_data.csv, temp_data.xlsx, temp_data.json")

print("\n--- End of Pandas Demonstration ---")