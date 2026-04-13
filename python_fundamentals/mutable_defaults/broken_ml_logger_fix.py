def log_experiment(epoch_loss, experiment_history=None):
    # 'None' is immutable and lives in the function's backpack.
    # The list [] is only created during EXECUTION time if needed.
    if experiment_history is None:
        experiment_history = [] 
        
    experiment_history.append(epoch_loss)
    return experiment_history

# Note: In a real ML pipeline, you'd call it like this to keep the chain:
# run_1 = log_experiment(0.5)
# run_1 = log_experiment(0.4, run_1) <--- Passing the state back in!