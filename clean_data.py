"""
Task 1: Data Cleaning and Preprocessing
Mall Customer Segmentation Data

Place the full Kaggle file Mall_Customers.csv in the data/ folder.
Run: python src/clean_data.py
Outputs: data/mall_customers_cleaned.csv and reports/cleaning_summary.txt
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
INPUT = DATA / "Mall_Customers.csv"
OUTPUT = DATA / "mall_customers_cleaned.csv"
SUMMARY = ROOT / "reports" / "cleaning_summary.txt"

if not INPUT.exists():
    raise FileNotFoundError(
        "Full source dataset not found. Download Mall_Customers.csv from "
        "https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python "
        "and save it inside the data/ folder. The included *_sample.csv is only a 10-row demo."
    )

df = pd.read_csv(INPUT)
before_rows, before_cols = df.shape
missing_before = int(df.isna().sum().sum())
duplicates_before = int(df.duplicated().sum())

# Standardize column names
df.columns = (
    df.columns.str.strip().str.lower()
      .str.replace(r"[^a-z0-9]+", "_", regex=True)
      .str.strip("_")
)

# Standardize text values
if "gender" in df.columns:
    df["gender"] = df["gender"].astype("string").str.strip().str.title()
    df["gender"] = df["gender"].replace({"M": "Male", "F": "Female"})

# Convert expected numeric columns safely
numeric_cols = ["customerid", "age", "annual_income_k", "spending_score_1_100"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove exact duplicate rows
df = df.drop_duplicates()

# Handle missing values: median for numeric columns; mode for categorical columns
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        if df[col].isna().any():
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)
    else:
        if df[col].isna().any():
            mode_values = df[col].mode(dropna=True)
            if not mode_values.empty:
                df[col] = df[col].fillna(mode_values.iloc[0])

# Remove rows that still lack an identifier, if identifier exists
if "customerid" in df.columns:
    df = df.dropna(subset=["customerid"])
    df["customerid"] = df["customerid"].astype("int64")

df.to_csv(OUTPUT, index=False)

summary = [
    "TASK 1 - DATA CLEANING SUMMARY",
    "Dataset: Mall Customer Segmentation Data",
    f"Rows before cleaning: {before_rows}",
    f"Columns before cleaning: {before_cols}",
    f"Missing cells before cleaning: {missing_before}",
    f"Duplicate rows before cleaning: {duplicates_before}",
    f"Rows after cleaning: {len(df)}",
    f"Columns after cleaning: {len(df.columns)}",
    f"Missing cells after cleaning: {int(df.isna().sum().sum())}",
    f"Duplicate rows after cleaning: {int(df.duplicated().sum())}",
    f"Cleaned file: {OUTPUT.relative_to(ROOT)}",
    "",
    "Actions: standardized headers and gender text; converted numeric columns;",
    "removed exact duplicates; filled numeric nulls with median and text nulls",
    "with mode; removed rows with missing customer ID.",
    "Note: imputation should be reviewed against the business context."
]
SUMMARY.write_text("\\n".join(summary), encoding="utf-8")
print("\\n".join(summary))
