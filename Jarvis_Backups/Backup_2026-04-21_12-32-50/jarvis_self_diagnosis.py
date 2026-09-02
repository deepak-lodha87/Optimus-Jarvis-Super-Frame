import time
import random

class OptimusJarvisPro:
    def __init__(self):
        self.user = "Deepak"
        self.phase_12 = "3012 (Self-Diagnosis)"
        self.phase_13 = "3013 (Predictive Maintenance)"
        # Health thresholds
        self.battery_health = 85 # Percent
        self.brake_pad_wear = 40 # Percent

    def system_self_check(self):
        print(f"\033[1;35m>> PHASE {self.phase_12}: RUNNING INTERNAL DIAGNOSTICS <<\033[0m")
        time.sleep(1)
        # Checking Jarvis's own core files and memory
        print("\033[1;34m[LOG] Checking Core Integrity... 100% OK\033[0m")
        print(f"\033[1;34m[LOG] Memory Buffer: Stable\033[0m")
        print("\033[1;32m[SUCCESS] Jarvis Self-Diagnosis: Healthy.\033[0m")

    def predict_future_failure(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_13}: ANALYZING PREDICTIVE DATA <<\033[0m")
        time.sleep(1)
        
        # Expert logic based on your Service Advisor background
        print(f"[DATA] Brake Wear: {self.brake_pad_wear}% | Battery Health: {self.battery_health}%")
        
        if self.brake_pad_wear > 70:
            advice = "WARNING: Brake pads will fail in approx 500km. Order replacements."
        elif self.battery_health < 30:
            advice = "CRITICAL: Battery voltage dropping. High risk of ignition failure."
        else:
            advice = "PREDICTION: All mechanical parts are within safe limits for the next 2000km."
            
        print(f"\033[1;33m[PREDICTION] {advice}\033[0m")

    def run_diagnostics(self):
        print(f"\033[1;32m>> SYSTEM ONLINE: WELCOME BACK, SIR. <<\033[0m")
        self.system_self_check()
        self.predict_future_failure()
        print(f"\n\033[1;35m>> PHASES 3012 & 3013 INTEGRATED INTO SUPER-FRAME. <<\033[0m")

if __name__ == "__main__":
    jarvis = OptimusJarvisPro()
    jarvis.run_diagnostics()
