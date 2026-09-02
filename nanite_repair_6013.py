import time, secrets, gc

class NaniteRepairSwarm:
    def __init__(self):
        self.nnrs_id = f"NNRS-{secrets.token_hex(4).upper()}"
        self.suit_integrity = 100 # Percentage (%)
        self.nodes = [
            (6009, "Swarm-Sync", "SYNCHRONIZING MICRO-BOT COLLECTIVE HIVE..."),
            (6010, "Damage-Map", "LOCATING MICRO-FRACTURES IN THE ARMOR..."),
            (6011, "Moly-Weld", "INITIATING ATOMIC-LEVEL MOLECULAR WELDING..."),
            (6012, "Nano-Replication", "DEPLOYING ADDITIONAL REPAIR UNITS..."),
            (6013, "Logic v415", "NNRS-CORE: ARMOR INTEGRITY RESTORED.")
        ]

    def simulate_damage(self):
        # Unique logic: Random damage between 15% to 40%
        damage = secrets.randbelow(26) + 15
        self.suit_integrity -= damage
        return damage

    def run_repair(self):
        print(f"\033[1;37m--- NEURAL-NANITE-REPAIR-SWARM ONLINE (ID: {self.nnrs_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        dmg = self.simulate_damage()
        print(f"\033[1;31mCRITICAL: Damage Detected! Integrity: {self.suit_integrity}%\033[0m")
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[REPAIRING... | INTEGRITY:{self.suit_integrity}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            self.suit_integrity += (dmg // 4)
            gc.collect()

        self.suit_integrity = 100
        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mFINAL STATUS: REPAIR COMPLETE. INTEGRITY: {self.suit_integrity}%\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS HAS HEALED THE SUPER-FRAME.\033[0m")

if __name__ == "__main__":
    swarm = NaniteRepairSwarm()
    swarm.run_repair()
