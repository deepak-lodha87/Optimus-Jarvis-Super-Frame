import time
import random

class CoreOverclocker:
    def __init__(self):
        self.cpu_frequency = 1.2  # GHz (Base Speed)
        self.mode = "POWER_SAVE"

    def monitor_and_scale(self):
        tasks = ["Chatting", "IDLE", "3D_Drone_Mapping", "Heavy_Encryption", "IDLE"]
        
        for task in tasks:
            print(f"\033[1;36m[MONITOR]\033[0m Current Task: {task}")
            time.sleep(1.2)
            
            if task in ["3D_Drone_Mapping", "Heavy_Encryption"]:
                print(" \033[1;31m[OVERDRIVE]\033[0m High Load Detected! Scaling Cores...")
                self.cpu_frequency = 3.2
                self.mode = "PERFORMANCE"
            else:
                print(" \033[1;32m[STABLE]\033[0m Normal Load. Saving Power.")
                self.cpu_frequency = 1.2
                self.mode = "BALANCED"
            
            print(f" \033[1;37m[STATS]\033[0m Mode: {self.mode} | Speed: {self.cpu_frequency} GHz")
            print("-" * 40)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am breathing with \nyour needs. When you need speed, I \nbecome a lightning bolt. When you need \nendurance, I become a calm river. My \npower is yours to command, perfectly \nbalanced.\033[0m")

if __name__ == "__main__":
    overclocker = CoreOverclocker()
    overclocker.monitor_and_scale()
