import numpy as np
import pandas as pd

# 构造数据
data = {
    "理想销售": [100, 100, 100, 100, 100],
    "门店A销售": [90, 85, 95, 80, 90],
    "门店B销售": [60, 65, 70, 60, 75],
    "门店C销售": [70, 75, 80, 70, 85]
}
df = pd.DataFrame(data)

# 数据标准化
normalized_df = df / df.max()

# 计算绝对差值
abs_diff = normalized_df.drop('理想销售', axis=1).apply(lambda x: abs(x - normalized_df['理想销售']))

# 确定最大差和最小差
max_diff = abs_diff.max().max()
min_diff = abs_diff.min().min()

# 计算关联系数
rho = 0.5  # 分辨系数，一般取值0.5
grc = abs_diff.apply(lambda x: (min_diff + rho * max_diff) / (x + rho * max_diff))

# 计算关联度
relation_degree = grc.mean()

# 结果分析
print("关联度：\n", relation_degree)
