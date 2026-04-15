import threading
import time

def long_running_task():
    print("Task started: Beginning 10-second loop...")
    for i in range(10):
        # The loop doesn't know the timer was cancelled!
        print(f"Step {i}...")
        time.sleep(1)
    print("Task finished.")

# Timer starts after 1 second
t = threading.Timer(1.0, long_running_task)
t.start()

# We cancel it after 2 seconds
time.sleep(2)
t.cancel() 
print("Cancel called.")