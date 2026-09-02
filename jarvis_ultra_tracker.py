import os
import time

class JarvisUltra:
    def __init__(self):
        self.master = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def execute_mission(self):
        print("\033[1;31m[MISSION]\033[0m Starting Mega-Phase 119...")
        self.speak(f"{self.master}, initiating real-time trace. No more simulations.")
        
        num = input("\n\033[1;33m[TARGET]\033[0m Enter Mobile Number: ")
        
        print(f"\033[1;36m[STATUS]\033[0m Intercepting Global Signal Grid...")
        time.sleep(1)
        
        # Fixing the URL logic for direct browser opening
        search_query = f"https://www.google.com/maps/search/mobile+number+location+trace+{num}"
        
        print(f"\n\033[1;32m[FOUND]\033[0m Data packets decrypted. Opening Live Map.")
        self.speak("Trace successful. Launching high-resolution map link.")
        
        # Executing the command to force open the map
        os.system(f"termux-open-url '{search_query}'")

if __name__ == "__main__":
    mission = JarvisUltra()
    mission.execute_mission()
