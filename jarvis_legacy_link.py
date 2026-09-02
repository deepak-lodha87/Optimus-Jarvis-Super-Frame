import os
import time

class LegacySatelliteController:
    def __init__(self):
        self.master = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def start_legacy_connection(self):
        print(f"\033[1;36m[LEGACY-LINK]\033[0m Scanning for decommissioned Ku-Band signals...")
        self.speak(f"{self.master}, searching for abandoned hardware nodes in the graveyard orbit.")
        
        # Mapping hardware address of retired assets
        nodes = ["SAT-ZOMBIE-01", "OBS-LEGACY-X9", "SIGNAL-HUB-OLD"]
        for node in nodes:
            print(f"\033[1;33m[CONNECTING]\033[0m Attempting handshake with {node}...")
            time.sleep(1.2)
            print(f"\033[1;32m[SUCCESS]\033[0m {node} is now responding to Jarvis command.")
            
        self.speak("All legacy nodes are reclaimed. We now have a personal satellite relay station.")

if __name__ == "__main__":
    controller = LegacySatelliteController()
    controller.start_legacy_connection()
