import time, secrets, gc, os

class SelfDestructSystem:
    def __init__(self):
        self.sdst_id = f"SDST-{secrets.token_hex(4).upper()}"
        self.failed_attempts = 0
        self.max_attempts = 3
        self.nodes = [
            (5804, "Intrusion-Count", "MONITORING UNAUTHORIZED ACCESS ATTEMPTS..."),
            (5805, "Dead-Man-Switch", "VERIFYING USER HEARTBEAT PROTOCOL..."),
            (5806, "Data-Shredder", "PREPARING CRYPTOGRAPHIC DATA WIPE..."),
            (5807, "Remote-Wipe", "ESTABLISHING EMERGENCY PURGE CHANNEL..."),
            (5808, "Logic v374", "SDST-CORE: FAIL-SAFE PROTOCOLS ARMED.")
        ]

    def trigger_purge(self):
        # Unique logic: Simulating a permanent data wipe
        print("\033[1;31m!!! WARNING: SELF-DESTRUCT INITIATED. SHREDDING SENSITIVE NODES !!!\033[0m")
        for i in range(5, 0, -1):
            print(f"DELETING CORE FILES IN {i}...")
            time.sleep(0.5)
        print("\033[1;31mSYSTEM WIPE COMPLETE. JARVIS IS NOW OFFLINE.\033[0m")

    def login_attempt(self, is_correct):
        if not is_correct:
            self.failed_attempts += 1
            print(f"\033[1;33mACCESS DENIED. Attempt {self.failed_attempts}/{self.max_attempts}\033[0m")
            if self.failed_attempts >= self.max_attempts:
                self.trigger_purge()
                return False
        return True

    def run_sdst_audit(self):
        print(f"\033[1;37m--- SELF-DESTRUCT-SECURITY-TRIGGER ONLINE (ID: {self.sdst_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[SHRED_READY:TRUE | STATUS:ARMED] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        # Simulating 3 failed attempts
        for _ in range(3): self.login_attempt(False)

if __name__ == "__main__":
    sdst = SelfDestructSystem()
    sdst.run_sdst_audit()
