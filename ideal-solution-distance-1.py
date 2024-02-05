import numpy as np
import matplotlib.pyplot as plt
from theme.unodc import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 原始理想数据点
ideal_point_original = (4.8413, 4.2312, 3.5071)
# 现实数据点
real_point_original = (2.3109, 2.2718, 3.5071)

# 标准化后的理想点为(1, 1, 1)
ideal_point = (1, 1, 1)
# 计算现实点的标准化比例
real_point_scale = tuple(r / i for r, i in zip(real_point_original, ideal_point_original))
# 应用比例以获得标准化的现实点
real_point = tuple(r * s for r, s in zip(ideal_point, real_point_scale))

# 创建一个新的3D图形
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d', facecolor='white')

# 绘制数据点
ax.scatter(*real_point, color=COLORS_RED[-2], s=100, label='Real Point', edgecolors='#381E21', zorder=100)
ax.scatter(*ideal_point, color=COLORS_GREEN[-2], s=100, label='Ideal Point', edgecolors='#381E21', zorder=100)

# 绘制从现实数据点到理想数据点的分向量
ax.plot([real_point[0], ideal_point[0]], [real_point[1], real_point[1]], [real_point[2], real_point[2]], linestyle='--',
        linewidth=2, color='#381E21')
ax.plot([real_point[0], real_point[0]], [real_point[1], ideal_point[1]], [real_point[2], real_point[2]], linestyle='--',
        linewidth=2, color='#381E21')
ax.plot([real_point[0], real_point[0]], [real_point[1], real_point[1]], [real_point[2], ideal_point[2]], linestyle='--',
        linewidth=2, color='#381E21')

# 绘制箭头
# ax.quiver(real_point[0], real_point[1], real_point[2],
#           ideal_point[0] - real_point[0], 0, 0,
#           color='#381E21', length=0.1, normalize=True)
# ax.quiver(real_point[0], real_point[1], real_point[2],
#           0, ideal_point[1] - real_point[1], 0,
#           color='#381E21', length=0.1, normalize=True)
# ax.quiver(real_point[0], real_point[1], real_point[2],
#           0, 0, ideal_point[2] - real_point[2],
#           color='#381E21', length=0.1, normalize=True)

# 设置图形的标签
# ax.set_xlabel('Finance', fontweight='bold')
# ax.set_ylabel('Expertise', fontweight='bold')
# ax.set_zlabel('International Collaboration', fontsize=6, fontweight='bold')

# 添加图例
ax.legend()

# 调整视角
ax.view_init(elev=35, azim=-55)

# 隐藏坐标轴的边框线
ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

# 设置坐标轴pane的边框颜色为透明
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

# 隐藏坐标轴面板的填充色
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# 定义新坐标轴的起点
origin = [0, 0, 0]  # 可以更改为所需的点

# 绘制新的坐标轴

# 箭头的长度
arrow_length = 1.2
arrow_ratio = 0.05

# 在箭头旁边放置坐标轴标签
ax.text(arrow_length, 0.1, -0.1, 'Finance', ha='left', va='center', fontsize=8)
ax.text(0, arrow_length + 0.1, -0.1, 'Expertise', ha='left', va='center', fontsize=8)
ax.text(-0.2, -0.1, arrow_length + 0.2, 'International Collaboration', ha='left', va='center', fontsize=8)

# 绘制X轴
ax.quiver(origin[0], origin[1], origin[2], 1, 0, 0, length=arrow_length, color='#381E21',
          arrow_length_ratio=arrow_ratio)
# 绘制Y轴
ax.quiver(origin[0], origin[1], origin[2], 0, 1, 0, length=arrow_length + 0.05, color='#381E21',
          arrow_length_ratio=arrow_ratio)
# 绘制Z轴
ax.quiver(origin[0], origin[1], origin[2], 0, 0, 1, length=arrow_length + 0.1, color='#381E21',
          arrow_length_ratio=arrow_ratio)

# 设置坐标轴的范围
ax.set_xlim([0, ax.get_xlim()[1]])
ax.set_ylim([0, ax.get_ylim()[1]])
ax.set_zlim([0, ax.get_zlim()[1]])

# 关闭原始坐标轴的刻度和标签
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# 设置刻度颜色为透明，但保留网格线
for tic in ax.xaxis.get_major_ticks():
    tic.tick1line.set_visible(True)  # 保留刻度线
    tic.label1.set_visible(False)  # 隐藏刻度标签
for tic in ax.yaxis.get_major_ticks():
    tic.tick1line.set_visible(True)
    tic.label1.set_visible(False)
for tic in ax.zaxis.get_major_ticks():
    tic.tick1line.set_visible(True)
    tic.label1.set_visible(False)

# 设置自定义坐标轴的刻度位置和标签
ticks_x = np.linspace(0, 1, 5)  # X轴的刻度
ticks_y = np.linspace(0.25, 1, 4)  # Y轴的刻度
ticks_z = np.linspace(0.25, 1, 4)  # Z轴的刻度

# 绘制自定义坐标轴的刻度和标签
for t in ticks_x:
    ax.text(t - 0.05, 0, -0.15, str(t), ha='center', va='center', color='#381E21')
for t in ticks_y:
    ax.text(0, t - 0.1, 0.15, str(t), ha='center', va='center', color='#381E21')
for t in ticks_z:
    ax.text(0, -0.15, t + 0.05, str(t), ha='center', va='center', color='#381E21')

# # 网格线的密度
# num_lines = 5
#
# # 获取坐标轴的最大值
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
# zlim = ax.get_zlim()
#
# # 生成线性空间以确定在哪里绘制网格线
# x_lines = np.linspace(xlim[0], xlim[1] - 0.05, num_lines)
# y_lines = np.linspace(ylim[0], ylim[1] - 0.05, num_lines)
# z_lines = np.linspace(zlim[0], zlim[1] - 0.05, num_lines)
#
# # 绘制平行于XY平面的网格线（在不同的Z值）
# for z in z_lines:
#     ax.plot(x_lines, [ylim[0]] * num_lines, z, linestyle=':', color='grey', alpha=0.5)
#     ax.plot([xlim[0]] * num_lines, y_lines, z, linestyle=':', color='grey', alpha=0.5)
#
# # 绘制平行于YZ平面的网格线（在不同的X值）
# for x in x_lines:
#     ax.plot([x] * num_lines, y_lines, np.full_like(y_lines, zlim[0]), linestyle=':', color='grey', alpha=0.5)
#
# # 绘制平行于XZ平面的网格线（在不同的Y值）
# for y in y_lines:
#     ax.plot(x_lines, [y] * num_lines, np.full_like(x_lines, zlim[0]), linestyle=':', color='grey', alpha=0.5)
#
# # 绘制与XZ平面平行的网格线（在Y轴的最大值处）
# for x in x_lines:
#     ax.plot([x, x], [ylim[0], ylim[0]], [zlim[0], zlim[1] - 0.05], linestyle=':', color='grey', alpha=0.5)
#
# # 绘制与YZ平面平行的网格线（在X轴的最大值处）
# for y in y_lines:
#     ax.plot([xlim[0], xlim[0]], [y, y], [zlim[0], zlim[1] - 0.05], linestyle=':', color='grey', alpha=0.5)

# 创建一个由所有角点坐标组成的列表
vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])

# 每个面由一系列顶点索引组成
faces = [[vertices[j] for j in [0, 1, 2, 3]],  # 下面
         [vertices[j] for j in [4, 5, 6, 7]],  # 上面
         [vertices[j] for j in [0, 1, 5, 4]],  # 前面
         [vertices[j] for j in [2, 3, 7, 6]],  # 后面
         [vertices[j] for j in [1, 2, 6, 5]],  # 右面
         [vertices[j] for j in [3, 0, 4, 7]]]  # 左面

# 创建3D多边形的集合
cube = Poly3DCollection(faces, linewidths=1, linestyles=':', edgecolors='#381E21', alpha=0.1)

# 设置每个面的颜色（这里我们使用相同的颜色和透明度）
face_color = (0.1, 0.7, 1, 0.1)  # 半透明的蓝色
cube.set_facecolor(face_color)

# 将创建的多边形集合添加到图形中
ax.add_collection3d(cube)

# 显示图形
plt.savefig(r'./output/Clients Resources-1.svg')
plt.show()
