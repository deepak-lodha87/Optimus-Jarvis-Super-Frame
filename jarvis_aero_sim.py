import time

class AeroSimulation:
    def __init__(self):
        self.air_density = 1.225  # Sea level density in kg/m3
        self.drag_coefficients = {
            "Sports Car": 0.3,
            "Fighter Jet": 0.02,
            "Square Box": 1.05,
            "Bullet": 0.29
        }

    def calculate_drag(self, vehicle, speed_kmh):
        # Speed ko m/s mein convert karna
        speed_ms = speed_kmh / 3.6
        print(f"\033[1;34m[SIMULATING] {vehicle} at {speed_kmh} km/h...\033[0m")
        time.sleep(1)
        
        if vehicle in self.drag_coefficients:
            cd = self.drag_coefficients[vehicle]
            # Drag Force formula: Fd = 1/2 * rho * v^2 * Cd * A (A constant maan kar)
            drag_force = 0.5 * self.air_density * (speed_ms ** 2) * cd
            
            print(f"  • Drag Coefficient: {cd}")
            print(f"  • Air Resistance Force: {drag_force:.2f} Newtons")
            
            if speed_kmh > 1200: # Supersonic
                return "\033[1;35m[SONIC BOOM] Breaking the sound barrier! Structure holding.\033[0m"
            return "\033[1;32m[STABLE] Aerodynamic profile is efficient.\033[0m"
        return "[ERROR] Vehicle profile not found."

if __name__ == "__main__":
    aero = AeroSimulation()
    print("-" * 50)
    print("   JARVIS AERODYNAMIC FLIGHT SIMULATOR")
    print("-" * 50)
    
    # Testing a Fighter Jet at Supersonic speed
    print(aero.calculate_drag("Fighter Jet", 1500))
    print("\n" + "-"*20 + "\n")
    # Testing a Sports Car at highway speed
    print(aero.calculate_drag("Sports Car", 200))
