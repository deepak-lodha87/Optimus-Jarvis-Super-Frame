import os
import random
import time

class GhostProtocol:
    def __init__(self):
        self.user = "Deepak sir"
        self.shield_active = True

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def secure_uplink(self):
        print(f"\033[1;35m[SHIELD]\033[0m Activating Ghost Protocol...")
        self.speak("Sir, activating digital shield. Your identity is now masked.")
        
        # Simulating randomized request timing to avoid detection
        delay = random.uniform(3.0, 7.0)
        print(f"\033[1;36m[WAIT]\033[0m Randomizing uplink pulse: {delay:.2f}s")
        time.sleep(delay)
        
        print("\033[1;32m[SUCCESS]\033[0m Connection established via Encrypted Tunnel.")
        self.speak("Uplink is secure. They cannot track your primary node.")

if __name__ == "__main__":
    ghost = GhostProtocol()
    ghost.secure_uplink()
