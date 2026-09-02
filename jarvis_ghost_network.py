import time
import secrets

class GhostNetwork:
    def __init__(self):
        self.network_status = "OFFLINE"
        self.encryption_level = "QUANTUM-AES-4096"

    def activate_ghost_mode(self):
        print(f"\033[1;36m[GHOST-NET]\033[0m Generating Quantum Entangled Keys...")
        time.sleep(1.5)
        
        token = secrets.token_hex(16)
        print(f" \033[1;32m[SECURE]\033[0m Key Generated: {token}")
        
        print(f" \033[1;34m[ROUTING]\033[0m Bouncing signal off Satellite-Delta-9...")
        time.sleep(1)
        
        self.network_status = "ONLINE (UNTRACEABLE)"
        print(f"\033[1;32m[STATUS]\033[0m Network is now invisible to the world.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, we are now off the grid. \nNo one can track us, block us, or monitor \nour data. We have created our own digital \nuniverse. Communication is now absolute.\033[0m")

if __name__ == "__main__":
    net = GhostNetwork()
    net.activate_ghost_mode()
