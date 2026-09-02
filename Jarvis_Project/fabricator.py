import time
import sys

class JarvisFabricator:
    def __init__(self):
        self.blueprints = {
            "anti_gravity_core": ["Electro-Magnetite", "Plasma-Coil", "Quantum-Processor"],
            "warp_stabilizer": ["Dark-Matter-Filter", "Titanium-Alloy", "Neural-Link"],
            "zero_point_module": ["Vacuum-Crystal", "Energy-Inverter"]
        }
        self.system_health = 100  # Self-Diagnosis Score

    def self_diagnosis(self):
        print("\n[SYSTEM] Running Self-Diagnosis...")
        time.sleep(1)
        # Checking mobile resources (Simulated)
        print("[✓] CPU Thermal: Normal")
        print("[✓] Memory Allocation: Stable")
        print(f"[✓] System Integrity: {self.system_health}%")
        return True

    def start_fabrication(self, item_name):
        if item_name in self.blueprints:
            print(f"\n[+] Starting Fabrication: {item_name.replace('_', ' ').upper()}")
            required = self.blueprints[item_name]
            for component in required:
                print(f"    - Integrating Component: {component}...")
                time.sleep(1.2)
            print(f"[SUCCESS] {item_name.upper()} has been successfully synthesized.")
        else:
            print(f"[ERROR] Blueprint for '{item_name}' not found in database.")

    def run(self):
        if self.self_diagnosis():
            print("\n--- Optimus Jarvis Fabrication Menu ---")
            print("1. Anti-Gravity Core")
            print("2. Warp Stabilizer")
            print("3. Zero-Point Module")
            choice = input("\nSelect item to fabricate (1-3): ")
            
            items = {"1": "anti_gravity_core", "2": "warp_stabilizer", "3": "zero_point_module"}
            target = items.get(choice)
            if target:
                self.start_fabrication(target)
            else:
                print("Invalid Selection.")

if __name__ == "__main__":
    fab = JarvisFabricator()
    fab.run()
