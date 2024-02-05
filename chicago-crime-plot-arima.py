import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
from theme.unodc import *


def sci_notation(x, pos):
    return f'{x:.0E}'


formatter = FuncFormatter(sci_notation)

data = pd.read_csv(r'data/Chicago_Crimes_Predictions-ARIMA.csv', encoding='utf-8')

data['Month'] = pd.to_datetime(data['Month'])
# data['Crime_Count_Predictions'] = data['Crime_Count_Predictions'].fillna(data['Crime_Count'])
for i in range(len(data)):
    if pd.isna(data['Crime_Count_Predictions'].iloc[i]):
        data['Crime_Count_Predictions'].iloc[i] = data['Crime_Count'].iloc[i]
data['Cumulative_Crime_Count'] = data['Crime_Count'].cumsum()
data['Cumulative_Crime_Predictions'] = data['Crime_Count_Predictions'].cumsum()
print(data)

plt.figure(figsize=(12, 8))
plt.plot(data['Month'], data['Cumulative_Crime_Count'], linestyle='-', color=COLORS_GREEN[-1], lw=1,
         label='Origin Data')
plt.plot(data['Month'], data['Cumulative_Crime_Predictions'], linestyle=':', color=COLORS_GREEN[1], lw=2,
         label='Predictive Data')
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Cumulative Crime Count')

plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,)))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().yaxis.set_major_formatter(formatter)

plt.legend()
plt.savefig(r'./output/Chicago Crime Events Counts.svg', bbox_inches='tight')
plt.show()
