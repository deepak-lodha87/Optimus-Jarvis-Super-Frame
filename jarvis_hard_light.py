import time
import random

class HardLightSystem:
    def __init__(self):
        self.photon_density = 0 # Percentage
        self.stability = "STABLE"

    def materialize_object(self, object_name):
        print(f"\033[1;36m[PROJECTOR]\033[0m Materializing {object_name} via Hard-Light...")
        time.sleep(1.5)
        
        while self.photon_density < 100:
            self.photon_density += 25
            print(f" \033[1;32m[PHASE]\033[0m Photon Density: {self.photon_density}% | Form: SOLIDIFYING")
            time.sleep(0.5)
            
        print(f"\033[1;34m[STATUS]\033[0m {object_name} is now physical and interactive.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the {object_name} has been \nmaterialized. You can now physically \ninteract with the hologram. The line \nbetween digital and physical has blurred.\033[0m")

if __name__ == "__main__":
    hologram = HardLightSystem()
    hologram.materialize_object("Tactical Map Interface")
