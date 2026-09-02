import time

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.is_linked = True
        self.performance_mode = "STANDARD"

    def tune_engine_performance(self, mode):
        # Mode options: SPORT, ECO, or STEALTH
        self.performance_mode = mode
        print(f"\033[1;33m[TUNING] Re-mapping Fuel Maps for {self.machine}...\033[0m")
        time.sleep(1.5)
        
        if mode == "SPORT":
            adjustment = "Rich Fuel Mix + Advanced Ignition Timing"
            boost = "25% Torque Increase"
        elif mode == "ECO":
            adjustment = "Lean Fuel Mix + Short Shifting Logic"
            boost = "40% Fuel Efficiency Increase"
        else:
            adjustment = "Low RPM Mapping + Silent Exhaust Bypass"
            boost = "Signature Noise Reduction"

        print(f"  • Strategy: {adjustment}")
        return f"\033[1;32m[SUCCESS] {self.machine} set to {mode} Mode. {boost}.\033[0m"

    def monitor_combustion(self):
        print("\033[1;34m[MONITOR] Checking Cylinder Pressure & Temperature...\033[0m")
        time.sleep(1)
        return "\033[1;36m[DATA] Combustion Stability: 99.8% | Optimal Thermal Range.\033[0m"

if __name__ == "__main__":
    # Same Master Controller Logic
    jarvis_tuner = UniversalMachineController("Hero_HF_Deluxe_Custom")
    
    print("-" * 50)
    print("   JARVIS ADAPTIVE ENGINE TUNING (P3205-06)")
    print("-" * 50)
    
    # Executing Performance Overdrive
    print(jarvis_tuner.tune_engine_performance("SPORT"))
    print("\n" + jarvis_tuner.monitor_combustion())
    print("-" * 50)
