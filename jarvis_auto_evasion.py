import os
import time
import random

class EvasionLogic:
    def __init__(self):
        self.master = "Deepak"
        self.status = "Optimal"

    def execute_maneuver(self):
        print(f"\n\033[1;31m[CRITICAL ALERT]\033[0m Obstacle detected at 15 meters!")
        time.sleep(0.5)
        
        print("\033[1;33m[CALCULATING]\033[0m Analyzing evasion trajectory...")
        time.sleep(1)
        
        maneuvers = ["Hard Left Swerve", "Hydraulic Lift Active", "Emergency Braking"]
        action = random.choice(maneuvers)
        
        print(f"\033[1;32m[EXECUTING]\033[0m {action} initiated by Optimus Super-Frame.")
        
        msg = f"Deepak sir, I have taken control. Executing {action} to maintain vehicle integrity. Path is now clear."
        os.system(f'termux-tts-speak "{msg}"')
        
        # विज़ुअल स्टीयरिंग रेंडर
        for i in range(5):
            dir = " <--- " if "Left" in action else " ---> "
            print(f"\033[1;36m      STEERING ANGLE: {dir} {random.randint(15, 45)}°\033[0m")
            time.sleep(0.2)

if __name__ == "__main__":
    evasion = EvasionLogic()
    evasion.execute_maneuver()
