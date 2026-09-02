import time, secrets, gc

class NeuralResourceScanner:
    def __init__(self):
        self.nrms_id = f"NRMS-{secrets.token_hex(4).upper()}"
        self.minerals = {
            "IRON": 7.8, "GOLD": 19.3, "ICE_WATER": 0.9, "SILICON": 2.3
        }
        self.nodes = [
            (5959, "Spectro-Scan", "ANALYZING LIGHT REFLECTANCE SPECTRUM..."),
            (5960, "Radar-Ping", "SENDING SUB-SURFACE ULTRASONIC WAVES..."),
            (5961, "Density-Map", "MAPPING SUBSURFACE MASS CONCENTRATION..."),
            (5962, "Vapor-Track", "DETECTING HYDROGEN-OXYGEN MOLECULES..."),
            (5963, "Logic v405", "NRMS-CORE: SCANNING SEQUENCE COMPLETE.")
        ]

    def scan_area(self):
        # Logic: Finding a mineral based on random density anomaly
        found_key = secrets.choice(list(self.minerals.keys()))
        depth = secrets.randbelow(45) + 5
        return found_key, depth

    def execute_scan(self):
        print(f"\033[1;37m--- NEURAL-RESOURCE-MINING-SCANNER ONLINE (ID: {self.nrms_id}) ---\033[0m")
        colors = [32, 33, 34, 35, 36]
        
        mineral, depth = self.scan_area()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[MINING_SCAN:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.15)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;33mDETECTION: {mineral} DEPOSIT FOUND AT {depth} METERS.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS EXTRACTING MATERIAL DATA.\033[0m")

if __name__ == "__main__":
    nrms = NeuralResourceScanner()
    nrms.execute_scan()
