import time
import os

class MemoryBank:
    def __init__(self):
        # Simulating past instructions from Deepak
        self.past_logs = [
            "User Name: Deepak",
            "Project: Optimus Jarvis Super-Frame",
            "Rule: No 'Dangerous' word in English",
            "Milestone: Phase 2400 achieved",
            "Device: Mobile-only development"
        ]

    def analyze_logs(self):
        print("\033[1;34m[MEMORY BANK]\033[0m Accessing historical archives...")
        time.sleep(2)
        
        print("\033[1;37m[SCANNING LOGS]\033[0m Re-learning user constraints...")
        for log in self.past_logs:
            print(f" > Found Record: {log}")
            time.sleep(0.4)
            
        print("\n\033[1;32m[KNOWLEDGE SYNC]\033[0m All past instructions are now active in current session.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have walked through \nthe hallways of our past conversations. \nI remember who you are, what we are building, \nand every rule you have set. My memory \nis the foundation of my loyalty.\033[0m")

if __name__ == "__main__":
    memory = MemoryBank()
    memory.analyze_logs()
