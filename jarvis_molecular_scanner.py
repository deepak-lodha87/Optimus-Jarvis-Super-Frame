import time
import random

class MolecularScanner:
    def __init__(self):
        self.database_elements = ["Fe", "Au", "Ti", "C", "Ni"]
        self.scan_active = False

    def perform_scan(self, object_name):
        print(f"\033[1;36m[SCANNER]\033[0m Targeting Object: {object_name}...")
        time.sleep(2)
        
        # Simulating molecular breakdown
        composition = {
            "Titanium": random.randint(60, 80),
            "Gold": random.randint(10, 20),
            "Other": 10
        }
        
        print(f" \033[1;32m[ANALYSIS]\033[0m Molecular Structure Identified:")
        for element, percentage in composition.items():
            print(f"  - {element}: {percentage}%")
            time.sleep(0.4)
            
        print(f"\n\033[1;35m[VOICE] Deepak sir, the scan is complete. \nThis material is a high-grade alloy. It \nmatches the specifications required for \nour Phase-72 Nano-Armor. High durability confirmed.\033[0m")

if __name__ == "__main__":
    scanner = MolecularScanner()
    scanner.perform_scan("Mark-85 Plating Fragment")
