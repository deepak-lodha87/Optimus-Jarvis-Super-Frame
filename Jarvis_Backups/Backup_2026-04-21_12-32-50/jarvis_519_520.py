import time
import random

class JarvisEnvironmentalLifeSupport:
    def __init__(self):
        self.phase_519 = "519.Molecular-Oxygen-Synthesis"
        self.phase_520 = "520.Zero-G-Flight-Stabilization"
        self.suit_pressure = 1.0  # Standard Atmospheric Pressure
        self.oxygen_level = 100

    def start_oxygen_synthesis(self, environment):
        print(f"\n--- [SYSTEM] Initializing {self.phase_519} ---")
        time.sleep(1)
        print(f"[JARVIS]: Detecting environment: {environment}...")
        
        if environment in ["Space", "Underwater", "Toxic_Zone"]:
            print("[ACTION]: Activating Molecular Scrubber and Oxygen Synthesizer.")
            time.sleep(1.5)
            print("[JARVIS]: Extracting O2 from surroundings/internal backup.")
            self.oxygen_level = 98
            print(f"[STATUS]: Oxygen Supply: {self.oxygen_level}% - STABLE.")
        else:
            print("[STATUS]: Normal air filtration active.")

    def calibrate_zero_g(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_520} ---")
        time.sleep(1)
        print("[JARVIS]: Detecting Zero-Gravity/Low-Gravity conditions...")
        
        # Zero-G में बैलेंस बनाए रखने के लिए थ्रस्टर्स का लॉजिक
        stabilization_data = {
            "Internal_Gyroscope": "Calibrated to 0.001 degree precision.",
            "Micro_Thrusters": "Active - Compensating for inertia.",
            "Magnetic_Boots": "Ready for surface attachment."
        }
        
        for module, status in stabilization_data.items():
            print(f" >> [STABILIZER]: {module} is {status}")
            time.sleep(0.7)
            
        print("\n[JARVIS]: Stabilization complete. Movement in Zero-G is now fluid.")

if __name__ == "__main__":
    jarvis_support = JarvisEnvironmentalLifeSupport()
    # Step 1: सांस लेने की तकनीक (जैसे Space में)
    jarvis_support.start_oxygen_synthesis("Space")
    # Step 2: जीरो ग्रेविटी में संतुलन
    jarvis_support.calibrate_zero_g()
