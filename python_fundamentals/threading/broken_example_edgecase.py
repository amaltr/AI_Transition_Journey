import threading
import time

#NOTE: Don't run this code. It will run forever.
def heartbeat():
    print(f"--- [HEARTBEAT] Model status: Healthy at {time.ctime()} ---")
    
    # 1. Create a NEW timer instance
    # 2. Tell it to call THIS same function again in 2 seconds
    new_timer = threading.Timer(2.0, heartbeat)
    
    # 3. Start the new timer
    new_timer.start()