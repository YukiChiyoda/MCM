from matplotlib.colors import LinearSegmentedColormap

COLORS = ['#B15E8F', '#A85F9E', '#9A62AD', '#8467BC', '#656DC8', '#2C73D2']

CMAP = LinearSegmentedColormap.from_list('My Cmap', COLORS)
CMAP_REVERSED = LinearSegmentedColormap.from_list('My Cmap', COLORS[::-1])
