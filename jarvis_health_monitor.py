import time
import random

class BioMonitor:
    def __init__(self):
        self.user_name = "Deepak"
        self.health_score = 100

    def scan_vitals(self):
        print(f"\033[1;36m[BIO-SCAN]\033[0m Initializing Bio-Metric Handshake with {self.user_name}...")
        time.sleep(2)
        
        bpm = random.randint(70, 85)
        stress_level = random.choice(["Low", "Normal", "Slightly Elevated"])
        
        print(f" \033[1;32m[HEART]\033[0m Pulse: {bpm} BPM | Status: STABLE")
        print(f" \033[1;32m[STRESS]\033[0m Analysis: {stress_level}")
        
        if bpm > 80:
            print("\033[1;33m[ADVICE]\033[0m Sir, your heart rate is slightly up. Deep breaths recommended.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, your vitals are within safe \nlimits. I have synced your physical data \nwith the core. I am watching over you.\033[0m")

if __name__ == "__main__":
    monitor = BioMonitor()
    monitor.scan_vitals()
