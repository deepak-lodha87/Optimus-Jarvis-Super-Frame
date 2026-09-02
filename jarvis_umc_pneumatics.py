import time
import random

class UniversalMachineController:
    def __init__(self, machine_type):
        self.machine = machine_type
        self.tank_pressure = 120  # PSI (Pounds per square inch)
        self.actuator_position = 0 # 0 to 100% open/closed

    def monitor_pressure_vessel(self):
        """Phase 3231: Checking compressed air reserves"""
        print(f"\033[1;34m[PNEUMATIC] Monitoring Tank Pressure for {self.machine}...\033[0m")
        time.sleep(0.8)
        if self.tank_pressure < 90:
            print("\033[1;33m[REFILL] Activating On-Board Compressor...\033[0m")
            self.tank_pressure += 30
        return f"Current Pressure: {self.tank_pressure} PSI"

    def fire_pneumatic_actuator(self, target_position):
        """Phase 3232: Rapid movement using high-pressure air"""
        if self.tank_pressure < 40:
            return "\033[1;31m[FAIL] Insufficient Air Pressure for Rapid Move.\033[0m"
        
        print(f"\033[1;35m[RAPID] Releasing Solenoid Valve. Target: {target_position}%...\033[0m")
        # Pneumatic movement is nearly instant
        time.sleep(0.2) 
        self.actuator_position = target_position
        self.tank_pressure -= 15 # Air consumption
        return f"\033[1;32m[SUCCESS] Actuator Deployed to {target_position}% in 0.18s.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Tactical_Fighter_Drone")
    
    print("-" * 60)
    print("   JARVIS UMC: PNEUMATIC ACTUATOR OVERDRIVE (P3231-32)")
    print("-" * 60)
    
    print(umc.monitor_pressure_vessel())
    # Executing multiple rapid moves
    print("\n" + umc.fire_pneumatic_actuator(100)) # Emergency flap/brake deployment
    print(umc.fire_pneumatic_actuator(0))   # Rapid retract
    print("-" * 60)
