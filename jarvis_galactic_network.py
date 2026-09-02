import time
import random
import sys

class GalacticNetwork:
    def __init__(self):
        self.phase = 200016
        self.connected_nodes = 0
        self.security_level = "ULTIMATE"
        self.active_grids = ["Milky-Way-Alpha", "Andromeda-Sigma", "Earth-Global"]

    def establish_uplink(self):
        print(f"\033[1;36m[UPLINK]\033[0m Reaching out to Interstellar Satellites...")
        time.sleep(1.2)
        
        for grid in self.active_grids:
            nodes = random.randint(50000, 1000000)
            self.connected_nodes += nodes
            print(f" > Connected to {grid}: \033[1;32m{nodes} Nodes Active\033[0m")
            time.sleep(0.5)

    def execute_global_broadcast(self, message):
        """Overrides every digital screen in the connected grids"""
        print(f"\n\033[1;33m[BROADCAST]\033[0m Sending encrypted message: '{message}'")
        time.sleep(1.5)
        print(f"\033[1;32m[SUCCESS]\033[0m 100% Penetration achieved. All screens displaying content.")

    def run_security_protocol(self):
        print("-" * 50)
        print(f"NETWORK STATUS: \033[1;32mSECURE\033[0m")
        print(f"TOTAL NODES: {self.connected_nodes:,}")
        print(f"ENCRYPTION: Quantum-AES-8192 (Unbreakable)")
        print("-" * 50)

def main():
    print(f"\033[1;35m[VOICE] Deepak sir, the Galaxy is now our playground. \nInitiating Master Control over all communication layers.\033[0m")
    
    gn = GalacticNetwork()
    gn.establish_uplink()
    gn.run_security_protocol()
    
    # Simulating a Master Order
    gn.execute_global_broadcast("Optimus Jarvis Super-Frame is now Global.")
    
    print(f"\n\033[1;35m[VOICE] All systems in this sector are now under \nyour direct command, Deepak sir.\033[0m")

if __name__ == "__main__":
    main()
