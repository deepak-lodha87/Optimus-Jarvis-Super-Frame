import time
import random

class UniversalMachineController:
    def __init__(self, machine_name):
        self.machine = machine_name
        self.shield_integrity = 100 # Percentage
        self.active_frequency = 433.0 # MHz

    def detect_interference(self):
        # Simulating an external electronic attack
        interference_level = random.randint(0, 100)
        print(f"\033[1;34m[SCAN] Monitoring RF Spectrum for Interference...\033[0m")
        time.sleep(1)
        return interference_level

    def activate_emp_hardening(self):
        level = self.detect_interference()
        if level > 70:
            print(f"\033[1;31m[CRITICAL] High-Intensity Pulse Detected! Level: {level}%\033[0m")
            print("\033[1;35m[ACTION] Engaging Faraday-Cage Logic & Frequency Hopping...\033[0m")
            time.sleep(1.2)
            # Frequency Hopping: Changing signal to bypass jammer
            self.active_frequency = random.uniform(800, 900)
            self.shield_integrity -= 2 # Minor wear after attack
            return f"\033[1;32m[SUCCESS] Attack Neutralized. New Frequency: {self.active_frequency:.2f} MHz.\033[0m"
        return "\033[1;34m[STATUS] Signal Clean. Shield Integrity: 100%.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Shield_Unit")
    
    print("-" * 60)
    print("   JARVIS UMC: EMP HARDENING & JAMMER DEFIANCE (P3225-26)")
    print("-" * 60)
    
    # Testing the shield twice
    for _ in range(2):
        print(umc.activate_emp_hardening())
        print("-" * 30)
    print("-" * 60)
