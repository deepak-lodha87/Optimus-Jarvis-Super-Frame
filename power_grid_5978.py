import time, secrets, gc

class NeuralPowerGrid:
    def __init__(self):
        self.nqpg_id = f"NQPG-{secrets.token_hex(4).upper()}"
        self.grid_output = 100.0 # Percentage (%)
        self.load_distribution = {"Life_Support": 30, "Engines": 50, "Shields": 20}
        self.nodes = [
            (5974, "Fusion-Core", "IGNITING COLD FUSION REACTION CHAMBER..."),
            (5975, "Wireless-Link", "BROADCASTING MICROWAVE POWER BEAMS..."),
            (5976, "Efficiency-Opt", "REROUTING SURPLUS ENERGY TO RESERVES..."),
            (5977, "Zero-Point", "EXTRACTING QUANTUM VACUUM FLUCTUATIONS..."),
            (5978, "Logic v408", "NQPG-CORE: POWER GRID SYNCHRONIZED.")
        ]

    def optimize_load(self):
        # Logic: If engines need more, take from non-essential systems
        self.load_distribution["Engines"] += 10
        self.load_distribution["Shields"] -= 10
        return self.load_distribution

    def run_grid_status(self):
        print(f"\033[1;37m--- NEURAL-QUANTUM-POWER-GRID ONLINE (ID: {self.nqpg_id}) ---\033[0m")
        colors = [33, 36, 32, 35, 31]
        
        new_load = self.optimize_load()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[GRID:STABLE | OUTPUT:{self.grid_output}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;33mCURRENT LOAD: Engines: {new_load['Engines']}% | Life Support: {new_load['Life_Support']}%\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS MANAGING THE ARC-REACTOR CORE.\033[0m")

if __name__ == "__main__":
    grid = NeuralPowerGrid()
    grid.run_grid_status()
