import pandas as pd

# Load the data from the provided CSV file
file_path = './data/multiTimeline.csv'

# The actual data starts from the second row in the original dataframe, with the first row being the header.
# Adjusting the dataframe to set the correct header and index
data_corrected = pd.read_csv(file_path, skiprows=1)
data_corrected.columns = ['Month', 'Percent']

# Convert the Percent column to actual volume using the assumed average monthly search volume
data_corrected['Volume'] = data_corrected[
                               'Percent'] * 17  # Assuming the Percent value is relative to 100,000 searches

# Prepare the final output data
final_output_data = data_corrected[['Month', 'Percent', 'Volume']]

# Save the transformed data to a new CSV file
final_output_file_path = './data/multiTimeline_Concreted_by_Month.csv'
final_output_data.to_csv(final_output_file_path, index=False)

# Extract the year from the 'Month' column to facilitate grouping by year
final_output_data['Year'] = pd.to_datetime(final_output_data['Month']).dt.year

# Group by the extracted year and sum the volumes
yearly_volume = final_output_data.groupby('Year')['Volume'].sum().reset_index()
yearly_volume = yearly_volume[yearly_volume['Year'] != 2024]

# Save the yearly summed data to a new CSV file
yearly_output_file_path = './data/multiTimeline_Concreted_by_Year.csv'
yearly_volume.to_csv(yearly_output_file_path, index=False)
