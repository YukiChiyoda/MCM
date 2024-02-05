from matplotlib.colors import LinearSegmentedColormap

COLORS = ['#33222C', '#B15E8F', '#DD6D88', '#FC8679', '#FFA86A', '#FFCF63', '#F9F871']
CMAP = LinearSegmentedColormap.from_list('My Cmap', COLORS)
CMAP_REVERSED = LinearSegmentedColormap.from_list('My Cmap', COLORS[::-1])
