import time

class NanotechSystem:
    def __init__(self):
        self.integrity = 100  # Percentage
        self.nanobot_status = "STABLE"

    def phase_2613(self):
        print("\033[1;35m>> INITIATING: [SYSTEM_ROOT_2613] - Molecular Assembly\033[0m")
        print("[LOG] Injecting Nanobot Swarm into system architecture...")
        time.sleep(1.2)
        print("[ACT] Aligning carbon nanotubes for structural reinforcement...")
        time.sleep(1.5)
        print("[RES] Nanotech Mesh active. Material can now change shape on command.")

    def phase_2614(self):
        print("\n\033[1;31m>> INITIATING: [SYSTEM_ROOT_2614] - Self-Healing Protocol\033[0m")
        # Simulating damage
        self.integrity = 65
        print(f"[WARN] Structural Integrity compromised: {self.integrity}%")
        time.sleep(1)
        
        print("[LOG] Activating Nanotech Reconstruction...")
        while self.integrity < 100:
            self.integrity += 5
            print(f"[ACT] Repairing molecular bonds... Integrity: {self.integrity}%", end='\r')
            time.sleep(0.4)
            
        print("\n[RES] Repair Complete. System Integrity restored to 100%.")
        print("\033[1;32m>> STATUS: NANOTECH FULLY INTEGRATED\033[0m")

if __name__ == "__main__":
    nano = NanotechSystem()
    nano.phase_2613()
    nano.phase_2614()
