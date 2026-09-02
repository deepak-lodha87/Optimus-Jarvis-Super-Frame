import time

class UniversalMachineController:
    def __init__(self, location):
        self.location = location
        self.water_tank = 0 # Liters
        self.humidity = 0 # Percentage

    def scan_atmosphere(self, hum_level):
        """Phase 3242: Detecting moisture particles in the air"""
        self.humidity = hum_level
        print(f"\033[1;34m[SENSOR] Humidity Level in {self.location}: {self.humidity}%\033[0m")
        return self.humidity

    def extract_liquid_h2o(self):
        """Phase 3243: High-speed condensation logic"""
        if self.humidity < 15:
            return "\033[1;31m[ERROR] Air too dry for extraction.\033[0m"
        
        print("\033[1;33m[EXTRACTOR] Cooling Peltier Plates to Dew Point...\033[0m")
        time.sleep(1.5)
        
        # Physics Logic: More humidity = faster extraction
        yield_rate = (self.humidity / 100) * 2.5
        self.water_tank += yield_rate
        
        print(f"\033[1;35m[PROCESS] Condensing Water Vapor... Yield: {yield_rate:.2f}L\033[0m")
        return f"\033[1;32m[SUCCESS] Extraction Complete. Current Tank: {self.water_tank:.2f} Liters.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Rajasthan_Desert")
    
    print("-" * 60)
    print("   JARVIS UMC: ATMOSPHERIC WATER EXTRACTION (P3242-43)")
    print("-" * 60)
    
    # Simulating dry desert air (25% humidity)
    umc.scan_atmosphere(25)
    print(umc.extract_liquid_h2o())
    print("-" * 60)
