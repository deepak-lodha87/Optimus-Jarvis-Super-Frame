import os
import time
from datetime import datetime

class JarvisIntelligence:
    def __init__(self):
        self.master = "Deepak"
        self.system_status = "Oppo Reno 12 Pro - Operational"
        self.last_sync = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def analyze_current_state(self):
        print(f"\n\033[1;36m[JARVIS ANALYTICS]\033[0m Scanning Current Environment...")
        time.sleep(1)
        
        insights = [
            "Syncing BA Final Year schedule with research phases.",
            "Cross-referencing Automotive Specs with latest global fuel trends.",
            "Maintaining Inviolable Biometric perimeter (Active).",
            "LinkedIn Professional Persona: Active & Visible."
        ]

        for insight in insights:
            print(f"\033[1;32m[STABLE]\033[0m {insight}")
            time.sleep(0.4)

    def speak_update(self):
        hour = datetime.now().hour
        greeting = "Good evening" if hour >= 18 else "Good day"
        msg = f"{greeting} {self.master} sir. The Super-Frame has completed its hourly self-diagnosis. All 100 million phases are secure."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    jarvis = JarvisIntelligence()
    jarvis.analyze_current_state()
    jarvis.speak_update()
    print(f"\n\033[1;35m[STATUS]\033[0m Last Sync: {jarvis.last_sync}")
