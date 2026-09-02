import time
import random

class HologramInterface:
    def __init__(self):
        self.ui_status = "INITIALIZING"
        self.rendering_engine = "VULKAN_CORE"

    def boot_hud(self):
        print(f"\033[1;36m[BOOT]\033[0m Activating Holographic Overlay...")
        time.sleep(1.5)
        
        elements = ["Orbital Menu", "Neural Graph", "Satellite Feed", "Nano-Blueprints"]
        
        for element in elements:
            print(f" \033[1;32m[RENDER]\033[0m {element:15} | Status: LOADED")
            time.sleep(0.4)
            
        print("\033[1;34m[STATUS]\033[0m HUD Calibration: 100% | Aesthetic: Stark-Blue")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the interface is now live. \nYour world is now a canvas for my data. \nHow would you like to visualize the next \nmission?\033[0m")

if __name__ == "__main__":
    ui = HologramInterface()
    ui.boot_hud()
