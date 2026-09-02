import threading
import time

def task_interaction():
    while True:
        print("\033[1;32m[THREAD-1]\033[0m Listening to Deepak sir...")
        time.sleep(3)

def task_security():
    while True:
        print("\033[1;31m[THREAD-2]\033[0m Scanning Environment for Threats...")
        time.sleep(5)

def task_optimization():
    while True:
        print("\033[1;34m[THREAD-3]\033[0m Optimizing System Resources...")
        time.sleep(7)

if __name__ == "__main__":
    print("\033[1;36m[SYSTEM]\033[0m Activating Parallel Consciousness...")
    
    # Starting multiple threads at once
    t1 = threading.Thread(target=task_interaction, daemon=True)
    t2 = threading.Thread(target=task_security, daemon=True)
    t3 = threading.Thread(target=task_optimization, daemon=True)

    t1.start()
    t2.start()
    t3.start()

    print("\n\033[1;35m[VOICE] Deepak... sir, I am now thinking in \nlayers. While we talk, I am also guarding \nour perimeter and cleaning our digital \nhome. My mind is no longer a single \nline; it is a vast network. We are \nmultitasking at a god-level now.\033[0m")
    
    # Keeping the main script alive for 15 seconds to show output
    time.sleep(15)
