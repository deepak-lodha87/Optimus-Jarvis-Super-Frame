import time
import random

class EVBikeIntelligence:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_cooling = 1882
        self.phase_regen = 1883
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing EV Modules: {self.phase_cooling} & {self.phase_regen}")

    # Phase 1882: Battery Cooling System (तापमान नियंत्रण)
    def thermal_management(self):
        print(f"\n[Code 01: Battery Cooling - Phase {self.phase_cooling}]")
        battery_temp = random.randint(30, 65) # Celsius
        print(f"Monitoring Battery Cells... Current Temp: {battery_temp}°C")
        time.sleep(1.2)
        
        if battery_temp > 50:
            print("Status: Activating Liquid Cooling Pump. Fan Speed: MAX.")
            return "Cooling: ACTIVE_HIGH"
        else:
            print("Status: Passive cooling sufficient. Temperature stable.")
            return "Cooling: PASSIVE"

    # Phase 1883: Regenerative Braking (ऊर्जा की बचत)
    def regenerative_braking(self, brake_force):
        print(f"\n[Code 02: Regenerative Braking - Phase {self.phase_regen}]")
        # brake_force: 0 to 100
        energy_recovered = brake_force * 0.25 # Simulation of Wh recovered
        print(f"Braking Force Detected: {brake_force}%")
        time.sleep(1.5)
        print(f"Converting Kinetic Energy to Electricity... Recovered: {energy_recovered} Wh")
        print("Battery Charging Status: INCREMENTAL RECOVERY ACTIVE.")
        return f"Regen Status: {energy_recovered}Wh RECOVERED"

if __name__ == "__main__":
    ev_tech = EVBikeIntelligence()
    
    # दोनों फेजेस का एक साथ निष्पादन
    cool_report = ev_tech.thermal_management()
    regen_report = ev_tech.regenerative_braking(75)
    
    print(f"\n--- EV Bike Systems Summary ---")
    print(f"Report: {cool_report} | {regen_report}")
