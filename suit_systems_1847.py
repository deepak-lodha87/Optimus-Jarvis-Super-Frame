import time

class IronManSuitSystems:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित है
        self.phase = 1847
        self.suit_model = "Mark_85_Optimus"
        print(f"--- {self.suit_model} Systems | Phase: {self.phase} ---")

    # कोड 1: Flight Thrusters Logic (Stability & Propulsion)
    def flight_thrusters(self):
        print(f"\n[Code 01: Flight Thrusters - Phase {self.phase}]")
        thruster_power = 85 # Percentage
        print(f"Igniting Palm and Boot Thrusters... Power at {thruster_power}%")
        time.sleep(1.2)
        print("Stabilizing flight altitude... Flight vector: LOCKED.")
        return "Thrusters: STABLE"

    # कोड 2: Life Support & Oxygen (Internal Environment)
    def life_support(self):
        print(f"\n[Code 02: Life Support - Phase {self.phase}]")
        oxygen_level = 98 # Percentage
        internal_temp = 22 # Celsius
        print(f"Monitoring Oxygen: {oxygen_level}% | Internal Temp: {internal_temp}°C")
        time.sleep(1.0)
        if oxygen_level > 90:
            print("Atmospheric filtration: ACTIVE. Oxygen supply is PURE.")
        return "Life Support: OPTIMAL"

if __name__ == "__main__":
    suit = IronManSuitSystems()
    
    # दोनों मॉड्यूल्स का एक साथ निष्पादन
    f_status = suit.flight_thrusters()
    l_status = suit.life_support()
    
    print(f"\n--- Phase {suit.phase} System Diagnostics Complete ---")
    print(f"Overall Status: {f_status} | {l_status}")
