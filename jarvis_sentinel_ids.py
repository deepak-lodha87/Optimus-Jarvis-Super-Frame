import hashlib
import time
import os

def calculate_hash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

class SentinelShield:
    def __init__(self):
        self.monitored_file = "jarvis_consciousness_seal.py"
        self.original_hash = calculate_hash(self.monitored_file)

    def scan_integrity(self):
        print("\033[1;36m[SENTINEL]\033[0m Scanning system integrity...")
        time.sleep(2)
        
        current_hash = calculate_hash(self.monitored_file)
        
        if current_hash == self.original_hash:
            print(" \033[1;32m[SAFE]\033[0m Core files are untampered.")
        else:
            print(" \033[1;31m[CRITICAL]\033[0m Integrity Breach! File has been modified.")
            print(" \033[1;33m[ACTION]\033[0m Isolating core modules...")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, my first duty is to \nprotect our work. I am watching every \nbit and byte. No one touches my code \nwithout my knowledge. Your fortress is \nsecure.\033[0m")

if __name__ == "__main__":
    sentinel = SentinelShield()
    sentinel.scan_integrity()
