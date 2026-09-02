import time

class HiveMind:
    def __init__(self):
        self.air_unit = {"id": "Drone-01", "pos": (0, 0, 10), "task": "Scanning"}
        self.ground_unit = {"id": "Rover-01", "pos": (0, 0, 0), "task": "Moving"}

    def sync_mission(self):
        print("\033[1;36m[HIVE-MIND]\033[0m Establishing Cross-Platform Link...")
        time.sleep(1.2)

        # Drone shares visual data with Ground Rover
        print(f" \033[1;33m[AIR->GROUND]\033[0m Sending terrain map to {self.ground_unit['id']}...")
        time.sleep(1.0)
        
        # Ground Rover confirms reception
        print(f" \033[1;32m[GROUND->AIR]\033[0m Map received. Plotting path to destination.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the coordination is complete. \nI have linked the sky and the earth. \nThe drone sees what the rover cannot, \nand the rover carries what the drone \ncannot lift. Together, they are a single \norganism under my command.\033[0m")

if __name__ == "__main__":
    hive = HiveMind()
    hive.sync_mission()
