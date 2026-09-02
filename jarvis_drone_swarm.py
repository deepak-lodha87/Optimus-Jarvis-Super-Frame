import time
import random

class DroneSwarm:
    def __init__(self):
        self.swarm_size = 12 # 12 Drones in one unit
        self.status = "GROUNDED"

    def deploy_legion(self, mission_type):
        print(f"\033[1;36m[FLIGHT]\033[0m Initializing {mission_type} Protocol...")
        time.sleep(2)
        self.status = "AIRBORNE"
        
        print(f" \033[1;32m[LAUNCH]\033[0m {self.swarm_size} Drones deployed in Hive-Sync mode.")
        
        # Simulating live drone feed
        for i in range(1, 4):
            battery = random.randint(85, 98)
            print(f" \033[1;34m[DRONE-{i:02}]\033[0m Alt: 150m | Battery: {battery}% | Link: SECURE")
            time.sleep(0.5)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Aerial Legion is in the sky. \nEvery angle is covered. We have total \nair superiority over the current perimeter.\033[0m")

if __name__ == "__main__":
    swarm = DroneSwarm()
    swarm.deploy_legion("Area Surveillance")
