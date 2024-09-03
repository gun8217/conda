import numpy as np

stream = np.array([3/7, 4/7])
stream_H = -np.sum(stream * np.log2(stream))
print(stream_H)

slope = np.array([5/7, 1/7, 1/7])
slope_H = -np.sum(slope * np.log2(slope))
print(slope_H)

# root node
elevation = np.array([1/7, 3/7, 2/7, 1/7])
elevation_H = -np.sum(elevation * np.log2(elevation))
print(elevation_H)
print()

# node_tree A
elevation_stream = np.array([2/3, 1/3])
elevation_stream_H = -np.sum(elevation_stream * np.log2(elevation_stream))
print(elevation_stream_H)
elevation_stream_IG = elevation_H - ((elevation_stream_H * 2/3) + (elevation_stream_H * 1/3))
print(elevation_stream_IG)
print()

# # node_tree A2
# elevation_slope2 = np.array([2/3, 1/3])
# elevation_slope2_H = -np.sum(elevation_stream * np.log2(elevation_stream))
# elevation_slope2_IG = elevation_H - ((elevation_slope2_H * 2/3) + (elevation_slope2_H * 1/3))
# print(elevation_slope2_IG)

# node_tree B
elevation_slope = np.array([1/2, 1/2])
elevation_slope_H = -np.sum(elevation_slope * np.log2(elevation_slope))
print(elevation_slope_H)
elevation_slope_IG = elevation_H - ((elevation_slope_H * 1/2) + (elevation_slope_H * 1/2))
print(elevation_slope_IG)

# # node_tree A - A
# elevation_stream_slope = np.array([1, 1])
# elevation_stream_slope_H = -np.sum(elevation_stream * np.log2(elevation_stream))
# elevation_stream_slope_IG = elevation_stream_H - ((elevation_stream_slope_H * 1/2) + (elevation_stream_slope_H * 1/2))
# print(elevation_stream_slope_IG)