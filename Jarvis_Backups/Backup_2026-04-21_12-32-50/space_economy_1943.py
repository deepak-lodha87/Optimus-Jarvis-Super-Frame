import time
import random

class SpaceSettlementCore:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_habitat = 1942
        self.phase_mining = 1943
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Space Frontier Modules: {self.phase_habitat} & {self.phase_mining}")

    # Phase 1942: Extraterrestrial Habitat Support (जीवन रक्षक प्रणाली)
    def monitor_habitat_environment(self):
        print(f"\n[Code 01: Habitat Support - Phase {self.phase_habitat}]")
        print("Checking Life Support Systems: Oxygen, Pressure, and Radiation shielding...")
        time.sleep(1.5)
        
        o2_level = round(random.uniform(19.5, 21.0), 2)
        radiation_shield = "ACTIVE"
        
        print(f"Oxygen Concentration: {o2_level}% | Radiation Protection: {radiation_shield}")
        if o2_level < 20:
            print("Action: Releasing reserve oxygen from algae-tanks...")
        return "Habitat: HABITABLE"

    # Phase 1943: Asteroid Mining Logic (कीमती खनिजों की खुदाई)
    def conduct_asteroid_mining(self, asteroid_id):
        print(f"\n[Code 02: Asteroid Mining - Phase {self.phase_mining}]")
        print(f"Anchoring mining drones to Asteroid: {asteroid_id}...")
        time.sleep(2.0)
        
        resources = {"Platinum": "2.5 tons", "Water_Ice": "500 liters", "Iron": "15 tons"}
        print(f"Extraction in Progress... Found: {resources}")
        print("Status: Refining raw materials into usable cargo.")
        return "Mining: HARVEST_COMPLETE"

if __name__ == "__main__":
    space_sys = SpaceSettlementCore()
    
    # दोनों फेजेस का निष्पादन
    env_report = space_sys.monitor_habitat_environment()
    mine_report = space_sys.conduct_asteroid_mining("Vesta-Alpha-07")
    
    print(f"\n--- Space Frontier Summary ---")
    print(f"Final Status: {env_report} | {mine_report}")
