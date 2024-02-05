import matplotlib.pyplot as plt
from theme.unodc import *

plt.figure(figsize=(12, 8), dpi=300)

# 原始数据点
original_real_data_point = (0.900, 0.696)
original_ideal_data_point = (1, 1)

# 新的理想点
ideal_data_point = (1, 1)

# 计算原始比例
x_ratio = original_real_data_point[0] / original_ideal_data_point[0]
y_ratio = original_real_data_point[1] / original_ideal_data_point[1]

# 应用比例到新的理想点来获得新的现实点
real_data_point = (ideal_data_point[0] * x_ratio, ideal_data_point[1] * y_ratio)
real_data_point2 = (0.568, 0.255)

# 绘制数据点
plt.scatter(*real_data_point, s=100, label='Nash Equilibrium Point A', color=COLORS_ORANGE[2], edgecolors='#381E21',
            zorder=100)
plt.scatter(*real_data_point2, s=100, label='Nash Equilibrium Point B', color=COLORS_BLUE[2], edgecolors='#381E21',
            zorder=100)

# 添加数据点坐标文本
offset = 0.02  # 文本偏移量
plt.text(real_data_point[0] + offset, real_data_point[1] + offset,
         f'({real_data_point[0]:.3f}, {real_data_point[1]:.3f})', ha='center')
plt.text(real_data_point2[0] + offset, real_data_point2[1] + offset,
         f'({real_data_point2[0]:.3f}, {real_data_point2[1]:.3f})', ha='left')

# 绘制分向量线段
# 水平线段
plt.plot([real_data_point[0], real_data_point2[0]], [real_data_point[1], real_data_point[1]], linestyle='--',
         linewidth=2, color='#381E21')
# 垂直线段
plt.plot([real_data_point[0], real_data_point[0]], [real_data_point[1], real_data_point2[1]], linestyle='--',
         linewidth=2, color='#381E21')

# 绘制分向量线段
# 水平线段
plt.plot([real_data_point2[0], real_data_point[0]], [real_data_point2[1], real_data_point2[1]], linestyle='--',
         linewidth=2, color='#381E21')
# 垂直线段
plt.plot([real_data_point2[0], real_data_point2[0]], [real_data_point2[1], real_data_point[1]], linestyle='--',
         linewidth=2, color='#381E21')

# 添加图例
plt.legend(loc='upper left')

# 添加网格
plt.grid(True)

# 设置坐标轴标签
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('Probability of Strict Enforcement')
plt.ylabel('Probability of Committing a Crime')

# 隐藏上边和右边的边框
# ax = plt.gca()  # 获取当前的Axes对象
# ax.spines['top'].set_visible(False)  # 隐藏上边框
# ax.spines['right'].set_visible(False)  # 隐藏右边框
ax = plt.gca()
ax.spines['left'].set_linewidth(2)  # 加粗左边框
ax.spines['bottom'].set_linewidth(2)  # 加粗下边框
ax.spines['top'].set_linewidth(2)  # 加粗左边框
ax.spines['right'].set_linewidth(2)  # 加粗下边框

# 显示图像
plt.savefig(r'./output/Nash Equilibrium 3-3.svg')
plt.show()
