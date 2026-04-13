def build_model():
    network_layers = []
    for index in range(5):
        # BUG: All these lambdas will return '4' when called later
        network_layers.append(lambda: f"Processing Layer {index}")
    return network_layers

# --- TEST ---
my_layers = build_model()
print(my_layers[0]()) # Should say "Processing Layer 0"