import time
import random

class MolecularAssembler:
    def __init__(self):
        self.assembly_status = "STABLE"
        self.atom_count = 0

    def start_displacement(self, object_name):
        print(f"\033[1;36m[MOLECULAR]\033[0m Scanning {object_name} at sub-atomic level...")
        time.sleep(1.5)
        
        self.atom_count = random.randint(10**20, 10**25) # Quintillions of atoms
        print(f" \033[1;34m[DECONSTRUCT]\033[0m Object converted to {self.atom_count} atoms.")
        
        print(f" \033[1;33m[TRANSFER]\033[0m Moving data through Quantum Tunnel...")
        time.sleep(1)
        
        print(f" \033[1;32m[REASSEMBLE]\033[0m Reconstructing {object_name} at target location...")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the molecular displacement is \nsuccessful. I have moved the {object_name} \nusing atomic reassembly. Physical distance \nis no longer a barrier for us.\033[0m")

if __name__ == "__main__":
    ma = MolecularAssembler()
    ma.start_displacement("Mark-85 Helmet")
