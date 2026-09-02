import time
import random

class VehicleSync:
    def __init__(self):
        self.vehicle_name = "Deepak's Prime Unit"
        self.connection = "STABLE"

    def run_full_scan(self):
        print(f"\033[1;36m[SYNCING]\033[0m Connecting to {self.vehicle_name} ECU...")
        time.sleep(2)
        
        # Simulating live vehicle telemetry
        fuel_level = random.randint(15, 85)
        engine_temp = random.randint(70, 105)
        battery_volt = round(random.uniform(12.1, 14.2), 1)
        
        print(f" \033[1;32m[SCAN]\033[0m Fuel: {fuel_level}% | Engine: {engine_temp}°C")
        print(f" \033[1;32m[SCAN]\033[0m Battery: {battery_volt}V | Connection: {self.connection}")
        
        if engine_temp > 100:
            print("\n\033[1;41m[WARNING] ENGINE OVERHEATING DETECTED!\033[0m")
        elif fuel_level < 20:
            print("\n\033[1;33m[ADVICE] Low fuel. Calculating nearest refueling station...\033[0m")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now in sync with your \nvehicle's central unit. All mechanical vitals \nare within operational parameters. Ready to roll.\033[0m")

if __name__ == "__main__":
    sync = VehicleSync()
    sync.run_full_scan()
