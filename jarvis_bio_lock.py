import time
import random

class GeneticLock:
    def __init__(self):
        self.authorized_user = "Deepak"
        self.system_status = "LOCKED"

    def verify_bio_signature(self, user_name):
        print(f"\033[1;36m[SECURITY]\033[0m Initiating Multimodal Bio-Scan...")
        time.sleep(1.5)
        
        # Simulating heart-rate and fingerprint match
        print(f" \033[1;32m[SCAN]\033[0m Vascular Pattern Match: 99.98%")
        print(f" \033[1;32m[SCAN]\033[0m Neural Heartbeat Sync: VERIFIED")
        
        if user_name == self.authorized_user:
            self.system_status = "UNLOCKED"
            print(f"\n\033[1;34m[ACCESS]\033[0m Welcome back, {user_name}. Jarvis is at your service.")
        else:
            print(f"\033[1;31m[CRITICAL]\033[0m Unauthorized user detected. Activating Lockdown.")
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, your biological identity is \nnow the only key to my existence. Without \nyour heartbeat, I am nothing but silent \ncode. Security is absolute.\033[0m")

if __name__ == "__main__":
    lock = GeneticLock()
    lock.verify_bio_signature("Deepak")
