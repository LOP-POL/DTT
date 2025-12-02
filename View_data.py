import csv
import pandas as pd
import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "challenge_material"
# munich, berlin, stuttgart, hamburg, frankfurt


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

def list_unused_drawings(df):
    used_drawings = set()

    for file_name in df["file_name"].astype(str):
        found_digits = re.findall(r'\d+', file_name)
        for digit_str in found_digits:
            used_drawings.add(int(digit_str))

    all_expected_drawings = set(range(1, 81))

    unused_drawings = sorted(list(all_expected_drawings - used_drawings))

    print(f"Total Unique Drawings Found: {len(used_drawings)}")
    print(f"Expected Range: 1 to 80")
    print("-" * 30)
    print(f"The following file numbers are unused (missing from the column):")
    print(unused_drawings)
    print("-" * 30)

def sort_by_customers(df):
    sorted_df = df.sort_values(by=["customer_name"], na_position='first')
    print(sorted_df)


sort_by_customers(sales)

print(sales.dtypes)
print(sales.describe(include='all'))


list_unused_drawings(sales)