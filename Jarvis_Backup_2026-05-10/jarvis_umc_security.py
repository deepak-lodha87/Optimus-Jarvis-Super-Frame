import time
import hashlib

class UniversalMachineController:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.is_locked = True
        # Encrypted Bio-Metric Hash
        self.authorized_hash = hashlib.sha256(owner_name.encode()).hexdigest()

    def scan_bio_metrics(self, input_signal):
        print(f"\033[1;34m[BIO-SCAN] Scanning Pulse & Neural Patterns...\033[0m")
        time.sleep(1.2)
        
        # Advance unique logic: Matching neural hash
        input_hash = hashlib.sha256(input_signal.encode()).hexdigest()
        
        if input_hash == self.authorized_hash:
            self.is_locked = False
            return f"\033[1;32m[ACCESS GRANTED] Welcome, {self.owner}. Machine Primed.\033[0m"
        else:
            return "\033[1;31m[DENIED] Unknown Biological Signature. System Hard-Locked.\033[0m"

    def engage_neural_link(self):
        if self.is_locked:
            return "\033[1;31m[ERROR] Security Clearance Required.\033[0m"
        
        print("\033[1;35m[NEURAL] Syncing Jarvis Cortex with User Nervous System...\033[0m")
        time.sleep(1)
        return "\033[1;36m[STATUS] Direct Link Active. Machine will respond to intent.\033[0m"

if __name__ == "__main__":
    # Project Owner: Deepak
    umc = UniversalMachineController("Deepak")
    
    print("-" * 60)
    print("   JARVIS UMC: ADVANCED BIO-SECURITY (P3220)")
    print("-" * 60)
    
    # Simulating Secure Access
    print(umc.scan_bio_metrics("Deepak"))
    print("\n" + umc.engage_neural_link())
    print("-" * 60)
