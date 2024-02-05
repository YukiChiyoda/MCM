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

# plt.fill_between(t_values, B_values, -100, color='#f7e1e2', alpha=0.5)
# plt.fill_between(t_values, C_values, -100, color='#accdea', alpha=0.5)

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

# 首先，我们计算 t=5 时 B 和 C 的值
B_at_5 = B(5)
C_at_5 = C(5)

# 标注 t=5 时的值
plt.scatter([5], [B_at_5], color=COLORS_BLUE[-1], clip_on=False, zorder=100)  # B(t)的点
plt.scatter([5], [C_at_5], color=COLORS_RED[-2], clip_on=False, zorder=100)  # C(t)的点

# 添加文本标注
plt.text(4.5, B_at_5, f'B(5)={B_at_5:.2f}', verticalalignment='bottom')
plt.text(4.5, C_at_5 + 0.2, f'C(5)={C_at_5:.2f}', verticalalignment='top')

plt.xlim(0, 5)
plt.ylim(0, max(B_values) + 0.5)
plt.xlabel(r'Time $t$')
plt.ylabel(r'Values')
plt.legend()
plt.grid(True)
plt.savefig(r'./output/Curve Fit without ROI.svg', bbox_inches='tight')
plt.show()
