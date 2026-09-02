import time
import random

class UniversalMachineController:
    def __init__(self):
        self.engine_temp_limit = 2000 # Celsius
        self.geo_fence_status = "INSIDE_BOUNDARY"
        self.pest_control = "OFF"

    def p3483_molecular_coating(self):
        return "\033[1;34m[MATERIAL] Nano-Ceramic Coating Active. Engine thermal resistance increased to 2000°C.\033[0m"

    def p3484_hydro_aero_flaps(self, rain_intensity):
        if rain_intensity > 70:
            return "\033[1;36m[AERO] Heavy Rain! Adjusting Hydro-Flaps for maximum water displacement.\033[0m"
        return "[STATUS] Standard aerodynamics active."

    def p3485_geo_fencing(self, current_lat_long):
        # Example boundary check
        if "Out_of_Range" in current_lat_long:
            self.geo_fence_status = "LOCKED"
            return "\033[1;31m[SECURITY] Geo-Fence Breach! Machine outside safe zone. Locking System.\033[0m"
        return "[STATUS] Inside safe perimeter."

    def p3486_pest_repellent(self):
        self.pest_control = "ON"
        return "\033[1;32m[SYSTEM] Ultrasonic Frequency Active. Protecting wiring from rodent damage.\033[0m"

    def p3487_heat_map_nav(self):
        return "\033[1;33m[NAV] Scanning Thermal Traffic Data. Route optimized for fuel efficiency and speed.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: ARMOR & NAVIGATION (P3483-3487)")
    print("-" * 60)
    
    print(umc.p3483_molecular_coating())
    print(umc.p3484_hydro_aero_flaps(85))
    print(umc.p3485_geo_fencing("City_Center"))
    print(umc.p3486_pest_repellent())
    print(umc.p3487_heat_map_nav())
    
    print("-" * 60)
    print("STATUS: Material Integrity & Geo-Security Grid Online.")
    print("-" * 60)
