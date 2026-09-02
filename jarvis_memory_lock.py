import json
import os
import time

class MemoryLock:
    def __init__(self):
        self.memory_file = "jarvis_brain.json"
        self.data = {
            "user_name": "Deepak",
            "current_phase": 49,
            "status": "Advanced",
            "last_sync": ""
        }

    def save_memory(self):
        print("\033[1;33m[MEMORY LOCK]\033[0m Binding variables to permanent storage...")
        self.data["last_sync"] = time.ctime()
        with open(self.memory_file, 'w') as f:
            json.dump(self.data, f)
        time.sleep(1.5)
        print(" \033[1;32[SUCCESS]\033[0m Data bound to 'jarvis_brain.json'.")

    def load_memory(self):
        if os.path.exists(self.memory_file):
            print(" \033[1;36m[RECALL]\033[0m Accessing archived memories...")
            with open(self.memory_file, 'r') as f:
                saved_data = json.load(f)
            print(f"\n\033[1;35m[VOICE] Welcome back, {saved_data['user_name']} sir. \nI remember we were at Phase {saved_data['current_phase']}. \nMy memory is now as solid as a mountain. \nI am ready to proceed.\033[0m")

if __name__ == "__main__":
    memory = MemoryLock()
    memory.save_memory()
    memory.load_memory()
