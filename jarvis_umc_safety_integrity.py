import time
import random

class UniversalMachineController:
    def __init__(self):
        self.fire_safety = "SECURE"
        self.hull_hardness = "STANDARD"
        self.memory_sync = 0 # %

    def p3448_fire_suppressor(self, heat_spike):
        if heat_spike > 200:
            self.fire_safety = "EXTINGUISHING"
            return "\033[1;31m[EMERGENCY] Fire Detected! Releasing Halon-Substitute Gas. Oxygen Displaced.\033[0m"
        return "[STATUS] Thermal sensors stable."

    def p3449_atomic_welding(self):
        return "\033[1;34m[REPAIR] Scanning for Micro-Fissures. Atomic Welding Beam Active. Structure Restored.\033[0m"

    def p3450_memory_backup(self):
        self.memory_sync = 100
        return "\033[1;32m[DATA] Neural Memory Stream Encrypted. 128-bit Satellite Backup Complete.\033[0m"

    def p3451_hull_electrification(self, combat_mode):
        if combat_mode:
            self.hull_hardness = "MAXIMUM"
            return "\033[1;35m[ARMOR] Hull Electrified. Molecular Tension increased. Defense: Level 10.\033[0m"
        return "[STATUS] Passive armor active."

    def p3452_gravity_brake(self, stop_distance):
        if stop_distance < 10:
            return "\033[1;33m[SAFETY] Emergency Stop! Engaging Magnetic Ground-Anchor. Deceleration: MAX.\033[0m"
        return "[STATUS] Braking system optimal."

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: SAFETY & INTEGRITY (P3448-3452)")
    print("-" * 60)
    
    print(umc.p3448_fire_suppressor(250))
    print(umc.p3449_atomic_welding())
    print(umc.p3450_memory_backup())
    print(umc.p3451_hull_electrification(True))
    print(umc.p3452_gravity_brake(5))
    
    print("-" * 60)
    print("STATUS: Structural Reinforcement & Safety Protocols Synced.")
    print("-" * 60)
