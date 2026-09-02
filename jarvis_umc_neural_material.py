import time
import random

class UniversalMachineController:
    def __init__(self):
        self.steering_source = "MANUAL"
        self.surface_cleanliness = 100 # %
        self.cabin_noise_db = 60 # Decibels

    def p3423_neural_steering(self, neural_intent):
        if neural_intent:
            self.steering_source = "NEURAL_LINK"
            return "\033[1;32m[NEURAL] Intent Detected. Bypassing physical controls. Steering Synced to User Brain.\033[0m"
        return "[STATUS] Manual steering active."

    def p3424_nano_repulsion(self, mud_exposure):
        if mud_exposure:
            self.surface_cleanliness = 100
            return "\033[1;34m[SURFACE] Hydrophobic Field Active. Repelling dirt and liquid instantly.\033[0m"
        return "[STATUS] Surface integrity clean."

    def p3425_fusion_thrusters(self, hazard_detected):
        if hazard_detected:
            return "\033[1;31m[TACTICAL] Hazard Alert! Firing Pulse-Thrusters for Evasive Leap.\033[0m"
        return "[STATUS] Thrusters on standby."

    def p3426_quantum_blackbox_sync(self):
        return "\033[1;35m[DATA] Quantum-Link established. Real-time telemetry streaming to Cloud Secure-Node.\033[0m"

    def p3427_anc_system(self, outside_noise):
        self.cabin_noise_db = max(10, outside_noise - 50)
        return f"\033[1;36m[COMFORT] Active Noise Cancellation ON. Interior Noise: {self.cabin_noise_db}dB.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: NEURAL & MATERIAL MASTERY (P3423-3427)")
    print("-" * 60)
    
    print(umc.p3423_neural_steering(True))
    print(umc.p3424_nano_repulsion(True))
    print(umc.p3425_fusion_thrusters(True))
    print(umc.p3426_quantum_blackbox_sync())
    print(umc.p3427_anc_system(85))
    
    print("-" * 60)
    print("STATUS: Neural Link & Nano-Surface Protocols Operational.")
    print("-" * 60)
