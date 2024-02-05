import pandas as pd
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA

# 加载数据
df = pd.read_csv('./data/Chicago_Crimes_Counts.csv', parse_dates=['Month'], index_col='Month')

# 计算预测的时间步长
reused_date = 1
last_date = df.index[-reused_date]
target_date = datetime(2024, 1, 1)
delta = target_date.year * 12 + target_date.month - (last_date.year * 12 + last_date.month)

# 构建并拟合模型
model = ARIMA(df['Crime_Count'][:-reused_date], order=(1, 1, 1))
model_fit = model.fit()

# 模型摘要
print(model_fit.summary())

# 进行预测
forecast = model_fit.forecast(steps=delta)

# 生成预测日期范围
forecast_dates = pd.date_range(start=last_date + timedelta(days=1), periods=delta, freq='MS')

# 将预测转换为DataFrame
forecast_df = df.copy()
# forecast_df = pd.DataFrame(forecast.values, index=forecast_dates, columns=['Crime_Count_Predictions'])

print(forecast)
print(forecast_df)

# 将forecast Series转换为DataFrame
forecast_df_new = forecast.reset_index()
forecast_df_new.columns = ['Month', 'Crime_Count_Predictions']  # 重命名列名

# 将Month列转换为datetime类型，确保两个DataFrame在合并时能够对齐
forecast_df_new['Month'] = pd.to_datetime(forecast_df_new['Month'])

# 重置forecast_df的索引，使Month成为一个列
forecast_df_reset = forecast_df.reset_index()
forecast_df_reset['Month'] = pd.to_datetime(forecast_df_reset['Month'])

# 合并forecast_df和forecast_df_new
merged_df = pd.merge(forecast_df_reset, forecast_df_new, on='Month', how='outer')

# 如果你想要保持Month作为索引
merged_df.set_index('Month', inplace=True)

print(merged_df)

merged_df.to_csv(r'./data/Chicago_Crimes_Predictions-ARIMA.csv', encoding='utf-8')
