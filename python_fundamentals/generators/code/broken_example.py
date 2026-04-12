# The dataset is a generator (lazy)
data_gen = (x for x in range(5))

# 1. Calculate the sum
total = sum(data_gen)
print(f"Total: {total}")

# 2. Try to find the max
maximum = max(data_gen)
print(f"Max: {maximum}")