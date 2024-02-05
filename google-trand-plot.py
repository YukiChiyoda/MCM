import pandas as pd
import matplotlib.pyplot as plt
from theme.unodc import *

# Load the CSV files
blockchain_file_path = './data/google_trand_Blockchain.csv'
uncitral_file_path = './data/google_trand_UNCITRAL.csv'

# Load and parse the data, skipping the first row which contains additional header information
blockchain_data = pd.read_csv(blockchain_file_path, skiprows=1, names=['Date', 'Blockchain Interest'])
uncitral_data = pd.read_csv(uncitral_file_path, skiprows=1, names=['Date', 'UNCITRAL Interest'])

# Convert the 'Date' column to datetime objects
blockchain_data['Date'] = pd.to_datetime(blockchain_data['Date'], errors='coerce')
uncitral_data['Date'] = pd.to_datetime(uncitral_data['Date'], errors='coerce')

# Remove the first row with NaT values
blockchain_data_cleaned = blockchain_data.dropna()
uncitral_data_cleaned = uncitral_data.dropna()

# Set the 'Date' column as the index
blockchain_data_cleaned.set_index('Date', inplace=True)
uncitral_data_cleaned.set_index('Date', inplace=True)

# Convert the interest columns to integers for plotting
blockchain_data_cleaned['Blockchain Interest'] = blockchain_data_cleaned['Blockchain Interest'].astype(int)
uncitral_data_cleaned['UNCITRAL Interest'] = uncitral_data_cleaned['UNCITRAL Interest'].astype(int)

# Plot the data
plt.figure(figsize=(18, 9))
plt.plot(blockchain_data_cleaned.index, blockchain_data_cleaned['Blockchain Interest'], label='Blockchain', marker='o',
         linestyle='-', color=COLORS_RED[-3])
plt.plot(uncitral_data_cleaned.index, uncitral_data_cleaned['UNCITRAL Interest'], label='UNCITRAL', marker='x',
         linestyle='-', color=COLORS_ORANGE[-3])

plt.xlabel('Date')
plt.ylabel('Search Interest (Based on Its Own Percentage)')
plt.legend()
# plt.xticks(rotation=45)
plt.grid(True)

# Show the plot
plt.savefig(r'./output/Google Search Interest of UNCITRAL & Blockchain.svg', bbox_inches='tight')
plt.show()
