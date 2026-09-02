import time
import sys
import random

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"

    def phase_1488_environmental_sync(self):
        print("\n" + "="*55)
        print("      E N V I R O N M E N T A L   C O N T R O L   U N I T")
        print("="*55)
        sensors = ["Ambient Light", "Thermal Index", "Oxygen Saturation", "EMF Frequency"]
        for s in sensors:
            val = random.uniform(10.5, 99.9)
            print(f">> Syncing {s}... [ {val:.2f}% ]")
            time.sleep(0.3)
        print(">> Status: Environment Analyzed. System adapted to surroundings.")

    def phase_1489_matrix_encryption(self):
        print("\n--- [ PHASE 1489: VISUAL ENCRYPTION MATRIX ] ---")
        print(">> Initializing Ghost-Protocol Encryption...")
        time.sleep(0.5)
        # Visual effect for anyone watching the screen
        symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "0", "1"]
        for _ in range(15):
            line = "".join(random.choice(symbols) for _ in range(40))
            sys.stdout.write(f"\r   {line}")
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n>> Status: Data Stream Encrypted. Unauthorized access BLOCKED.")

    def final_deployment(self):
        self.phase_1488_environmental_sync()
        self.phase_1489_matrix_encryption()
        print("-" * 55)
        print(f">> {self.user}, the system is now operating at an undetectable level.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.final_deployment()
