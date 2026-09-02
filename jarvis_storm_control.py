import time
import random

class StormControl:
    def __init__(self):
        self.drone_status = "STATIONARY"
        self.charge_level = 100

    def initiate_seeding(self):
        print(f"\033[1;36m[WEATHER-MOD]\033[0m Targeting localized cloud formation...")
        time.sleep(1.5)
        
        # Simulating cloud dispersal
        cloud_density = 85 # 85% density
        print(f" \033[1;33m[ACTION]\033[0m Deploying Silver Iodide pulse. Current Density: {cloud_density}%")
        
        while cloud_density > 20:
            cloud_density -= random.randint(10, 20)
            print(f" \033[1;32m[PROGRESS]\033[0m Cloud Density dropping: {max(cloud_density, 0)}%")
            time.sleep(0.8)
            
        print("\033[1;34m[STATUS]\033[0m Visibility Restored. Localized weather cleared.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the path is clear. I have \ndispersed the fog and stabilized the local \nair pressure. You are clear for the next \noperation.\033[0m")

if __name__ == "__main__":
    storm = StormControl()
    storm.initiate_seeding()
