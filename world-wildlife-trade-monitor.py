import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.patches import FancyArrowPatch

# Load the trade flow data
data_path = './data/comptab_processed_data.csv'
trade_data = pd.read_csv(data_path)

# Load the shapefile
shapefile_path = './data/ne_110m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)

# Get the centroids of the countries and store them in a dictionary
world['centroid'] = world.centroid
centroids = world.set_index('ISO_A2')['centroid'].to_dict()


# Function to get coordinates from centroids dictionary
def get_coordinates(country_code):
    centroid = centroids.get(country_code)
    if centroid:
        return (centroid.x, centroid.y)
    return (None, None)


# Add coordinates to the trade data DataFrame
trade_data['Importer_coords'] = trade_data['Importer'].apply(get_coordinates)
trade_data['Exporter_coords'] = trade_data['Exporter'].apply(get_coordinates)

# Remove rows with missing coordinates
trade_data.dropna(subset=['Importer_coords', 'Exporter_coords'], inplace=True)


# Function to draw arrows on the map
def draw_arrow(ax, point1, point2, trade_volume, max_trade):
    scale_factor = 2
    arrow_width = (trade_volume / max_trade) * scale_factor
    arrow_width = max(arrow_width, 0.5)
    ax.annotate('', xy=point2, xycoords='data', xytext=point1, textcoords='data', alpha=1,
                arrowprops=dict(arrowstyle="-|>", color='#c6153c', lw=arrow_width))


# Function to draw curved arrows on the map
def draw_curved_arrow(ax, point1, point2, trade_volume, max_trade):
    scale_factor = 2
    arrow_width = (trade_volume / max_trade) * scale_factor
    arrow_width = max(arrow_width, 0.5)

    # Create a FancyArrowPatch object with a custom path
    # This creates a curved path from point1 to point2
    style = "Simple, tail_width=0.5, head_width=4, head_length=8"
    np.random.seed(114514)
    rad = np.random.rand()
    arrow = FancyArrowPatch(point1, point2, connectionstyle=f"arc3, rad={rad}", arrowstyle=style, color='#c6153c',
                            lw=arrow_width)

    ax.add_patch(arrow)


# Function to draw centroids on the map
def draw_centroid(ax, centroid, volume, max_volume, color):
    scale_factor = 300
    circle_size = (volume / max_volume) * scale_factor
    circle_size = max(circle_size, 1)
    ax.scatter(centroid.x, centroid.y, s=circle_size, color=color, alpha=0.56, edgecolors='none')


# Function to create a custom legend
def create_custom_legend(ax):
    legend_elements = [
        Line2D([0], [0], color='#c6153c', lw=4, label='High Volume Flow', alpha=1),
        Line2D([0], [0], color='#c6153c', lw=2, label='Medium Volume Flow', alpha=0.8),
        Line2D([0], [0], color='#c6153c', lw=1, label='Low Volume Flow', alpha=0.5),
        # Line2D([0], [0], marker='o', color='w', label='Seized mass equivalent (tons)',
        #        markerfacecolor='grey', markersize=15),
        # Line2D([0], [0], marker='o', color='w', label='15',
        #        markerfacecolor='grey', markersize=10),
        # Line2D([0], [0], marker='o', color='w', label='9',
        #        markerfacecolor='grey', markersize=7),
        # Line2D([0], [0], marker='o', color='w', label='<1',
        #        markerfacecolor='grey', markersize=3),
        Patch(facecolor='#70b28b', label='Exporting Countries'),
        Patch(facecolor='#d47185', label='Importing Countries')
    ]

    ax.legend(
        handles=legend_elements,
        loc='lower left',
        bbox_to_anchor=(0.05, 0.2),
        title="Legend",
        labelspacing=1.015,
        borderpad=1.005
    )


# Plotting the map
fig, ax = plt.subplots(1, 1, figsize=(20, 12))
fig.patch.set_facecolor('#c9dde5')
ax.set_facecolor('#add8e6')
world.plot(ax=ax, color='#ffffff')
max_trade = trade_data['Trade Volume'].max()

# Highlighting exporter and importer countries
exporter_countries = world[world['ISO_A2'].isin(trade_data['Exporter'])]
importer_countries = world[world['ISO_A2'].isin(trade_data['Importer'])]
exporter_countries.plot(ax=ax, color='#f4e3d4')
importer_countries.plot(ax=ax, color='#f4e3d4')

# Drawing arrows for trade flows
for _, row in trade_data.iterrows():
    if all(row['Exporter_coords']) and all(row['Importer_coords']):
        # draw_arrow(ax, row['Exporter_coords'], row['Importer_coords'], row['Trade Volume'], max_trade)
        draw_curved_arrow(ax, row['Exporter_coords'], row['Importer_coords'], row['Trade Volume'], max_trade)

# Drawing centroids for exporter and importer countries
for code in trade_data['Exporter'].unique():
    volume = trade_data[trade_data['Exporter'] == code]['Trade Volume'].sum()
    centroid = centroids.get(code)
    if centroid:
        draw_centroid(ax, centroid, volume, max_trade, '#70b28b')

for code in trade_data['Importer'].unique():
    volume = trade_data[trade_data['Importer'] == code]['Trade Volume'].sum()
    centroid = centroids.get(code)
    if centroid:
        draw_centroid(ax, centroid, volume, max_trade, '#d47185')

# ax.set_title('Customized World Trade Flow Map', fontsize=20)
create_custom_legend(ax)
ax.set_axis_off()

plt.savefig(r'./output/Top 20 Flows of Wildlife Trade.svg', bbox_inches='tight')
plt.show()
