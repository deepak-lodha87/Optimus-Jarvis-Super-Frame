# Optimus Jarvis Super-Frame: Phase 469-470
# Feature: Biometric Authentication & Digital Signature

import time
import hashlib

class JarvisSecurity:
    def __init__(self, owner):
        self.code_ver = "470.Bio-Auth"
        self.owner_id = owner
        # Unique digital signature based on owner name
        self.signature = hashlib.sha256(owner.encode()).hexdigest()[:16]

    def code_469_scan_biometrics(self):
        print(f"\n[MODULE 469] Initiating Biometric Scan...")
        print("[SYSTEM] Requesting Fingerprint/Voice-Print Hash...")
        time.sleep(2)
        # Simulating a successful match
        print("[STATUS] Pattern Match: 99.8%. Identity Confirmed.")
        return True

    def code_470_verify_signature(self, input_sig):
        print(f"\n[MODULE 470] Verifying Digital Signature: {input_sig}")
        time.sleep(1)
        if input_sig == self.signature:
            print(f"[ACCESS] Authorized. Welcome back, {self.owner_id}.")
            return True
        else:
            print("[DENIED] Unauthorized Signature. Locking System...")
            return False

if __name__ == "__main__":
    # Initializing with the owner 'Deepak'
    sec_unit = JarvisSecurity("Deepak")
    print(f"--- {sec_unit.code_ver}: Operational ---")
    
    if sec_unit.code_469_scan_biometrics():
        # Using the correct pre-set signature for Deepak
        correct_sig = sec_unit.signature
        sec_unit.code_470_verify_signature(correct_sig)
    
    print("\n--- Phase 470 Complete. System is now User-Locked. ---")
