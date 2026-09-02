import time
import random

class NanoCore:
    def __init__(self):
        self.particle_count = 1000000 # 1 Million Nanobots
        self.assembly_status = "STABLE"

    def initiate_assembly(self, object_name):
        print(f"\033[1;36m[NANO-CORE]\033[0m Activating Molecular Assemblers for: {object_name}")
        time.sleep(2)
        
        progress = 0
        while progress < 100:
            progress += random.randint(10, 20)
            if progress > 100: progress = 100
            print(f" \033[1;32m[+] ASSEMBLLING:\033[0m {progress}% Lattice Synced...")
            time.sleep(0.7)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the {object_name} has been \nconstructed at a molecular level. The nano-particles \nare holding a stable configuration. Your \nphysical blueprint is ready for deployment.\033[0m")

if __name__ == "__main__":
    nano = NanoCore()
    nano.initiate_assembly("Tactical Gauntlet")
