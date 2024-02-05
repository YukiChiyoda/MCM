import numpy as np
import matplotlib.pyplot as plt

# 初始化原始数据
x0 = np.array([34, 45, 78, 90])

# 计算累加生成序列
x1 = np.cumsum(x0)

# 初始化af参数和z1序列
af = 0.4
z1 = np.zeros(x1.shape)
z1[0] = 0  # z1的第一个元素是0

# 计算z1序列，即累加生成序列的均值序列
for i in range(1, len(x1)):
    z1[i] = x1[i] * af + (1 - af) * x1[i - 1]

# 初始化Y和X矩阵
Y = x0[1:].reshape(-1, 1)  # 目标变量
X = np.vstack((-z1[1:], np.ones(len(z1) - 1))).T  # 解释变量，包括z1和常数项

# 使用最小二乘法计算系数B
B = np.linalg.inv(X.T @ X) @ X.T @ Y
a, b = B.flatten()  # 展开B获取a和b

# 预测下一个值
# pred_n_1 = (x0[0] - b / a) * np.exp(-a * len(x0)) * (1 - np.exp(a))

# 设置x的范围和计算对应的y值进行s绘图
x = np.arange(0, len(x0) + 5, 0.1)
y3 = (x0[0] - b / a) * np.exp(-a * x) * (1 - np.exp(a))
print(y3)

# 绘制y3
plt.plot(x, y3, '-')

# 绘制原始数据点
n0 = np.arange(len(x0))
plt.plot(n0, x0, '*')

# 显示图表
plt.show()
