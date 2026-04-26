import torch

#Do not run this code
# Assume model, optimizer, loss_function, and data_loader are defined
model.train() # 1. Set to training mode (enables Dropout/BatchNorm)

for epoch in range(num_epochs):
    for batch_data, batch_target in data_loader: # 2. Process data in batches
        
        # 1. The Emptying (Crucial Step)
        optimizer.zero_grad()
        
        # 2. The Forward Pass
        predictions = model(batch_data)
        loss = loss_function(predictions, batch_target)
        
        # 3. The Backward Pass
        loss.backward()
        
        # 4. The Weight Update
        optimizer.step()
        
    print(f"Epoch {epoch} complete.")