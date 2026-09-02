import time
import random

class SonarNavigation:
    def __init__(self):
        self.depth = 120 # meters
        self.water_density = "High"

    def emit_sonar_pulse(self):
        print("\033[1;34m[SONAR] Emitting Acoustic Pulse (Ping)... 🔊\033[0m")
        time.sleep(1.5)
        # Analyzing Echo-Back signal for terrain mapping
        distance_to_floor = random.randint(50, 200)
        print(f"  • Echo Returned. Sea-Floor Depth: {distance_to_floor}m")
        return distance_to_floor

class DepthControl:
    def maintain_buoyancy(self, target_depth):
        print(f"\033[1;35m[CONTROL] Adjusting Ballast Tanks for {target_depth}m...\033[0m")
        time.sleep(1.2)
        print("  • Equalizing Internal/External Pressure... [OK]")
        return "\033[1;32m[STABLE] Sub-Surface Position Locked.\033[0m"

if __name__ == "__main__":
    sonar = SonarNavigation()
    marine_ctrl = DepthControl()
    
    print("-" * 50)
    print("   JARVIS SUB-SURFACE SONAR NAVIGATION (P3183-84)")
    print("-" * 50)
    
    floor_dist = sonar.emit_sonar_pulse()
    print("\n" + marine_ctrl.maintain_buoyancy(150))
    print("-" * 50)
