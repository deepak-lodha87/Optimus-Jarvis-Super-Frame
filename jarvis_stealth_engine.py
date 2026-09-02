import time
import random

class StealthEngine:
    def __init__(self):
        self.optical_cloak = "INACTIVE"
        self.radar_signature = "HIGH"

    def activate_ghost_mode(self):
        print(f"\033[1;36m[STEALTH]\033[0m Engaging Ghost Protocol...")
        time.sleep(1.5)
        
        self.optical_cloak = "ACTIVE (98% Transparency)"
        self.radar_signature = "MINIMAL (Ghost Pattern)"
        
        print(f" \033[1;32m[+][OPTICAL]\033[0m Adaptive Camouflage: {self.optical_cloak}")
        print(f" \033[1;32m[+][RADAR]\033[0m Cross-section: {self.radar_signature}")
        print(" \033[1;34m[STATUS]\033[0m Drone is now virtually invisible to all sensors.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Aerial Legion has gone \ncompletely dark. They are now 'Ghosts' in \nthe sky. Observation is active, but we \nremain undetected.\033[0m")

if __name__ == "__main__":
    ghost = StealthEngine()
    ghost.activate_ghost_mode()
