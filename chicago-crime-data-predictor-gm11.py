import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'./data/Chicago_Crimes_Counts.csv', encoding='utf-8')

data['Month'] = pd.to_datetime(data['Month'])
data['Cumulative_Crime_Count'] = data['Crime_Count'].cumsum()

x0 = np.array(data['Crime_Count'])

x1 = np.cumsum(x0)

af = 0.4
z1 = np.zeros(x1.shape)
z1[0] = 0

for i in range(1, len(x1)):
    z1[i] = x1[i] * af + (1 - af) * x1[i - 1]

Y = x0[1:].reshape(-1, 1)
X = np.vstack((-z1[1:], np.ones(len(z1) - 1))).T

B = np.linalg.inv(X.T @ X) @ X.T @ Y
a, b = B.flatten()

x = np.arange(0, len(x0) + 12 * 7, 1)  # 预测到2024-01
y3 = (x0[0] - b / a) * np.exp(-a * x) * (1 - np.exp(a))
print(y3)

plt.plot(x, y3, '-')

n0 = np.arange(len(x0))
plt.plot(n0, x0, '*')

# plt.show()

data['Month'] = pd.to_datetime(data['Month'])

# 找到最后一个月份
last_month = data['Month'].max()

# 生成未来月份数据，预测到2024年01月
months_to_predict = pd.date_range(start=last_month, periods=12 * 7 + 1, freq='M')[1:]  # 生成额外的月份数据

# 创建新的DataFrame以包含预测的月份
new_rows = pd.DataFrame({"Month": months_to_predict})

# 将新行添加到现有DataFrame
extended_data = pd.concat([data, new_rows], ignore_index=True)

# 确保Month列以字符串格式回写，与原始数据格式保持一致
extended_data['Month'] = extended_data['Month'].dt.strftime('%Y-%m')
extended_data['Cumulative_Crime_Count'][:len(data['Cumulative_Crime_Count'])] = data['Cumulative_Crime_Count']
extended_data['Crime_Predictions'] = y3
extended_data['Cumulative_Crime_Predictions'] = extended_data['Crime_Predictions'].cumsum()

# 显示扩展后的数据的最后几行，确保格式正确
print(extended_data.tail())
extended_data.to_csv(r'./data/Chicago_Crimes_Predictions-GM11.csv', index=False, encoding='utf-8')
