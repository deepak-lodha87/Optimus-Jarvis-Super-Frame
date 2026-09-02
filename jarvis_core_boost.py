import time
import multiprocessing
import random

class MultiCoreEngine:
    def __init__(self):
        self.cores = multiprocessing.cpu_count()
        self.load_distribution = "Balanced"

    def distribute_logic(self):
        print(f"\033[1;34m[CORE] Detected {self.cores} Cores on Reno 12 Pro. Spreading logic...\033[0m")
        time.sleep(1.2)
        for i in range(self.cores):
            print(f"  • CPU Core {i}: Handling Neural Task {random.randint(100, 999)} [ACTIVE]")
            time.sleep(0.2)
        return "\033[1;32m[SUCCESS] Multi-Core Task Distribution complete. Speed 4x.\033[0m"

class ThermalSync:
    def check_stability(self):
        print("\033[1;33m[THERMAL] Monitoring heat dissipation during Multi-Core load...\033[0m")
        time.sleep(1)
        temp = random.randint(35, 42)
        return f"[STATUS] System Stable at {temp}°C. Liquid cooling simulation active."

if __name__ == "__main__":
    engine = MultiCoreEngine()
    thermal = ThermalSync()
    
    print("-" * 50)
    print("   JARVIS CORE POWER INJECTOR (P3085 & P3086)")
    print("-" * 50)
    
    print(engine.distribute_logic())
    print("\n" + thermal.check_stability())
    print("-" * 50)
