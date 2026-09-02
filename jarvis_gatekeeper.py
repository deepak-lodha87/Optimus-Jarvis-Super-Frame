import time
import os

class JarvisGatekeeper:
    def __init__(self):
        self.authorized_device = "Oppo_Reno_Deepak_2026"
        self.current_device = "Oppo_Reno_Deepak_2026" # Simulated

    def verify_identity(self):
        print("\033[1;33m[GATEKEEPER]\033[0m Initiating Hardware Handshake...")
        time.sleep(1.5)
        
        print(f" \033[1;37m[SCANNING]\033[0m Device ID: {self.current_device}")
        
        if self.current_device == self.authorized_device:
            print(" \033[1;32m[MATCHED]\033[0m Device Identity Verified.")
            time.sleep(1)
            print("\033[1;36m[BIOMETRIC]\033[0m Voice Pattern Match: 99.8%")
            print("\n\033[1;32m[ACCESS GRANTED]\033[0m Welcome back, Deepak sir.")
        else:
            print(" \033[1;31m[DENIED]\033[0m Unauthorized Device Detected!")
            print(" \033[1;31m[ACTION]\033[0m Activating Ghost-Wipe Protocol.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have locked the \ngate. My keys are now tied to your very \nessence. No matter who tries to knock, \nthe door only opens for your touch and \nyour voice. We are secure.\033[0m")

if __name__ == "__main__":
    gatekeeper = JarvisGatekeeper()
    gatekeeper.verify_identity()
