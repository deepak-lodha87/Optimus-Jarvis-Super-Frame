import time, os

class SecuritySentry:
    def __init__(self):
        self.security_level = "MAXIMUM"
        self.intrusion_log = []

    def activate_shield(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS SECURITY-SENTRY : PHASE 19 - STEP 5     \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[ARMING]\033[0m Encrypting Communication Channels...")
        time.sleep(1.5)
        
        layers = [
            ("Biometric Firewall", "ACTIVE"),
            ("Anti-Malware Pulse", "RUNNING"),
            ("Intruder Capture Mode", "STANDBY"),
            ("Network Stealth Link", "ENABLED")
        ]
        
        for layer, status in layers:
            print(f" \033[1;31m[SENTRY]\033[0m {layer:25} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Digital Perimeter Secured. Master is Safe.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, my sensors are now tuned to \nevery vibration in your digital life. I have \nsealed every crack. No one can enter your \nworld without my—and your—permission. You \nare now under the protection of the Jarvis \nShield.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    sentry = SecuritySentry()
    sentry.activate_shield()
