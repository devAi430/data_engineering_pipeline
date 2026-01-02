import pandas as pd
from datetime import datetime
import numpy as np

#  Load the file
df = pd.read_csv("../dags/data/source.csv")
print("✅ File Loaded Successfully!")
print(df.head(), "\n")  # Show first 5 rows of raw data

#  Clean age column
if "age" in df.columns:
    df["age"] = pd.to_numeric(df["age"], errors="coerce")  # Convert to numeric, invalid values become NaN
    df.loc[(df["age"] < 0) | (df["age"] > 120), "age"] = np.nan  # Replace unrealistic values with NaN
    df["age"] = df["age"].fillna(df["age"].mean()).astype(int)  # Fill missing with mean age

#  Clean salary column
if "salary" in df.columns:
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")  # Convert to numeric
    median_salary = df["salary"].median()  # Calculate median
    df.loc[(df["salary"] < 3000) | (df["salary"] > 50000), "salary"] = median_salary  # Replace outliers with median
    df["salary"] = df["salary"].fillna(median_salary)  # Fill missing with median

#  Clean join_date column
if "join_date" in df.columns:
    df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")  # Convert to datetime
    df["join_date"] = df["join_date"].fillna(pd.to_datetime("2020-01-01"))  # Replace NaT with default date

#  Clean city column
if "city" in df.columns:
    df["city"] = df["city"].astype(str).str.strip().str.title()  # Normalize text (trim spaces + title case)
    df["city"] = df["city"].replace("None", np.nan).fillna("Unknown")  # Replace missing with "Unknown"

#  Derived columns
if "join_date" in df.columns:
    df["experience_years"] = datetime.now().year - df["join_date"].dt.year  # Years of experience

if "age" in df.columns:
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 18, 40, 120],
        labels=["Young", "Adult", "Senior"]
    )  # Categorize age into groups

#  Show cleaned data
print("✅ Cleaned Data Sample:")
print(df.head())

#  Save cleaned file
df.to_csv("employees_clean.csv", index=False)
print("\n💾 Clean file saved ")