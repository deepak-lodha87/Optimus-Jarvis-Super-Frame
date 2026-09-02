import time
import random

class EnergySiphon:
    def __init__(self):
        self.battery_level = 75.0
        self.temp_core = 38.5 # Celsius

    def process_incoming_energy(self, impact_joules, heat_level):
        print(f"\033[1;36m[SIPHON]\033[0m Detecting External Energy Inflow...")
        time.sleep(1)
        
        # Logic: Convert heat and impact into battery power
        conversion_factor = 0.15
        energy_gained = impact_joules * conversion_factor
        self.battery_level += energy_gained
        
        print(f" \033[1;33m[THERMAL]\033[0m Heat Dissipated: {heat_level}°C Stabilized.")
        print(f" \033[1;32m[CHARGE]\033[0m Energy Siphoned: +{energy_gained:.2f}%")
        
        if self.battery_level > 100: self.battery_level = 100
        print(f" \033[1;34m[SYSTEM]\033[0m Current Core Power: {self.battery_level:.2f}%")

        print(f"\n\033[1;35m[VOICE] Deepak sir, the kinetic siphon is active. \nAny external force directed at us is now \nmerely a source of fuel. We are effectively \nself-charging under pressure.\033[0m")

if __name__ == "__main__":
    shield = EnergySiphon()
    shield.process_incoming_energy(impact_joules=120, heat_level=800)
