import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import Normalize
from matplotlib.ticker import ScalarFormatter

from theme.unodc import *

# Load the shapefile
shapefile_path = './data/ne_110m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)

# Load your data
data_path = './data/comptab_2018-01-29 16_00_comma_separated.csv'
data = pd.read_csv(data_path)

# Filter data for the terms 'live', 'bodies', or 'skins'
terms_to_include = ['live', 'bodies', 'skins']
filtered_data = data[data['Term'].isin(terms_to_include)]

# Take the maximum between 'Importer reported quantity' and 'Exporter reported quantity'
pd.options.mode.chained_assignment = None
filtered_data['Reported Quantity'] = filtered_data[['Importer reported quantity', 'Exporter reported quantity']].max(
    axis=1)
# print(filtered_data.sort_values('Reported Quantity', ascending=False).head())

# Summarize data at the country level
grouped_filtered_data = filtered_data.groupby('Importer').agg({'Reported Quantity': 'sum'}).reset_index()
grouped_filtered_data['Reported Quantity'] *= 0.3664

# Merge the summarized data with the world GeoDataFrame
world_with_data = world.merge(grouped_filtered_data, how="left", left_on='ISO_A2', right_on='Importer')

# Plotting the heatmap
fig, ax = plt.subplots(1, 1, figsize=(20, 12))
# plt.subplots_adjust(left=0.06, bottom=0.05, right=0.98, top=1.3)
norm = Normalize(vmin=0.1e7, vmax=3.7e7)
world_with_data.plot(
    column='Reported Quantity',
    cmap=CMAP,
    ax=ax,
    edgecolor='#331F11',
    linewidth=0.3,
    legend=True,
    norm=norm,
    legend_kwds={
        # 'label': "Reported Quantity of Wildlife Trade by Country, from CITES",
        'orientation': "vertical",
        'shrink': 0.4,
        'aspect': 10,
        'pad': -0.01,
        'format': ScalarFormatter(useMathText=True)
    },
    missing_kwds={
        'color': 'lightgrey',
    }
)
# ax.set_title('Heatmap of Reported Quantity (Filtered Data)')
ax.set_axis_off()

legend_elements = [Patch(facecolor=CMAP(0), edgecolor='#331F11', label='Data Present'),
                   Patch(facecolor='lightgrey', edgecolor='#331F11', label='No Data')]
ax.legend(handles=legend_elements, loc='lower right', title='Legend', bbox_to_anchor=(1.09, 0.05))

# Add text 'a)' to the upper left corner of the plot
ax.text(0.05, 0.99, 'b)', transform=ax.transAxes, verticalalignment='top', horizontalalignment='left', fontsize=24,
        fontweight='bold', color='black')

plt.savefig(r'./output/Wildlife Trade Volume after Improving.svg', bbox_inches='tight')
plt.show()
