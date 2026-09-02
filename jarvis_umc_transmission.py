import time

class UniversalMachineController:
    def __init__(self, machine_type):
        self.machine = machine_type
        self.current_gear = 0
        self.rpm = 0

    def sync_transmission(self):
        print(f"\033[1;34m[UMC-GEAR] Interfacing with {self.machine} Gearbox-Actuators...\033[0m")
        time.sleep(1.2)
        print("  • Bypassing Manual Clutch Override... [OK]")
        return "\033[1;32m[READY] Transmission is now under Jarvis Logic Control.\033[0m"

    def shift_logic(self, speed, incline):
        print(f"\033[1;33m[LOGIC] Analyzing Speed ({speed}km/h) & Incline ({incline}°)...\033[0m")
        time.sleep(0.8)
        
        # Unique Logic for Gear Selection
        if incline > 15: # Climbing a hill
            self.current_gear = 2
            action = "Downshifting for Maximum Torque"
        elif speed > 100:
            self.current_gear = 5
            action = "Upshifting for High-Speed Stability"
        else:
            self.current_gear = 3
            action = "Cruising Gear Active"
            
        return f"\033[1;32m[ACTION] {action}. Current Gear: {self.current_gear}\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Military_Grade_UAV")
    
    print("-" * 50)
    print("   JARVIS UMC: TRANSMISSION & GEAR LOGIC (P3207)")
    print("-" * 50)
    
    print(umc.sync_transmission())
    print("\n" + umc.shift_logic(120, 5)) # High speed, low incline
    print(umc.shift_logic(30, 20))  # Low speed, steep hill
    print("-" * 50)
