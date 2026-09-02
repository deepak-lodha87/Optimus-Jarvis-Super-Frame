import time
import sys

class AntiTheftSystem:
    def __init__(self):
        self.authorized_owner = "Deepak_Sir"
        self.authorized_device_id = "OP_69" # Sample ID

    def verify_access(self, user_id):
        print(f"\033[1;31m[SECURITY]\033[0m Scanning User Identity...")
        time.sleep(2)
        
        if user_id != self.authorized_owner:
            print("\033[1;41m[ALARM] UNAUTHORIZED ACCESS DETECTED!\033[0m")
            print("\033[1;31m[ACTION] Initiating Code Scrambling... Data Wipe in 3s.\033[0m")
            time.sleep(3)
            # Logic: sys.exit() or os.remove()
        else:
            print(f"\033[1;32m[ACCESS GRANTED]\033[0m Welcome back, {self.authorized_owner}.")
            print(f"\033[1;34m[VOICE] Deepak sir, the system is secure. \nI have monitored all background pings. \nNo unauthorized attempts found.\033[0m")

if __name__ == "__main__":
    guard = AntiTheftSystem()
    guard.verify_access("Deepak_Sir") # Only Deepak can pass
