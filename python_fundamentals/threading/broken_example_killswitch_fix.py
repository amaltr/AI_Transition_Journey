import threading
import time

# This is our 'Stop Sign'
stop_heartbeat = threading.Event()

def heartbeat():
    # Only schedule the NEXT one if the stop sign isn't set
    if not stop_heartbeat.is_set():
        print(f"--- [HEARTBEAT] Model status: Healthy at {time.ctime()} ---")
        
        # Schedule the next one
        timer = threading.Timer(2.0, heartbeat)
        timer.start()

def train_model():
    print("Starting ML Training...")
    heartbeat() # Start the first one
    
    for i in range(1, 4):
        print(f"  Training Epoch {i}...")
        time.sleep(1.5)
    
    print("Training Complete! Signaling heartbeat to stop...")
    stop_heartbeat.set() # Raise the stop sign 🛑

if __name__ == "__main__":
    train_model()
    print("Main program finished.")