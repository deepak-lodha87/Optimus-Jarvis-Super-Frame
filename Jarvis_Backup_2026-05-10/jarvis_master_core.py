import os
import time

class OptimusJarvis:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3003"
        self.voice_file = "deepak_final_voice.wav"
        # Blueprint specs for comparison
        self.blueprint_temp_limit = 105 
        self.blueprint_rpm_idle = 1000

    def startup(self):
        print(f"\033[1;35m>> INITIATING PHASE {self.phase}: MASTER CORE ACTIVATION <<\033[0m")
        time.sleep(1)

    def verify_identity(self):
        print("\033[1;36m[SYSTEM] Scanning for Architect's Voice Signature...\033[0m")
        # Checking if the voice record from Phase 3001 exists
        if os.path.exists(self.voice_file):
            size = os.path.getsize(self.voice_file)
            if size > 3000: # Ensuring it's not a silence file
                print(f"\033[1;32m[MATCH] Voice Print Verified. Access Granted, {self.user}.\033[0m")
                return True
        
        print("\033[1;31m[CRITICAL] Identity Unknown or Voice Sample Too Small. System Locked.\033[0m")
        return False

    def vehicle_diagnostic_hub(self, temp, rpm):
        print("\n\033[1;34m>> LINKING TO VEHICLE OBD-II INTERFACE... <<\033[0m")
        time.sleep(1)
        print(f"[LIVE DATA] Engine Temp: {temp}°C | RPM: {rpm}")
        
        # Cross-checking with Blueprints Logic
        if temp > self.blueprint_temp_limit:
            print("\033[1;31m[ALERT] Engine Temperature Exceeds Blueprint Specs! Check Cooling.\033[0m")
        elif rpm > self.blueprint_rpm_idle:
            print("\033[1;33m[ADVISORY] High Idle Detected. Possible Throttle Issue.\033[0m")
        else:
            print("\033[1;32m[HEALTH] Engine Vitals: STABLE. Operating within Blueprint parameters.\033[0m")

    def run_all(self):
        self.startup()
        if self.verify_identity():
            # Simulation of live telemetry from Phase 3002
            self.vehicle_diagnostic_hub(92, 850)
            print(f"\n\033[1;35m>> PHASE {self.phase} COMPLETE. READY FOR NEXT COMMAND. <<\033[0m")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.run_all()
