import time
import random

class SpaceSurvivalSystem:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_life = 1876
        self.phase_rad = 1877
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Deep Space Survival: {self.phase_life} & {self.phase_rad}")

    # Phase 1876: Life Support System (CO2 Scrubbing & Water Recycling)
    def life_support_monitor(self):
        print(f"\n[Code 01: Life Support - Phase {self.phase_life}]")
        oxygen_level = 21.0 # Percentage
        co2_level = 0.04 # Percentage
        print(f"Current Oxygen: {oxygen_level}% | CO2 Level: {co2_level}%")
        time.sleep(1.2)
        print("Scrubbing CO2... Recycling moisture from air... [OK]")
        print("Status: Atmosphere is PURE and BREATHABLE.")
        return "Life Support: OPTIMAL"

    # Phase 1877: Radiation Shielding (Cosmic Ray Protection)
    def radiation_shield_status(self):
        print(f"\n[Code 02: Radiation Shielding - Phase {self.phase_rad}]")
        outside_radiation = random.randint(50, 500) # millisieverts
        print(f"External Cosmic Radiation: {outside_radiation} mSv")
        time.sleep(1.5)
        # मैग्नेटिक शील्ड और लेड लाइनिंग सिमुलेशन
        internal_exposure = outside_radiation * 0.001
        print(f"Magnetic Deflector: ACTIVE | Internal Exposure: {internal_exposure} mSv")
        print("Status: Crew protected from Solar Flares.")
        return "Shielding: ACTIVE"

if __name__ == "__main__":
    survival_core = SpaceSurvivalSystem()
    
    # दोनों फेजेस का निष्पादन
    life_report = survival_core.life_support_monitor()
    rad_report = survival_core.radiation_shield_status()
    
    print(f"\n--- Spaceship Survival Summary ---")
    print(f"Final Report: {life_report} | {rad_report}")
