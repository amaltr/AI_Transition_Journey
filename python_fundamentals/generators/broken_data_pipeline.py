# Raw stream
raw_data = range(10)

# Stage 1: Filter evens
evens = (x for x in raw_data if x % 2 == 0)

# Stage 2: Square them
squared = (x**2 for x in evens)

# BUG: The developer thinks they can 're-use' evens here
# Stage 3: Print evens, then print squared
for item in evens:
    print(f"Original Even: {item}")

for item in squared:
    print(f"Squared Even: {item}")