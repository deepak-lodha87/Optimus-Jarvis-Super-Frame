import time
import random

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.suspension_height = "Normal"
        self.damping_stiffness = 50 # Percentage

    def calibrate_hydraulics(self):
        print(f"\033[1;34m[UMC-HYDRAULIC] Pressurizing Fluid Lines in {self.machine}...\033[0m")
        time.sleep(1.5)
        print("  • Valve Alignment: 100% | Pressure: 2500 PSI")
        return "\033[1;32m[READY] Suspension System is now Under Jarvis Command.\033[0m"

    def adjust_for_terrain(self, terrain_type):
        print(f"\033[1;33m[SENSING] Terrain Detected: {terrain_type}...\033[0m")
        time.sleep(1)
        
        if terrain_type == "OFF-ROAD":
            self.suspension_height = "High"
            self.damping_stiffness = 80
            action = "Increasing Ground Clearance & Stiffness"
        elif terrain_type == "HIGHWAY":
            self.suspension_height = "Low"
            self.damping_stiffness = 30
            action = "Lowering Center of Gravity for Aerodynamics"
        else:
            self.suspension_height = "Normal"
            self.damping_stiffness = 50
            action = "Standard Damping Active"

        return f"\033[1;32m[ACTION] {action}. Height: {self.suspension_height}, Stiffness: {self.damping_stiffness}%\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Heavy_Duty_Explorer")
    
    print("-" * 50)
    print("   JARVIS UMC: HYDRAULIC & SUSPENSION (P3208-09)")
    print("-" * 50)
    
    print(umc.calibrate_hydraulics())
    print("\n" + umc.adjust_for_terrain("OFF-ROAD"))
    print(umc.adjust_for_terrain("HIGHWAY"))
    print("-" * 50)
