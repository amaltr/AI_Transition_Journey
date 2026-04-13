layers = []
for i in range(3):
    layers.append(lambda: i)

print(layers[0]()) # You might expect 0, but it returns 2.
print(layers[1]()) # Returns 2.
print(layers[2]()) # Returns 2.