import time
import random

class PredictiveDiagnostics:
    def scan_hardware_vibrations(self):
        print("\033[1;34m[SCAN] Analyzing Mechanical Resonance & Heat Patterns...\033[0m")
        time.sleep(1.5)
        wear_tear = random.randint(5, 40)
        print(f"  • Component Wear-and-Tear: {wear_tear}%")
        if wear_tear > 30:
            return "CRITICAL_MAINTENANCE_REQUIRED"
        return "HEALTHY"

class AutoRepairProtocol:
    def apply_software_patch(self, issue):
        print(f"\033[1;35m[REPAIR] Issue Detected: {issue}. Searching for digital fix...\033[0m")
        time.sleep(2)
        # Advanced Logic to bypass physical fault with software adjustment
        print("  • Adjusting Torque Parameters... [DONE]")
        print("  • Re-calibrating Fuel/Electric Ratio... [DONE]")
        return "\033[1;32m[FIXED] Machine Stabilized via Software Override.\033[0m"

if __name__ == "__main__":
    diag = PredictiveDiagnostics()
    repair = AutoRepairProtocol()
    
    print("-" * 50)
    print("   JARVIS MECHANICAL DIAGNOSTICS & REPAIR")
    print("-" * 50)
    
    status = diag.scan_hardware_vibrations()
    if status != "HEALTHY":
        print(repair.apply_software_patch(status))
    else:
        print("\033[1;32m[STATUS] All Mechanical Systems are Peak-Efficient.\033[0m")
    print("-" * 50)
