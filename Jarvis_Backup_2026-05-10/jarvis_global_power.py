import time

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.satellite_count = 24
        self.core_temp = "3200 K"

    def phase_1470_satellite_uplink(self):
        print("\n--- [ PHASE 1470: GLOBAL SATELLITE LINK ] ---")
        print(f">> Establishing connection with {self.satellite_count} orbital nodes...")
        time.sleep(0.5)
        print(">> Signal Strength: MAXIMUM.")
        print(">> Status: Global coverage active. Real-time data sync enabled.")

    def phase_1471_energy_stabilization(self):
        print("\n--- [ PHASE 1471: ENERGY CORE STABILIZATION ] ---")
        print(f">> Monitoring Thermal Levels: {self.core_temp}")
        time.sleep(0.6)
        print(">> Containment Field: REINFORCED.")
        print(">> Status: Energy output is stable and fluctuating within safe margins.")

    def activate_global_network(self):
        print(f"--- [ OPTIMUS JARVIS: GLOBAL INFRASTRUCTURE ] ---")
        self.phase_1470_satellite_uplink()
        self.phase_1471_energy_stabilization()
        print("-" * 45)
        print(f">> {self.user}, the global network and power systems are synchronized.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.activate_global_network()
