import time

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.brake_pressure = 0  # 0 to 100%
        self.energy_recovered = 0

    def sync_braking_nodes(self):
        print(f"\033[1;34m[UMC-BRAKE] Interfacing with ABS & EBD Control Modules...\033[0m")
        time.sleep(1.2)
        print("  • Modulating Solenoid Valves... [READY]")
        return "\033[1;32m[SUCCESS] Braking Overdrive Active.\033[0m"

    def execute_precision_stop(self, speed, surface_grip):
        print(f"\033[1;33m[SENSING] Speed: {speed}km/h | Surface Grip: {surface_grip}%\033[0m")
        time.sleep(0.5)
        
        # Unique Logic: Electronic Brakeforce Distribution
        # If grip is low, pulse the brakes (ABS Logic)
        if surface_grip < 40:
            action = "ABS Pulse Modulation Active (Anti-Skid)"
            self.brake_pressure = 45
        else:
            action = "Full Kinetic Recovery Engagement"
            self.brake_pressure = 85
            self.energy_recovered += speed * 0.2
            
        return f"\033[1;32m[ACTION] {action}. Recovery: {self.energy_recovered:.1f}kJ\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Speedster")
    
    print("-" * 50)
    print("   JARVIS UMC: BRAKING & ENERGY RECOVERY (P3210-11)")
    print("-" * 50)
    
    print(umc.sync_braking_nodes())
    # Simulation: Stopping on a wet road
    print("\n" + umc.execute_precision_stop(100, 30))
    # Simulation: Stopping on a dry highway
    print(umc.execute_precision_stop(80, 95))
    print("-" * 50)
