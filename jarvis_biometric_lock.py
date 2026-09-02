import os
import time
import getpass

class BiometricShield:
    def __init__(self):
        self.master = "Deepak"
        self.auth_token = "OPTIMUS-1050-X"

    def verify_identity(self):
        print(f"\n\033[1;36m[AUTHENTICATION REQUIRED]\033[0m Initializing Biometric Scan...")
        time.sleep(1.5)
        
        # जार्विस मास्टर की पहचान पूछ रहा है
        user_input = input(f"\n\033[1;37mEnter Master Voice-Key/Password for {self.master}: \033[0m")
        
        if user_input.lower() == "optimus":
            self.grant_access()
        else:
            self.deny_access()

    def grant_access(self):
        os.system('clear')
        print("\n\033[1;32m[ACCESS GRANTED] Identity Confirmed: Hello Deepak Sir.\033[0m")
        print("==========================================================")
        msg = "Welcome back Deepak sir. All systems are online and secured by your biometric signature."
        os.system(f'termux-tts-speak "{msg}"')
        
        # डिजिटल सिग्नेचर रेंडर
        for _ in range(3):
            print("\033[1;34m[DECRYPTING CORE FILES] . . . . . . [SUCCESS]\033[0m")
            time.sleep(0.5)

    def deny_access(self):
        print("\n\033[1;31m[ACCESS DENIED] Unknown Entity Detected. Locking Core Modules.\033[0m")
        msg = "Intruder alert. Access denied."
        os.system(f'termux-tts-speak "{msg}"')
        exit()

if __name__ == "__main__":
    shield = BiometricShield()
    shield.verify_identity()
