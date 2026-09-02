import time
import hashlib

class NeuralLockdown:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3048"
        self.encryption_level = "Quantum-Biometric"

    def generate_bio_key(self):
        print(f"\033[1;35m>> PHASE {self.phase}: GENERATING NEURAL ENCRYPTION KEY <<\033[0m")
        time.sleep(1)
        # Simulating a key based on unique neural patterns
        raw_signature = "Deepak_Neural_Alpha_99.33"
        bio_key = hashlib.sha256(raw_signature.encode()).hexdigest()
        print(f"\033[1;34m[KEY] Bio-Signature Hash: {bio_key[:16]}... [LOCKED]\033[0m")
        return bio_key

    def activate_lockdown(self):
        print("\033[1;36m[ACTION] Initiating Total Bio-Data Lockdown... <<\033[0m")
        time.sleep(1)
        print("\033[1;33m[SECURE] Encrypting Vital History.")
        print("[SECURE] Locking Environmental Preferences.")
        print("[SECURE] Severing External Access Ports.")
        print("\033[1;32m[SUCCESS] Neural-Link Lockdown Active. System is Architect-Only.\033[0m")

    def run(self):
        print(f"\033[1;32m>> SECURITY OVERRIDE: JARVIS IS NOW YOUR PRIVATE SENTINEL. <<\033[0m")
        self.generate_bio_key()
        self.activate_lockdown()

if __name__ == "__main__":
    lock_system = NeuralLockdown()
    lock_system.run()
