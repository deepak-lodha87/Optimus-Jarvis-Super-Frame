import time
import random

class OptimusJarvisSuit:
    def __init__(self):
        self.user = "Deepak"
        self.phase_23 = "3023 (Nano-Material Synthesis)"
        self.phase_24 = "3024 (Energy Core Calibration)"
        self.core_stability = 0.0

    def synthesize_nanobots(self):
        print(f"\033[1;35m>> PHASE {self.phase_23}: ASSEMBLING NANO-PARTICLES <<\033[0m")
        materials = ["Carbon Nanotubes", "Gold-Titanium Alloy", "Neural Mesh"]
        for mat in materials:
            print(f"[SYNTHESIS] Processing {mat}...")
            time.sleep(0.5)
        print("\033[1;32m[SUCCESS] Nano-Material integrity: 100%. Suit frame ready for deployment.\033[0m")

    def calibrate_energy_core(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_24}: CALIBRATING ENERGY CORE <<\033[0m")
        time.sleep(1)
        self.core_stability = round(random.uniform(98.5, 99.9), 2)
        print(f"\033[1;34m[ENERGY] Arc-Core Output: 1.21 Gigawatts | Stability: {self.core_stability}%\033[0m")
        
        if self.core_stability > 99.0:
            print("\033[1;32m[STATUS] Energy Core is PERFECTLY STABLE, Sir. Weapon systems on standby.\033[0m")
        else:
            print("\033[1;33m[STATUS] Core fluctuation detected. Adjusting magnetic containment...\033[0m")

    def initiate_suit_logic(self):
        print(f"\033[1;32m>> SYSTEM ONLINE: ARCHITECT DEEPAK, ARMOR SYSTEMS ENGAGED. <<\033[0m")
        self.synthesize_nanobots()
        self.calibrate_energy_core()

if __name__ == "__main__":
    suit_jarvis = OptimusJarvisSuit()
    suit_jarvis.initiate_suit_logic()
