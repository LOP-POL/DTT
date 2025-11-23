import csv
import pandas as pd
import os

script_dir = os.path.dirname(__file__)
rel_path = "challenge_material"


sales = pd.read_csv(os.path.join(script_dir, rel_path, "customers_sales.csv"))
print(sales)
sales_null_values = sales.isnull()
print(sales_null_values)

def filter_missing_values(df):
    missing_values = df[df.isna().any(axis=1)]
    if missing_values.empty:
        print("✅ Dataset has no missing values")
    else:
        print(missing_values)


def list_unique_values(df):
    column_names = list(df)

    for col in column_names:
        print("\n")
        print (col)
        print(df[col].unique())

def list_duplicate_values(df):
    duplicates = df.duplicated()
    duplicate_indices = list(duplicates[duplicates].index)
    print("\nDuplicate rows at indices: ")
    print(duplicate_indices)
    print(df.loc[duplicate_indices])



filter_missing_values(sales)
list_unique_values(sales)
list_duplicate_values(sales)