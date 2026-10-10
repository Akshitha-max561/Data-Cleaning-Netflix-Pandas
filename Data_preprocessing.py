import pandas as pd

# 1. Load the dataset
df = pd.read_csv("netflix_titles.csv")

# 2. Show first few rows of the original data
print("Original Data:\n", df.head())

# 3. Show the number of missing values in each column
print("\nMissing Values:\n", df.isnull().sum())

# 4. Remove duplicate rows (if any)
df = df.drop_duplicates()

# 5. Fill or remove missing values
# For simplicity, drop rows with missing 'rating', 'duration' and 'date_added'
df = df.dropna(subset=['rating', 'duration', 'date_added'])

# Fill missing 'country' and 'cast' with 'Unknown'
df['country'] = df['country'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')

# Fill missing 'director' with 'Not Available'
df['director'] = df['director'].fillna('Not Available')

# 6. Fix date format
# Strip leading/trailing spaces and convert to datetime
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors='coerce')

# 7. Standardize column names (lowercase and replace spaces with _)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 8. Show cleaned data summary
print("\nCleaned Data Sample:\n", df.head())

# 9. Show updated missing values
print("\nMissing Values After Cleaning:\n", df.isnull().sum())

# 10. Save cleaned dataset to a new CSV file
df.to_csv("netflix_cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as 'netflix_cleaned.csv'")
