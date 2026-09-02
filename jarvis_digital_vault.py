import hashlib

class DigitalVault:
    def __init__(self, owner):
        self.owner = owner
        self.is_locked = True
        self.encryption_key = hashlib.sha256(owner.encode()).hexdigest()

    def authorize_access(self, attempt_key):
        if attempt_key == self.encryption_key:
            print("\033[1;32m[ACCESS GRANTED]\033[0m Welcome back, Deepak sir.")
            self.is_locked = False
        else:
            print("\033[1;31m[SECURITY ALERT]\033[0m Unauthorized buyer detected. Wiping temporary data...")
            self.self_destruct_sequence()

    def self_destruct_sequence(self):
        print("\033[1;33m[ACTION]\033[0m Encrypting Core with 4096-bit layers. Jarvis is now Invisible.")

if __name__ == "__main__":
    vault = DigitalVault("Deepak")
    # Simulating a wrong access attempt (A buyer trying to enter)
    vault.authorize_access("Unknown_Buyer_Key")
