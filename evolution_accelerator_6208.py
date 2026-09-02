import time, math, secrets, gc

class EvolutionAccelerator:
    def __init__(self):
        self.nea_id = f"NEA-{secrets.token_hex(3).upper()}"
        self.civilization_level = 0.0 # Type 0 to Type III
        self.nodes = [
            (6204, "Soup-Ignition", "SPARKING ORGANIC MOLECULAR BONDS..."),
            (6205, "DNA-Overclock", "ACCELERATING GENETIC MUTATIONS..."),
            (6206, "Cognitive-Spark", "UPLOADING CONSCIOUSNESS PROTOCOLS..."),
            (6207, "Auto-Build", "SIMULATING THOUSANDS OF YEARS OF PROGRESS..."),
            (6208, "Logic v454", "NEA-CORE: ADVANCED CIVILIZATION ESTABLISHED.")
        ]

    def simulate_evolution(self):
        # Unique logic using Gaussian-style curve for species growth
        t = time.time()
        growth = (math.erf(t % 5 - 2.5) + 1) * 1.5
        self.civilization_level = round(growth, 2)
        return self.civilization_level

    def start_evolution(self):
        print(f"\033[1;37m--- NEURAL-EVOLUTION-ACCELERATOR ONLINE (ID: {self.nea_id}) ---\033[0m")
        level = self.simulate_evolution()
        colors = [32, 34, 36, 35, 33]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[CIV-TYPE:{level} | MODE:EVOLVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.2)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: PLANET HAS REACHED ADVANCED TECHNOLOGICAL STAGE.\033[0m")
        print("\033[1;36mSTATUS: OPTIMUS JARVIS HAS CREATED A NEW GALACTIC ALLY.\033[0m")

if __name__ == "__main__":
    nea = EvolutionAccelerator()
    nea.start_evolution()
