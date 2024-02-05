import numpy as np


# 定义模糊逻辑乘法和加法的函数
def fuzzy_logic_multiply_and_add(weights, relation_matrix):
    composite_evaluation = np.zeros(relation_matrix.shape[1])
    for i, weight in enumerate(weights):
        for j in range(relation_matrix.shape[1]):
            temp = min(weight, relation_matrix[i][j])
            composite_evaluation[j] = max(composite_evaluation[j], temp)
    return composite_evaluation


# 定义归一化函数
def normalize_vector(vector):
    sum_of_elements = np.sum(vector)
    if sum_of_elements == 0:
        return vector
    return vector / sum_of_elements


# 定义权重向量
W = np.array([0.2, 0.3, 0.5])

# 定义项目字典，存储每个项目的评价矩阵
projects = {
    '甲': np.array([
        [0.7, 0.2, 0.1],
        [0.1, 0.2, 0.7],
        [0.3, 0.6, 0.1]
    ]),
    '乙': np.array([
        [0.3, 0.6, 0.1],
        [1, 0, 0],
        [0.7, 0.3, 0]
    ]),
    '丙': np.array([
        [0.1, 0.4, 0.5],
        [1, 0, 0],
        [0.1, 0.3, 0.6]
    ])
    # 可以继续添加更多项目...
}

# 计算每个项目的综合评价结果并归一化
results = {}
for name, R in projects.items():
    B_fuzzy = fuzzy_logic_multiply_and_add(W, R)
    B_normalized = normalize_vector(B_fuzzy)
    results[name] = np.round(B_normalized, 2)

print(results)
