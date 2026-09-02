import os
import time

class OptimusJarvis:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3004"
        self.voice_file = "deepak_final_voice.wav"
        # Blueprint Thresholds
        self.max_temp = 105
        self.idle_rpm = 1000

    def system_boot(self):
        print(f"\033[1;35m>> INITIATING PHASE {self.phase}: MASTER UNIFIED CORE <<\033[0m")
        time.sleep(1)
        print("\033[1;34m[LOG] Synchronizing Security and Engineering Modules...\033[0m")

    def security_check(self):
        print("\n\033[1;36m>> STEP 1: BIOMETRIC VOICE VERIFICATION <<\033[0m")
        if os.path.exists(self.voice_file):
            size = os.path.getsize(self.voice_file)
            if size > 3000:
                print(f"\033[1;32m[MATCH] Voice Signature Verified. Identity: {self.user}\033[0m")
                return True
        print("\033[1;31m[DENIED] Voice Signature Missing or Invalid. Access Revoked.\033[0m")
        return False

    def vehicle_check(self, temp, rpm):
        print("\n\033[1;36m>> STEP 2: REAL-TIME VEHICLE TELEMETRY <<\033[0m")
        time.sleep(1)
        print(f"[DATA] Engine Temperature: {temp}°C | RPM: {rpm}")
        
        # Cross-Comparison with Blueprints
        if temp > self.max_temp:
            print("\033[1;31m[CRITICAL] Engine Overheating! Check Cooling System Immediately.\033[0m")
        elif rpm > self.idle_rpm:
            print("\033[1;33m[ADVISORY] High RPM detected. Blueprint specifies 800-900 for idle.\033[0m")
        else:
            print("\033[1;32m[HEALTH] All Vitals Stable. Gadi Ready Hai, Sir.\033[0m")

    def execute(self):
        self.system_boot()
        if self.security_check():
            # Simulated data from your OBD-II success earlier
            self.vehicle_check(temp=92, rpm=850)
            print(f"\n\033[1;35m>> PHASE {self.phase} COMPLETE: MASTER CORE STANDING BY. <<\033[0m")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.execute()
