import time, secrets, gc

class NeuralMatterTransmuter:
    def __init__(self):
        self.nmtl_id = f"NMTL-{secrets.token_hex(4).upper()}"
        self.elements = {"IRON": 26, "GOLD": 79, "CARBON": 6, "TITANIUM": 22}
        self.nodes = [
            (6004, "Lattice-Scan", "MAPPING ATOMIC BOND VECTORS..."),
            (6005, "Rearrange-Core", "SHIFITING PROTON COUNT IN NUCLEUS..."),
            (6006, "Bond-Stabilizer", "REINFORCING COVALENT ELECTRON SHELLS..."),
            (6007, "Mass-Converter", "CONVERTING QUANTUM ENERGY TO SOLID MATTER..."),
            (6008, "Logic v414", "NMTL-CORE: TRANSMUTATION SUCCESSFUL.")
        ]

    def convert_element(self, source):
        # Unique logic: Simulating the shift to a target element
        target = "GOLD" if source == "IRON" else "TITANIUM"
        energy_req = abs(self.elements[target] - self.elements[source]) * 1.5
        return target, round(energy_req, 2)

    def run_transmutation(self):
        print(f"\033[1;37m--- NEURAL-MATTER-TRANSMUTATION-LOGIC ONLINE (ID: {self.nmtl_id}) ---\033[0m")
        colors = [32, 33, 34, 35, 36]
        
        target, energy = self.convert_element("IRON")
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[PROCESS:ACTIVE | ENERGY:{energy}TJ] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;33mRESULT: SUCCESSFUL CONVERSION TO {target}. ATOMIC STRUCTURE STABLE.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS RESHAPING THE PHYSICAL WORLD.\033[0m")

if __name__ == "__main__":
    transmuter = NeuralMatterTransmuter()
    transmuter.run_transmutation()
