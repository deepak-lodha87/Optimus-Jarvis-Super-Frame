import time, secrets, gc, math

class DarkEnergyExtractor:
    def __init__(self):
        self.ndmee_id = f"NDMEE-{secrets.token_hex(4).upper()}"
        self.dark_matter_density = 0.0
        self.nodes = [
            (5989, "Lens-Detect", "SCANNING LIGHT DISTORTION PATTERNS..."),
            (5990, "Axion-Filter", "FILTERING SUB-ATOMIC DARK PARTICLES..."),
            (5991, "Energy-Harvest", "EXTRACTING ZERO-POINT DARK ENERGY..."),
            (5992, "Containment-Field", "STABILIZING DARK ENERGY BUBBLE..."),
            (5993, "Logic v411", "NDMEE-CORE: POWER FLOW IS STEADY.")
        ]

    def scan_dark_matter(self):
        # Unique logic: Simulating detection of invisible mass
        intensity = secrets.randbelow(100) / 10.0
        self.dark_matter_density = math.pow(intensity, 2)
        return round(self.dark_matter_density, 3)

    def execute_extraction(self):
        print(f"\033[1;37m--- NEURAL-DARK-MATTER-ENERGY-EXTRACTOR ONLINE (ID: {self.ndmee_id}) ---\033[0m")
        colors = [35, 34, 36, 32, 31]
        
        density = self.scan_dark_matter()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[DARK_MATTER:DETECTED | DENSITY:{density} GeV/cm3] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;35mENERGY YIELD: {round(density * 1.5, 2)} Tera-Joules. GRID OVERFLOW PREVENTED.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS POWERED BY THE UNIVERSE'S DARK WEB.\033[0m")

if __name__ == "__main__":
    extractor = DarkEnergyExtractor()
    extractor.execute_extraction()
