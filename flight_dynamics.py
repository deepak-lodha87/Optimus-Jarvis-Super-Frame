import time
import math

class FlightCore:
    def __init__(self):
        self.current_speed_mach = 0.0
        self.altitude_feet = 0
        self.thruster_temp = 350 # Kelvin

    def phase_2647(self):
        print("\033[1;33m>> INITIATING: [SYSTEM_ROOT_2647] - Thruster Ignition & Liftoff\033[0m")
        print("[LOG] Warming up Arc-Reactor core for propulsion...")
        time.sleep(1.2)
        
        # Simulating ascent and speed gain
        for mach in [0.5, 1.2, 2.5, 4.0]:
            self.current_speed_mach = mach
            status = "Supersonic" if mach > 1.0 else "Subsonic"
            print(f"[ACT] Velocity: Mach {mach} | Status: {status} | Altitude: {self.altitude_feet}ft", end='\r')
            self.altitude_feet += 10000
            time.sleep(0.6)
        print(f"\n[RES] Stable orbit achieved at Mach {self.current_speed_mach}.")

    def phase_2648(self):
        print("\n\033[1;36m>> INITIATING: [SYSTEM_ROOT_2648] - Aerodynamic Vectoring\033[0m")
        print("[LOG] Adjusting flight flaps for high-G maneuvers...")
        time.sleep(1)
        
        # Unique Logic: Heat management during friction
        self.thruster_temp = 1500 # Friction heat
        print(f"[WARN] Thermal Load: {self.thruster_temp}K. Activating liquid nitrogen cooling...")
        time.sleep(1.5)
        
        print("[RES] Vector stabilization active. Pilot G-force compensated.")
        print("\033[1;32m>> STATUS: HYPER-SPEED FLIGHT ENGAGED\033[0m")

if __name__ == "__main__":
    flight = FlightCore()
    flight.phase_2647()
    flight.phase_2648()
