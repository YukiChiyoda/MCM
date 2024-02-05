import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置随机数种子以便结果可复现
np.random.seed(42)

# 生成随机数据
# 假设每组数据有50个点
num_points = 50

# "Before GGDP"的数据点
x_before = np.random.normal(0, 1, num_points)  # 均值0，标准差1
y_before = np.random.normal(0, 1, num_points)
z_before = np.random.normal(0, 1, num_points)

# "After GGDP"的数据点
x_after = np.random.normal(1, 1, num_points)  # 均值1，标准差1
y_after = np.random.normal(1, 1, num_points)
z_after = np.random.normal(1, 1, num_points)

# 创建一个新的图形并添加一个3D子图
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# 为"Before GGDP"的数据点绘制散点图
scatter_before = ax.scatter(x_before, y_before, z_before, color='blue', label='Before GGDP')

# 为"After GGDP"的数据点绘制散点图
scatter_after = ax.scatter(x_after, y_after, z_after, color='red', label='After GGDP')

# 设置坐标轴标签
ax.set_xlabel('Temperature')
ax.set_ylabel('Ecology')
ax.set_zlabel('Environment')

# 创建图例
ax.legend()

# 显示绘图结果
plt.show()
