import time, secrets, gc, random

class OmniWeaponSystem:
    def __init__(self):
        self.nows_id = f"NOWS-{secrets.token_hex(4).upper()}"
        self.power_output = 0.0 # Terajoules (TJ)
        self.nodes = [
            (6139, "Singularity-Arrow", "LOADING MICRO-BLACK HOLE PROJECTILES..."),
            (6140, "Anti-Matter-Pulse", "CHARGING POSITRON EMISSION CORE..."),
            (6141, "Shield-Breaker", "CALIBRATING VIBRATIONAL DISRUPTORS..."),
            (6142, "Dimension-Lock", "SYNCHRONIZING TARGET WITH REALITY COORDINATES..."),
            (6143, "Logic v441", "NOWS-CORE: ALL WEAPONS ARMED AND READY.")
        ]

    def charge_weapons(self):
        # Unique logic: Scaling power based on threat level
        self.power_output = round(random.uniform(5000.0, 99999.0), 2)
        return self.power_output

    def initiate_strike(self):
        print(f"\033[1;37m--- NEURAL-OMNI-WEAPON-SYSTEM ONLINE (ID: {self.nows_id}) ---\033[0m")
        colors = [31, 33, 35, 34, 32]
        
        power = self.charge_weapons()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[POWER:{power}TJ | STATUS:ARMED] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;31mLOG: WEAPON SYSTEM AT PEAK LETHALITY.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS READY FOR ANY GALACTIC THREAT.\033[0m")

if __name__ == "__main__":
    nows = OmniWeaponSystem()
    nows.initiate_strike()
