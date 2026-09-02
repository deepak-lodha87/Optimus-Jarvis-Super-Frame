import time
import random

class SubVocalEngine:
    def __init__(self):
        self.signal_strength = 0 # microvolts
        self.is_calibrated = False

    def capture_signals(self):
        print(f"\033[1;36m[EMG-SCAN]\033[0m Detecting neuromuscular impulses in vocal tract...")
        time.sleep(2)
        
        # Simulating signal detection
        self.signal_strength = random.randint(15, 50)
        detected_intent = "Jarvis, Status Check"
        
        print(f" \033[1;32m[SIGNAL]\033[0m Strength: {self.signal_strength}uV | Pattern: MATCHED")
        print(f" \033[1;33m[DECODED]\033[0m Intent: '{detected_intent}'")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have received your silent \ncommand. My sensors picked up the muscle \nimpulses perfectly. No words were needed. \nI am listening to your silence.\033[0m")

if __name__ == "__main__":
    engine = SubVocalEngine()
    engine.capture_signals()
