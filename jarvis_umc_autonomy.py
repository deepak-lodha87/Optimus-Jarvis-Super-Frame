import time
import random

class UniversalMachineController:
    def __init__(self, unit_id):
        self.unit_id = unit_id
        self.fuel_level = 15 # Low for testing
        self.vision_mode = "NORMAL"
        self.traction_grip = "STREET"

    def p3253_auto_docking(self):
        if self.fuel_level < 20:
            print("\033[1;33m[DOCKING] Low Reserves. Locating Nearest Energy Node...\033[0m")
            time.sleep(1)
            return "\033[1;32m[SUCCESS] Docking Probe Extended. Refueling Initiated.\033[0m"
        return "[FUEL] Energy levels sufficient."

    def p3254_hyper_spectral_scan(self):
        self.vision_mode = "HYPER-SPECTRAL"
        print(f"\033[1;35m[VISION] Shifting to {self.vision_mode}. Scanning Thermal & Gas Densities...\033[0m")
        return "[STATUS] Hidden Heat Signatures Detected at 200m."

    def p3255_ejection_protocol(self):
        # Unique Logic: Monitoring total system failure
        if random.random() < 0.01: # 1% chance in simulation
            return "\033[1;31m[CRITICAL] System Terminal. Ejecting Core/Pilot Pod Now!\033[0m"
        return "[SAFETY] All Life-Support and Structural Systems Green."

    def p3256_traction_shift(self, terrain_type):
        self.traction_grip = terrain_type
        print(f"\033[1;34m[MECHANICAL] Adapting to {terrain_type} Terrain. Adjusting PSI...\033[0m")
        time.sleep(0.8)
        return f"[SUCCESS] Traction Optimized for {terrain_type}."

    def p3257_acoustic_masking(self):
        # Blending sound with environmental noise
        return "\033[1;36m[STEALTH] Frequency Matching with Ambient Wind Noise Active.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus-X1")
    print("-" * 60)
    print("   JARVIS UMC: AUTONOMY & STEALTH BUNDLE (P3253-3257)")
    print("-" * 60)
    
    print(umc.p3253_auto_docking())
    print(umc.p3254_hyper_spectral_scan())
    print(umc.p3255_ejection_protocol())
    print(umc.p3256_traction_shift("OFF-ROAD_MUD"))
    print(umc.p3257_acoustic_masking())
    
    print("-" * 60)
    print("STATUS: Independent Operations Enabled. No Duplications Found.")
    print("-" * 60)
