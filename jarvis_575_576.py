import time
import random

class JarvisPlanetaryDefense:
    def __init__(self):
        self.phase_575 = "575.Dark-Energy-Pulse-Weaponry"
        self.phase_576 = "576.Planetary-Scale-Shield-Generation"
        self.shield_integrity = 0.0
        self.weapon_charge = 0.0

    def fire_dark_energy_pulse(self, target_distance):
        print(f"\n--- [SYSTEM] Initializing {self.phase_575} ---")
        time.sleep(1)
        print("[JARVIS]: Concentrating Dark-Matter particles into the core-emitter...")
        
        # हथियार चार्ज करने का लॉजिक
        while self.weapon_charge < 100:
            self.weapon_charge += 20
            print(f" >> [CHARGING]: Pulse Battery at {self.weapon_charge}%")
            time.sleep(0.5)
            
        print(f"[ACTION]: Firing Dark-Energy Pulse at target {target_distance} km away!")
        print("[JARVIS]: Molecular bonds of the target have been dissolved. Threat eliminated.")
        self.weapon_charge = 0

    def deploy_planetary_shield(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_576} ---")
        time.sleep(1)
        print("[JARVIS]: Synchronizing global satellite array for Shield-Grid...")
        
        # पूरी पृथ्वी को ढंकने वाली ढाल का लॉजिक
        grid_sections = ["North-Hemisphere", "South-Hemisphere", "Equatorial-Belt"]
        
        for section in grid_sections:
            print(f" >> [ACTIVATING]: Plasma-Grid over {section}...")
            time.sleep(1)
            
        self.shield_integrity = 100.0
        print(f"[STATUS]: Planetary Shield is 100% Active. Earth is now invisible to long-range sensors.")

if __name__ == "__main__":
    jarvis_defense = JarvisPlanetaryDefense()
    # Step 1: डार्क एनर्जी पल्स चलाना
    jarvis_defense.fire_dark_energy_pulse(500000)
    # Step 2: पूरी पृथ्वी के चारों ओर सुरक्षा ढाल बनाना
    jarvis_defense.deploy_planetary_shield()
