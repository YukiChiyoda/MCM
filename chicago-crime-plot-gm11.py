import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter


def sci_notation(x, pos):
    return f'{x:.0E}'


formatter = FuncFormatter(sci_notation)

data = pd.read_csv(r'data/Chicago_Crimes_Predictions-GM11.csv', encoding='utf-8')

data['Month'] = pd.to_datetime(data['Month'])
data['Cumulative_Crime_Count'] = data['Crime_Count'].cumsum()

plt.figure(figsize=(12, 8))
plt.plot(data['Month'], data['Cumulative_Crime_Count'], linestyle='-', color='r', label='Origin Data')
plt.plot(data['Month'], data['Cumulative_Crime_Predictions'], linestyle='-', color='b', label='Predictive Data')
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Cumulative Crime Count')

plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,)))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().yaxis.set_major_formatter(formatter)

plt.savefig(r'./output/Chicago Crime Events Counts.svg', bbox_inches='tight')
plt.show()
