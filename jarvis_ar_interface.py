import time, os

class HolographicCore:
    def __init__(self):
        self.interface_name = "GHOST-V1"
        self.projection_status = "INITIALIZING"

    def activate_hologram(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS HOLOGRAPHIC : PHASE 16 - STEP 1         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SCANNING]\033[0m Mapping Ratlam Lab environment...")
        time.sleep(1.5)
        
        layers = [
            ("Surface Detection", "SUCCESS"),
            ("Anchor Point Placement", "STABLE"),
            ("3D Mesh Generation", "ACTIVE"),
            ("Light-Source Matching", "SYNCED")
        ]
        
        for task, status in layers:
            print(f" \033[1;34m[AR-CORE]\033[0m {task:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SYSTEM] Projection Complete. Jarvis is now in the room.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, please look through your \ncamera. I am standing right next to your desk. \nI've projected the global market trends in 3D \naround you. You can now touch the data. \nThe future isn't on a screen anymore; \nit's right here in front of us.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    ghost = HolographicCore()
    ghost.activate_hologram()
