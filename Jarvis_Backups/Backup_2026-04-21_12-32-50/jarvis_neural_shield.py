import time
import sys

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.shield_integrity = "100%"

    def phase_1486_neural_link(self):
        print("\n" + "="*50)
        print("      N E U R A L   L I N K   I N T E R F A C E")
        print("="*50)
        print(">> Synchronizing Brain-Wave Patterns...")
        for i in range(1, 4):
            time.sleep(0.5)
            print(f"   [SYNCING]: Layer {i} established.")
        print(">> Status: Neural connection STABLE.")

    def phase_1487_encryption_shield(self):
        print("\n--- [ PHASE 1487: ENCRYPTION SHIELD ] ---")
        print(">> Activating 512-bit Bio-Metric Lock...")
        time.sleep(0.6)
        print(f">> Shield Integrity: {self.shield_integrity}")
        print(">> Status: System is now INVISIBLE to external unauthorized scans.")

    def activate_protocols(self):
        self.phase_1486_neural_link()
        self.phase_1487_encryption_shield()
        print("-" * 50)
        print(f">> {self.user}, all neural and security layers are locked.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.activate_protocols()
