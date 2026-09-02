import time
import os
from datetime import datetime

def log_activity(task):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("jarvis_log.txt", "a") as file:
        file.write(f"[{now}] Action: {task}\n")

def phase_71_logger():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 71 ---")
    print("--- [INITIALIZING ACTIVITY LOGGER] ---")
    time.sleep(1)

    print("📝 Jarvis is now recording your session.")
    action = input("💬 What did you do today? (e.g., Coding, Testing): ")
    
    log_activity(action)
    
    print(f"✅ Activity '{action}' has been saved to 'jarvis_log.txt'.")
    print("\n[LOG HISTORY]:")
    os.system("tail -n 5 jarvis_log.txt")

if __name__ == "__main__":
    phase_71_logger()
