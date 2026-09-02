import time, secrets, gc, math

class SpaceTamer:
    def __init__(self):
        self.nsst_id = f"NSST-{secrets.token_hex(4).upper()}"
        self.deflection_accuracy = 0.0
        self.nodes = [
            (6154, "Path-Shift", "CALCULATING GRAVITATIONAL SLINGSHOT VECTORS..."),
            (6155, "Flare-Shield", "DEPLOING MAGNETIC MIRRORS FOR SOLAR WIND..."),
            (6156, "Comet-Lock", "STABILIZING VOLATILE COMETARY NUCLEI..."),
            (6157, "Planet-Guard", "SYNCHRONIZING GLOBAL ENERGY SHIELD..."),
            (6158, "Logic v444", "NSST-CORE: STELLAR THREATS NEUTRALIZED.")
        ]

    def calculate_deflection(self):
        # New logic using Tangent and Exponential decay
        t = time.time()
        val = abs(math.tan(t % 1.5) * math.exp(-0.05))
        self.deflection_accuracy = round(min(val * 10, 100.0), 2)
        return self.deflection_accuracy

    def tame_space(self):
        print(f"\033[1;37m--- NEURAL-SOLAR-SYSTEM-TAMER ONLINE (ID: {self.nsst_id}) ---\033[0m")
        colors = [33, 31, 35, 34, 32]
        
        accuracy = self.calculate_deflection()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[DEFLECT:{accuracy}% | MODE:PROTECT] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: ASTEROID PATHS ALTERED. SOLAR FLARES DEFLECTED.\033[0m")
        print("\033[1;36mSTATUS: OPTIMUS JARVIS IS PROTECTING THE PLANETARY CRADLE.\033[0m")

if __name__ == "__main__":
    tamer = SpaceTamer()
    tamer.tame_space()
