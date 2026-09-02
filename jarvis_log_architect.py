import os
import datetime

class LogArchitect:
    def __init__(self):
        self.master = "Deepak"
        self.log_file = "jarvis_system.log"

    def write_log(self, event):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] EVENT: {event}\n"
        
        with open(self.log_file, "a") as f:
            f.write(log_entry)
        
        print(f"\033[1;32m[LOGGED]:\033[0m {event}")

    def initialize_archiving(self):
        print(f"\n\033[1;35m[LOG ARCHITECT ACTIVE]\033[0m Securing system history...")
        self.write_log("Optimus Jarvis Super-Frame expanded to Phase 142.")
        os.system('termux-tts-speak "Deepak sir, system logging is now active. Every action is being archived."')

if __name__ == "__main__":
    arch = LogArchitect()
    arch.initialize_archiving()
