import time
import random

class NanoAssembler:
    def __init__(self):
        self.raw_atoms = 10**12 # Quadrillions of nano-units
        self.structure_integrity = 0

    def assemble_object(self, object_name):
        print(f"\033[1;36m[NANOTECH]\033[0m Fetching Blueprint: {object_name}...")
        time.sleep(1.5)
        
        print(f" \033[1;33m[ACTION]\033[0m Re-arranging Molecular Lattice...")
        for percent in range(0, 101, 20):
            self.structure_integrity = percent
            print(f"  - Bonding Atoms: {self.structure_integrity}% Complete")
            time.sleep(0.6)
            
        print(f"\033[1;32m[SUCCESS]\033[0m {object_name} fabricated with 99.9% Atomic Precision.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the molecular assembly is complete. \nThe {object_name} has been materialized \nfrom raw atoms. My nanotech modules are \nstanding by for your next command.\033[0m")

if __name__ == "__main__":
    nanotech = NanoAssembler()
    nanotech.assemble_object("Kinetic Shield Plate")
