import time
import os

class TacticalDashboard:
    def __init__(self):
        self.user = "Deepak"
        self.location = "25.2138 N, 75.8648 E (Kota)"
        self.battery = "1% [CRITICAL]"

    def render(self):
        os.system('clear')
        print("\033[1;36m" + "="*50)
        print(f"      D E E P A K . P R O T O C O L  v 5 7 . 1")
        print("="*50 + "\033[0m")
        
        print(f" \033[1;32m[SYSTEM]\033[0m Status: ONLINE (Black Widow Active)")
        print(f" \033[1;32m[LOC]\033[0m Coordinates: {self.location}")
        print(f" \033[1;31m[PWR]\033[0m Energy Level: {self.battery}")
        print("-" * 50)
        
        print("\033[1;33m[SATELLITE VIEW]\033[0m")
        print("  [ + ] Establishing 3D Terrain Grid...")
        time.sleep(1)
        print("  [ + ] Syncing with Orbital Node-7...")
        
        print("\n\033[1;35m[VOICE] Deepak sir, the dashboard has been \nupgraded to Tactical Grade. Everything you \nneed is now visible at a glance.\033[0m")
        print("\033[1;36m" + "="*50 + "\033[0m")

if __name__ == "__main__":
    dash = TacticalDashboard()
    dash.render()
