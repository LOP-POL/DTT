from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))

coordinates = {
    "Berlin": (52.52, 13.4050),
    "Stuttgart": (48.7758, 9.1829),
    "Munich": (48.1351, 11.5820),
    "Hamburg": (53.5511, 9.9937),
    "Frankfurt": (50.1109, 8.6821)
}


m = Basemap(
    projection='merc',
    llcrnrlat=47,
    urcrnrlat=55,
    llcrnrlon=5,
    urcrnrlon=15,
    lat_ts=20,
    resolution='i'
)

# Softer, modern colors
land_color = "#f2efe9"        # warm light beige
water_color = "#c7dcef"       # soft pastel blue
border_color = "#555555"       # neutral dark gray
state_line_color = "#888888"   # softer gray

# Draw map
m.drawmapboundary(fill_color=water_color)
m.fillcontinents(color=land_color, lake_color=water_color)

m.drawcoastlines(color=border_color, linewidth=0.8)
m.drawcountries(color=border_color, linewidth=1.0)

# German state boundaries (if you loaded a shapefile)
m.readshapefile('gadm41_DEU_1', 'germany_states', drawbounds=True)
for shp in m.germany_states:
     pass   # lines already drawn by drawbounds=True

# Parallels / meridians in subtle colors
m.drawparallels(np.arange(47, 56, 1), labels=[1,0,0,0], color="#bbbbbb")
m.drawmeridians(np.arange(5, 16, 1), labels=[0,0,0,1], color="#bbbbbb")

# --- Plot cities ---
for city, (lat, lon) in coordinates.items():
    x, y = m(lon, lat)  # convert lat/lon to map projection coordinates
    m.plot(x, y, 'o', markersize=8, markeredgecolor='black')
    plt.text(x + 10000, y + 10000, city, fontsize=9, fontweight='bold')  # small offset

plt.title("Location of Branches with Order Sizes", fontsize=14)
plt.tight_layout()
plt.show()
