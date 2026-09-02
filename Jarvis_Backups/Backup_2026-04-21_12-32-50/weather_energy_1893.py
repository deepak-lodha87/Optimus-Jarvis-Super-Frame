import time
import random

class EnvironmentalController:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_weather = 1892
        self.phase_lightning = 1893
        self.energy_storage = 5000 # Megajoules
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Nature-Tech: {self.phase_weather} & {self.phase_lightning}")

    # Phase 1892: Weather Prediction & Analysis (मौसम का विश्लेषण)
    def analyze_weather(self):
        print(f"\n[Code 01: Weather Analysis - Phase {self.phase_weather}]")
        conditions = ["Thunderstorm", "Clear_Sky", "Heavy_Rain", "Solar_Flare"]
        current = random.choice(conditions)
        print(f"Scanning Atmospheric Pressure... Current State: {current}")
        time.sleep(1.2)
        return current

    # Phase 1893: Lightning Energy Harvesting (बिजली से ऊर्जा बनाना)
    def harvest_lightning(self, weather_state):
        print(f"\n[Code 02: Lightning Harvesting - Phase {self.phase_lightning}]")
        if weather_state == "Thunderstorm":
            print("Action: Deploying grounding rods and energy capacitors...")
            time.sleep(1.5)
            recovered_energy = random.randint(1000, 5000)
            self.energy_storage += recovered_energy
            print(f"Lightning Strike Captured! Energy Recovered: {recovered_energy} MJ")
            print(f"Total Grid Power: {self.energy_storage} MJ")
            return "Harvesting: SUCCESS"
        else:
            print("Status: No lightning detected. Energy harvesting on standby.")
            return "Harvesting: STANDBY"

if __name__ == "__main__":
    env_ctrl = EnvironmentalController()
    
    # दोनों फेजेस का निष्पादन
    current_weather = env_ctrl.analyze_weather()
    h_report = env_ctrl.harvest_lightning(current_weather)
    
    print(f"\n--- Environmental Power Summary ---")
    print(f"Report: Weather is {current_weather} | {h_report}")
