import time

class ChemistryLab:
    def __init__(self):
        self.element_database = {
            "H2O": "Pure Water - Safe for consumption",
            "CO": "Carbon Monoxide - Lethal Gas",
            "C8H10N4O2": "Caffeine - Energy Booster",
            "NaCl": "Sodium Chloride - Common Salt"
        }

    def phase_2623(self):
        print("\033[1;35m>> INITIATING: [SYSTEM_ROOT_2623] - Molecular Spectroscopy\033[0m")
        print("[LOG] Activating laser-induced breakdown sensors...")
        time.sleep(1.2)
        print("[ACT] Capturing light absorption patterns of the target sample...")
        time.sleep(1.5)
        print("[RES] Molecular signature captured. Cross-referencing database...")

    def phase_2624(self):
        print("\n\033[1;33m>> INITIATING: [SYSTEM_ROOT_2624] - Substance Identification\033[0m")
        # Simulating a random scan of a sample
        sample_formula = "C8H10N4O2" 
        print(f"[LOG] Target Formula Detected: {sample_formula}")
        time.sleep(1)
        
        if sample_formula in self.element_database:
            analysis = self.element_database[sample_formula]
            print(f"[RES] Analysis Result: {analysis}")
        else:
            print("[RES] Unknown substance. Recommendation: Avoid contact.")
            
        print("\033[1;32m>> STATUS: CHEMICAL SENSORS CALIBRATED\033[0m")

if __name__ == "__main__":
    lab = ChemistryLab()
    lab.phase_2623()
    lab.phase_2624()
