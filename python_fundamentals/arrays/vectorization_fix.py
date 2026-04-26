import numpy as np

# 1. Initialize the array (Contiguous block of memory)
readings = np.array([10, 20, 30, 40, 50])

# 2. Vectorized Operation: 
# This tells the CPU/GPU to apply "times 2" to the whole block 
# in one go, rather than stepping through indices.
doubled_readings = readings * 2 

# 3. Output the result
print(f"Original: {readings}")
print(f"Doubled:  {doubled_readings}")