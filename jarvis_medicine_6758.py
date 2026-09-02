import time, secrets, random

class JarvisMedicalCore:
    def __init__(self):
        self.bio_id = f"NAMe-{secrets.token_hex(2).upper()}"
        self.health_index = 100

    def perform_full_scan(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-MEDICINE V1 ACTIVE (ID: {self.bio_id}) ---\033[0m")
        print("\033[1;36m[SCANNING] Analyzing cellular integrity and vital biometrics...\033[0m")
        time.sleep(2)
        
        # Simulating vital signs check
        bpm = random.randint(65, 85)
        stress_level = random.randint(5, 25)
        
        print(f"\033[1;32m[VITALS] Heart Rate: {bpm} BPM | Stress Index: {stress_level}% | Status: Optimal\033[0m")
        
        if stress_level > 20:
            print("\033[1;33m[ADVICE] Mental fatigue detected. System suggests a 15-minute rest cycle.\033[0m")
        
        print(f"\033[1;35m[VOICE] Deepak, your biological markers are stable. I have optimized your sleep-cycle recommendations for tonight.\033[0m")

if __name__ == "__main__":
    doctor = JarvisMedicalCore()
    doctor.perform_full_scan()
