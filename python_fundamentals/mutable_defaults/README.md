# Mutable Default Arguments in Python

## Overview
This folder explores the classic Python "gotcha" of mutable default arguments. It demonstrates why using mutable objects (like `list`, `dict`, or `set`) as default values in function definitions can lead to unexpected and hard-to-debug behaviors, especially in ML pipelines where state might accidentally leak between runs.

## The Gotcha
In Python, default arguments are evaluated **only once** when the function definition is executed (interpreted), *not* every time the function is called. 

If you use a mutable object like `[]` as a default:
```python
def log_experiment(epoch_loss, experiment_history=[]):
    experiment_history.append(epoch_loss)
    return experiment_history
```
That specific list `[]` acts like a static variable attached to the function. Every invocation of `log_experiment` without the `experiment_history` argument will share and modify that exact same list in memory.

## The Fix
The standard industry practice is to use the immutable `None` as the default value, and then initialize the mutable object inside the function body. The function body is executed every time the function is called, ensuring a fresh object is created:

```python
def log_experiment(epoch_loss, experiment_history=None):
    if experiment_history is None:
        experiment_history = []
    
    experiment_history.append(epoch_loss)
    return experiment_history
```

## Folder Contents
- `default_mech.py`: Demonstrates the underlying mechanism by inspecting `test_func.__defaults__` and showing how the default tuple mutates.
- `broken_ml_logger.py`: Simulates a broken ML logging function where experiment histories incorrectly bleed into one another.
- `broken_nl_logger_fix.py`: Contains the corrected implementation using the `None` pattern.
