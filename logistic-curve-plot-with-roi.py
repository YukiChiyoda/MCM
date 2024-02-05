import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from theme.unodc import *


# 定义给定的函数导数
def dB1_dt(t):
    return 1 / (1 + np.exp(-t))


def dB2_dt(t):
    return 1 + np.sin(t)


def dB3_dt(t):
    return 1 / (1 + t)


def dB4_dt(t):
    return 1


# 定义权重
w1, w2, w3, w4 = 0.4, 0.3, 0.2, 0.1


# 定义C的组成部分的函数
def C2(t):
    return t - np.exp(-t)


def C3(t):
    return 1 - np.exp(-t)


# 定义γ值
γ1, γ2, γ3 = 0.4, 0.4, 0.2


# 积分函数以计算B(t)和C(t)，考虑B3的初始值
def B(t):
    return (
            w1 * quad(dB1_dt, 0, t)[0] +
            w2 * quad(dB2_dt, 0, t)[0] +
            w3 * (quad(dB3_dt, 0, t)[0] + 1) +  # 考虑B3的初始值
            w4 * quad(dB4_dt, 0, t)[0]
    )


def C(t):
    C1 = 3
    return (γ1 * C1 +
            γ2 * C2(t) +
            γ3 * C3(t))


# 生成时间点
t_values = np.arange(0, 5.001, 0.001)

# 计算B(t)和C(t)的值
B_values = [B(t) for t in t_values]
C_values = [C(t) for t in t_values]

# 绘制B(t)和C(t)
plt.figure(figsize=(10, 6))
plt.plot(t_values, B_values, label=r'$B(t)$', color=COLORS_BLUE[-1])
plt.plot(t_values, C_values, label=r'$C(t)$', linestyle='--', color=COLORS_RED[-2])

# 修正：生成布尔数组
where_b_less_c = np.array(B_values) < np.array(C_values)
where_b_greater_c = np.array(B_values) > np.array(C_values)

# 使用修正后的布尔数组
plt.fill_between(t_values, B_values, C_values, where=where_b_less_c, color=COLORS_RED[0], alpha=0.5)
plt.fill_between(t_values, B_values, C_values, where=where_b_greater_c, color=COLORS_BLUE[0], alpha=0.5)

# 计算NB和ROI的值，避免除以零
NB_values = np.array(B_values) - np.array(C_values)
ROI_values = np.where(np.array(C_values) != 0, NB_values / np.array(C_values), 0)
plt.plot(t_values, ROI_values, label=r'$ROI$', color=COLORS_ORANGE[3], linestyle='-.')

# 寻找并绘制交点及标注坐标
for i in range(1, len(t_values)):
    if (B_values[i - 1] - C_values[i - 1]) * (B_values[i] - C_values[i]) < 0:
        # 计算交点的近似时间
        t_intersect = t_values[i]
        # 计算交点的近似值
        b_intersect = B_values[i]
        # 绘制交点
        plt.scatter([t_intersect], [b_intersect], color=COLORS_RED[-3], zorder=100)
        # 标注坐标
        plt.annotate(f'({t_intersect:.2f}, {b_intersect:.2f})', (t_intersect, b_intersect),
                     textcoords="offset points",
                     xytext=(-20, 10), ha='center')

plt.fill_between(t_values, ROI_values, -100, color=COLORS_ORANGE[0], alpha=0.5)

plt.xlim(0, 5)
plt.ylim(min(ROI_values) - 0.5, max(B_values) + 0.5)
plt.xlabel(r'Time $t$')
plt.ylabel(r'Values')
plt.legend()
plt.grid(True)
plt.savefig(r'./output/Curve Fit with ROI.svg', bbox_inches='tight')
plt.show()
