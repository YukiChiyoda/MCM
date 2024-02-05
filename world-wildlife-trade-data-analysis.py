import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
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
top_trades = filtered_data[['Importer', 'Exporter']].copy()
top_trades['Trade Volume'] = filtered_data[['Importer reported quantity', 'Exporter reported quantity']].max(
    axis=1)
top_trades = top_trades.sort_values('Trade Volume', ascending=False)

nations_trades = top_trades.groupby('Importer', as_index=True).sum()
print(nations_trades.sort_values('Trade Volume', ascending=False).head())
print(nations_trades.loc['DE']['Trade Volume'] / top_trades['Trade Volume'].sum())
