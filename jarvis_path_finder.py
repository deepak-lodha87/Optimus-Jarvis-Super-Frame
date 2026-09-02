import time
import random

class PathFinder:
    def __init__(self):
        self.terrains = {
            "Asphalt": {"Friction": "High", "Power_Req": "Low"},
            "Loose_Sand": {"Friction": "Low", "Power_Req": "Extreme"},
            "Rocky_Path": {"Friction": "Medium", "Power_Req": "High"}
        }

    def analyze_surface(self):
        current_surface = random.choice(list(self.terrains.keys()))
        data = self.terrains[current_surface]
        
        print(f"\033[1;36m[SCANNING]\033[0m Surface Detected: {current_surface}")
        time.sleep(1.2)
        
        print(f" \033[1;37m[DATA]\033[0m Friction: {data['Friction']} | Power Demand: {data['Power_Req']}")
        
        if current_surface == "Loose_Sand":
            print(" \033[1;33m[ADAPT]\033[0m Engaging 'Sand-Crawler' Mode. Increasing Torque by 40%.")
        elif current_surface == "Rocky_Path":
            print(" \033[1;33m[ADAPT]\033[0m Activating Active-Suspension. Reducing Speed for stability.")
        else:
            print(" \033[1;32m[STATUS]\033[0m Surface Optimal. Maintaining Cruise Velocity.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am reading the ground \nbeneath us. Whether it is a smooth road \nor a mountain trail, I will find the \nmost efficient path. The Earth is our \nplayground, and I know every inch of it.\033[0m")

if __name__ == "__main__":
    path = PathFinder()
    path.analyze_surface()
