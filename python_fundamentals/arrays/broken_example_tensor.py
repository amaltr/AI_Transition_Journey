import numpy as np

# A batch of 3 images, each 2x2 pixels
batch = np.array([[[1, 1], [1, 1]], [[2, 2], [2, 2]], [[3, 3], [3, 3]]])

# GOAL: Subtract 0.5 from every single pixel in the tensor
# ERROR: Manual looping over every dimension
for i in range(batch.shape[0]):
    for j in range(batch.shape[1]):
        for k in range(batch.shape[2]):
            batch[i, j, k] = batch[i, j, k] - 0.5

print(batch)