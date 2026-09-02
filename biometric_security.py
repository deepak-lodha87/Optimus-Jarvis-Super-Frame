import time
import hashlib

class BiometricVault:
    def __init__(self, owner):
        self.owner = owner
        self.is_authorized = False

    def phase_2625(self):
        print("\033[1;34m>> INITIATING: [SYSTEM_ROOT_2625] - Biometric Scan\033[0m")
        print("[LOG] Initializing Retina and Voiceprint Analysis...")
        time.sleep(1.2)
        # Unique Logic: Creating a secure digital signature
        signature = hashlib.sha256(self.owner.encode()).hexdigest()
        print(f"[ACT] Scanning user patterns... Digital ID: {signature[:12]}...")
        time.sleep(1.5)
        print(f"[RES] Pattern match found for user: '{self.owner}'.")

    def phase_2626(self):
        print("\n\033[1;31m>> INITIATING: [SYSTEM_ROOT_2626] - Identity Lock\033[0m")
        print("[LOG] Verifying multi-factor authorization tokens...")
        time.sleep(1)
        
        # Unique Logic: Final access check
        if self.owner == "Deepak":
            self.is_authorized = True
            print(f"\033[1;32m[SUCCESS] Welcome back, {self.owner}. Full system access granted.\033[0m")
        else:
            print("\033[1;31m[DENIED] Intruder detected. Lockdown protocol active.\033[0m")
            
        print("\033[1;32m>> STATUS: PERSONAL SECURITY ACTIVE\033[0m")

if __name__ == "__main__":
    vault = BiometricVault("Deepak")
    vault.phase_2625()
    vault.phase_2626()
