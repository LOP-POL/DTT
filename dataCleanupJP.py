#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import re


# In[2]:


rel_path = "challenge_material"
df = pd.read_csv(os.path.join(rel_path, "customers_sales.csv"))


# In[3]:


df.head()


# In[4]:


df.info()


# In[32]:


df.describe()


# Fixing the typo

# In[5]:


df['customer_name'] = df['customer_name'].replace('AutoPart AG', 'AutoParts AG')


# Finding the missing values and adding them as TechFab Industries, Hamburg Branch, 2000.

# In[7]:


def fix_missing(df):
    files = os.listdir('challenge_material\\10991360')

    existing_files = df['file_name'].dropna().unique()
    missing_files = [f for f in files if f not in existing_files]

    print(f"Missing files: {len(missing_files)}")
    return missing_files

missing = fix_missing(df)

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


# In[8]:


def branchPerCustomer(df):
    branch_per_cust = df.groupby('customer_name')['customer_branch'].value_counts()

    return branch_per_cust




branchPerCustomer(df)


# In[10]:


df.head()

