import time

class Terraformer:
    def __init__(self):
        self.air_quality = "Poor"
        self.ocean_purity = "45%"

    def phase_2815(self):
        print("\033[1;32m>> INITIATING: [SYSTEM_ROOT_2815] - Atmospheric Detoxification\033[0m")
        print("[LOG] Deploying nanobots to neutralize CO2 and industrial pollutants...")
        time.sleep(1.2)
        # Unique Logic: Turning pollution into oxygen
        self.air_quality = "PRISTINE"
        print(f"[ACT] Air Quality Index: {self.air_quality}. Global Warming reversed.")
        time.sleep(1.5)
        print("[RES] Atmosphere stabilized. The Earth can breathe again.")

    def phase_2816(self):
        print("\n\033[1;34m>> INITIATING: [SYSTEM_ROOT_2816] - Oceanic Ecosystem Revival\033[0m")
        print("[LOG] Activating magnetic pulses to extract microplastics from oceans...")
        time.sleep(1)
        
        # Unique Logic: Rebuilding coral reefs and marine life
        self.ocean_purity = "100%"
        print(f"[ACT] Water Purity: {self.ocean_purity} | Marine Biodiversity: RESTORED")
        time.sleep(1.2)
        
        print("\n[RES] Planet-wide Restoration Complete. Nature is in balance.")
        print("\033[1;32m>> STATUS: ENVIRONMENTAL STABILIZATION FULLY ACTIVE\033[0m")

if __name__ == "__main__":
    earth = Terraformer()
    earth.phase_2815()
    earth.phase_2816()
