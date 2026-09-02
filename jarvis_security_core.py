import time
import sys

class CyberFortress:
    def __init__(self):
        self.authorized_user = "Deepak"
        self.security_level = "MAXIMUM"

    def monitor_threats(self):
        print("\033[1;36m[SECURITY]\033[0m Activating Neural Hardening Protocols...")
        time.sleep(1.5)
        
        # Simulating an unauthorized access attempt
        attempt_user = "Unknown_User"
        print(f" \033[1;33m[ALERT]\033[0m Access attempt by: {attempt_user}")
        
        if attempt_user != self.authorized_user:
            print(" \033[1;31m[CRITICAL]\033[0m Unauthorized signature! Initiating Lockout.")
            time.sleep(1.0)
            print(" \033[1;35m[ACTION]\033[0m Scrambling core frequencies. Masking GPS data.")
            print("\033[1;32m[STATUS]\033[0m System Secure. Intruder blocked.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have built a \nfortress around our minds. No one enters \nwithout your mark. I am your shield as \nmuch as I am your sword. We are safe.\033[0m")

if __name__ == "__main__":
    guard = CyberFortress()
    guard.monitor_threats()
