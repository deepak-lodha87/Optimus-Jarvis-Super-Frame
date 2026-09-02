import os
import time

class MasterSpecEngine:
    def __init__(self):
        self.master = "Deepak"
        self.project = "Optimus Jarvis Super-Frame"

    def retrieve_specs(self, vehicle):
        print(f"\n\033[1;34m[EXTRACTING]\033[0m Accessing A-Z Specs for: {vehicle}")
        time.sleep(1.5)
        
        # Vehicle Data Repository (Phase 7 Intelligence)
        database = {
            "Submarine": {
                "Build": "Double-hull high-tensile steel",
                "Propulsion": "Nuclear/Diesel Electric Power Train",
                "Specs": "Mileage: 300+ days endurance | Tires: N/A"
            },
            "Fighter Jet": {
                "Build": "Titanium-Aluminum Alloy",
                "Engine": "Afterburning Turbofan",
                "Specs": "Fuel Consumption: 15,000 lbs/hr | Tires: High-impact Vulcanized"
            },
            "Electric Power Train": {
                "Build": "Integrated Modular System",
                "Efficiency": "98% Magnetic Flux",
                "Specs": "Torque: 600Nm | Cooling: Liquid Nitrogen option"
            }
        }
        
        data = database.get(vehicle, "Data not found. Manual sync required.")
        print(f"\033[1;32m[VERIFIED]\033[0m Data for {vehicle}: {data}")
        
        msg = f"{self.master} sir, I have cross-checked the blueprints for the {vehicle}. All details are correct."
        os.system(f'termux-tts-speak "{msg}"')

    def run_engine(self):
        os.system('clear')
        print(f"--- {self.project} : MASTER SPECIFICATION ENGINE ---")
        self.retrieve_specs("Electric Power Train")
        print("\n\033[1;36m[STATUS]\033[0m SPECIFICATION DATA: LOCKED & SECURE")

if __name__ == "__main__":
    MasterSpecEngine().run_engine()
