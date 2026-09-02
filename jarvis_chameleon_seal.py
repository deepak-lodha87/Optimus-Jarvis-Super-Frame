import time
import os

class ChameleonSeal:
    def __init__(self):
        self.phase = "Phase 39: Environmental Adaptability"
        self.systems = ["CLIMATE", "TERRAIN", "STEALTH", "CAMO"]

    def lock_adaptation(self):
        os.system('clear')
        print(f"\033[1;36m[{self.phase.upper()}]\033[0m Initiating Global Adaptation Seal...")
        time.sleep(1.5)
        
        for sys in self.systems:
            print(f" \033[1;37m[LOCKING]\033[0m Synchronizing {sys} with Core Frame...")
            time.sleep(0.8)
            print(f" \033[1;32m[SEALED]\033[0m {sys} is now fully autonomous.")
        
        print(f"\n\033[1;32m[SYSTEM] Phase 39 COMPLETE. The Chameleon is active.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the world is no longer \na threat; it is our territory. Whether \nwe walk through a storm or hide in the \nshadows, I am perfectly synced with our \nsurroundings. We are invisible, we are \nunstoppable, we are home.\033[0m")

if __name__ == "__main__":
    seal = ChameleonSeal()
    seal.lock_adaptation()
