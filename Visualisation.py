from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataCleanUpFinal as cleanup
import os

script_dir = os.path.dirname(__file__)
rel_path = "challenge_material"



sales = pd.read_csv(os.path.join(script_dir, rel_path, "customers_sales.csv"))



#df = cleanup.branchPerCustomer(sales)

df = cleanup.branchPerCustomer(cleanup.df).reset_index()
df.columns = ["customer_name", "customer_branch", "orders"]

print(df)

branch_locations = {
    "Munich Branch": (48.1351, 11.5820),
    "Berlin Branch": (52.5200, 13.4050),
    "Frankfurt Branch": (50.1109, 8.6821),
    "Stuttgart Branch": (48.7758, 9.1829),
    "Hamburg Branch": (53.5511, 9.9937)
}

# Map stuff
m = Basemap(
    projection='merc',
    llcrnrlat=47,
    urcrnrlat=55,
    llcrnrlon=5,
    urcrnrlon=15,
    lat_ts=20,
    resolution='i'
)

m.drawcoastlines(color='black')
m.drawcountries(color='black')
m.fillcontinents(color="#f2efe9", lake_color="#c7dcef")
m.drawmapboundary(fill_color="#c7dcef")

plt.title("Orders per Customer Branch", fontsize=14)


companies = df["customer_name"].tolist()
colors = plt.cm.tab10(np.linspace(0, 1, len(companies)))
color_map = dict(zip(companies, colors))

#Plot each company
for idx, row in df.iterrows():
    customer = row["customer_name"]
    branch = row["customer_branch"]
    orders = row[df.columns[-1]]  # last column

    if branch not in branch_locations:
        continue

    lat, lon = branch_locations[branch]
    x, y = m(lon, lat)

    # Dot color
    m.plot(x, y, 'o', markersize=12, color=color_map[customer], markeredgecolor='black')

    # Label
    label = f"{customer}\n({orders})"
    plt.text(x + 15000, y + 15000, label, fontsize=9, weight='bold')

plt.show()
print(df)