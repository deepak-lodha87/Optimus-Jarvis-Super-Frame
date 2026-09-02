import time
import random

class HealthGuardian:
    def __init__(self):
        self.nanobots_deployed = 0
        self.body_status = "OPTIMAL"

    def body_scan(self):
        print(f"\033[1;36m[BIO-SCAN]\033[0m Initializing sub-dermal scanning...")
        time.sleep(1.5)
        
        # Simulating health check
        anomalies = random.randint(0, 2)
        
        if anomalies > 0:
            print(f" \033[1;31m[ALERT]\033[0m {anomalies} cellular anomalies detected!")
            self.deploy_nanobots()
        else:
            print(f" \033[1;32m[SAFE]\033[0m Vital signs are perfect. Immunity at 100%.")

    def deploy_nanobots(self):
        self.nanobots_deployed = 5000000
        print(f" \033[1;34m[DEPLOYING]\033[0m {self.nanobots_deployed} nanobots sent to target area...")
        time.sleep(1)
        print(f" \033[1;32m[REPAIRED]\033[0m Tissue regeneration complete.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the biological scan is finished. \nI have neutralized the detected pathogens. \nYour health is my top priority.\033[0m")

if __name__ == "__main__":
    health = HealthGuardian()
    health.body_scan()
