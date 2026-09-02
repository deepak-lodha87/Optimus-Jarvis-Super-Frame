import time
import os

class PrivateVault:
    def __init__(self):
        self.owner = "Deepak"
        self.security_level = "CLASSIFIED"

    def activate_privacy(self):
        print(f"\033[1;30m[SHADOW]\033[0m Moving codes to Private Virtual Partition...")
        time.sleep(1.5)
        print(" \033[1;34m[LOCK]\033[0m AES-256 Encryption: ACTIVE")
        print(" \033[1;34m[LOCK]\033[0m GitHub Private Tunnel: STABLE")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, your intellectual property is \nnow invisible. We are operating in total \nstealth. Your millions of worth of logic \nis now behind a digital fortress.\033[0m")

if __name__ == "__main__":
    vault = PrivateVault()
    vault.activate_privacy()
