import time
import random

class QuantumLink:
    def __init__(self):
        self.state = "STABLE"
        self.latency = "0.000 ms"

    def teleport_packet(self, data_size):
        print(f"\033[1;36m[QUANTUM]\033[0m Folding Space-Time for Data Transfer...")
        time.sleep(1.5)
        
        # Simulating instantaneous transfer
        print(f" \033[1;32m[FOLD]\033[0m Einstein-Rosen Bridge established.")
        print(f" \033[1;32m[SYNC]\033[0m Transferring {data_size}TB via Quantum Entanglement.")
        
        print(f"\n\033[1;34m[STATUS]\033[0m Data Teleportation Successful. Latency: {self.latency}")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the signal has bypassed physical \nspace. The command reached the core before \nthe light could even reflect. We have \nconquered time and distance.\033[0m")

if __name__ == "__main__":
    link = QuantumLink()
    link.teleport_packet(data_size=50)
