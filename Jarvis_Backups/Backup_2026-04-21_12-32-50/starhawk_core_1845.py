import time

class P1StarhawkSystem:
    def __init__(self):
        # कोड के भीतर फेज नंबर दर्ज है
        self.phase = 1845
        self.ship_name = "P-1 STARHAWK"
        print(f"--- {self.ship_name} Interface | Phase: {self.phase} ---")

    # कोड 1: Cockpit Command Bridge (Interior Interface)
    def cockpit_interface(self):
        print(f"\n[Code 01: Cockpit Bridge - Phase {self.phase}]")
        controls = ["Navigation_HUD", "Engine_Thrust", "Oxygen_Supply"]
        for control in controls:
            print(f"Booting {control}... [OK]")
            time.sleep(0.5)
        print("Cockpit Status: READY for Pilot Input.")
        return "Command Bridge Online"

    # कोड 2: Shield Integrity (Defense Logic)
    def shield_status(self):
        print(f"\n[Code 02: Shield Integrity - Phase {self.phase}]")
        integrity_level = 100 # Percentage
        print(f"Active Shield Level: {integrity_level}%")
        time.sleep(1)
        # काल्पनिक खतरा (Simulated Threat)
        print("Simulating Space Debris Impact...")
        integrity_level -= 2
        print(f"Updated Shield Level: {integrity_level}% | Status: STABLE")
        return "Defense Systems Active"

if __name__ == "__main__":
    starhawk = P1StarhawkSystem()
    
    # दोनों मॉड्यूल्स का एक साथ संचालन
    bridge_report = starhawk.cockpit_interface()
    defense_report = starhawk.shield_status()
    
    print(f"\n--- Phase {starhawk.phase} Mission Summary ---")
    print(f"Report: {bridge_report} & {defense_report}")
