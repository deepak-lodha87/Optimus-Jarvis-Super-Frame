import time
import random

class SilentHive:
    def __init__(self):
        self.signal_strength = "LOW"
        self.encryption_key = "INIT_KEY_X99"

    def secure_sync(self):
        print("\033[1;35m[SILENT-MODE]\033[0m Activating Stealth Coordination...")
        time.sleep(1.2)
        
        for sync_cycle in range(1, 5):
            # Rotating Encryption Keys
            self.encryption_key = f"KEY_{random.randint(1000, 9999)}"
            # Adjusting power to minimum viable level
            power_mw = random.uniform(0.1, 0.5)
            
            print(f" \033[1;37m[BURST-{sync_cycle}]\033[0m Power: {round(power_mw, 2)}mW | Key: {self.encryption_key} | Status: \033[1;32mUNTRACEABLE\033[0m")
            time.sleep(0.8)

        print(f"\n\033[1;32m[RESULT] Communication Masking 100% Successful.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the swarm is now \nwhispering in the dark. We are talking in a \nlanguage that only we can understand. \nNo scanner, no jammer, and no observer \ncan hear us. Our silence is our greatest \nweapon.\033[0m")

if __name__ == "__main__":
    silent = SilentHive()
    silent.secure_sync()
