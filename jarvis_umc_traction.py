import time
import random

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.wheel_speeds = [0, 0, 0, 0] # RPM for 4 wheels

    def monitor_traction(self):
        print(f"\033[1;34m[UMC-TRACTION] Analyzing Wheel Speed Sensors...\033[0m")
        time.sleep(1)
        # Simulating one wheel slipping in mud
        self.wheel_speeds = [1200, 1200, 3500, 1200] 
        return self.wheel_speeds

    def apply_torque_vectoring(self):
        speeds = self.monitor_traction()
        print(f"\033[1;33m[ALERT] Wheel Spin Detected on Rear-Right Wheel ({speeds[2]} RPM)!\033[0m")
        time.sleep(0.8)
        
        # Unique Logic: Shifting Torque from slipping wheel to gripping wheels
        print("\033[1;35m[LOGIC] Activating Differential Lock & Torque Transfer...\033[0m")
        time.sleep(1)
        
        corrected_speeds = [1350, 1350, 1350, 1350]
        return f"\033[1;32m[SUCCESS] Traction Regained. Power redistributed to all wheels.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Offroader")
    
    print("-" * 50)
    print("   JARVIS UMC: TRACTION & TORQUE VECTORING (P3212-13)")
    print("-" * 50)
    
    print(umc.apply_torque_vectoring())
    print("-" * 50)
