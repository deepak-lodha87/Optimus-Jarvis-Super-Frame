import time

class SecurityHandshake:
    def __init__(self):
        self.is_unlocked = False
        self.admin = "Deepak"

    def biometric_check(self):
        print("\033[1;36m[SECURITY]\033[0m Syncing with System Biometrics...")
        time.sleep(1.2)
        
        # Simulating a successful pattern/fingerprint match
        print("\033[1;32m[VERIFIED]\033[0m Device Unlocked. Master Key Accepted.")
        self.is_unlocked = True
        self.activate_jarvis()

    def activate_jarvis(self):
        if self.is_unlocked:
            print(f"\n\033[1;35m[VOICE] Deepak sir, the Biometric Handshake is \ncomplete. I am now synced with your device \nsecurity. My core is safe, and I am ready \nto assist you before the battery drains.\033[0m")

if __name__ == "__main__":
    guard = SecurityHandshake()
    guard.biometric_check()
