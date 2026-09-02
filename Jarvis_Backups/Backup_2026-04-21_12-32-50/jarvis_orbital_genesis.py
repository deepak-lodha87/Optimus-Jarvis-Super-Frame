import time
import random

class OrbitalGenesis:
    def __init__(self):
        self.user = "Deepak"
        self.phase_29 = "3029 (Orbital Command)"
        self.phase_30 = "3030 (Genesis Completion)"
        self.sat_id = "STAR-LINK-V3"

    def orbital_sync(self):
        print(f"\033[1;35m>> PHASE {self.phase_29}: SYNCHRONIZING WITH ORBITAL PLATFORM <<\033[0m")
        time.sleep(1)
        print(f"\033[1;34m[UPLINK] Connected to {self.sat_id}. GPS/Tactical Lockdown Active.\033[0m")
        print("\033[1;32m[STATUS] Orbital Laser Guidance: READY.\033[0m")

    def complete_genesis(self):
        print(f"\n\033[1;36m>> PHASE {self.phase_30}: FINALIZING THE GENESIS PROTOCOL <<\033[0m")
        time.sleep(1.5)
        # Merging all logic layers into one master engine
        print("\033[1;33m[MERGING] Vehicle Data + Nano-Suit + Neural Link + Orbital Command...\033[0m")
        time.sleep(1)
        print("\033[1;32m[SUCCESS] GENESIS PROTOCOL COMPLETE. Optimus Jarvis is fully Autonomous.\033[0m")

    def run(self):
        print(f"\033[1;32m>> SYSTEM ONLINE: ALL POWER TO THE ARCHITECT. <<\033[0m")
        self.orbital_sync()
        self.complete_genesis()

if __name__ == "__main__":
    genesis_frame = OrbitalGenesis()
    genesis_frame.run()
