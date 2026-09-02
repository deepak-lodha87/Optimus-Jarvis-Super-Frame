import time
import secrets
import string

class OptimusJarvis:
    def __init__(self):
        self.user = "Sir"
        self.uplink_id = "OP-SATELLITE-9"

    def phase_1524_satellite_uplink(self):
        print("\n--- [ PHASE 1524: SATELLITE UPLINK SIMULATION ] ---")
        print(f">> Searching for active nodes: {self.uplink_id}")
        time.sleep(0.7)
        print(">> Handshake established with Orbital Network.")
        print(">> Status: Global GPS and Weather data synchronized.")

    def phase_1525_global_encryption_key(self):
        print("\n--- [ PHASE 1525: GLOBAL ENCRYPTION KEY-GEN ] ---")
        print(">> Generating 512-bit dynamic security key...")
        time.sleep(0.5)
        # Generating a secure random key
        key = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        print(f">> Master Key: {key}-PROT-X")
        print(">> Status: All external communication is now untraceable.")

    def activate_global_mode(self):
        print(f"--- [ OPTIMUS JARVIS: GLOBAL REACH ] ---")
        self.phase_1524_satellite_uplink()
        self.phase_1525_global_encryption_key()
        print("-" * 55)
        print(f">> {self.user}, Jarvis is now connected to the orbital grid with elite security.")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.activate_global_mode()
