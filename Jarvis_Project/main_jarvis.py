import os
import time

class OptimusJarvisSuperFrame:
    def __init__(self):
        self.version = "316.0.1"
        self.modules = {
            "Alien Tech": "alien_eng.py",
            "Fabricator": "fabricator.py",
            "Core Bridge": "core_bridge.py"
        }

    def check_integrity(self):
        print(f"--- Launching Optimus Jarvis Super-Frame v{self.version} ---")
        for name, file in self.modules.items():
            if os.path.exists(file):
                print(f"[✓] {name} Module: Linked")
            else:
                print(f"[!] Warning: {name} ({file}) not found.")
        time.sleep(1)

    def material_converter(self):
        print("\n[+] Entering Material Conversion Mode...")
        raw_material = input("Enter available scrap (e.g., Iron, Copper, Battery): ")
        print(f"[*] Processing {raw_material} through Molecular Rearranger...")
        time.sleep(2)
        # Advanced Logic: Converting Earth metals to Exotic ones
        converted = f"Exotic-{raw_material}-Alloy"
        print(f"[SUCCESS] {raw_material} converted to {converted}!")
        print("[INFO] This material can now be used in the Fabricator.")

    def menu(self):
        self.check_integrity()
        print("\n1. Run Alien Simulation\n2. Open Fabricator\n3. Material Converter\n4. Exit")
        choice = input("\nMaster Command >> ")
        
        if choice == "1":
            os.system("python alien_eng.py")
        elif choice == "2":
            os.system("python fabricator.py")
        elif choice == "3":
            self.material_converter()
        elif choice == "4":
            print("Shutting down...")
            exit()

if __name__ == "__main__":
    jarvis = OptimusJarvisSuperFrame()
    while True:
        jarvis.menu()
