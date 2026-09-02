import time
import random

class UniversalMachineController:
    def __init__(self):
        self.collision_threat = False
        self.auth_status = "LOCKED"

    def p3363_particle_scan(self):
        density = random.uniform(0.1, 10.0)
        return f"\033[1;36m[SCANNER] Sub-Atomic Density: {density:.2f}. Material identified as Carbon-Fiber Composite.\033[0m"

    def p3364_collision_avoidance(self, object_dist):
        if object_dist < 5:
            self.collision_threat = True
            return "\033[1;31m[AUTO-PILOT] Collision Imminent! Calculating Evasive Maneuver in 0.002s...\033[0m"
        return "[AUTO-PILOT] Path clear."

    def p3365_gait_auth(self, walk_pattern):
        if walk_pattern == "DEEPAK_SIGNATURE":
            self.auth_status = "UNLOCKED"
            return "\033[1;32m[AUTH] Gait Analysis Confirmed. Identity: Deepak. Welcome back.\033[0m"
        return "[DENIED] Unknown pattern detected."

    def p3366_thruster_balance(self):
        return "\033[1;34m[AERO] Activating Nano-Thrusters for Micro-Stability Adjustments.\033[0m"

    def p3367_protocol_translator(self):
        return "\033[1;35m[COMMS] Handshake Established with External Satellite. Translating Protocol: X-10.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: AUTONOMOUS CONTROL BUNDLE (P3363-3367)")
    print("-" * 60)
    
    print(umc.p3363_particle_scan())
    print(umc.p3365_gait_auth("DEEPAK_SIGNATURE"))
    print(umc.p3364_collision_avoidance(3))
    print(umc.p3366_thruster_balance())
    print(umc.p3367_protocol_translator())
    
    print("-" * 60)
    print("STATUS: Autonomous Decision Matrix Operational.")
    print("-" * 60)
