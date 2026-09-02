import time, secrets, gc, math, itertools

class KineticEnergyRecuperation:
    def __init__(self):
        self.ker_id = f"KER-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5639, "Braking-Harvest", "CONVERTING FRICTIONAL HEAT TO DC POWER..."),
            (5640, "Inertial-Charge", "CAPTURING KINETIC MOTION VECTORS..."),
            (5641, "Regen-Circuit", "STABILIZING HIGH-VOLTAGE POWER INPUT..."),
            (5642, "Efficiency-Map", "OPTIMIZING RECUPERATION RATIO..."),
            (5643, "Logic v341", "KER-CORE: ENERGY RECUPERATION ACTIVE.")
        ]

    def process_energy_stream(self, packets):
        # Unique logic: Accumulating energy units in real-time
        return list(itertools.accumulate(packets))

    def activate_harvesting(self):
        print(f"\033[1;37m--- KINETIC-ENERGY-RECUPERATION ONLINE (ID: {self.ker_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        energy_packets = [secrets.randbelow(50) for _ in range(5)]
        stored_total = self.process_energy_stream(energy_packets)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            current_yield = stored_total[i]
            print(f"\033[1;{colors[i]}m[YIELD:{current_yield}Wh | EFF:94%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mKER STATUS: REGENERATIVE POWER CYCLES ARE OPERATIONAL.\033[0m")

if __name__ == "__main__":
    ker = KineticEnergyRecuperation()
    ker.activate_harvesting()
