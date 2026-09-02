import time
import random

class PredictiveMaintenance:
    def __init__(self):
        self.components = ["Engine Oil", "Brake Pads", "Battery Health", "Tire Pressure"]

    def forecast_health(self):
        print("\033[1;34m[PREDICTION] Analyzing historical data patterns...\033[0m")
        time.sleep(1)
        target = random.choice(self.components)
        wear_tear = random.randint(60, 95)
        
        print(f"  • Component: {target}")
        print(f"  • Predicted Wear: {wear_tear}%")
        
        if wear_tear > 80:
            return f"\033[1;31m[ADVICE] High probability of failure in 500km. Replace {target} soon.\033[0m"
        return f"\033[1;32m[OK] {target} is stable for now.\033[0m"

class SelfCorrection:
    def check_errors(self):
        print("\033[1;35m[SELF-REPAIR] Scanning Jarvis source code for logic gaps...\033[0m")
        time.sleep(1.2)
        # Simulating a self-fix
        return "\033[1;32m[FIXED] Minor syntax lag detected in P3071. Optimization applied.\033[0m"

if __name__ == "__main__":
    pm = PredictiveMaintenance()
    sc = SelfCorrection()
    
    print("-" * 50)
    print("   JARVIS SMART LOGIC: PREDICTION & REPAIR")
    print("-" * 50)
    
    print(pm.forecast_health())
    print("\n" + sc.check_errors())
    print("-" * 50)
