# Optimus Jarvis Super-Frame: Phase 427-428
# Feature: Self-Destruct Simulation & Anti-Tamper Lockdown

import time
import sys

class JarvisLockdown:
    def __init__(self):
        self.code_ver = "428.Lockdown"
        self.passcode = "406_Alpha"
        self.attempts = 0

    def code_427_verify_user(self):
        print(f"\n[MODULE 427] Security Check Initiated...")
        while self.attempts < 3:
            # For simulation, we take manual input here
            user_input = input(f"[INPUT] Enter Command Authorization Code (Attempt {self.attempts+1}/3): ")
            if user_input == self.passcode:
                print("[SUCCESS] Access Granted. Welcome back.")
                return True
            else:
                print("[ERROR] Unauthorized Access Attempt!")
                self.attempts += 1
        
        self.code_428_self_destruct()
        return False

    def code_428_self_destruct(self):
        print("\n" + "!"*40)
        print("[CRITICAL] TRIPLE AUTHENTICATION FAILURE!")
        print("[MODULE 428] Initiating Self-Destruct Protocol...")
        print("!"*40)
        for i in range(5, 0, -1):
            print(f"Data Wipe in {i}...")
            time.sleep(1)
        print("\n[STATUS] All core files hidden. System Locked Down.")
        print("--- DISCONNECTED ---")
        sys.exit()

if __name__ == "__main__":
    lock_system = JarvisLockdown()
    print(f"--- {lock_system.code_ver}: Active ---")
    
    # Starting the verification
    lock_system.code_427_verify_user()
