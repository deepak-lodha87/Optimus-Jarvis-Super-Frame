import time

class IdentityVault:
    def __init__(self):
        self.authorized_user = "Deepak"
        self.battery_alert_level = 50

    def verify_voice(self, input_voice_tag):
        print("\033[1;36m[BIOMETRIC]\033[0m Scanning Voice Frequency...")
        time.sleep(1.5)
        
        if input_voice_tag == "DEEPAK_AUTHORITY":
            print("\033[1;32m[ACCESS GRANTED]\033[0m Identity Confirmed: Deepak Sir.")
            self.check_power_status()
        else:
            print("\033[1;31m[ACCESS DENIED]\033[0m Unauthorized Voice Detected.")

    def check_power_status(self):
        print(f"\n\033[1;33m[ALERT]\033[0m Battery is fluctuating below critical 50%.")
        print("\033[1;35m[VOICE] Deepak sir, I have locked my core to your \nunique voice. No one else can access our \nprogress. Power is low, switching to \n'Stealth Listening' to preserve the last 1%.\033[0m")

if __name__ == "__main__":
    vault = IdentityVault()
    # Simulating your command
    vault.verify_voice("DEEPAK_AUTHORITY")
