import pandas as pd

# 加载数据，跳过错误行
files = [
    './data/Chicago_Crimes_2001_to_2004.csv',
    './data/Chicago_Crimes_2005_to_2007.csv',
    './data/Chicago_Crimes_2008_to_2011.csv',
    './data/Chicago_Crimes_2012_to_2017.csv'
]

df_list = []
for file in files:
    df_temp = pd.read_csv(file, on_bad_lines='skip', low_memory=False)
    df_list.append(df_temp)

df = pd.concat(df_list, ignore_index=True)

# 解析日期并创建一个新的月份列
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
df['Month'] = df['Date'].dt.to_period('M')

# 按月份统计犯罪数量
monthly_crimes = df.groupby('Month').size()

# 绘制折线图
monthly_crimes.plot(kind='line', figsize=(10, 6))

# 导出数据到CSV
monthly_crimes.to_csv('Chicago_Crimes_Counts.csv', header=['Crime_Count'])
