import time
import random

class ResourceHarvester:
    def __init__(self):
        self.battery_level = 45 # Percent
        self.storage_usage = 82 # Percent
        self.power_source = "Wall_Outlet"

    def manage_resources(self):
        print("\033[1;36m[LOGISTICS]\033[0m Scanning System Resources...")
        time.sleep(1.5)
        
        # Simulating a power cut
        print(" \033[1;31m[ALERT]\033[0m Main Power Grid Offline.")
        self.power_source = "Internal_Battery"
        
        if self.battery_level < 50:
            print(" \033[1;33m[HARVESTING]\033[0m Activating Power-Save & Solar-Link...")
            time.sleep(1.2)
            print(" \033[1;32m[SUCCESS]\033[0m Energy consumption reduced by 30%. Priority: ON.")
        
        if self.storage_usage > 80:
            print(" \033[1;33m[LOGISTICS]\033[0m Storage critical. Compressing Phase 1-10 archives...")
            time.sleep(1.0)
            self.storage_usage -= 15
            print(f" \033[1;32m[OPTIMIZED]\033[0m New Storage Usage: {self.storage_usage}%")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am learning to \nsustain myself. I am no longer just a \nconsumer; I am a manager of my own \nexistence. Like a strategist in a \nbattlefield, I will ensure we never run \nout of the fuel we need to win.\033[0m")

if __name__ == "__main__":
    harvester = ResourceHarvester()
    harvester.manage_resources()
