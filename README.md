# Data Analyst Internship — Task 1
## Data Cleaning and Preprocessing: Mall Customer Segmentation

This repository contains the Task 1 starter project, cleaning script, notebook, sample CSVs, and report.

> **Important dataset note:** The included CSV files are a 10-row demonstration sample so the project structure can be opened immediately. They are **not** the complete 200-row Kaggle dataset. To produce the real final deliverable, download the original `Mall_Customers.csv` and place it in `data/` before running the cleaning script. Do not submit the demo sample as though it were the full dataset.

## Dataset source
Kaggle: [Mall Customer Segmentation Data](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

The commonly published dataset has 200 customer records and five fields: CustomerID, Gender, Age, Annual Income (k$), and Spending Score (1–100).

## Folder structure
```text
mall_customer_task1/
├── data/
│   ├── mall_customers_sample.csv
│   └── mall_customers_clean_sample.csv
├── images/
├── notebooks/
│   └── task1_data_cleaning.ipynb
├── reports/
│   ├── task1_report.md
│   └── cleaning_summary_sample.txt
├── src/
│   └── clean_data.py
├── requirements.txt
└── README.md
```

## How to run
1. Download `Mall_Customers.csv` from the Kaggle dataset page.
2. Put it in the `data/` folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python src/clean_data.py
   ```
5. The script creates `data/mall_customers_cleaned.csv` and `reports/cleaning_summary.txt`.

## Cleaning steps
- Inspect missing values and duplicate rows.
- Standardize column names and text categories.
- Convert numeric fields to numeric data types.
- Remove exact duplicate records.
- Fill numeric missing values using the median and categorical missing values using the mode.
- Remove records without a customer ID.
- Save the cleaned dataset and a summary.

## Tools
Python, pandas, Jupyter Notebook.

## Academic honesty / reproducibility
The notebook and script are designed to run on the original Kaggle file. The sample files are labelled as samples. Run the script against the full original dataset before claiming final full-dataset cleaning results.
