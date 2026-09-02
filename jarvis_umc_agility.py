import time
import random

class UniversalMachineController:
    def __init__(self):
        self.rear_steer_angle = 0
        self.neural_latency = 0.001 # Seconds
        self.drs_active = False

    def p3438_rear_steering(self, turn_radius):
        if turn_radius < 5:
            self.rear_steer_angle = 5
            return "\033[1;32m[HANDLING] Tight Turn! Activating Rear-Wheel Counter-Steer for Maximum Agility.\033[0m"
        return "[STATUS] Standard steering active."

    def p3439_friction_kill(self):
        return "\033[1;34m[MATERIAL] Molecular Lubricant Dispersed. Friction levels dropped to 0.00001%.\033[0m"

    def p3440_neural_overclock(self):
        self.neural_latency = 0.0005
        return f"\033[1;35m[NEURAL] Link Overclocked. Response Time reduced to {self.neural_latency}s. Pure Instinct Drive.\033[0m"

    def p3441_drs_activation(self, speed):
        if speed > 180:
            self.drs_active = True
            return "\033[1;33m[AERO] High Speed Detected. Opening DRS Wing for Drag Reduction.\033[0m"
        return "[STATUS] High Downforce mode active."

    def p3442_heat_storage(self, core_temp):
        if core_temp > 90:
            return "\033[1;36m[ENERGY] Excess Heat Captured. Charging Liquid-Salt Storage for Auxiliary Power.\033[0m"
        return "[STATUS] Thermal levels normal."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: AGILITY & NEURAL SPEED (P3438-3442)")
    print("-" * 60)
    
    print(umc.p3438_rear_steering(3))
    print(umc.p3439_friction_kill())
    print(umc.p3440_neural_overclock())
    print(umc.p3441_drs_activation(200))
    print(umc.p3442_heat_storage(95))
    
    print("-" * 60)
    print("STATUS: Agility Matrix & Neural Sync Optimized.")
    print("-" * 60)
