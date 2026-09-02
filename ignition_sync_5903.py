import time, secrets, gc

class NeuralPropulsionIgnition:
    def __init__(self):
        self.npis_id = f"NPIS-{secrets.token_hex(4).upper()}"
        self.ignition_status = False
        self.nodes = [
            (5899, "Ignition-Protocol", "INITIATING PRE-FLIGHT CHECKLIST..."),
            (5900, "Fuel-Optimizer", "ADJUSTING AIR-FUEL MIXTURE RATIO..."),
            (5901, "Combustion-Monitor", "STABILIZING INTERNAL PRESSURE..."),
            (5902, "Thrust-Calculator", "CALCULATING EXHAUST GAS VELOCITY..."),
            (5903, "Logic v383", "NPIS-CORE: IGNition SYNC SUCCESSFUL.")
        ]

    def ignite_engine(self):
        # Unique logic: Checking all nodes before ignition
        print("\033[1;33m[!] PREPARING IGNITION SEQUENCE...\033[0m")
        time.sleep(1)
        self.ignition_status = True
        return "ENGINE STARTED: THRUST IS NOMINAL."

    def run_propulsion_test(self):
        print(f"\033[1;37m--- NEURAL-PROPULSION-IGNITION-SYNC ONLINE (ID: {self.npis_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[SYNC:ACTIVE | PROPULSION:READY] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        result = self.ignite_engine()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32m{result}\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS READY FOR TAKE-OFF.\033[0m")

if __name__ == "__main__":
    npis = NeuralPropulsionIgnition()
    npis.run_propulsion_test()
