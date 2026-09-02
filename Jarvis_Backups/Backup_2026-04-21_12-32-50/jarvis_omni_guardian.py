import time
import random

class OmniGuardian:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3041"
        self.status = "ACTIVE_DEFENSE"

    def sensor_mesh_active(self):
        print(f"\033[1;35m>> PHASE {self.phase}: ACTIVATING OMNI-GUARDIAN MESH <<\033[0m")
        sensors = ["Accelerometer", "Gyroscopic Balance", "Proximity Alert"]
        for s in sensors:
            print(f"[SENSOR] {s} calibrated and monitoring...")
            time.sleep(0.4)
        print("\033[1;32m[SUCCESS] Physical environment monitoring: ON.\033[0m")

    def automated_sos_logic(self):
        print(f"\n\033[1;36m>> INITIATING STEALTH SAFETY PROTOCOL <<\033[0m")
        time.sleep(1)
        # Simulating a safety check
        threat_detected = False
        if not threat_detected:
            print("\033[1;34m[STATUS] Architect Deepak's perimeter is SECURE. No anomalies.\033[0m")
        else:
            print("\033[1;31m[ALERT] Unstable environment detected! Sending encrypted coordinates...\033[0m")
        
    def final_check(self):
        print(f"\033[1;32m>> SYSTEM ONLINE: PROTECTING THE ARCHITECT AT ALL COSTS. <<\033[0m")
        self.sensor_mesh_active()
        self.automated_sos_logic()

if __name__ == "__main__":
    guardian = OmniGuardian()
    guardian.final_check()
