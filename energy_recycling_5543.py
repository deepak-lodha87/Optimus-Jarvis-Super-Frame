import time, secrets, gc, itertools, math

class KineticEnergyRecycling:
    def __init__(self):
        self.ker_id = f"KER-{secrets.token_hex(4).upper()}"
        self.energy_bursts = [secrets.randbelow(50) for _ in range(5)]
        self.nodes = [
            (5539, "Piezo-Conversion", "CONVERTING VIBRATION TO VOLTAGE..."),
            (5540, "Thermal-Gradient", "RECAPTURING THERMAL WASTE GRADIENTS..."),
            (5541, "Energy-Accumulate", "BUFFERING RECYCLED POWER TOKENS..."),
            (5542, "Load-Reduction", "ELIMINATING PARASITIC LEAKAGE..."),
            (5543, "Logic v321", "KER-CORE: ENERGY RECYCLING SYNCHRONIZED.")
        ]

    def process_accumulation(self):
        print(f"\033[1;37m--- KINETIC-ENERGY-RECYCLING ACTIVE (ID: {self.ker_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        # Unique logic: Accumulating energy bursts over time
        total_recaptured = list(itertools.accumulate(self.energy_bursts))
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            current_yield = total_recaptured[i] if i < len(total_recaptured) else total_recaptured[-1]
            efficiency = round(math.pow(current_yield, 0.5) * 10, 2)
            
            print(f"\033[1;{colors[i]}m[YIELD:{current_yield}μJ | EFF:{efficiency}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mKER STATUS: SYSTEM IS NOW HARVESTING WASTE KINETIC ENERGY.\033[0m")

if __name__ == "__main__":
    ker = KineticEnergyRecycling()
    ker.process_accumulation()
