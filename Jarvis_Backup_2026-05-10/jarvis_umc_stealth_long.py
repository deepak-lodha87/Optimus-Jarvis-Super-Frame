import time
import random

class UniversalMachineController:
    def __init__(self):
        self.body_color = "METALLIC_SILVER"
        self.hull_integrity = 100 # %
        self.coolant_flow = "NORMAL"

    def p3333_chameleon_paint(self, environment):
        colors = {"FOREST": "DEEP_GREEN", "DESERT": "SAND_BROWN", "URBAN": "CONCRETE_GREY"}
        self.body_color = colors.get(environment, "MATTE_BLACK")
        return f"\033[1;32m[STEALTH] Environment Scanned: {environment}. Adaptive Paint set to {self.body_color}.\033[0m"

    def p3334_engine_wear_prediction(self):
        failure_prob = random.uniform(0.1, 5.0)
        return f"\033[1;33m[AI-SCAN] Predictive Analysis: Component failure probability {failure_prob:.2f}% in next 500km.\033[0m"

    def p3335_hull_breach_seal(self):
        print("\033[1;31m[REPAIR] Micro-Breach detected in outer shell! Deploying Nano-Sealant...\033[0m")
        time.sleep(0.8)
        self.hull_integrity = 100
        return "[SUCCESS] Breach Sealed. Structural pressure stabilized."

    def p3336_mag_locks(self, auth_key):
        if auth_key == "DEEPAK_3336":
            return "\033[1;34m[ACCESS] Magnetic Field Reversed. Doors Unlocked.\033[0m"
        return "[SECURE] Magnetic Deadbolt Active. Entry Denied."

    def p3337_coolant_overdrive(self, current_temp):
        if current_temp > 105:
            self.coolant_flow = "MAX_FLUSH"
            return "\033[1;36m[THERMAL] Engine Heat Spike! Coolant Flow at 40L/min.\033[0m"
        return "[STATUS] Thermal levels within safety limits."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: STEALTH & LONGEVITY BUNDLE (P3333-3337)")
    print("-" * 60)
    
    print(umc.p3333_chameleon_paint("FOREST"))
    print(umc.p3334_engine_wear_prediction())
    print(umc.p3335_hull_breach_seal())
    print(umc.p3336_mag_locks("DEEPAK_3336"))
    print(umc.p3337_coolant_overdrive(110))
    
    print("-" * 60)
    print("STATUS: Ghost-Mode Active. Engine Lifecycle Extended.")
    print("-" * 60)
