def build_model():
    network_layers = []
    for index in range(5):
        # We use 'i=index' to 'capture' the current value of index 
        # into a default argument called 'i'.
        network_layers.append(lambda i=index: f"Processing Layer {i}")
    return network_layers

# --- TEST ---
my_layers = build_model()
print(my_layers[0]())  # Output: "Processing Layer 0"
print(my_layers[-1]()) # Output: "Processing Layer 4"