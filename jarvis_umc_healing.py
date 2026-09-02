import time

class UniversalMachineController:
    def __init__(self, machine_part):
        self.part = machine_part
        self.surface_damage = 0 # 0% to 100%
        self.nanite_reservoir = 100 # Fuel for healing

    def scan_surface_integrity(self, damage_detected):
        self.surface_damage = damage_detected
        print(f"\033[1;34m[SCAN] Detecting Structural Damage on {self.part}: {self.surface_damage}%\033[0m")
        return self.surface_damage

    def initiate_molecular_repair(self):
        """Phase 3241: Activating Shape-Memory Polymers"""
        if self.surface_damage > 0:
            print("\033[1;33m[HEALING] Heating Bio-Synthetic Skin Layers...\033[0m")
            time.sleep(1.5)
            print("\033[1;35m[REPAIR] Nanites Bridging the Gap in Molecular Lattice...\033[0m")
            time.sleep(1)
            self.surface_damage = 0
            self.nanite_reservoir -= 5
            return "\033[1;32m[SUCCESS] Surface Integrity Restored. Scratch/Dent Erased.\033[0m"
        return "No repair needed."

if __name__ == "__main__":
    umc = UniversalMachineController("Aerospace_Fuselage_Skin")
    
    print("-" * 60)
    print("   JARVIS UMC: BIO-SYNTHETIC SELF-HEALING (P3241)")
    print("-" * 60)
    
    # Simulating a 15% surface scratch
    umc.scan_surface_integrity(15)
    print(umc.initiate_molecular_repair())
    print("-" * 60)
