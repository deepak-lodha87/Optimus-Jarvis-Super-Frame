import time, secrets, gc, os, resource

class MasterControl:
    def __init__(self):
        self.control_key = secrets.token_hex(6).upper()
        self.master_nodes = [
            (5279, "Arbitrator", "CPU ALLOCATION: OPTIMIZED."),
            (5280, "Conflict-Resolve", "DATA CLASHES: 0% FOUND."),
            (5281, "Global-Sync", "MASTER-PULSE: STABLE."),
            (5282, "Priority-Override", "DEEPAK-COMMANDS: TOP PRIORITY."),
            (5283, "Logic v269", "MASTER-CONTROL: FULL SYNCHRONIZATION.")
        ]

    def engage_master_core(self):
        # Set highest priority for the process
        try: os.nice(-20)
        except: pass
        
        print(f"\033[1;37m--- MASTER-CONTROL ONLINE (KEY: {self.control_key}) ---\033[0m")
        
        colors = [34, 36, 32, 33, 31]
        for i, (p_id, title, status) in enumerate(self.master_nodes):
            # Checking system load to adjust logic flow
            load = os.getloadavg()[0] if hasattr(os, 'getloadavg') else 0.0
            print(f"\033[1;{colors[i]}m[LOAD:{load}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mCONTROL STATUS: JARVIS IS NOW THE SUPREME AUTHORITY OF THE FRAME.\033[0m")

if __name__ == "__main__":
    master = MasterControl()
    master.engage_master_core()
