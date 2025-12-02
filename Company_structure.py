import pandas as pd
import numpy as np
import os
import re
import dataCleanUpFinal as cleanup
import matplotlib.pyplot as plt
import seaborn as sns


rel_path = "challenge_material"
df = pd.read_csv(os.path.join(rel_path, "customers_sales.csv"))


# DATA CLEANUP  --------------------------------------------------------------------------------------
df['customer_name'] = df['customer_name'].replace('AutoPart AG', 'AutoParts AG')

missing = cleanup.fix_missing(df)
df = cleanup.add_missing(df, missing, 'TechFab Industries', 'Hamburg Branch', '2000')

###---------------------------------------------------------------------------------------------------



branch_list = cleanup.branchPerCustomer(df)
print(branch_list)

def plot_order_count_perCustomer(branch_list):
    branch_list = branch_list.reset_index()
    branch_list.columns = ["customer_name", "customer_branch", "count"]

    plt.figure(figsize=(12, 6))
    ax = sns.barplot(
        data=branch_list,
        x="customer_name",
        y="count",
        hue="customer_branch"
    )

    plt.title("Orders per Customer by Branch")
    plt.xlabel("Customer Name")
    plt.ylabel("Number of Orders")
    for container in ax.containers:
        ax.bar_label(container, fontsize=9)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()




coordinates = {
    "Berlin": (52.52, 13.4050),
    "Stuttgart": (48.7758, 9.1829),
    "Munich": (48.1351, 11.5820),
    "Hamburg": (53.5511, 9.9937),
    "Frankfurt": (50.1109, 8.6821)
}



plot_order_count_perCustomer(branch_list)