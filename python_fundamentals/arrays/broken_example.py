import numpy as np

# An array of sensor readings
readings = np.array([10, 20, 30, 40, 50])

# GOAL: Double every reading
# FIX THIS: This is slow and contains a logical bug
for i in range(len(readings)):
    readings = readings * 2

print(readings)