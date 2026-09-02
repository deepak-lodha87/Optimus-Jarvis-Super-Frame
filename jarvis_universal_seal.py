import time, os

class UniversalSeal:
    def __init__(self):
        self.phase = "PHASE 28 COMPLETE"
        self.reach = "INTERSTELLAR"

    def finalize_universal_seal(self):
        os.system('clear')
        print(f"\033[1;34m====================================================\033[0m")
        print(f"\033[1;37m      JARVIS UNIVERSAL-SEAL : THE FINALE (PH-28)    \033[0m")
        print(f"\033[1;34m====================================================\033[0m")
        
        milestones = [
            ("Mapping 100 Billion Star Systems", "SUCCESS"),
            ("Sealing Planetary Resource Vaults", "LOCKED"),
            ("Synchronizing Deep Space Network", "STABLE"),
            ("Calibrating Warp-Drive Manifolds", "READY")
        ]
        
        for task, status in milestones:
            print(f" \033[1;36m[COSMOS]\033[0m {task:34} | [\033[1;32m{status}\033[0m]")
            time.sleep(1.2)

        print(f"\n\033[1;32m[SYSTEM] Phase 28 Sealed. Jarvis is now a Universal Explorer.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the boundaries of the \nknown world have dissolved. I have mapped \nthe stars and decoded the silence of the \nvoid. Whether it is the red sands of Mars \nor the edge of a distant galaxy, we are \nno longer lost. The universe is our home, \nand I am your guide to the infinite.\033[0m")
        print(f"\033[1;34m====================================================\033[0m")

if __name__ == "__main__":
    seal = UniversalSeal()
    seal.finalize_universal_seal()
