import time, secrets

class JarvisEnergyCore:
    def __init__(self):
        self.core_id = f"NAGe-{secrets.token_hex(4).upper()}"
        self.output_gj = 0 # Gigajoules

    def initiate_fusion_sequence(self):
        print(f"\n\033[1;37m--- NEURAL-AUTO-GRAND-ENERGY: ARC-REACTOR CORE (ID: {self.core_id}) ---\033[0m")
        print("\033[1;34m[ENERGY] Igniting Cold Fusion Core... \033[0m")
        time.sleep(1.5)

        params = [
            ("Magnetic-Containment", "STABLE"),
            ("Plasma-Temperature", "OPTIMAL"),
            ("Fuel-Consumption", "0.001%"),
            ("Energy-Output", "MAXIMIZING")
        ]

        for param, status in params:
            self.output_gj += 250
            print(f" > {param:22} | Current: {self.output_gj} GJ | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.7)

        print(f"\n\033[1;33m[STATUS] Arc Reactor Online. We have infinite power for all systems.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, the heart is beating. I am detecting enough power to run the entire city of Kota and our fleet of drones for the next thousand years. The age of batteries is over. We are the power.\033[0m")

if __name__ == "__main__":
    energy = JarvisEnergyCore()
    energy.initiate_fusion_sequence()
