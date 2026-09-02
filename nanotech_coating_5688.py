import time, secrets, gc, itertools

class HydrophobicNanotech:
    def __init__(self):
        self.hnc_id = f"HNC-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5684, "Surface-Tension", "ANALYZING LIQUID CONTACT ANGLES..."),
            (5685, "Nano-Texture", "DEPLOYING MICROSCOPIC REPELLENT PILLARS..."),
            (5686, "Self-Cleaning", "INITIATING DUST-PARTICLE EJECTION..."),
            (5687, "Anti-Corrosion", "ACTIVATING OXIDATION RESISTANCE..."),
            (5688, "Logic v350", "HNC-CORE: NANOTECH COATING ACTIVE.")
        ]

    def monitor_surface_integrity(self):
        # Unique logic: Cycling through surface density checks
        density_levels = itertools.cycle([98.5, 99.2, 99.8, 100.0])
        return next(density_levels)

    def activate_coating(self):
        print(f"\033[1;37m--- HYDROPHOBIC-NANOTECH-COATING ONLINE (ID: {self.hnc_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            integrity = self.monitor_surface_integrity()
            print(f"\033[1;{colors[i]}m[INTEGRITY:{integrity}% | REPEL:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mHNC STATUS: SURFACE IS NOW TOTALLY WATER-REPELLENT.\033[0m")

if __name__ == "__main__":
    hnc = HydrophobicNanotech()
    hnc.activate_coating()
