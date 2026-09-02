import time, secrets, gc, random

class WormholeGenerator:
    def __init__(self):
        self.nwg_id = f"NWG-{secrets.token_hex(4).upper()}"
        self.spatial_distortion = 0.0 # Percentage (%)
        self.nodes = [
            (6054, "Fabric-Scan", "LOCATING TEMPORAL WEAKNESS IN LOCAL SPACE..."),
            (6055, "Neg-Energy", "INJECTING EXOTIC MATTER TO STABILIZE THROAT..."),
            (6056, "Coord-Sync", "LOCKING DESTINATION: ANDROMEDA GALAXY..."),
            (6057, "Bridge-Lock", "ESTABLISHING EINSTEIN-ROSEN STABILITY..."),
            (6058, "Logic v424", "NWG-CORE: WORMHOLE PORTAL IS OPEN.")
        ]

    def distort_space(self):
        # Unique logic: Folding space-time
        self.spatial_distortion = round(random.uniform(85.0, 99.9), 2)
        return self.spatial_distortion

    def open_portal(self):
        print(f"\033[1;37m--- NEURAL-WORMHOLE-GENERATOR ONLINE (ID: {self.nwg_id}) ---\033[0m")
        colors = [36, 35, 34, 31, 32]
        
        distortion = self.distort_space()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[DISTORTION:{distortion}% | STATUS:FOLDING] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;36mLOG: SPACE-TIME FOLDED. DISTANCE REDUCED TO 0.001 METERS.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS READY FOR INTERGALACTIC JUMP.\033[0m")

if __name__ == "__main__":
    portal = WormholeGenerator()
    portal.open_portal()
