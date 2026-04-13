def log_experiment(epoch_loss, experiment_history=[]):
    """
    Records the loss for an epoch. 
    Should return only the history for the CURRENT experiment.
    """
    experiment_history.append(epoch_loss)
    return experiment_history

# --- TEST CASE ---
run_v1 = log_experiment(0.5)
run_v1 = log_experiment(0.4) 

run_v2 = log_experiment(0.9) # This should be [0.9]

print(f"Run 2 History: {run_v2}") 
# CURRENT BUG: Prints [0.5, 0.4, 0.9]
# DESIRED GOAL: Prints [0.9]