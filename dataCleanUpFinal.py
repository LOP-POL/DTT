import os

import pandas as pd

rel_path = "challenge_material"
df = pd.read_csv(os.path.join(rel_path, "customers_sales.csv"))


# Fixing the typo
df['customer_name'] = df['customer_name'].replace('AutoPart AG', 'AutoParts AG')

# Finding the missing values and adding them as TechFab Industries, Hamburg Branch, 2000
def find_missing(df):
    files = os.listdir('challenge_material\\10991360')

    existing_files = df['file_name'].dropna().unique()
    missing_files = [f for f in files if f not in existing_files]

    return missing_files

missing = find_missing(df)

def add_missing(df, missing, customer_name, customer_branch, order_quantity):
    if len(missing) == 0:
        return df

    new_rows = pd.DataFrame({
        'file_name': missing,
        'customer_name': [customer_name] * len(missing),
        'customer_branch': [customer_branch] * len(missing),
        'order_quantity': [order_quantity] * len(missing)
    })

    return pd.concat([df, new_rows], ignore_index=True)

df = add_missing(df, missing, 'TechFab Industries', 'Hamburg Branch', '2000')

def branchPerCustomer(df):
    return df.groupby('customer_name')['customer_branch'].value_counts()
branchPerCustomer(df)
