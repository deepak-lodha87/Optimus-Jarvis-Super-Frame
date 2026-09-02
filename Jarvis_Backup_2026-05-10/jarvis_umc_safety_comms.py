import time

class UniversalMachineController:
    def __init__(self):
        self.cabin_pressure = 101.3 # Standard kPa
        self.encryption_key = "QUANTUM_LOCKED_3361"

    def p3358_pressure_regulator(self, ext_pressure):
        if ext_pressure < 80:
            self.cabin_pressure = 101.3
            return "\033[1;32m[ENVIRONMENT] Low External Pressure. Pressurizing Cabin for User Comfort.\033[0m"
        return "[STATUS] External pressure stable."

    def p3359_sleep_monitor(self, brain_wave):
        if brain_wave == "REM":
            return "\033[1;34m[NEURAL] User in Deep Sleep. Switching Machine to Low-Noise Ghost Mode.\033[0m"
        return "[NEURAL] User Awake. Monitoring focus levels."

    def p3360_mag_parachute(self, fall_velocity):
        if fall_velocity > 50:
            return "\033[1;31m[SAFETY] Rapid Descent! Engaging Magnetic Drag Parachute.\033[0m"
        return "[SAFETY] Descent rate normal."

    def p3361_quantum_encrypt(self):
        return f"\033[1;35m[SECURITY] Signal Encrypted via {self.encryption_key}. Anti-Interception Active.\033[0m"

    def p3362_heat_dissipation(self):
        return "\033[1;33m[THERMAL] Dissipating Kinetic Friction Heat via Nano-Cooling Ribs.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SAFETY & COMMS BUNDLE (P3358-3362)")
    print("-" * 60)
    
    print(umc.p3358_pressure_regulator(70))
    print(umc.p3359_sleep_monitor("REM"))
    print(umc.p3360_mag_parachute(65))
    print(umc.p3361_quantum_encrypt())
    print(umc.p3362_heat_dissipation())
    
    print("-" * 60)
    print("STATUS: Quantum Encryption & Cabin Safety Operational.")
    print("-" * 60)
