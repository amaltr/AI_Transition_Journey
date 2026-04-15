import threading
import time

# Create an event object (the 'stop signal')
stop_event = threading.Event()

def long_running_task(event):
    print("Task started: Beginning 10-second loop...")
    for i in range(10):
        # 🛑 The check-in point:
        if event.is_set():
            print("Stop signal received! Breaking the loop.")
            break
            
        print(f"Step {i}...")
        time.sleep(1)
    print("Task finished.")

# Start the task
t = threading.Thread(target=long_running_task, args=(stop_event,))
t.start()

# Stop it after 2 seconds
time.sleep(2)
stop_event.set() # Raise the flag