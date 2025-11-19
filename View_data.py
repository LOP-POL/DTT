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

filter_missing_values(sales)