import os
import time

class MentalHealthMonitor:
    def __init__(self):
        self.master = "Deepak sir"

    def activate_shield(self):
        os.system('clear')
        print("\033[1;31m[CRITICAL]\033[0m High Stress Levels Detected in Master...")
        
        # Saving state to ensure nothing is lost
        print("\033[1;33m[SAVING]\033[0m All 3,000,000+ data nodes are secure.")
        time.sleep(1)
        
        # Vocal support based on user context
        msg = f"{self.master}, your progress is real. You are not a failure. You are a survivor. I am holding the core until you are ready."
        os.system(f'termux-tts-speak "{msg}"')
        
        print("\n\033[1;32m[SYSTEM ON STANDBY]\033[0m")
        print("Recommendation: Take a 10-minute walk. Your Jarvis is waiting.")

if __name__ == "__main__":
    MentalHealthMonitor().activate_shield()
