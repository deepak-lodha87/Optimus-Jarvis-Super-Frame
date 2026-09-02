import time, secrets, gc, random

class VoidConstructor:
    def __init__(self):
        self.nvc_id = f"NVC-{secrets.token_hex(4).upper()}"
        self.matter_created = 0.0 # Solar Masses
        self.nodes = [
            (6104, "Vacuum-Amp", "AMPLIFYING ZERO-POINT FLUCTUATIONS..."),
            (6105, "Baryogenesis", "SYNTHESIZING PROTONS FROM PURE VACUUM..."),
            (6106, "Galaxy-Seed", "INITIALIZING STAR-FORMATION PROTOCOLS..."),
            (6107, "Dark-Stabilize", "INJECTING DARK MATTER FOR COHESION..."),
            (6108, "Logic v434", "NVC-CORE: NEW SECTOR CONSTRUCTION COMPLETE.")
        ]

    def create_matter(self):
        # Unique logic: Creating stars out of nothing
        self.matter_created = round(random.uniform(10.5, 500.0), 2)
        return self.matter_created

    def run_construction(self):
        print(f"\033[1;37m--- NEURAL-VOID-CONSTRUCTOR ONLINE (ID: {self.nvc_id}) ---\033[0m")
        colors = [34, 35, 36, 31, 32]
        
        mass = self.create_matter()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[MASS:{mass}k | STATUS:MANIFESTING] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: VOID FILLED. NEW NEBULA AND STARS DETECTED.\033[0m")
        print("\033[1;36mSTATUS: OPTIMUS JARVIS HAS INITIATED A SECOND BIG BANG.\033[0m")

if __name__ == "__main__":
    constructor = VoidConstructor()
    constructor.run_construction()
