import time
import math

class UniversalMachineController:
    def __init__(self, cargo_type):
        self.cargo = cargo_type
        self.current_tilt = 0.0  # Degrees
        self.gimbal_correction = 0.0

    def read_gyro_sensor(self, machine_lean):
        """Phase 3235: Sensing the machine's angle relative to gravity"""
        self.current_tilt = machine_lean
        print(f"\033[1;34m[GYRO] Machine Lean Detected: {self.current_tilt}°\033[0m")
        return self.current_tilt

    def apply_auto_leveling(self, machine_lean):
        """Phase 3236: Counter-balancing the tilt using high-speed servos"""
        lean = self.read_gyro_sensor(machine_lean)
        
        # Unique Logic: Mirroring the angle to stay level
        self.gimbal_correction = -lean 
        
        print("\033[1;33m[STABILIZING] Activating Servo Motors for Counter-Tilt...\033[0m")
        time.sleep(0.5)
        
        net_angle = lean + self.gimbal_correction
        return f"\033[1;32m[SUCCESS] {self.cargo} is Level. Net Tilt: {net_angle}° (Perfectly Flat)\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Precision_LiDAR_Sensor")
    
    print("-" * 60)
    print("   JARVIS UMC: GYROSCOPIC AUTO-LEVELING (P3235-36)")
    print("-" * 60)
    
    # Simulation: Machine leans 25 degrees left on a curve
    print(umc.apply_auto_leveling(25.5))
    print("-" * 60)
