import time, secrets

class OptimusJarvis:
    def __init__(self):
        self.version = "UMC-6748"

    def run_molecular_lab(self, material_name):
        print(f"\n\033[1;37m--- {self.version} : MOLECULAR LAB ACTIVE ---\033[0m")
        print(f"\033[1;36m[SYNTHESIZING] Simulating Atomic Structure for: {material_name}...\033[0m")
        time.sleep(2)
        
        # Stability Threshold changed from 85 to 10 (High chance of STABLE)
        stability = secrets.randbelow(100)
        if stability > 10: 
            status = "\033[1;32mSTABLE\033[0m"
            result = "Material ready for physical prototyping."
        else:
            status = "\033[1;31mUNSTABLE\033[0m"
            result = "Re-aligning carbon bonds..."

        print(f"\033[1;33m[RESULT] Density: High | Thermal Resistance: 2500°C | Integrity: {status}\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, simulation results are in. We have achieved structural stability.\033[0m")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.run_molecular_lab("Nano-Vibranium Alloy")
