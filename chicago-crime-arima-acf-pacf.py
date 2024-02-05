import pandas as pd
import matplotlib.pyplot as plt
from theme.unodc import *
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

register_matplotlib_converters()

data = pd.read_csv(r'data/Chicago_Crimes_Counts.csv', encoding='utf-8')

data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)

plt.figure(figsize=(12, 6))


def force_change_color(my_ax, my_color):
    from matplotlib.collections import PolyCollection, LineCollection
    for item in my_ax.collections:
        if type(item) == PolyCollection:
            item.set_facecolor(my_color)
        if type(item) == LineCollection:
            item.set_color(my_color)
    for item in ax.lines:
        item.set_color(my_color)


for i in range(2):
    ax = plt.subplot(1, 2, i + 1)
    plt.grid(True)
    plt.xlabel('Lag')
    if i == 0:
        plot_acf(data['Crime_Count'], ax=plt.gca(), lags=20, color=COLORS_GREEN[-1])
        force_change_color(ax, COLORS_GREEN[2])
    else:
        plot_pacf(data['Crime_Count'], ax=plt.gca(), lags=20, method='ywm', color=COLORS_GREEN[1])
        force_change_color(ax, COLORS_GREEN[2])

plt.legend()
plt.savefig(r'./output/ACF & PACF of Arima Model.svg', bbox_inches='tight')
plt.show()
