import threading
import time

def heartbeat():
    print(f"--- [HEARTBEAT] Model status: Healthy at {time.ctime()} ---")
    # Hint: The worker finishes here and leaves the office forever.
    # How do we tell them to come back in 2 seconds?

def train_model():
    print("Starting 'Heavy' ML Training...")
    # We want a heartbeat every 2 seconds while this "trains"
    timer = threading.Timer(2.0, heartbeat)
    timer.start()
    
    # Simulating a long training process
    for i in range(1, 6):
        print(f"  Training Epoch {i}...")
        time.sleep(1.5)
    print("Training Complete!")

if __name__ == "__main__":
    train_model()