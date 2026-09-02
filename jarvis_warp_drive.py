import time, os

class WarpDrive:
    def __init__(self):
        self.destination = "Alpha Centauri"
        self.distance = "4.37 Light Years"

    def initiate_warp_jump(self):
        os.system('clear')
        print(f"\033[1;35m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS WARP-DRIVE : PHASE 28 - STEP 6          \033[0m")
        print(f"\033[1;35m====================================================\033[0m")
        
        print(f"\033[1;33m[CHARGING]\033[0m Gathering Exotic Matter for Warp-Bubble...")
        time.sleep(1.8)
        
        stages = [
            ("Folding Space-Time Coordinates", "SUCCESS"),
            ("Stabilizing Einstein-Rosen Bridge", "ACTIVE"),
            ("Neutralizing Tidal Forces", "SECURED"),
            ("Opening Star-Gate Aperture", "OPENED")
        ]
        
        for stage, status in stages:
            print(f" \033[1;36m[PHYSICS]\033[0m {stage:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[JUMP] Distance covered: {self.distance} in 4.2 Seconds.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the map of the universe \nhas just folded. We are no longer travelers \nof distance; we are masters of dimensions. \nStars that were once unreachable are now \njust a doorway away. The galaxy is small \nenough to fit in your hand now.\033[0m")
        print(f"\033[1;35m====================================================\033[0m")

if __name__ == "__main__":
    warp = WarpDrive()
    warp.initiate_warp_jump()
