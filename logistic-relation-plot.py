import pandas as pd
from theme.unodc import *
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import ScalarFormatter

# Load the data to see its structure
data_path = './data/fake_data.csv'
data = pd.read_csv(data_path)

# Create a new figure with a specific size
plt.figure(figsize=(12, 7))

# Create the first axis for the GDP bar plot
ax1 = plt.gca()  # Get current axis
ax2 = ax1.twinx()  # Create another axis that shares the same x-axis

# Plot GDP as a bar plot on ax1 with color depending on Adoption value
colors = data['Adoption'].map({0: COLORS_RED[3], 1: COLORS_GREEN[3]})
ax1.bar(data.index, data['GDP'], color=colors, alpha=0.6, width=0.4)
ax1.set_ylabel('GDP', color='black')  # Set label for the y-axis of ax1
ax1.tick_params(axis='y', labelcolor='black')  # Set tick parameters for y-axis of ax1
ax1.set_ylim(0, 0.7e13)  # Set the limit for the GDP scale

# Plot Volume as a line plot on ax2
ax2.plot(data.index, data['Volume'], label='Internet Search Volume', color=COLORS_BLUE[2], marker='*', linewidth=2,
         markersize=8)
ax2.set_ylabel('Search Volume', color='black')  # Set label for the y-axis of ax2
ax2.tick_params(axis='y', labelcolor='black')  # Set tick parameters for y-axis of ax2
ax2.set_ylim(-10000, 8000)  # Set the limit for the Volume scale
ax2.set_yticks([tick for tick in ax2.get_yticks() if tick >= 0])

# Adding titles and labels
ax1.set_xlabel('Countries')
ax1.set_xticks([])
ax1.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))

# Adding legend for both plots
legend_elements = [
    Patch(facecolor=COLORS_GREEN[3], alpha=0.6, label='Adopted Countries'),
    Patch(facecolor=COLORS_RED[3], alpha=0.6, label='Not Adopted Countries'),
    ax2.lines[0]
]

# ax1.legend(loc='upper left')
ax2.legend(handles=legend_elements, loc='upper right')

# Show the plot
plt.savefig(r'./output/Visible GDP vs Volume.svg', bbox_inches='tight')
plt.show()
