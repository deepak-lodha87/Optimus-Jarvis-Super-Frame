import os
import time

class ExternalAccessLock:
    def __init__(self):
        self.master = "Deepak"
        self.auth_token = False

    def request_biometric_gateway(self, target_system):
        print(f"\n\033[1;33m[SECURITY ALERT]\033[0m Connection to {target_system} detected.")
        print("\033[1;36m[AUTHENTICATING]\033[0m Pushing biometric request to Master Mobile...")
        
        # यह सिम्युलेट करता है कि मोबाइल पर फिंगरप्रिंट लिया जा रहा है
        time.sleep(1)
        steps = ["Activating Retina Scanner...", "Waiting for Fingerprint Confirmation...", "Syncing Hardware Keys..."]
        
        for step in steps:
            print(f"\033[1;32m[PROCESSING]\033[0m {step}")
            time.sleep(0.5)

        self.auth_token = True
        msg = f"{self.master} sir, external access granted. Biometric handshake successful."
        os.system(f'termux-tts-speak "{msg}"')
        print(f"\033[1;32m[ACCESS GRANTED]\033[0m Secure tunnel to {target_system} is now open.")

if __name__ == "__main__":
    ExternalAccessLock().request_biometric_gateway("Remote Command Center")
