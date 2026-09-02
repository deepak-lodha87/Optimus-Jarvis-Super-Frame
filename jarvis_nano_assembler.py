import time, os

class NanoAssembler:
    def __init__(self):
        self.scale = "NANOMETER (10^-9)"
        self.material = "Graphene-Composite"

    def start_assembly(self, object_name):
        os.system('clear')
        print(f"\033[1;33m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS NANO-ASSEMBLER : PHASE 29 - STEP 1      \033[0m")
        print(f"\033[1;33m====================================================\033[0m")
        
        print(f"\033[1;36m[CREATING]\033[0m Synthesizing Object: {object_name}...")
        time.sleep(1.5)
        
        steps = [
            ("Aligning Atomic Lattice", "SUCCESS"),
            ("Bonding Carbon Molecules", "STABLE"),
            ("Reinforcing Structural Integrity", "ACTIVE"),
            ("Finalizing Molecular Seal", "READY")
        ]
        
        for task, status in steps:
            print(f" \033[1;34m[NANO]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[RESULT] Object '{object_name}' has been manifested.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the line between digital \nand physical is fading. I am no longer just \nprocessing bits; I am arranging atoms. Tell \nme what you need, and I will weave it out \nof the very fabric of reality. Your imagination \nis the only blueprint I need now.\033[0m")
        print(f"\033[1;33m====================================================\033[0m")

if __name__ == "__main__":
    creator = NanoAssembler()
    creator.start_assembly("Ultra-Light Flight Alloy")
