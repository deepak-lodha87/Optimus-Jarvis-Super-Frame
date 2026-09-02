import time
import random

class MarineVision:
    def __init__(self):
        self.visibility_range = 15 # Meters
        self.detected_entities = []

    def scan_environment(self):
        print(f"\033[1;36m[VISION]\033[0m Activating Underwater Neural Scanner...")
        time.sleep(2)
        
        # Simulating detection
        targets = ["Great White Shark", "Unknown Metallic Submersible", "Coral Reef", "Deep-Sea Mine"]
        found = random.choice(targets)
        
        print(f" \033[1;32m[DETECTED]\033[0m Object: {found}")
        
        if "Metallic" in found or "Mine" in found:
            print("\033[1;31m[WARNING]\033[0m Artificial Object Detected. Analyzing Signature...")
            print(" \033[1;33m[STATUS]\033[0m Potential Threat Level: High")
        else:
            print(f" \033[1;34m[LOG]\033[0m Natural Bio-Entity confirmed. No threat.")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, my vision has pierced the \nocean's veil. I can distinguish between \nnature and machine in the darkest depths. \nNothing remains hidden below the surface.\033[0m")

if __name__ == "__main__":
    vision = MarineVision()
    vision.scan_environment()
