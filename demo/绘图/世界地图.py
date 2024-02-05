import geopandas as gpd
import matplotlib.pyplot as plt

# 加载内置的世界地图数据
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# 你可以在这里添加自己的数据来为每个国家/地区设定颜色
# 例如，使用一些随机数据来表示不同的颜色
world['RandomValue'] = world['pop_est'] / max(world['pop_est'])

# 绘制地图
fig, ax = plt.subplots(1, 1)
world.plot(column='RandomValue', ax=ax, legend=True,
           legend_kwds={'label': "Rate", 'orientation': "horizontal"})

plt.show()
