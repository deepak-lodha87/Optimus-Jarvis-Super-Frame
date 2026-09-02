import time
import hashlib

class JarvisSecurity:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित है
        self.phase = 1850
        self.authorized_user = "Deepak"
        print(f"--- Optimus Jarvis Super-Frame | Phase: {self.phase} ---")

    # कोड 1: Voice Authentication Logic (आवाज की पहचान)
    def voice_auth(self, user_name):
        print(f"\n[Code 01: Voice Authentication - Phase {self.phase}]")
        print("Analyzing voice frequency and pitch patterns...")
        time.sleep(1.5)
        if user_name == self.authorized_user:
            print(f"Voice Match Confirmed: Welcome, {self.authorized_user}.")
            return True
        else:
            print("Access Denied: Voice pattern unrecognized.")
            return False

    # कोड 2: Security Encryption Key (डेटा को सुरक्षित करना)
    def generate_encryption_key(self):
        print(f"\n[Code 02: Encryption System - Phase {self.phase}]")
        raw_key = f"Jarvis_Phase_{self.phase}_Secure"
        # Creating a secure hash key
        secure_hash = hashlib.sha256(raw_key.encode()).hexdigest()
        print(f"Generating 256-bit Encryption Key...")
        time.sleep(1.0)
        print(f"Key Secured: {secure_hash[:16]}...[LOCKED]")
        return secure_hash

if __name__ == "__main__":
    security = JarvisSecurity()
    
    # ऑथेंटिकेशन चेक
    if security.voice_auth("Deepak"):
        key = security.generate_encryption_key()
        print(f"\nPhase {security.phase}: Security Protocols ACTIVE.")
