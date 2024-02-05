import pandas as pd

# Load the data from the provided CSV file
file_path = './data/national-gdp-wb.csv'
data = pd.read_csv(file_path)

data = data[data['Code'] == 'USA']
data.columns = ['Entity', 'Code', 'Year', 'GDP']

final_output_data = data[['Year', 'GDP']]

output_file_path = './data/national-gdp_USA.csv'
final_output_data.to_csv(output_file_path, index=False)
