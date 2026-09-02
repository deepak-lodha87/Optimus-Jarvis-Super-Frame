import time
import threading

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.core_temp = 85.0  # Celsius
        self.cryo_status = "READY"
        self.is_active = True

    def thermal_scanner_thread(self):
        """Advanced Background Monitor: Milisecond Scanning"""
        while self.is_active:
            # Simulated heat buildup during high-speed operation
            if self.core_temp > 105:
                self.deploy_cryo_surge()
            time.sleep(0.5)

    def deploy_cryo_surge(self):
        print(f"\n\033[1;31m[CRITICAL] Thermal Threshold Breached: {self.core_temp}°C\033[0m")
        print("\033[1;35m[ACTION] Injecting Cryogenic Coolant Mist (Liquid Nitrogen Based)...\033[0m")
        time.sleep(1.2)
        self.core_temp -= 25.5
        print(f"\033[1;32m[SUCCESS] Temperature Stabilized: {self.core_temp}°C. Engine Safe.\033[0m")

    def high_performance_run(self):
        print(f"--- {self.machine} HIGH-STRESS TEST START ---")
        for i in range(5):
            self.core_temp += 10
            print(f"System Load: {20*(i+1)}% | Current Temp: {self.core_temp}°C")
            time.sleep(0.8)
        self.is_active = False

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Core_Turbine")
    
    print("-" * 60)
    print("   JARVIS UMC: ADVANCED THERMAL SHIELDING (P3218-19)")
    print("-" * 60)
    
    # Start background thermal thread
    scanner = threading.Thread(target=umc.thermal_scanner_thread)
    scanner.start()
    
    # Run the machine test
    umc.high_performance_run()
    scanner.join()
    print("-" * 60)
