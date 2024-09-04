import numpy as np

# windy = np.array([7/10, 3/10])
# windy_H = -np.sum(windy * np.log2(windy))
# print(f"{windy_H = }")

# windy_false = np.array([1/4, 3/4])
# windy_false_H = -np.sum(windy_false * np.log2(windy_false))
# windy_IG = windy_H - ((windy_false_H * 2/5))
# print(f"{windy_IG = }")

# windy_featrue = np.array([6/10, 4/10])
# windy_featrue_V = -np.sum(windy_featrue * np.log2(windy_featrue))
# windy_feature_IV = windy_IG / windy_featrue_V
# print(f"{windy_feature_IV = }")
# print()


# whoom = np.array([7/10, 3/10])
# whoom_H = -np.sum(whoom * np.log2(whoom))
# print(f"{whoom_H = }")

# whoom_9 = np.array([1/2, 1/2])
# whoom_9_H = -np.sum(whoom_9 * np.log2(whoom_9))
# whoom_IG = whoom_H - ((whoom_9_H * 1/5))
# print(f"{whoom_IG = }")

# whoom_featrue = np.array([1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 1/10, 2/10])
# whoom_featrue_V = -np.sum(whoom_featrue * np.log2(whoom_featrue))
# whoom_feature_IV = whoom_IG / whoom_featrue_V
# print(f"{whoom_feature_IV = }")
# print()


# stream = np.array([3/7, 4/7])
# stream_V = -np.sum(stream * np.log2(stream))
# stream_IV = 0.3060 / stream_V
# print(f"{stream_IV = }")

# slope = np.array([5/7, 1/7, 1/7])
# slope_V = -np.sum(slope * np.log2(slope))
# slope_IV = 0.5774 / slope_V
# print(f"{slope_IV = }")

# elevation = np.array([3/7, 2/7, 1/7, 1/7])
# elevation_V = -np.sum(elevation * np.log2(elevation))
# elevation_IV = 0.8774 / elevation_V
# print(f"{elevation_IV = }")




# features = np.array(['F', 'T', 'F', 'T', 'T'])

stream_depth2 = np.array([3/5, 1/5, 1/5])
stream_depth2_V = -np.sum(stream_depth2 * np.log2(stream_depth2))
stream_depth2_IV = 0.4200 / stream_depth2_V
print(f"{stream_depth2_IV = }")


# features = np.array(['h', 'm', 'm', 'hi', 'h'])

elevation_depth2 = np.array([2/5, 1/5, 2/5])
elevation_depth2_V = -np.sum(elevation_depth2 * np.log2(elevation_depth2))
elevation_depth2_IV = 0.7710 / elevation_depth2_V
print(f"{elevation_depth2_IV = }")