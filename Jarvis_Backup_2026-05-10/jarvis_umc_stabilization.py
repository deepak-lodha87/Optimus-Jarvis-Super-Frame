import time

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.lean_angle = 0 # Degrees
        self.stabilizer_active = False

    def monitor_gyroscope(self):
        print(f"\033[1;34m[UMC-STABILITY] Reading Gyroscope & Accelerometer Data...\033[0m")
        time.sleep(1)
        # Simulating a sharp left turn with a 25-degree lean
        self.lean_angle = 25 
        return self.lean_angle

    def stabilize_chassis(self):
        angle = self.monitor_gyroscope()
        print(f"\033[1;33m[ALERT] Critical Lean Angle Detected: {angle}°\033[0m")
        time.sleep(0.8)
        
        if angle > 20:
            print("\033[1;35m[ACTION] Engaging Active Anti-Roll Bars & Hydraulic Counter-Force...\033[0m")
            self.stabilizer_active = True
            time.sleep(1)
            return "\033[1;32m[SUCCESS] Chassis Leveled. Rollover Risk Prevented.\033[0m"
        return "\033[1;34m[STATUS] Balance Stable.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Armored_Unit")
    
    print("-" * 50)
    print("   JARVIS UMC: CHASSIS STABILIZATION (P3214-15)")
    print("-" * 50)
    
    print(umc.stabilize_chassis())
    print("-" * 50)
