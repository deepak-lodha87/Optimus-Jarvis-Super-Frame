import time
import random

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.magnetic_viscosity = 10 # Current stiffness (1-100)
        self.road_condition = "SMOOTH"

    def scan_road_surface(self):
        """Phase 3244: LiDAR-based terrain scanning"""
        surface_depth = random.uniform(-10, 10) # Cm (Negative is a pothole)
        print(f"\033[1;34m[SCANNER] Analyzing Road Topography... Offset: {surface_depth:.1f}cm\033[0m")
        return surface_depth

    def adjust_magnetic_dampers(self):
        """Phase 3245: Changing fluid density using electromagnetic coils"""
        offset = self.scan_road_surface()
        
        print("\033[1;33m[EMS] Modulating Electromagnetic Coils...\033[0m")
        time.sleep(0.5)
        
        if offset < -5: # Pothole detected
            self.magnetic_viscosity = 5 # Make it super soft
            action = "SOFTENING for Pothole Impact"
        elif offset > 5: # Speed bump or rock
            self.magnetic_viscosity = 80 # Make it stiff to prevent bottoming
            action = "STIFFENING for Impact Support"
        else:
            self.magnetic_viscosity = 40 # Balanced
            action = "MAINTAINING Cruise Stability"
            
        return f"\033[1;32m[SUCCESS] {action}. Viscosity set to {self.magnetic_viscosity}%.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Raptor_Frame")
    
    print("-" * 60)
    print("   JARVIS UMC: MAGNETIC SUSPENSION TUNING (P3244-45)")
    print("-" * 60)
    
    # Simulating a sudden pothole
    print(umc.adjust_magnetic_dampers())
    print("-" * 60)
