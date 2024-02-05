import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the logistic function
def logistic_function(x1, x2):
    return 1 / (1 + np.exp(-(0.4968 + 0.4039 * x1 + 0.6473 * x2)))


# Generate a meshgrid for x1 and x2
x1_range = np.linspace(-10, 10, 100)
x2_range = np.linspace(-10, 10, 100)
x1, x2 = np.meshgrid(x1_range, x2_range)

# Calculate P for each (x1, x2) pair
P = logistic_function(x1, x2)

# Plotting
fig = plt.figure(dpi=600, figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(x1, x2, P, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel('X1 Axis')
ax.set_ylabel('X2 Axis')
ax.set_zlabel('Probability (P)')

# Add a color bar which maps values to colors
color_bar = fig.colorbar(surface, shrink=0.5, aspect=5)
color_bar.set_label('Probability (P)')

# Show the plot
plt.savefig('./output/Probability Map.svg', transparent=True)
plt.show()
