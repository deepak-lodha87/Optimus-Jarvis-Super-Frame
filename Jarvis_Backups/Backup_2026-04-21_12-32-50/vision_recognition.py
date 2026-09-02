import time

class IdentityVault:
    def __init__(self, user_name):
        self.authorized_user = user_name
        self.access_granted = False

    def phase_2595(self):
        print("\033[1;36m>> INITIATING: [SYSTEM_ROOT_2595] - Visual Scanning Engine\033[0m")
        print("[LOG] Activating Front-Facing Camera Sensors")
        time.sleep(1)
        print("[ACT] Mapping 30,000 infrared dots for depth perception...")
        time.sleep(1.5)
        print("[RES] Facial geometry captured. Processing mesh data.")

    def phase_2596(self):
        print(f"\n\033[1;32m>> INITIATING: [SYSTEM_ROOT_2596] - Identity Verification\033[0m")
        print(f"[LOG] Matching scan against encrypted records for: {self.authorized_user}")
        time.sleep(1.2)
        
        # Advance check logic
        match_percentage = 99.8
        if match_percentage > 95:
            self.access_granted = True
            print(f"[RES] Match Found: {match_percentage}% Accuracy.")
            print(f"\033[1;32m[ACCESS] Welcome back, {self.authorized_user}. System Unlocked.\033[0m")
        else:
            print("\033[1;31m[DENIED] Unauthorized identity detected.\033[0m")

if __name__ == "__main__":
    # Identity set to Deepak as per profile
    vault = IdentityVault("Deepak")
    vault.phase_2595()
    vault.phase_2596()
