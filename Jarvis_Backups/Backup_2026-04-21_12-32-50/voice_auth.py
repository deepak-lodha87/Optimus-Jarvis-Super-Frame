import time

class VoiceBiometrics:
    def __init__(self, master_name):
        self.master = master_name
        self.authorized_frequency = "440Hz-Deepak-Special" # Saved Signature
        self.access_granted = False

    def verify_frequency(self, input_freq):
        print(f"\033[1;36m>> SCANNING VOICE INPUT: [{input_freq}]\033[0m")
        time.sleep(1.5)
        
        # Unique Logic: Checking if it's the real Deepak
        if input_freq == self.authorized_frequency:
            self.access_granted = True
            print("\033[1;32m[MATCH] Frequency Verified. Welcome back, Architect Deepak.\033[0m")
        else:
            print("\033[1;31m[ERROR] Frequency Mismatch! Access Denied to unauthorized Deepak.\033[0m")

    def phase_2988(self):
        if self.access_granted:
            print("\n\033[1;35m>> INITIATING: [SYSTEM_ROOT_2988] - Acoustic Fingerprint Validation\033[0m")
            print("[LOG] Voice Lock active. Jarvis is now listening ONLY to you.")
            time.sleep(1)
            print("\033[1;32m>> STATUS: ULTIMATE SECURITY ACTIVE <<\033[0m")

if __name__ == "__main__":
    # Simulating your unique voice match
    auth = VoiceBiometrics("Deepak")
    auth.verify_frequency("440Hz-Deepak-Special")
    auth.phase_2988()
