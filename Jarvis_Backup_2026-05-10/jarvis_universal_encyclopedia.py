import time

class MachineEncyclopedia:
    def __init__(self):
        self.domains = {
            "Aviation": ["Fighter Jet", "Drone", "Airplane"],
            "Maritime": ["Submarine", "Ship", "UAV-Boat"],
            "Terrestrial": ["Car", "Truck", "Motorcycle"],
            "Autonomous": ["Robotic-Arm", "Electrical-Train"]
        }

    def load_domain_specs(self, domain):
        print(f"\033[1;34m[DATABASE] Loading Blueprints for {domain} Domain...\033[0m")
        time.sleep(1)
        if domain in self.domains:
            for machine in self.domains[domain]:
                print(f"  • {machine}: Full Specifications Loaded [100%]")
                time.sleep(0.3)
        return f"\033[1;32m[SUCCESS] Jarvis is now expert in {domain} mechanics.\033[0m"

class PhysicsEngine:
    def calculate_environmental_force(self, domain):
        print(f"\033[1;35m[PHYSICS] Calculating resistance for {domain} medium...\033[0m")
        time.sleep(1.2)
        forces = {
            "Aviation": "Aerodynamic Lift & Drag",
            "Maritime": "Hydrodynamic Buoyancy",
            "Terrestrial": "Friction & Torque Optimization"
        }
        return f"\033[1;36m[LOG] Applied Physics: {forces.get(domain, 'Universal Dynamics')}\033[0m"

if __name__ == "__main__":
    jarvis_db = MachineEncyclopedia()
    physics = PhysicsEngine()
    
    print("-" * 50)
    print("   JARVIS UNIVERSAL MACHINE ENCYCLOPEDIA (P3147-48)")
    print("-" * 50)
    
    for d in ["Aviation", "Maritime", "Terrestrial"]:
        print(jarvis_db.load_domain_specs(d))
        print(physics.calculate_environmental_force(d))
        print("-" * 30)
