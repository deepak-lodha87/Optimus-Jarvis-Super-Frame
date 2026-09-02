import time

class JarvisExtremeClimate:
    def __init__(self):
        self.phase_963 = "963.Cryogenic-Hardening"
        self.phase_964 = "964.Anti-Icing-Thermal-Mesh"
        self.external_temp = -45.0  # Celsius
        self.internal_stability = True

    def stabilize_cryo_temp(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_963} ---")
        print(f"[JARVIS]: Detecting external temperature: {self.external_temp}°C")
        
        cryo_protocols = [
            "Insulating battery-core with aerogel layers.",
            "Adjusting lubricant viscosity for freezing-point.",
            "Heating internal circuits to prevent brittle-fracture."
        ]
        
        for protocol in cryo_protocols:
            print(f" >> [CRYOGENICS]: {protocol}")
            time.sleep(1.2)
            
        print("[JARVIS]: Internal systems stabilized for sub-zero operation.")

    def prevent_ice_buildup(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_964} ---")
        print("[JARVIS]: Activating surface-heating mesh...")
        
        ice_steps = [
            "Sending electrical pulses to wing-tips and vents.",
            "Breaking micro-ice crystals via vibration-frequency.",
            "Coating outer-frame with hydrophobic-nano-layer."
        ]
        
        for step in ice_steps:
            print(f" >> [DE-ICING]: {step}")
            time.sleep(1.4)
            
        print("\n[JARVIS]: Anti-Icing active. Aerodynamics cleared.")

if __name__ == "__main__":
    climate = JarvisExtremeClimate()
    # Behad thand ke liye systems ko adjust karna
    climate.stabilize_cryo_temp()
    # Baraf ko jamne se rokna
    climate.prevent_ice_buildup()
