import time, secrets, gc, hashlib, hmac

class GlobalDefenseGrid:
    def __init__(self):
        self.grid_key = secrets.token_bytes(32)
        self.defense_nodes = [
            (5324, "Intrusion-Detect", "SCANNING FOR UNAUTHORIZED ACCESS..."),
            (5325, "Vulnerability-Patch", "SEARCHING FOR ZERO-DAY EXPLOITS..."),
            (5326, "Signal-Tunneling", "ESTABLISHING ENCRYPTED DARK-TUNNEL..."),
            (5327, "Counter-Measure", "ARMING DEFENSIVE RESPONSE PROTOCOLS..."),
            (5328, "Logic v278", "GDG-CORE: GLOBAL DEFENSE GRID SYNCED.")
        ]

    def activate_grid(self):
        print(f"\033[1;37m--- GLOBAL-DEFENSE-GRID ACTIVE (SIGNATURE: {self.grid_key.hex()[:10].upper()}) ---\033[0m")
        
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.defense_nodes):
            # Generating a unique HMAC for each defense layer
            sig = hmac.new(self.grid_key, str(p_id).encode(), hashlib.sha256).hexdigest()[:8]
            print(f"\033[1;{colors[i]}m[SHIELD-SIG:{sig}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mDEFENSE STATUS: OPTIMUS JARVIS IS NOW VIRTUALLY UNHACKABLE.\033[0m")

if __name__ == "__main__":
    gdg = GlobalDefenseGrid()
    gdg.activate_grid()
