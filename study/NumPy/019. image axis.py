import numpy as np

C, H, W = 3, 100, 200

images1 = np.random.randint(0, 256, size=(C, H, W))
gray_image1 = np.mean(images1, axis=(0))

images2 = np.random.randint(0, 256, size=(H, W, C))
gray_image2 = np.mean(images2, axis=(-1))