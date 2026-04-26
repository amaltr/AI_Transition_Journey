import numpy as np

# Simulate a flattened input vector (e.g., from a 28x28x3 image)
# Total elements: 28 * 28 * 3 = 2352
flat_input = np.random.rand(2352)

# Reshape to a column vector (2352, 1)
# -1 automatically calculates the first dimension (2352) based on total elements
# 1 fixes the second dimension as a column
column_vector = flat_input.reshape(-1, 1)

# Verify the result
print(f"Original 1D array shape: {flat_input.shape}")
print(f"New 2D column vector shape: {column_vector.shape}")