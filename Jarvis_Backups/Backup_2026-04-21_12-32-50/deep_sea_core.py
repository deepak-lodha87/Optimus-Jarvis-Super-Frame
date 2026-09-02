import time

class OceanicNav:
    def __init__(self):
        self.depth_meters = 0
        self.hull_integrity = 100

    def phase_2629(self):
        print("\033[1;34m>> INITIATING: [SYSTEM_ROOT_2629] - Abyssal Mapping\033[0m")
        print("[LOG] Activating Multi-beam Sonar Arrays...")
        time.sleep(1.2)
        print("[ACT] Scanning seafloor topography for thermal vents...")
        time.sleep(1.5)
        print("[RES] Bathymetric map generated. Safe passage identified through the trench.")

    def phase_2630(self):
        print("\n\033[1;36m>> INITIATING: [SYSTEM_ROOT_2630] - Hydrostatic Load Balancing\033[0m")
        print("[LOG] Monitoring external pressure levels...")
        time.sleep(1)
        
        # Unique Logic: Simulating descent into the deep
        for depth in range(0, 5001, 1000):
            pressure = depth * 0.101 # Simple bar calculation
            print(f"[ACT] Descending... Current Depth: {depth}m | Pressure: {pressure:.2f} bar", end='\r')
            time.sleep(0.5)
            
        print(f"\n[RES] Target Depth Reached: 5000m. Hull reinforcement holding steady.")
        print("\033[1;32m>> STATUS: SUB-AQUATIC SYSTEMS STABILIZED\033[0m")

if __name__ == "__main__":
    sub_nav = OceanicNav()
    sub_nav.phase_2629()
    sub_nav.phase_2630()
