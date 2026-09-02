import os
import json
import time
from datetime import datetime

class JarvisMemory:
    def __init__(self):
        self.memory_file = "jarvis_memory.json"
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump({"reminders": []}, f)

    def add_reminder(self, task, rem_time):
        with open(self.memory_file, 'r') as f:
            data = json.load(f)
        
        data["reminders"].append({"task": task, "time": rem_time})
        
        with open(self.memory_file, 'w') as f:
            json.dump(data, f)
        
        msg = f"Task registered, Deepak sir. I will remind you about {task} at {rem_time}."
        print(f"\033[1;32m[MEMORY SAVED]:\033[0m {task}")
        os.system(f'termux-tts-speak "{msg}"')

    def check_reminders(self):
        now = datetime.now().strftime("%H:%M")
        with open(self.memory_file, 'r') as f:
            data = json.load(f)
        
        for item in data["reminders"]:
            if item["time"] == now:
                msg = f"Alert Deepak sir! It is {now}. Time for: {item['task']}"
                print(f"\033[1;31m[REMINDER]:\033[0m {item['task']}")
                os.system(f'termux-tts-speak "{msg}"')
                # टास्क पूरा होने के बाद हटाना (Optional)

if __name__ == "__main__":
    mem = JarvisMemory()
    print("\n\033[1;36m[MEMORY MODULE ACTIVE]\033[0m")
    
    choice = input("1. Add Reminder\n2. Check Status\nChoose: ")
    
    if choice == "1":
        task = input("What should I remember? ")
        t = input("At what time? (HH:MM format): ")
        mem.add_reminder(task, t)
    else:
        mem.check_reminders()
