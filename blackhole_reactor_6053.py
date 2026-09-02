import time, secrets, gc, random

class BlackHolePowerCell:
    def __init__(self):
        self.nbhpc_id = f"NBHPC-{secrets.token_hex(4).upper()}"
        self.energy_output = 0.0 # Petawatts (PW)
        self.nodes = [
            (6049, "Singularity-Fix", "LOCKING MICRO-SINGULARITY IN MAGNETIC CAGE..."),
            (6050, "Hawking-Harvest", "EXTRACTING THERMAL RADIATION FROM HORIZON..."),
            (6051, "Horizon-Stabilize", "CALIBRATING MASS-ENERGY CONVERSION RATIO..."),
            (6052, "Zero-Point-Sync", "TAPPING INTO VACUUM FLUCTUATIONS..."),
            (6053, "Logic v423", "NBHPC-CORE: INFINITE POWER CYCLE ESTABLISHED.")
        ]

    def monitor_output(self):
        # Unique logic: Simulating massive energy production
        self.energy_output = round(random.uniform(500.0, 999.9), 2)
        return self.energy_output

    def initiate_power(self):
        print(f"\033[1;37m--- NEURAL-BLACK-HOLE-POWER-CELL ONLINE (ID: {self.nbhpc_id}) ---\033[0m")
        colors = [34, 35, 36, 31, 32]
        
        output = self.monitor_output()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[OUTPUT:{output}PW | STATUS:CRITICAL_MAX] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;33mFINAL STATUS: OPTIMUS JARVIS IS NOW POWERED BY A MICRO-SINGULARITY.\033[0m")
        print("\033[1;32mENERGY LEVEL: INFINITE | LIFESPAN: 10^12 YEARS.\033[0m")

if __name__ == "__main__":
    reactor = BlackHolePowerCell()
    reactor.initiate_power()
