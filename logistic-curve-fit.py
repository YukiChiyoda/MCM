import numpy as np
import pandas as pd
from theme.rainbow import *
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LightSource

# data_1 = pd.read_csv(r'./data/multiTimeline_Concreted_by_Year.csv', encoding='utf-8')
# data_2 = pd.read_csv(r'./data/national-gdp_USA.csv', encoding='utf-8')
# merged_data = pd.merge(data_1, data_2, on='Year', how='inner')
merged_data = pd.read_csv(r'./data/fake_data.csv', encoding='utf-8')

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Reshape data for scaling
volume_reshaped = merged_data['Volume'].values.reshape(-1, 1)
gdp_reshaped = merged_data['GDP'].values.reshape(-1, 1)

# Scale the Volume and GDP columns
merged_data['Normalized_Volume'] = scaler.fit_transform(volume_reshaped)
merged_data['Normalized_GDP'] = scaler.fit_transform(gdp_reshaped)

X = np.array(list(zip(merged_data['Normalized_Volume'], merged_data['Normalized_GDP'])))  # 特征数据，每个内部数组代表一个观测的x1和x2
y = np.array(merged_data['Adoption'])  # 目标变量，表示每个观测的结果

# 创建逻辑回归模型实例
model = LogisticRegression()

# 拟合模型
model.fit(X, y)

# 打印拟合参数
# print("b0 (intercept):", model.intercept_)
# print("b1, b2 (coefficients):", model.coef_)

# 获取模型参数
b0 = model.intercept_[0]  # 截距
b1, b2 = model.coef_[0]  # 系数

# 构建模型函数的字符串表示
model_function = f"P(x) = 1 / (1 + e^(-({b0:.4f} + {b1:.4f}*x1 + {b2:.4f}*x2)))"
print(model_function)

# from sklearn.metrics import *
#
# # 假设你已经有了一个测试集 X_test, y_test
# # X_test, y_test = ... # 你需要提供测试数据集
#
# # 使用模型进行预测
# y_pred = model.predict(X)  # 预测分类
# y_proba = model.predict_proba(X)  # 预测属于各类的概率
#
# # 计算评估指标
# accuracy = accuracy_score(y, y_pred)
# precision = precision_score(y, y_pred)
# recall = recall_score(y, y_pred)
# f1 = f1_score(y, y_pred)
# roc_auc = roc_auc_score(y, y_proba[:, 1])  # 注意：使用正类的概率
# logloss = log_loss(y, y_proba)
# mse = mean_squared_error(y, y_pred)
# r2 = r2_score(y, y_pred)
#
# print(f"MSE: {mse:.4f}")
# print(f"R^2: {r2:.4f}")
# print(f"Accuracy: {accuracy:.4f}")
# print(f"Precision: {precision:.4f}")
# print(f"Recall: {recall:.4f}")
# print(f"F1 Score: {f1:.4f}")
# print(f"ROC AUC: {roc_auc:.4f}")
# print(f"Log Loss: {logloss:.4f}")

# 打印模型函数
# print("拟合后的模型函数是：")
# print(model_function)

# 使用模型进行预测
# new_X = np.array([[2, 3], [3, 6]])  # 新的观测值
# predictions = model.predict(new_X)  # 预测分类
# probabilities = model.predict_proba(new_X)  # 预测属于各类的概率

# print("Predictions:", predictions)
# print("Probabilities:", probabilities)

x1 = np.linspace(0, 1, 100)  # x轴的100个点
x2 = np.linspace(0, 1, 100)  # y轴的100个点

# final_x = []
# final_y = []
# final_z = []
#
# for i in range(len(x1)):
#     for j in range(len(x2)):
#         probabilities = model.predict_proba(np.array([[x1[i], x2[j]]]))
#         final_x.append(x1[i])
#         final_y.append(x2[i])
#         final_z.append(probabilities[0][1])
#
# # 创建一个新的图形和一个3D子图
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # 使用trisurf创建三维等高线图
# ax.plot_trisurf(final_x, final_y, final_z, cmap='terrain')
#
# # 设置图表标题和坐标轴标签
# ax.set_title('3D Terrain Contour Map')
# ax.set_xlabel('X Coordinate')
# ax.set_ylabel('Y Coordinate')
# ax.set_zlabel('Height/Value')
#
# # 显示图表
# plt.show()
# 假设这些是从逻辑回归模型中获取的参数
# 为了演示，我将使用随机值
b0 = model.intercept_  # 截距
b1, b2 = model.coef_[0]

# 创建x1和x2的网格
x1, x2 = np.meshgrid(np.linspace(0, 1, 100), np.linspace(0, 1, 100))

# 将x1和x2的网格展平，然后堆叠，为预测准备
X_grid = np.column_stack((x1.ravel(), x2.ravel()))


# 使用模型进行预测概率
# 注意：这里用到的model是之前已经训练好的逻辑回归模型
# 由于这里是示例代码，我们直接用模型参数创建概率，而不是调用model.predict_proba
def predict_proba(X):
    # 计算线性组合
    z = b0 + X[:, 0] * b1 + X[:, 1] * b2
    # 应用逻辑函数
    return 1 / (1 + np.exp(-z))


# 获取P(1)的概率
probabilities = predict_proba(X_grid).reshape(x1.shape)

# 绘制热力图
plt.figure(figsize=(8, 6))
plt.imshow(probabilities, extent=(0, 1, 0, 1), origin='lower', cmap=CMAP, aspect='auto')
plt.colorbar(label='P(1) Probability')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.savefig(r'./output/Probability Heatmap.svg', bbox_inches='tight')
plt.show()
