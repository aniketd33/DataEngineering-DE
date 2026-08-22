import pandas as pd


# 1. Extract
df = pd.read_csv("raw/jobs.csv")

print("Original shape:", df.shape)


# 2. Clean column names
df.columns = df.columns.str.strip().str.lower()


# 3. Clean text
df["role"] = df["role"].str.strip().str.title()
df["location"] = df["location"].str.strip().str.title()


# 4. Convert salary
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)


# 5. Handle missing role
df["role"] = df["role"].fillna("Unknown")


# 6. Remove duplicates
df = df.drop_duplicates()


# 7. Create new column
df["annual_salary"] = df["salary"] * 12


# 8. Save cleaned data
df.to_csv(
    "output/clean_jobs.csv",
    index=False
)

print("Final shape:", df.shape)
print("Pipeline completed!")