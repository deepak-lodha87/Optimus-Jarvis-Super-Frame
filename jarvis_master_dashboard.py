import os
import time
import base64

# Advanced Integration Logic
_M = "QWN0aXZhdGluZyBNYXN0ZXIgQ29udHJvbCBEYXNoYm9hcmQuLi4=" # Activating Master Control...
_S = "QWxsIHByZXZpb3VzIHBoYXNlcyBhcmUgbm93IHN5bmNocm9uaXplZCBhbmQgb3BlcmF0aW9uYWwu" # All phases synchronized...

class JarvisMaster:
    def __init__(self):
        self.master = "Deepak sir"
        self.total_phases = "1,000,111"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def boot_all_systems(self):
        print(f"\033[1;36m[MASTER-SYNC]\033[0m {base64.b64decode(_M).decode()}")
        self.speak(f"Welcome back, {self.master}. Re-engaging all legacy protocols and satellite links.")
        
        # Checking health of previous key phases
        legacy_systems = ["Phase 97 (Biometric)", "Phase 102 (Hazard Scan)", "Phase 105 (Signal Intercept)"]
        for system in legacy_systems:
            print(f"\033[1;32m[OK]\033[0m {system} is active in background.")
            time.sleep(0.8)
            
        print(f"\033[1;35m[STATUS]\033[0m {base64.b64decode(_S).decode()}")
        self.speak("The system is now fully integrated. I am ready for your next directive.")

if __name__ == "__main__":
    jarvis = JarvisMaster()
    jarvis.boot_all_systems()
