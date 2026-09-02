import time
import random

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.version = "12.0.0"
        self.systems = ["Neural Firewall", "Hydraulic Arms", "AR Engine", "Core Reactor"]

    def self_diagnosis(self):
        print(f"--- [ STARTING SELF-DIAGNOSIS PROTOCOL ] ---")
        for system in self.systems:
            time.sleep(0.4)
            status = random.choice(["OPTIMAL", "STABLE", "SYNCHRONIZED"])
            print(f">> Checking {system}: {status}")
        
        # Checking for any 'Blown Fuses' or Logic Gaps
        print(f">> Circuit Integrity: 100%. No logical fractures detected.")
        print("-" * 45)

    def run_phase_1453(self):
        print(f"--- [ OPTIMUS JARVIS V{self.version} ] ---")
        self.self_diagnosis()
        print(f">> {self.user}, all systems are green. Proceed with construction?")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.run_phase_1453()
