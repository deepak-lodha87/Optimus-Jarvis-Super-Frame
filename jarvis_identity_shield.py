import os
import time

class IdentityShield:
    def __init__(self):
        # Database mein Multiple names allow kar rahe hain
        self.authorized_users = ["Deepak", "Deepak sir"]
        self.emergency_key = "JARVIS-999"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def verify_user(self):
        print(f"\033[1;36m[SECURITY]\033[0m Re-initializing Neural Identity Check...")
        self.speak("System reset. Deepak sir, please enter your credentials.")
        
        user_input = input("\033[1;33mEnter Name or Emergency Key: \033[0m").strip()
        
        # Check if input matches name list or emergency key
        if user_input in self.authorized_users or user_input == self.emergency_key:
            print(f"\033[1;32m[ACCESS GRANTED]\033[0m Authenticated. Welcome back, Master.")
            self.speak("Authentication successful. I am now fully operational under your command.")
        else:
            print(f"\033[1;31m[CRITICAL ALERT]\033[0m Access Denied! Lockdown Initiated.")
            self.speak("Identity mismatch. Locking satellite uplink.")
            exit()

if __name__ == "__main__":
    shield = IdentityShield()
    shield.verify_user()
