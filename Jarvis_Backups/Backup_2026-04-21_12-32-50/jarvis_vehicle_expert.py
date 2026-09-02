import time

class VehicleExpert:
    def __init__(self):
        # Common DTC Codes for Honda/Kia
        self.dtc_database = {
            "P0300": "Random/Multiple Cylinder Misfire Detected.",
            "P0117": "Engine Coolant Temperature Sensor Circuit Low.",
            "P0420": "Catalyst System Efficiency Below Threshold.",
            "P0562": "System Voltage Low (Battery/Alternator Issue).",
            "P0171": "System Too Lean (Fuel/Air mixture issue)."
        }

    def analyze_fault(self, code):
        print(f"\033[1;34m[SCANNING] Analyzing Fault Code: {code}...\033[0m")
        time.sleep(1)
        if code in self.dtc_database:
            return f"\033[1;32m[SOLUTION] {self.dtc_database[code]}\033[0m"
        else:
            return "\033[1;31m[ERROR] Unknown Code. Please check the OBD-II connection.\033[0m"

if __name__ == "__main__":
    expert = VehicleExpert()
    print("-" * 40)
    print("   JARVIS VEHICLE DIAGNOSTIC INTERFACE")
    print("-" * 40)
    # Testing with a common battery/voltage issue
    result = expert.analyze_fault("P0562")
    print(result)
