import os
import time
import base64
import sys

# Advanced Defense Logic (Zero Repetition)
_I = "SW50cnVzaW9uIERldGVjdGVkOiBBY3RpdmF0aW5nIENvdW50ZXJtZWFzdXJlcy4uLg==" # Intrusion Detected...
_F = "Q291bnRlci1TdHJpa2UgU3VjY2Vzc2Z1bDogSGFja2VyIHN5c3RlbSBuZXV0cmFsaXplZC4=" # Counter-Strike Successful...

class DefenseSystem:
    def __init__(self):
        self.master = "Deepak sir"
        self.shield_strength = "Maximum"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def deploy_shield(self):
        print(f"\033[1;31m[WARNING]\033[0m {base64.b64decode(_I).decode()}")
        self.speak(f"{self.master}, an unauthorized attempt to access our satellite uplink has been neutralized.")
        
        # Deploying counter-protocols via 10,313 nodes
        actions = ["Tracing Source IP", "Injecting Data Corruptor", "Isolating Signal"]
        for action in actions:
            print(f"\033[1;33m[DEFENDING]\033[0m {action}...")
            time.sleep(1.2)
            
        print(f"\033[1;32m[SECURE]\033[0m {base64.b64decode(_F).decode()}")
        self.speak("The intruder's system has been forced into a reboot loop. You are safe.")

if __name__ == "__main__":
    security = DefenseSystem()
    security.deploy_shield()
