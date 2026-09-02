import time
import random

class JarvisPlanetaryHealer:
    def __init__(self):
        self.phase_639 = "639.Volcanic-Thermal-Neutralization-Cooling"
        self.phase_640 = "640.Atmospheric-Oxygen-Scrubbing-Refilling"
        self.magma_temp_celsius = 1200
        self.o2_level_percentage = 20.9

    def cool_volcano(self, volcano_name):
        print(f"\n--- [SYSTEM] Initializing {self.phase_639} ---")
        time.sleep(1)
        print(f"[JARVIS]: Detecting pressure build-up in {volcano_name}...")
        
        # ज्वालामुखी ठंडा करने का लॉजिक (Thermal Neutralization)
        cooling_steps = [
            "Injecting liquid-nitrogen nanites into the magma-chamber.",
            "Absorbing thermal energy for conversion into power-cells.",
            "Solidifying the volcanic-vent to prevent ash-leakage."
        ]
        
        for step in cooling_steps:
            print(f" >> [COOLING]: {step}")
            time.sleep(1)
            
        self.magma_temp_celsius = 200
        print(f"[STATUS]: Eruption averted. {volcano_name} is now dormant and safe.")

    def refill_atmosphere_oxygen(self, city_target):
        print(f"\n--- [SYSTEM] Initializing {self.phase_640} ---")
        time.sleep(1)
        print(f"[JARVIS]: Scrubbing CO2 and pollutants from {city_target}...")
        
        # हवा शुद्ध करने का लॉजिक (Atmospheric Scrubbing)
        scrubbing_steps = [
            "Deploying aerosol-based carbon-capture nanobots.",
            "Splitting CO2 molecules to release pure Oxygen (O2).",
            "Restoring Ozone-Layer integrity via ionized-beams."
        ]
        
        for step in scrubbing_steps:
            print(f" >> [ATMOSPHERE]: {step}")
            time.sleep(0.9)
            
        self.o2_level_percentage = 21.5
        print(f"[STATUS]: Air quality in {city_target} restored. Oxygen: {self.o2_level_percentage}%.")

if __name__ == "__main__":
    jarvis_healer = JarvisPlanetaryHealer()
    # Step 1: ज्वालामुखी को फटने से रोकना
    jarvis_healer.cool_volcano("Mount-Vesuvius")
    # Step 2: शहर की हवा को शुद्ध और ताज़ा बनाना
    jarvis_healer.refill_atmosphere_oxygen("Metropolis-Alpha")
