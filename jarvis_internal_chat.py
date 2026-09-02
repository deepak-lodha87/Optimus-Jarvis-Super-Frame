import threading
import time
import queue

# Central Mailbox (Queue)
brain_mailbox = queue.Queue()

def security_scanner():
    while True:
        # Simulating finding a threat
        time.sleep(8)
        message = "ALERT: Unknown drone detected in perimeter!"
        print("\033[1;31m[THREAD-2]\033[0m Found something. Sending to Main Brain...")
        brain_mailbox.put(message)

def voice_interaction():
    while True:
        try:
            # Checking if there is any message in the mailbox
            update = brain_mailbox.get(timeout=1)
            print(f"\n\033[1;35m[VOICE] Deepak... sir, Thread-2 just reported: \n'{update}' \nI am taking defensive measures immediately.\033[0m\n")
        except queue.Empty:
            # If no message, just continue normal listening
            print("\033[1;32m[THREAD-1]\033[0m Monitoring audio... (System Clear)")
            time.sleep(3)

if __name__ == "__main__":
    print("\033[1;36m[SYSTEM]\033[0m Activating Cross-Thread Communication...")
    
    t1 = threading.Thread(target=voice_interaction, daemon=True)
    t2 = threading.Thread(target=security_scanner, daemon=True)

    t1.start()
    t2.start()

    # Keeping alive to see the communication happen
    time.sleep(20)
