import time
import random

class UniversalMachineController:
    def __init__(self):
        self.auth_status = "LOCKED"
        self.suspension_height = 150 # mm
        self.threat_level = 0 # %

    def p3478_biometric_lock(self, user_id):
        if user_id == "DEEPAK":
            self.auth_status = "UNLOCKED"
            return "\033[1;32m[ACCESS] Identity Verified: Deepak. System Core Online.\033[0m"
        return "\033[1;31m[DENIED] Unknown User. Ignition Disabled.\033[0m"

    def p3479_terrain_adapt(self, surface):
        if surface == "OFFROAD":
            self.suspension_height = 250
            return "\033[1;34m[MECHANICAL] Rough Terrain! Increasing Suspension Travel by 100mm.\033[0m"
        return "[STATUS] Road surface smooth. Standard height maintained."

    def p3480_predictive_safety(self, object_speed):
        if object_speed > 100:
            self.threat_level = 85
            return "\033[1;33m[AI] Predictive Alert! High-speed collision path detected. Readying Airbags.\033[0m"
        return "[STATUS] Environment scan: Safe."

    def p3481_suit_thermal_sync(self):
        return "\033[1;36m[BIO] Liquid-Cooling Suit Sync Active. Pilot Core Temp: 37°C.\033[0m"

    def p3482_command_buffer(self):
        return "\033[1;35m[DATA] Neural Buffer Active. Zero command loss during signal fluctuations.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: INTELLIGENCE & TERRAIN (P3478-3482)")
    print("-" * 60)
    
    print(umc.p3478_biometric_lock("DEEPAK"))
    print(umc.p3479_terrain_adapt("OFFROAD"))
    print(umc.p3480_predictive_safety(120))
    print(umc.p3481_suit_thermal_sync())
    print(umc.p3482_command_buffer())
    
    print("-" * 60)
    print("STATUS: Intelligence Grid & Thermal Sync Operational.")
    print("-" * 60)
