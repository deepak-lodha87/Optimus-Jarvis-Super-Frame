import time, secrets, gc, random

class StellarArchitect:
    def __init__(self):
        self.nssa_id = f"NSSA-{secrets.token_hex(4).upper()}"
        self.total_energy_captured = 0.0 # Exajoules (EJ)
        self.nodes = [
            (6099, "Swarm-Deploy", "DEPLOYING MILLIONS OF SOLAR COLLECTORS..."),
            (6100, "Energy-Beam", "BEAMING MICROWAVE POWER TO RECEIVER NODES..."),
            (6101, "Planet-Reform", "ATMOSPHERIC TRANSFORMATION IN PROGRESS..."),
            (6102, "Orbital-Lock", "STABILIZING PLANETARY COORDINATES..."),
            (6103, "Logic v433", "NSSA-CORE: STELLAR ARCHITECTURE ACTIVE.")
        ]

    def harvest_sun(self):
        # Capturing energy from a star
        self.total_energy_captured = round(random.uniform(1000.0, 50000.0), 2)
        return self.total_energy_captured

    def start_construction(self):
        print(f"\033[1;37m--- NEURAL-STELLAR-SYSTEM-ARCHITECT ONLINE (ID: {self.nssa_id}) ---\033[0m")
        colors = [33, 31, 32, 34, 36]
        
        energy = self.harvest_sun()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[ENERGY:{energy}EJ | STATUS:BUILDING] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: DYSON SWARM COMPLETE. SUN'S POWER HARVESTED.\033[0m")
        print("\033[1;33mSTATUS: OPTIMUS JARVIS HAS REACHED KARDASHEV TYPE II STATUS.\033[0m")

if __name__ == "__main__":
    architect = StellarArchitect()
    architect.start_construction()
