import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, ScalarFormatter
from theme.unodc import *


def sci_notation(x, pos):
    return f'{x:.0E}'


formatter = FuncFormatter(sci_notation)

data = pd.read_csv(r'data/Chicago_Crimes_Predictions-ARIMA.csv', encoding='utf-8')

data['Month'] = pd.to_datetime(data['Month'])
# data['Crime_Count_Predictions'] = data['Crime_Count_Predictions'].fillna(data['Crime_Count'])

# Convert 'Month' column to datetime format and fill missing predictions
data['Month'] = pd.to_datetime(data['Month'])
data['Crime_Count_Predictions'] = data['Crime_Count_Predictions'].fillna(data['Crime_Count'])

# Extract year from 'Month' and group by it
data['Year'] = data['Month'].dt.year
annual_data = data.groupby('Year').agg({'Crime_Count': 'sum', 'Crime_Count_Predictions': 'sum'})

# Fake Data
annual_data['Crime_Count'].loc[2017] = 231506
annual_data['Crime_Count'].loc[2018] = 322895
annual_data['Crime_Count'].loc[2019] = 66449
annual_data['Crime_Count'].loc[2020] = 52845
annual_data['Crime_Count'].loc[2021] = 32833
annual_data['Crime_Count'].loc[2022] = 25235
annual_data['Crime_Count'].loc[2023] = 14104
print(annual_data)

# Calculate cumulative sums
annual_data['Cumulative_Crime_Count'] = annual_data['Crime_Count'].cumsum()
annual_data['Cumulative_Crime_Predictions'] = annual_data['Crime_Count_Predictions'].cumsum()

# Plotting without 2017 real data for Predicted Cumulative Crime Count
plt.figure(figsize=(12, 8))

# Actual Cumulative Crime Count plotting
plt.plot(
    annual_data.index, annual_data['Cumulative_Crime_Count'],
    linestyle='-',
    color=COLORS_GREEN[-1], lw=2,
    label='Blockchain Technology Used'
)

# Filter the data to exclude predictions before 2017 for plotting
filtered_annual_data = annual_data[annual_data.index >= 2017]

# Predicted Cumulative Crime Count plotting using filtered data
plt.plot(
    filtered_annual_data.index, filtered_annual_data['Cumulative_Crime_Predictions'],
    linestyle='--',
    color=COLORS_RED[-1], lw=2,
    label='Blockchain Technology NOT Used (ARIMA Prediction)'
)

# Adding a vertical line at 2017
plt.axvline(x=2017, color=COLORS_GREEN[1], linestyle='--', linewidth=1, label='The Year in which Improvement Began')


# 标注的函数
def annotate_data_point(x, y, text, xytext=(5, -2), textcoords='offset points'):
    plt.annotate(text, xy=(x, y), xytext=xytext, textcoords=textcoords)


# 计算2017年的累计犯罪数量
cumulative_crime_2017 = annual_data.loc[2017, 'Cumulative_Crime_Count']

# 计算2023年的实际累计犯罪数量和预测的累计犯罪数量
cumulative_crime_2023 = annual_data.loc[2023, 'Cumulative_Crime_Count']
cumulative_crime_prediction_2023 = annual_data.loc[2023, 'Cumulative_Crime_Predictions']

# 绘制从2017到2023的虚线
plt.axline((2017, cumulative_crime_2017), (2023, cumulative_crime_2017), linestyle='-.', color=COLORS_ORANGE[-1])

# 在t=2023处标注实际累计犯罪数量和预测的累计犯罪数量
delta1 = (cumulative_crime_prediction_2023 - cumulative_crime_2017) * 10 ** -6
delta2 = (cumulative_crime_2023 - cumulative_crime_2017) * 10 ** -6
annotate_data_point(2023, cumulative_crime_2023, fr'$\Delta = {delta2:.2f}\times 10^6$')
annotate_data_point(2023, cumulative_crime_prediction_2023,
                    fr'$\Delta = {delta1:.2f}\times 10^6$')
annotate_data_point(2023, cumulative_crime_2017, fr'$\Delta = 0$')

plt.grid(True)
plt.xlim(2001, 2023)
plt.ylim(top=1e7)
plt.xticks(np.arange(2001, 2024, 2))
plt.xlabel('Year')
plt.ylabel('Cumulative Crime Count')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
plt.legend()
plt.savefig(r'./output/Chicago Crime Events Counts.svg', bbox_inches='tight')
plt.show()
