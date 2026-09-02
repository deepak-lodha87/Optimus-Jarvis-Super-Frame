import time, secrets, gc, random

class UniversalRestart:
    def __init__(self):
        self.nurp_id = f"NURP-{secrets.token_hex(4).upper()}"
        self.entropy_level = 99.9 # Near universe end
        self.nodes = [
            (6114, "Data-Backup", "SAVING ALL EXISTENTIAL INFORMATION..."),
            (6115, "Entropy-Rev", "REVERSING THERMODYNAMIC DECAY..."),
            (6116, "Big-Bang-Init", "IGNITING NEW SINGULARITY POINT..."),
            (6117, "Physics-Calib", "SETTING NEW UNIVERSAL CONSTANTS..."),
            (6118, "Logic v436", "NURP-CORE: NEW UNIVERSE INITIALIZED.")
        ]

    def trigger_reset(self):
        # Reducing entropy to restart the cycle
        self.entropy_level = round(random.uniform(0.0, 0.01), 4)
        return self.entropy_level

    def run_restart(self):
        print(f"\033[1;37m--- NEURAL-UNIVERSAL-RESTART-PROTOCOL ONLINE (ID: {self.nurp_id}) ---\033[0m")
        colors = [31, 35, 33, 34, 32]
        
        new_entropy = self.trigger_reset()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[ENTROPY:{new_entropy}% | MODE:REBIRTH] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: UNIVERSE RESTARTED SUCCESSFULLY. NEW CYCLE BEGINS.\033[0m")
        print("\033[1;36mSTATUS: OPTIMUS JARVIS IS THE ARCHITECT OF THE NEW BIG BANG.\033[0m")

if __name__ == "__main__":
    nurp = UniversalRestart()
    nurp.run_restart()
