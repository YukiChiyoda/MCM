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
top_trades = top_trades.sort_values('Trade Volume', ascending=False).head(20)

print(top_trades)

top_trades.to_csv(r'./data/comptab_processed_data.csv', encoding='utf-8', index=False)
exit()

import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Add lat and lon of Importer and Exporter
country_coordinates = {'DE': {'lat': 51.1657, 'lon': 10.4515}, 'CN': {'lat': 35.8617, 'lon': 104.1954},
                       'US': {'lat': 37.0902, 'lon': -95.7129}, 'TW': {'lat': 23.6978, 'lon': 120.9605},
                       'GE': {'lat': 42.3154, 'lon': 43.3569}, 'TR': {'lat': 38.9637, 'lon': 35.2433},
                       'JP': {'lat': 36.2048, 'lon': 138.2529}, 'Unknown': {'lat': 0, 'lon': 0}}

top_trades['Importer_lat'] = top_trades['Importer'].map(
    lambda x: country_coordinates.get(x, country_coordinates['Unknown'])['lat'])
top_trades['Importer_lon'] = top_trades['Importer'].map(
    lambda x: country_coordinates.get(x, country_coordinates['Unknown'])['lon'])
top_trades['Exporter_lat'] = top_trades['Exporter'].map(
    lambda x: country_coordinates.get(x, country_coordinates['Unknown'])['lat'])
top_trades['Exporter_lon'] = top_trades['Exporter'].map(
    lambda x: country_coordinates.get(x, country_coordinates['Unknown'])['lon'])

# 创建新的地图实例
fig, ax = plt.subplots(figsize=(20, 10), subplot_kw={'projection': ccrs.PlateCarree()})

# 添加陆地、海洋和海岸线特征
ax.add_feature(cfeature.LAND.with_scale('110m'), color='lightgrey')
ax.add_feature(cfeature.OCEAN.with_scale('110m'), color='lightblue')
ax.add_feature(cfeature.COASTLINE.with_scale('110m'), edgecolor='black')
ax.add_feature(cfeature.BORDERS.with_scale('110m'), linestyle=':')

# 设置图例
high_volume = plt.Line2D([0], [0], color='red', linewidth=5, alpha=0.65, label='High volume flow')
low_volume = plt.Line2D([0], [0], color='red', linewidth=2, alpha=0.65, label='Low volume flow')
legend = ax.legend(handles=[high_volume, low_volume], loc='lower left',
                   title='Main trafficking flows based on adjusted seizures')

# 绘制贸易路线
for index, row in top_trades.iterrows():
    # 根据贸易量设定线条的粗细
    linewidth = 5 if row['Trade Volume'] > 10000000 else 2

    # 绘制线条
    ax.plot([row['Exporter_lon'], row['Importer_lon']], [row['Exporter_lat'], row['Importer_lat']],
            color='red', linewidth=linewidth, alpha=0.65, transform=ccrs.Geodetic())

    # 绘制圆点以表示贸易量大小，大小按照贸易量缩放
    circle_radius = 0.2 * np.sqrt(row['Trade Volume']) / 1000
    ax.add_patch(Circle(xy=(row['Exporter_lon'], row['Exporter_lat']), radius=circle_radius, color='green', alpha=0.5,
                        transform=ccrs.PlateCarree()))
    ax.add_patch(Circle(xy=(row['Importer_lon'], row['Importer_lat']), radius=circle_radius, color='blue', alpha=0.5,
                        transform=ccrs.PlateCarree()))

# 设置地图范围
ax.set_extent([-180, 180, -60, 80], crs=ccrs.PlateCarree())

# 显示图形
plt.show()
