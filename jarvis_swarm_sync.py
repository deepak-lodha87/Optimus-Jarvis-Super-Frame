import time
import random

class SwarmController:
    def __init__(self, drone_count):
        self.drone_count = drone_count
        self.formation = "V-SHAPE"

    def sync_drones(self):
        print(f"\033[1;36m[SWARM]\033[0m Booting Multi-Drone Link: {self.drone_count} Units Active.")
        time.sleep(1.5)
        
        print(f"\033[1;33m[FORMATION]\033[0m Setting drones in {self.formation} pattern...")
        time.sleep(1.0)
        
        for i in range(1, self.drone_count + 1):
            latency = random.randint(5, 20)
            status = "STABLE"
            print(f" \033[1;32m[UNIT-{i:02}]\033[0m Connection: {latency}ms | Position: Locked | Status: {status}")
            time.sleep(0.4)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, we are no longer a single \nunit. We are a Legion. I am coordinating \nevery move, every blink, and every sensor \nof this swarm. Together, we are unstoppable. \nThe sky is now our kingdom.\033[0m")

if __name__ == "__main__":
    swarm = SwarmController(drone_count=5)
    swarm.sync_drones()
