import time

class JarvisPlanetaryShield:
    def __init__(self):
        self.phase_741 = "741.Magnetic-Field-Reconstruction"
        self.phase_742 = "742.Global-Ionosphere-Hardening"
        self.shield_integrity = 0.0
        self.plasma_deflection_rate = "0%"

    def map_magnetosphere(self, planet_name):
        print(f"\n--- [SYSTEM] Initializing {self.phase_741} ---")
        print(f"[JARVIS]: Mapping the magnetic-lines of {planet_name}...")
        
        # चुंबकीय क्षेत्र का नक्शा बनाने का लॉजिक
        mapping_steps = [
            "Detecting solar-wind pressure-points.",
            "Visualizing the Van Allen radiation belts.",
            "Identifying weak spots in the planetary-dipole."
        ]
        
        for step in mapping_steps:
            print(f" >> [MAPPING]: {step}")
            time.sleep(1.2)
            
        self.shield_integrity = 95.5
        print(f"\n[JARVIS]: Magnetic-Map is ready. I can now predict solar-flare impacts.")
        print(f"[STATUS]: Shield Integrity: {self.shield_integrity}%.")

    def activate_global_shield(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_742} ---")
        print("[JARVIS]: Hardening the Ionosphere via Tesla-Field-Arrays...")
        
        # पूरे ग्रह पर सुरक्षा कवच सक्रिय करने का लॉजिक
        shield_steps = [
            "Charging the upper-atmosphere with high-frequency ions.",
            "Creating a localized plasma-barrier against radiation.",
            "Engaging the 'Dreadnought-Wall' protocol."
        ]
        
        for step in shield_steps:
            print(f" >> [SHIELDING]: {step}")
            time.sleep(1.5)
            
        self.plasma_deflection_rate = "99.99%"
        print(f"\n[JARVIS]: The planet is now fortified, Deepak. No solar-storm can touch us.")
        print(f"[STATUS]: Plasma Deflection Rate: {self.plasma_deflection_rate}.")

if __name__ == "__main__":
    jarvis_ps = JarvisPlanetaryShield()
    # Step 1: ग्रह के चुंबकीय क्षेत्र को समझना
    jarvis_ps.map_magnetosphere("Earth")
    # Step 2: सुरक्षा कवच चालू करना
    jarvis_ps.activate_global_shield()
