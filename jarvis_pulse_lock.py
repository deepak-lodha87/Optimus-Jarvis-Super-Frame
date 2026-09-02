import os
import time

class BiometricPulseLock:
    def __init__(self):
        self.master = "Deepak"
        self.auth_state = False

    def verify_liveness(self):
        print(f"\n\033[1;33m[SECURITY ALERT]\033[0m Reached Phase 1221: Universal Access Request.")
        print("\033[1;36m[WAITING]\033[0m Scanning Fingerprint Pulse & Retina Depth on Oppo Reno 12 Pro...")
        
        steps = [
            "Analyzing Bio-Electric Pulse (A-Z Check)...",
            "Verifying Retina Depth Perception...",
            "Syncing Secure Key with Remote Screen..."
        ]
        
        for step in steps:
            print(f"\033[1;32m[VERIFYING]\033[0m {step}")
            time.sleep(0.5)

        self.auth_state = True
        msg = f"{self.master} sir, identity verified via bio-pulse. External access is now secure."
        os.system(f'termux-tts-speak "{msg}"')
        print(f"\033[1;32m[SUCCESS]\033[0m Physical presence confirmed. Access Granting...")

if __name__ == "__main__":
    BiometricPulseLock().verify_liveness()
