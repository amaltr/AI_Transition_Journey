# The Factory: A "Blueprint" that can generate a fresh stream anytime.
def get_evens():
    raw_data = range(10)
    return (x for x in raw_data if x % 2 == 0)

# Now, we use the factory to get fresh streams whenever we need them
# 1. Get a stream for printing
for item in get_evens():
    print(f"Original Even: {item}")

# 2. Get a DIFFERENT stream for squaring
# The 'squared' generator now has its OWN independent 'get_evens' stream
squared = (x**2 for x in get_evens())

for item in squared:
    print(f"Squared Even: {item}")