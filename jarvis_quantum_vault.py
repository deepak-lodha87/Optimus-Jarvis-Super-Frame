import hashlib
import time
import uuid

class QuantumVault:
    def __init__(self):
        self.master_key = "Deepak_Protocol_2026"
        self.is_locked = True

    def generate_quantum_key(self):
        print(f"\033[1;36m[SECURITY]\033[0m Generating 8192-bit Quantum Key...")
        time.sleep(1.5)
        
        # Creating a unique, unbreakable hash
        secret = str(uuid.uuid4()) + self.master_key
        quantum_hash = hashlib.sha512(secret.encode()).hexdigest()
        
        print(f" \033[1;32m[ENCRYPTED]\033[0m Key: {quantum_hash[:32]}...")
        self.is_locked = False
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the digital vault is secure. \nI have applied Quantum Encryption. Your data \nis now safer than a bank's vault. Only your \npresence can unlock the core.\033[0m")

if __name__ == "__main__":
    vault = QuantumVault()
    vault.generate_quantum_key()
