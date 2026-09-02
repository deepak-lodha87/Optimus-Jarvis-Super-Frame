import time
import random

class HardwareMonitor:
    def __init__(self):
        self.device = "Oppo Reno 12 Pro 5G"
        self.temp_threshold = 45 # Celsius

    def check_vitals(self):
        # Simulating hardware data
        cpu_usage = random.randint(20, 85)
        ram_free = random.randint(500, 4000) # MB
        temp = random.randint(30, 50)
        
        print(f"\033[1;36m[MONITOR] Scanning {self.device} Vitals...\033[0m")
        time.sleep(1)
        
        print(f"  • CPU Usage: {cpu_usage}%")
        print(f"  • Available RAM: {ram_free} MB")
        print(f"  • Core Temp: {temp}°C")
        
        if temp > self.temp_threshold:
            print(f"\033[1;31m[CRITICAL] Thermal Throttling Active! Cool down required.\033[0m")
        else:
            print(f"\033[1;32m[STABLE] Hardware operating within safe limits.\033[0m")

if __name__ == "__main__":
    monitor = HardwareMonitor()
    print("-" * 50)
    print("   JARVIS HARDWARE HEALTH INTERFACE")
    print("-" * 50)
    monitor.check_vitals()
