import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from theme.rainbow import *
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

plt.figure(0, figsize=(18, 12))
plt.subplots_adjust(left=0.06, bottom=0.05, right=0.97, top=0.96, wspace=0.2, hspace=0.2)
style = {
    "cmap": ListedColormap(COLORS),
    # "shading": 'gouraud',
    "vmin": 3500,
    "vmax": 5000
}

data = pd.read_csv(r'data/Chicago_Crimes_Counts.csv', encoding='utf-8')
x = np.arange(0, len(data))
y = np.array(data['Crime_Count'])

t = 1e8
k = []
p_max, q_max = 5, 5
warnings.filterwarnings('ignore')


def draw(d, px, py, paic, pbic):
    for k in range(2):
        ax = plt.subplot(2, 3, k * 3 + d + 1)
        # plt.grid(True, c='w')
        plt.title(fr"{'AIC' if k % 2 == 0 else 'BIC'} Result when $d={d}$")
        plt.xlabel(r"Parameter $q$ in ARIMA Model")
        plt.ylabel(r"Parameter $p$ in ARIMA Model")
        plt.pcolormesh(px, py, paic if k % 2 == 0 else pbic, **style)
        plt.colorbar(shrink=0.9)
        # for p in range(p_max):
        #     for q in range(q_max):
        #         plt.text(q, p, f'{paic[p, q] if k % 2 == 0 else pbic[p, q]:.0f}',
        #                  ha='center', va='center', color='w', fontsize=6)


for d in range(3):
    paic = np.zeros((p_max, q_max))
    pbic = np.zeros((p_max, q_max))

    for p in range(p_max):
        for q in range(q_max):
            model = sm.tsa.ARIMA(y, order=(p, d, q))
            results = model.fit()
            aic, bic = results.aic, results.bic
            # if p == d == q == 1:
            #     aic *= 0.952
            #     bic *= 0.95
            if t > np.mean([aic, bic]):
                t = np.mean([aic, bic])
                k = [p, d, q, aic, bic]
            paic[p, q] = aic
            pbic[p, q] = bic
            print(f'p={p}, d={d}, q={q}: aic={aic} | bic={bic}')

    px, py = np.meshgrid(range(p_max), range(q_max))

    draw(d, px, py, paic, pbic)

print(f'★p={k[0]}, d={k[1]}, q={k[2]}: aic={k[3]} | bic={k[4]}')
plt.savefig(r'./output/AIC & BIC of Arima Model.svg', bbox_inches='tight')
plt.show()
