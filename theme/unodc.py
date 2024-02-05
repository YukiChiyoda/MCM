from matplotlib.colors import LinearSegmentedColormap

GREY = '#c5aca2'
COLORS_RED = ['#e4abad', '#D94B61', '#d9425c', '#c6153c', '#9e1625']
COLORS_GREEN = ['#b4d9b9', '#52a36d', '#33855b', '#006b37']
COLORS_BLUE = ['#d0e7ee', '#81c6d3', '#00a8bb']
COLORS_ORANGE = ['#fde2ce', '#f0bda1', '#d8875d', '#db6034', '#c54304']
CMAP = LinearSegmentedColormap.from_list('My Cmap', ['#FFEFCE', '#f47a20', '#9c4f3b', '#893523'])
CMAP_REVERSED = LinearSegmentedColormap.from_list('My Cmap', ['#893523', '#9c4f3b', '#f47a20', '#FFEFCE'])

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    color = COLORS_ORANGE
    positions = np.arange(len(color))
    height = 0.5

    plt.figure(figsize=(10, 2))
    plt.barh(positions, [height] * len(color), color=color, height=height)

    plt.xticks([])
    plt.yticks([])
    plt.box(False)
    plt.show()
