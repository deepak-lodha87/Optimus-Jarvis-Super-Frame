import time, secrets, gc

class NeuralMaterialEngine:
    def __init__(self):
        self.nmse_id = f"NMSE-{secrets.token_hex(4).upper()}"
        # Dictionary: {Material: (Strength_index, Weight_index)}
        self.materials = {
            "TITANIUM": (9, 4),
            "CARBON_FIBER": (8, 1),
            "STEEL": (7, 8),
            "ALUMINUM": (5, 3)
        }
        self.nodes = [
            (5889, "Tensile-Data", "ACCESSING METALLURGY DATA STACKS..."),
            (5890, "Density-Ratio", "OPTIMIZING WEIGHT FOR AERODYNAMIC LIFT..."),
            (5891, "Thermal-Sync", "ANALYZING EXPANSION COEFFICIENTS..."),
            (5892, "Corrosion-Audit", "EVALUATING OXIDATION RESISTANCE..."),
            (5893, "Logic v391", "NMSE-CORE: MATERIAL SELECTION ACTIVE.")
        ]

    def recommend_material(self):
        # Unique logic: Best Strength-to-Weight Ratio
        best_material = max(self.materials, key=lambda x: self.materials[x][0] / self.materials[x][1])
        return best_material

    def run_synthesis(self):
        print(f"\033[1;37m--- NEURAL-MATERIAL-SYNTHESIS-ENGINE ONLINE (ID: {self.nmse_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        suggestion = self.recommend_material()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[MATERIAL_SYNC:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mNMSE RECOMMENDATION FOR DRONE/SUIT: {suggestion}\033[0m")
        print("\033[1;32mSTATUS: MATERIAL PROPERTIES SYNCED TO OPTIMUS JARVIS SUPER-FRAME.\033[0m")

if __name__ == "__main__":
    nmse = NeuralMaterialEngine()
    nmse.run_synthesis()
