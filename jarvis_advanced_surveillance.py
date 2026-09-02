import time
import random

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.protocol = "Guardian-Alpha"

    def phase_1530_biometric_surveillance(self):
        print("\n--- [ PHASE 1530: BIOMETRIC HEALTH SURVEILLANCE ] ---")
        print(">> Scanning user vitals via remote sensors...")
        time.sleep(0.6)
        heart_rate = random.randint(70, 85)
        stress_level = "LOW"
        print(f">> Heart Rate: {heart_rate} BPM | Stress Analysis: {stress_level}")
        print(">> Status: User health is within optimal parameters.")

    def phase_1531_hazard_mitigation(self):
        print("\n--- [ PHASE 1531: ENVIRONMENTAL HAZARD MITIGATION ] ---")
        print(">> Analyzing air toxicity and radiation levels...")
        time.sleep(0.7)
        hazards = ["Toxic Gas Leak", "Thermal Flare", "Radiation Spike", "None"]
        detected = hazards[-1] # Selecting 'None' for simulation
        print(f">> Hazard Scan: {detected} | Risk Level: 0%")
        print(">> Status: Environment is safe for operational deployment.")

    def activate_guardian(self):
        print(f"--- [ OPTIMUS JARVIS: {self.protocol} ] ---")
        self.phase_1530_biometric_surveillance()
        self.phase_1531_hazard_mitigation()
        print("-" * 55)
        print(f">> {self.user}, Jarvis is now monitoring your physical state and your surroundings.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.activate_guardian()
