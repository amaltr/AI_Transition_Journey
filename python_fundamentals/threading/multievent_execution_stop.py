import threading
import time

def process_pipeline(event):
    # Step A ⚙️
    print("Running Step A...")
    if event.is_set():
        print("Stopping after Step A.")
        return
    time.sleep(1)

    # Step B ⚙️
    print("Running Step B...")
    if event.is_set():
        print("Stopping after Step B.")
        return
    time.sleep(1)

    # Step C ⚙️
    print("Running Step C...")
    if event.is_set():
        print("Stopping after Step C.")
        return
    time.sleep(1)

    print("Pipeline complete.")

# 1. Initialize the stop signal
stop_event = threading.Event()

# 2. Start the timer/thread
t = threading.Timer(0, process_pipeline, args=[stop_event])
t.start()

# 3. Simulate user action: stop it during Step B
time.sleep(1.5) 
print("!!! User requested stop !!!")
stop_event.set()