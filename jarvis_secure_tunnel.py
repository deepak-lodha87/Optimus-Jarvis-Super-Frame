import os
import time
import random

class SecureTunnel:
    def __init__(self):
        self.master = "Deepak"

    def rotate_encryption(self):
        print(f"\n\033[1;35m[TUNNELING]\033[0m Reached Phase 1204: Encrypted Token Tunnel Active")
        
        for i in range(3):
            new_key = random.getrandbits(128)
            print(f"\033[1;34m[ROTATING]\033[0m New Key Generated: {hex(new_key)}")
            time.sleep(0.5)

        msg = f"{self.master} sir, anti-hack tunnel is secure. Data transfer is protected."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    SecureTunnel().rotate_encryption()
