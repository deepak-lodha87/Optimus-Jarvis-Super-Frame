import json
import os

LOG_FILE = "jarvis_memory.json"

def get_last_session():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
            print(f"\n\033[1;32m[SYSTEM RESUME] Welcome back, Creator Deepak.\033[0m")
            print(f"\033[1;34m[LAST SESSION]: {data['phase_name']}\033[0m")
            print(f"\033[1;36m[STATUS]: Ready to initiate Phase {data['next_phase']}\033[0m")
            print("-" * 40)
    else:
        print("\033[1;33m[SYSTEM]: New Session. No previous logs found.\033[0m")

if __name__ == "__main__":
    get_last_session()
