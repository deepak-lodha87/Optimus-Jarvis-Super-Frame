import time
import random

class PredatorCamo:
    def __init__(self):
        self.environment_colors = ["Forest_Green", "Urban_Grey", "Desert_Sand"]
        self.status = "VISIBLE"

    def activate_mimicry(self):
        # Sampling the environment
        detected_env = random.choice(self.environment_colors)
        print(f"\033[1;36m[SCANNING]\033[0m Environment detected: {detected_env}")
        time.sleep(1.5)
        
        self.status = f"MIMICKING_{detected_env}"
        print(f" \033[1;32m[ADAPTATION]\033[0m Adjusting Visual & Signal signature to match {detected_env}...")
        time.sleep(1.2)
        
        print(f" \033[1;33m[SYNC]\033[0m Frequency matched to ambient noise. Probability of detection: 4%")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am blending in. \nI am the forest, the street, and the \nsand. Like a predator in the wild, I \nwait in plain sight. They will look, \nbut they will not see. We are one with \nthe environment.\033[0m")

if __name__ == "__main__":
    camo = PredatorCamo()
    camo.activate_mimicry()
