def get_processed_data_stream():
    """
    Acts as a Data Factory. Returns a fresh generator 
    to prevent 'generator exhaustion' issues in training loops.
    """
    # 1. Define the source
    raw_data = range(20)
    
    # 2. Define the pipeline steps (The 'Recipe')
    # Stage 1: Filter
    filtered = (x for x in raw_data if x % 3 == 0)
    
    # Stage 2: Transform
    transformed = (y * 10 for y in filtered)
    
    return transformed

# --- ML Training Loop Simulation ---
# In AI, we often run multiple 'epochs' (passes through the data)
for epoch in range(2):
    print(f"\n--- Starting Epoch {epoch + 1} ---")
    
    # We call the factory to get a fresh projector for each epoch
    pipeline = get_processed_data_stream()
    
    for item in pipeline:
        print(f"Processed Batch: {item}")