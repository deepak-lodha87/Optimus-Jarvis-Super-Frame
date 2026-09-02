import time
import random

class SharedPathfinder:
    def __init__(self):
        self.drone_view = "CLEAR"
        self.rover_pos = 0

    def start_mission(self):
        print("\033[1;36m[MISSION]\033[0m Starting Collaborative Navigation...")
        time.sleep(1.2)

        for step in range(1, 6):
            print(f"\n\033[1;37m[STEP {step}]\033[0m")
            # Drone scans ahead
            obstacle = random.choice([True, False, False])
            
            if obstacle:
                print(" \033[1;33m[AIR-SCOUT]\033[0m Danger detected! Re-routing Ground Unit.")
                print(" \033[1;32m[GROUND-UNIT]\033[0m Path updated. Moving safely around obstacle.")
            else:
                print(" \033[1;32m[AIR-SCOUT]\033[0m Path clear for 10 meters.")
                print(f" \033[1;34m[GROUND-UNIT]\033[0m Advancing to position: {step * 10}m")
            
            time.sleep(0.8)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, the collaboration is \nflawless. The Sky-Lord has become the eyes, \nand the Rover has become the feet. They \nmove as one mind, ensuring no obstacle \ncan stop our progress. We are carving our \nown path.\033[0m")

if __name__ == "__main__":
    path = SharedPathfinder()
    path.start_mission()
