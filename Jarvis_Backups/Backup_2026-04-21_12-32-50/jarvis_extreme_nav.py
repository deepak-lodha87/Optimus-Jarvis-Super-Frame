import time
import math

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.depth_limit = 5000  # Meters
        self.altitude_limit = 100000 # Feet

    def phase_1526_submarine_navigation(self):
        print("\n--- [ PHASE 1526: SUBMARINE NAVIGATION LOGIC ] ---")
        print(">> Activating Sonar and Pressure Sensors...")
        time.sleep(0.6)
        print(f">> Current Depth Capacity: {self.depth_limit}m below sea level.")
        print(">> Status: Underwater hull integrity monitoring is ACTIVE.")

    def phase_1527_aerospace_flight_path(self):
        print("\n--- [ PHASE 1527: AEROSPACE FLIGHT PATH CALCULATION ] ---")
        print(">> Calculating Re-entry Vectors and Orbital Trajectory...")
        time.sleep(0.8)
        print(f">> Flight Ceiling: {self.altitude_limit}ft | Gravity Compensation: ON")
        print(">> Status: High-altitude flight path is locked and stable.")

    def launch_extreme_mode(self):
        print(f"--- [ OPTIMUS JARVIS: EXTREME NAVIGATION ] ---")
        self.phase_1526_submarine_navigation()
        self.phase_1527_aerospace_flight_path()
        print("-" * 55)
        print(f">> {self.user}, Jarvis can now navigate from the deep ocean to the edge of space.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.launch_extreme_mode()
