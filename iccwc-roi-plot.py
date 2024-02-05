import numpy as np
from matplotlib import pyplot as plt
from theme.unodc import *

w1, w2, w3, w4 = 0.2, 0.2, 0.2, 0.4
r1, r2, r3 = 0.45, 0.5, 0.05


def C1():
    return 25


def C2(t):
    return t - np.exp(-t)


def C3(t):
    return 1 - np.exp(-t)


def C(t):
    return r1 * C1() + r2 * C2(t) + r3 * C3(t)


def dB1dt(t):
    return 1 / (1 + np.exp(-t))


def dB2dt(t):
    return 1 + np.sin(t)


def dB3dt(t):
    return 1 / (1 + t)


def dB4dt():
    return 1


def dBdt(t):
    return w1 * dB1dt(t) + w2 * dB2dt(t) + w3 * dB3dt(t) + w4 * dB4dt()


def solve(init, step, end):
    t_values = np.arange(0, end, step)
    B1_values = np.zeros(len(t_values))
    B2_values = np.zeros(len(t_values))
    B3_values = np.zeros(len(t_values))
    B4_values = np.zeros(len(t_values))
    B_values = np.zeros(len(t_values))
    C_values = np.zeros(len(t_values))
    NB_values = np.zeros(len(t_values))
    ROI_values = np.zeros(len(t_values))
    B1_values[0], B2_values[0], B3_values[0], B4_values[0], B_values[0] = init[0], init[1], init[2], init[3], init[4]

    for i in range(1, len(t_values)):
        B1_values[i] = B1_values[i - 1] + dB1dt(i) * step
        B2_values[i] = B2_values[i - 1] + dB2dt(i) * step
        B3_values[i] = B3_values[i - 1] + dB3dt(i) * step
        B4_values[i] = B4_values[i - 1] + dB4dt() * step
        B_values[i] = B_values[i - 1] + dBdt(i) * step
        C_values[i] = C(i)
        NB_values[i] = B_values[i] - C(i)
        ROI_values[i] = NB_values[i] / C(i)

    keys = ['t', 'B1', 'B2', 'B3', 'B4', 'B', 'C', 'NB', 'ROI']
    values = [t_values, B1_values, B2_values, B3_values, B4_values, B_values, C_values, NB_values, ROI_values]
    return dict(zip(keys, values))


result = solve([0, 0, 0, 0, 3], 1, 12 * 5)

# plt.plot(result['t'], result['B1'], ls='-', lw=2, label=rf'$B1$')
# plt.plot(result['t'], result['B2'], ls='-', lw=2, label=rf'$B2$')
# plt.plot(result['t'], result['B3'], ls='-', lw=2, label=rf'$B3$')
# plt.plot(result['t'], result['B4'], ls='-', lw=2, label=rf'$B4$')
plt.plot(result['t'], result['B'], ls='-', lw=2, label=rf'$B$')
plt.plot(result['t'], result['C'], ls=':', lw=2, label=rf'$C$')

plt.xlim(left=1)
plt.legend()
plt.show()
