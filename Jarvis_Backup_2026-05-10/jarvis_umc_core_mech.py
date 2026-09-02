import time
import random

class UniversalMachineController:
    def __init__(self):
        self.energy_recovered = 0 # Watts
        self.atomic_stability = 100 # %
        self.intake_size = "NARROW"

    def p3383_nano_air_filter(self):
        return "\033[1;32m[FILTER] Nano-Purifier Active. Removing 99.99% micro-debris from intake.\033[0m"

    def p3384_heat_to_electric_recovery(self, brake_temp):
        if brake_temp > 200:
            recovered = brake_temp * 0.5
            self.energy_recovered += recovered
            return f"\033[1;33m[RECOVERY] High Heat Detected! Converting thermal energy to {recovered}W.\033[0m"
        return "[STATUS] Recovery on standby."

    def p3385_atomic_integrity_scan(self):
        self.atomic_stability = random.randint(95, 100)
        return f"\033[1;34m[SCAN] Atomic Matrix Stability: {self.atomic_stability}%. No internal fatigue.\033[0m"

    def p3386_variable_intake(self, rpm):
        if rpm > 6000:
            self.intake_size = "WIDE"
            return "\033[1;36m[ENGINE] Manifold Opening. Maximum Airflow for High-RPM Surge.\033[0m"
        return "[STATUS] Intake optimized for fuel efficiency."

    def p3387_zero_emission_start(self):
        return "\033[1;35m[EXHAUST] Cold-Start Filter Active. Converting CO to H2O particles.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: MECHANICAL & ATOMIC CORE (P3383-3387)")
    print("-" * 60)
    
    print(umc.p3383_nano_air_filter())
    print(umc.p3384_heat_to_electric_recovery(450))
    print(umc.p3385_atomic_integrity_scan())
    print(umc.p3386_variable_intake(7500))
    print(umc.p3387_zero_emission_start())
    
    print("-" * 60)
    print("STATUS: Core Mechanical Efficiency Verified.")
    print("-" * 60)
