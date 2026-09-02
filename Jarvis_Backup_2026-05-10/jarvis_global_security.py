import time
import random

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.global_zones = ["Asia-Pacific", "North-Atlantic", "Deep-Space-Network"]

    def phase_1484_global_threat_detection(self):
        print("\n--- [ PHASE 1484: GLOBAL THREAT DETECTION ] ---")
        print(">> Accessing Global Satellite Feeds...")
        time.sleep(0.5)
        for zone in self.global_zones:
            risk_level = random.choice(["LOW", "MINIMAL", "NEUTRAL"])
            print(f"   [SCANNING]: {zone} | Risk Factor: {risk_level}")
            time.sleep(0.3)
        print(">> Status: No imminent threats identified in primary sectors.")

    def phase_1485_autonomous_defense(self):
        print("\n--- [ PHASE 1485: AUTONOMOUS DEFENSE PROTOCOL ] ---")
        print(">> Syncing with Defense Satellite Network...")
        time.sleep(0.6)
        print(">> Status: Firewall Layers REINFORCED.")
        print(">> Defense Mode: Passive Monitoring (Active Response Standby).")

    def initiate_security_grid(self):
        print(f"--- [ OPTIMUS JARVIS: SECURITY GRID ] ---")
        self.phase_1484_global_threat_detection()
        self.phase_1485_autonomous_defense()
        print("-" * 50)
        print(f">> {self.user}, global monitoring is synchronized and secured.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.initiate_security_grid()
