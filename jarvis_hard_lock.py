import os
import subprocess
import time

class HardwareVault:
    def __init__(self):
        self.master = "Deepak"

    def authenticate(self):
        print(f"\n\033[1;36m[HARDWARE CHECK]\033[0m Initializing Fingerprint Sensor...")
        
        # यह कमांड सीधे फोन के असली फिंगरप्रिंट सेंसर को एक्टिवेट करती है
        # 'termux-fingerprint' असली हार्डवेयर एक्सेस है, सिमुलेशन नहीं।
        result = subprocess.getoutput("termux-fingerprint")

        if '"auth_result": "AUTH_RESULT_SUCCESS"' in result:
            self.grant_access()
        else:
            self.deny_access()

    def grant_access(self):
        os.system('clear')
        print(f"\n\033[1;32m[VERIFIED]\033[0m Master {self.master} recognized via Biometric Hardware.")
        msg = f"Biometric confirmed. Welcome back, Deepak sir. Optimus Super-Frame is now under your direct control."
        os.system(f'termux-tts-speak "{msg}"')
        print("\n\033[1;34m[CORE STATUS]: ACTIVE & UNLOCKED\033[0m")

    def deny_access(self):
        print("\n\033[1;31m[SECURITY BREACH]\033[0m Biometric mismatch. Shutting down Termux session.")
        os.system('termux-tts-speak "Intruder detected. System lockdown initiated."')
        time.sleep(1)
        # सुरक्षा के लिए सेशन बंद कर देगा
        exit()

if __name__ == "__main__":
    vault = HardwareVault()
    vault.authenticate()
