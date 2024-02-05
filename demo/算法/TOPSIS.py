import numpy as np


def topsis_with_interval_optimization(decision_matrix_dict, weights):
    def interval_optimum_score(value, optimal_range, tolerance=None):
        A, B = optimal_range
        lower_tolerance, upper_tolerance = tolerance if tolerance else (float('-inf'), float('inf'))
        if value < lower_tolerance or value > upper_tolerance:
            return 0
        if A <= value <= B:
            return 1
        if value < A:
            return 1 - (A - value) / (A - lower_tolerance)
        else:  # value > B
            return 1 - (value - B) / (upper_tolerance - B)

    # 提取值并进行标准化
    norm_matrix = []
    for criteria, data in decision_matrix_dict.items():
        if data["preference"] == "range":
            # 处理区间最优型指标
            optimal_range = data["optimal_range"]
            tolerance = data.get("tolerance")
            scores = [interval_optimum_score(value, optimal_range, tolerance) for value in data["values"]]
            norm_matrix.append(scores)
        else:
            # 处理常规指标
            values = np.array(data["values"])
            norm_values = values / np.sqrt((values ** 2).sum())
            norm_matrix.append(norm_values)

    norm_matrix = np.array(norm_matrix)

    # 应用权重
    weighted_norm_matrix = norm_matrix * weights.reshape(-1, 1)

    # 计算理想解和负理想解
    ideal_solution = np.array([weighted_norm_matrix[i].max() if decision_matrix_dict[criteria]["preference"] == "max"
                               else weighted_norm_matrix[i].min()
                               for i, criteria in enumerate(decision_matrix_dict)])

    nadir_solution = np.array([weighted_norm_matrix[i].min() if decision_matrix_dict[criteria]["preference"] == "max"
                               else weighted_norm_matrix[i].max()
                               for i, criteria in enumerate(decision_matrix_dict)])

    # 计算距离
    distance_to_ideal = np.sqrt(((weighted_norm_matrix.T - ideal_solution) ** 2).sum(axis=1))
    distance_to_nadir = np.sqrt(((weighted_norm_matrix.T - nadir_solution) ** 2).sum(axis=1))

    # 计算相对接近度
    relative_closeness = distance_to_nadir / (distance_to_ideal + distance_to_nadir)

    return relative_closeness


# 示例使用
transposed_decision_matrix_dict_with_range = {
    "价格": {"values": [3000, 4000, 3500], "preference": "min"},
    "性能": {"values": [8, 9, 7], "preference": "max"},
    "信号强度": {"values": [70, 60, 80], "preference": "range", "optimal_range": (65, 75), "tolerance": (50, 90)}
}

# 权重向量
weights_with_range = np.array([0.3, 0.5, 0.2])

# 计算相对接近度
relative_closeness_with_range = topsis_with_interval_optimization(transposed_decision_matrix_dict_with_range,
                                                                  weights_with_range)
print(relative_closeness_with_range, relative_closeness_with_range.argsort()[::-1] + 1)  # 相对接近度及排序（品牌编号）
