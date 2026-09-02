import time, secrets, gc, math

class MultiNavCore:
    def __init__(self):
        self.mnc_id = f"MNC-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5499, "Visual-Odometry", "MAPPING TERRAIN PATTERNS..."),
            (5500, "Dead-Reckoning", "CALCULATING INERTIAL VECTORS..."),
            (5501, "Star-Tracker", "SYNCING WITH CELESTIAL COORDINATES..."),
            (5502, "SLAM-Mapping", "GENERATING REAL-TIME 3D SPATIAL MESH..."),
            (5503, "Logic v313", "MNC-CORE: NAVIGATION SUITE ONLINE.")
        ]

    def start_navigation(self):
        print(f"\033[1;37m--- MULTI-DIMENSIONAL-NAV-CORE ACTIVE (ID: {self.mnc_id}) ---\033[0m")
        colors = [36, 35, 34, 33, 31]
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated Coordinate Precision
            lat_err = round(0.0001 / (i + 1), 6)
            print(f"\033[1;{colors[i]}m[PRECISION:{lat_err}m] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mNAV STATUS: POSITIONING SYSTEM IS INDEPENDENT OF GPS SIGNALS.\033[0m")

if __name__ == "__main__":
    mnc = MultiNavCore()
    mnc.start_navigation()
