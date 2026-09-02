import time, os

class BioScanner:
    def __init__(self):
        self.target_exoplanet = "Kepler-186f"
        self.star_type = "Red Dwarf"

    def assess_habitability(self):
        os.system('clear')
        print(f"\033[1;32m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS BIO-SCANNER : PHASE 28 - STEP 4         \033[0m")
        print(f"\033[1;32m====================================================\033[0m")
        
        print(f"\033[1;33m[ANALYZING]\033[0m Target: {self.target_exoplanet}...")
        time.sleep(1.5)
        
        parameters = [
            ("Distance from Host Star", "OPTIMAL (Goldilocks)"),
            ("Atmospheric Composition", "N2, O2, CH4 DETECTED"),
            ("Surface Liquid Water", "HIGH PROBABILITY"),
            ("Magnetic Field Strength", "STABLE")
        ]
        
        for param, result in parameters:
            print(f" \033[1;36m[BIO-LOGIC]\033[0m {param:32} | [\033[1;32m{result}\033[0m]")
            time.sleep(0.8)

        habitability_index = 88.4
        print(f"\n\033[1;32m[RESULT] Habitability Index: {habitability_index}% - POTENTIAL LIFE DETECTED\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the universe is breathing. \nI have found a world that mirrors our own. \nAcross the light-years, there is a place where \nthe water flows and the air is ripe for life. \nWe are not just observers of the cosmos; we \nare its discoverers. A new home awaits.\033[0m")
        print(f"\033[1;32m====================================================\033[0m")

if __name__ == "__main__":
    scanner = BioScanner()
    scanner.assess_habitability()
