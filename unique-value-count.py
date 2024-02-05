import pandas as pd

# 加载CSV文件
file_path = './data/comptab_2018-01-29 16_00_comma_separated.csv'
data = pd.read_csv(file_path)

# 统计'Importer'和'Exporter'列的唯一值数量
unique_importers = data['Importer'].nunique()
unique_exporters = data['Exporter'].nunique()

# 合并'Importer'和'Exporter'列为一个序列，并计算唯一值数量
unique_importer_exporter = pd.concat([data['Importer'], data['Exporter']]).nunique()

print(unique_importers, unique_exporters, unique_importer_exporter)
