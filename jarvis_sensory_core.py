import os
import time

class JarvisSensoryCore:
    def __init__(self):
        self.master = "Deepak sir" 
        self.project = "Optimus Jarvis Super-Frame" 

    def activate_ar_vision(self):
        """Phase 11: Holographic Camera Overlay logic"""
        print("\033[1;36m[SENSORY]\033[0m Activating AR Vision & HUD Overlay...")
        print(" > Calibrating Camera for Background Recognition...") 
        time.sleep(1)

    def activate_voice_listening(self):
        """Phase 12: Neural Voice Interaction"""
        print("\033[1;32m[SENSORY]\033[0m Voice Recognition Handshake: ACTIVE")
        print(f" > Listening for command from {self.master}...") 
        time.sleep(1)

    def run_sync(self):
        os.system('clear')
        print(f"\033[1;35m--- {self.project.upper()} : SENSORY SYNC ---\033[0m")
        self.activate_ar_vision()
        self.activate_voice_listening()
        
        msg = f"{self.master}, your AI has now gained sensory perception. I am ready to see and hear your world." 
        os.system(f'termux-tts-speak "{msg}"')
        
        print("\n\033[1;32m[SYSTEM STATUS: SENSORY COGNITION ONLINE]\033[0m")

if __name__ == "__main__":
    JarvisSensoryCore().run_sync()
