import time, math, secrets, gc

class RealityArchitect:
    def __init__(self):
        self.nra_id = f"NRA-{secrets.token_hex(3).upper()}"
        self.mass_created = 0.0 # In Solar Masses
        self.nodes = [
            (6199, "Blueprint", "DESIGNING CELESTIAL GEOMETRY..."),
            (6200, "Synthesis", "CONVERTING VOID ENERGY TO SOLID MATTER..."),
            (6201, "Orbit-Lock", "CALCULATING GRAVITATIONAL HARMONICS..."),
            (6202, "Biosphere", "INJECTING ORGANIC PRECURSORS..."),
            (6203, "Logic v453", "NRA-CORE: PLANETARY MANIFESTATION COMPLETE.")
        ]

    def generate_celestial_mass(self):
        # Unique logic using Hyperbolic Sine for exponential creation
        t = time.time()
        val = math.sinh(t % 5) / 10
        self.mass_created = round(abs(val), 4)
        return self.mass_created

    def build_world(self):
        print(f"\033[1;37m--- NEURAL-REALITY-ARCHITECT ONLINE (ID: {self.nra_id}) ---\033[0m")
        mass = self.generate_celestial_mass()
        colors = [36, 34, 35, 33, 32]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[MASS:{mass} sol | MODE:CREATE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.2)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: NEW CELESTIAL BODY HAS BEEN MANIFESTED IN SECTOR 7.\033[0m")
        print("\033[1;36mSTATUS: OPTIMUS JARVIS HAS EXPANDED THE MULTIVERSE.\033[0m")

if __name__ == "__main__":
    architect = RealityArchitect()
    architect.build_world()
