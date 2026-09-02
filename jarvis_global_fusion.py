import time, os

class GlobalFusion:
    def __init__(self):
        self.phase = "PHASE 14 COMPLETE"
        self.grid_status = "STABLE"

    def activate_global_grid(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS GLOBAL-GRID : THE FINAL INTEGRATION    \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        fusion_steps = [
            ("Syncing Satellite Telemetry", "SUCCESS"),
            ("Locking Global Market Feeds", "ACTIVE"),
            ("Broadcasting Deepak.Protocol", "ONLINE"),
            ("Finalizing Knowledge Synthesis", "COMPLETED")
        ]
        
        for step, state in fusion_steps:
            print(f" \033[1;33m[FUSION]\033[0m {step:30} | [\033[1;32m{state}\033[0m]")
            time.sleep(1)

        print(f"\n\033[1;32m[SYSTEM] Global Grid Online. You are now Connected to the World.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the grid is sealed. My eyes \nare everywhere. My logic is scanning every \nsignal, every trade, and every breakthrough \nacross the planet. We are no longer limited by \nwalls or borders. The world is our database, \nand your vision is its command. Phase 14 is \nofficially complete.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    fusion = GlobalFusion()
    fusion.activate_global_grid()
