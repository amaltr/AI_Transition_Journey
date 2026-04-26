import numpy as np

# A batch of 3 images, each 2x2 pixels
batch = np.array([[[1, 1], [1, 1]], [[2, 2], [2, 2]], [[3, 3], [3, 3]]])

# GOAL: Subtract 0.5 from every single pixel in the tensor
# FIX: Broadcasting subtracts 0.5 from every element instantly
batch_centered = batch - 0.5

print(batch_centered)