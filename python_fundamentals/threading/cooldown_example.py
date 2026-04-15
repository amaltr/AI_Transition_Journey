import threading
import time

can_fetch = True

def unlock_api():
    global can_fetch
    print("\n[SYSTEM] Cool-down finished. You can fetch again.")
    can_fetch = True

def fetch_data():
    global can_fetch
    if can_fetch:
        print("Fetching data from API... 📡")
        can_fetch = False
        # Schedule the unlock 3 seconds from now
        threading.Timer(3.0, unlock_api).start()
    else:
        print("Error: Please wait for the cool-down!")

# Simulation
fetch_data() # Works
fetch_data() # Fails (Too soon)
time.sleep(3.1)
fetch_data() # Works again