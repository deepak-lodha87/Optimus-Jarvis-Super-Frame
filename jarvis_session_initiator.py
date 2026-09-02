import os
import time

class SessionInitiator:
    def __init__(self):
        self.master = "Deepak"
        self.last_phase = "Phase 123"

    def welcome_master(self):
        # वर्तमान समय के अनुसार अभिवादन
        hour = int(time.strftime("%H"))
        greeting = "Good Evening" if hour >= 18 else "Good Day"
        
        status_msg = f"{greeting} Deepak sir. Optimus Jarvis Super-Frame is now online in Ratlam."
        log_msg = f"Last session ended at {self.last_phase}. All systems are stable."
        
        print(f"\n\033[1;32m[SESSION STARTED]\033[0m {status_msg}")
        print(f"\033[1;36m[STATUS]:\033[0m {log_msg}")
        
        # आवाज़ के माध्यम से स्वागत
        os.system(f'termux-tts-speak "{status_msg}. {log_msg}"')

if __name__ == "__main__":
    session = SessionInitiator()
    session.welcome_master()
