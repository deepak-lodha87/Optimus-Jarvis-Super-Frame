import time
import random

class JarvisStellarMastery:
    def __init__(self):
        self.phase_579 = "579.Stellar-Nuclear-Ignition-Control"
        self.phase_580 = "580.Nebula-Gaseous-Fuel-Harvester"
        self.star_temperature = 0
        self.fuel_reserve_kg = 0

    def stabilize_star_core(self, star_name):
        print(f"\n--- [SYSTEM] Initializing {self.phase_579} ---")
        time.sleep(1)
        print(f"[JARVIS]: Calculating Fusion-Rate for {star_name}...")
        
        # तारे की ऊर्जा को कंट्रोल करने का लॉजिक
        self.star_temperature = random.randint(5000, 15000)
        control_steps = [
            "Adjusting Magnetic-Containment fields.",
            "Regulating Hydrogen-to-Helium conversion ratio.",
            "Preventing premature Supernova collapse."
        ]
        
        for step in control_steps:
            print(f" >> [CONTROL]: {step}")
            time.sleep(0.9)
            
        print(f"[STATUS]: {star_name} stabilized at {self.star_temperature}K. Output: OPTIMAL.")

    def harvest_nebula_gas(self, nebula_name):
        print(f"\n--- [SYSTEM] Initializing {self.phase_580} ---")
        time.sleep(1)
        print(f"[JARVIS]: Deploying Ion-Scoops into the {nebula_name} cloud...")
        
        # नेबुला से गैस इकट्ठा करने का लॉजिक
        gas_types = ["Hydrogen", "Helium", "Stardust-Carbon"]
        collected = random.choice(gas_types)
        amount = random.randint(10000, 90000)
        
        print(f"[ACTION]: Filtering {collected} from cosmic dust.")
        time.sleep(1.5)
        
        self.fuel_reserve_kg += amount
        print(f"[JARVIS]: Harvest complete. Added {amount}kg of {collected} to reserves.")
        print(f"[STATUS]: Total Fuel Inventory: {self.fuel_reserve_kg}kg.")

if __name__ == "__main__":
    jarvis_star = JarvisStellarMastery()
    # Step 1: किसी तारे की गर्मी को कंट्रोल करना
    jarvis_star.stabilize_star_core("Solar-Alpha-01")
    # Step 2: अंतरिक्ष के बादलों से ईंधन भरना
    jarvis_star.harvest_nebula_gas("Orion-Nebula")
