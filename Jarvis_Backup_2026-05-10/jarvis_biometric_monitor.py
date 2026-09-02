import time
import random

class BiometricMonitor:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3044 (Biometric Vitality)"
        self.status = "MONITORING"

    def scan_vitals(self):
        print(f"\033[1;35m>> PHASE {self.phase}: SCANNING ARCHITECT'S VITALS <<\033[0m")
        time.sleep(1)
        # Simulating biometric data
        heart_rate = random.randint(70, 85)
        hydration = random.randint(85, 100)
        fatigue_level = random.choice(["Low", "Normal", "Elevated"])
        
        print(f"\033[1;34m[VITALS] Heart Rate: {heart_rate} BPM | Hydration: {hydration}%")
        print(f"[VITALS] Fatigue Analysis: {fatigue_level}\033[0m")
        
        if fatigue_level == "Elevated":
            print("\033[1;31m[ADVICE] Architect Deepak, your fatigue is rising. Recommend a short break.\033[0m")
        else:
            print("\033[1;32m[STATUS] All systems nominal. You are fit for mission, Sir.\033[0m")

    def execute(self):
        print(f"\033[1;32m>> BIOMETRIC LINK ESTABLISHED. <<\033[0m")
        self.scan_vitals()

if __name__ == "__main__":
    monitor = BiometricMonitor()
    monitor.execute()
