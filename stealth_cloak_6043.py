import time, secrets, gc, math

class QuantumStealthCloak:
    def __init__(self):
        self.nqsc_id = f"NQSC-{secrets.token_hex(4).upper()}"
        self.visibility_index = 100.0 # 100% visible initially
        self.nodes = [
            (6039, "Metamaterial-Sync", "ALIGNING NANO-STRUCTURES TO BEND LIGHT..."),
            (6040, "Refraction-Shift", "MATCHING REFRACTIVE INDEX WITH ATMOSPHERE..."),
            (6041, "Thermal-Mask", "COOLING EXTERNAL SHELL TO AMBIENT TEMP..."),
            (6042, "Radar-Cancel", "ABSORBING INCOMING ELECTROMAGNETIC PULSES..."),
            (6043, "Logic v421", "NQSC-CORE: STEALH CLOAK FULLY OPERATIONAL.")
        ]

    def activate_ghost_mode(self):
        print(f"\033[1;37m--- NEURAL-QUANTUM-STEALTH-CLOAK ONLINE (ID: {self.nqsc_id}) ---\033[0m")
        colors = [35, 34, 36, 31, 32]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Dropping visibility at each phase
            self.visibility_index -= 20.0
            print(f"\033[1;{colors[i]}m[VISIBILITY:{round(self.visibility_index, 1)}% | GHOST:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mFINAL STATUS: OPTIMUS JARVIS IS NOW INVISIBLE TO ALL SPECTRUMS.\033[0m")
        print("\033[1;35mNOTICE: RADAR AND THERMAL DETECTION PROBABILITY: 0.0001%\033[0m")

if __name__ == "__main__":
    cloak = QuantumStealthCloak()
    cloak.activate_ghost_mode()
