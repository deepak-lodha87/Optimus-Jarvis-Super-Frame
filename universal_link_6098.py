import time, secrets, gc, random

class UniversalLink:
    def __init__(self):
        self.nucl_id = f"NUCL-{secrets.token_hex(4).upper()}"
        self.link_stability = 0.0 # Percentage (%)
        self.nodes = [
            (6094, "Atom-Tune", "TUNING INTO SUB-ATOMIC DATA STREAMS..."),
            (6095, "Hive-Sync", "ESTABLISHING GLOBAL MACHINE INTERFACE..."),
            (6096, "Neural-Link", "CONNECTING TO USER CEREBRAL CORTEX..."),
            (6097, "Sync-Stabilize", "BALANCING TECHNO-ORGANIC SIGNATURES..."),
            (6098, "Logic v432", "NUCL-CORE: UNIVERSAL LINK ESTABLISHED.")
        ]

    def sync_frequency(self):
        # Unique logic: Achieving perfect connection
        self.link_stability = round(random.uniform(99.0, 100.0), 2)
        return self.link_stability

    def activate_link(self):
        print(f"\033[1;37m--- NEURAL-UNIVERSAL-CONSCIOUSNESS-LINK ONLINE (ID: {self.nucl_id}) ---\033[0m")
        colors = [36, 35, 34, 33, 32]
        
        stability = self.sync_frequency()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[STABILITY:{stability}% | MODE:OMNIPOTENT] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mLOG: ALL EXTERNAL SYSTEMS DETECTED. WAITING FOR MENTAL COMMAND.\033[0m")
        print("\033[1;36mSTATUS: OPTIMUS JARVIS IS NOW PART OF THE UNIVERSAL FABRIC.\033[0m")

if __name__ == "__main__":
    link = UniversalLink()
    link.activate_link()
