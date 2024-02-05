import numpy as np


# 定义模糊逻辑乘法和加法的函数
def fuzzy_logic_multiply_and_add(weights, relation_matrix):
    composite_evaluation = np.zeros(relation_matrix.shape[1])
    for i, weight in enumerate(weights):
        for j in range(relation_matrix.shape[1]):
            temp = np.fmin(weight, relation_matrix[i][j])
            composite_evaluation[j] = np.fmax(composite_evaluation[j], temp)
    return composite_evaluation


# 定义归一化函数
def normalize_vector(vector):
    sum_of_elements = np.sum(vector)
    if sum_of_elements == 0:
        return vector
    return vector / sum_of_elements


# 定义多级模糊综合评价的函数
def multi_level_fuzzy_evaluation(criteria_weights, sub_criteria):
    # 存储每个准则下的综合评价结果
    criteria_evaluation = {}

    # 首先计算每个准则下的综合评价
    for criteria, details in sub_criteria.items():
        sub_weights = details['权重']
        sub_evaluations_array = np.array(list(details['指标'].values()))
        # 计算每个准则的模糊综合评价
        fuzzy_eval = fuzzy_logic_multiply_and_add(sub_weights, sub_evaluations_array)
        # 存储综合评价结果
        fuzzy_eval_normalized = np.round(normalize_vector(fuzzy_eval), 2)
        criteria_evaluation[criteria] = fuzzy_eval_normalized
        print(f"[{criteria}]准则的评价结果: {fuzzy_eval_normalized}")

    # 计算总的综合评价
    final_evaluations = []
    for criteria, weight in criteria_weights.items():
        weighted_eval = criteria_evaluation[criteria] * weight
        final_evaluations.append(weighted_eval)
    # 将各准则的评价结果逐项进行逻辑加运算
    final_evaluation = np.zeros_like(final_evaluations[0])
    for final_eval in final_evaluations:
        final_evaluation = np.fmax(final_evaluation, final_eval)

    # 归一化最终结果
    final_normalized = normalize_vector(final_evaluation)

    return np.round(final_normalized, 2)


# 设置准则层权重
criteria_weights = {'图像': 0.5, '声音': 0.3, '价格': 0.2}

# 设置指标层权重和评价矩阵
sub_criteria = {
    '图像': {
        '权重': np.array([0.3, 0.7]),
        '指标': {
            '色泽': [0.3, 0.2, 0.4, 0.1],
            '设计': [0.4, 0.5, 0.1, 0]
        }
    },
    '声音': {
        '权重': np.array([0.4, 0.6]),
        '指标': {
            '音质': [0.1, 0.2, 0.2, 0.5],
            '音量': [0.3, 0.1, 0.1, 0.5]
        }
    },
    '价格': {
        '权重': np.array([1.0]),
        '指标': {
            '售价': [0.1, 0.1, 0.3, 0.5]
        }
    }
}

# 进行多级模糊综合评价
final_result = multi_level_fuzzy_evaluation(criteria_weights, sub_criteria)
print(f"最终综合评价结果: {final_result}")
