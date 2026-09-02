import os
import subprocess

class AutoRepair:
    def __init__(self):
        self.target_file = "jarvis_3d_core.py"

    def scan_for_errors(self):
        print("\033[1;33m[SCANNING]\033[0m Checking core files for bugs...")
        # Ye code files ke andar "IndexError" ka logic check karega
        with open(self.target_file, 'r') as f:
            content = f.read()
            if "N if N > 0 else 0" in content:
                print("\033[1;31m[BUG FOUND]\033[0m Outdated index logic detected.")
                self.apply_patch()
            else:
                print("\033[1;32m[CLEAN]\033[0m No critical bugs found.")

    def apply_patch(self):
        print("\033[1;34m[REPAIRING]\033[0m Applying Phase 80 Emergency Patch...")
        # Purane galat code ko sahi code se badalna
        os.system(f"sed -i 's/N if N > 0 else 0/N % char_len/g' {self.target_file}")
        print("\033[1;32m[FIXED]\033[0m Core integrity restored.")
        os.system('termux-tts-speak "Deepak sir, I have repaired the core rotation bug. You can now run the 3D module safely."')

if __name__ == "__main__":
    repair = AutoRepair()
    repair.scan_for_errors()
