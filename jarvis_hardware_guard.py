import time
import random

class ResourceThrottler:
    def __init__(self):
        self.max_temp = 45 # Celsius

    def monitor_thermal(self):
        current_temp = random.randint(35, 50)
        print(f"\033[1;36m[THERMAL] Current Core Temperature: {current_temp}°C\033[0m")
        
        if current_temp > self.max_temp:
            print("\033[1;31m[WARNING] Temperature exceeding limit! Throttling CPU to 50%...\033[0m")
            time.sleep(1)
            return "THROTTLED"
        return "OPTIMAL"

class PowerManager:
    def optimize_battery(self, status):
        print("\033[1;34m[POWER] Analyzing Battery Discharge Rate...\033[0m")
        time.sleep(1.2)
        if status == "THROTTLED":
            return "\033[1;32m[ACTION] Background processes suspended to save energy.\033[0m"
        return "\033[1;32m[ACTION] Full Power available for Jarvis Core operations.\033[0m"

if __name__ == "__main__":
    guard = ResourceThrottler()
    power = PowerManager()
    
    print("-" * 50)
    print("   JARVIS HARDWARE GUARD & POWER LOGIC (P3121-22)")
    print("-" * 50)
    
    thermal_status = guard.monitor_thermal()
    print(power.optimize_battery(thermal_status))
    print("-" * 50)
