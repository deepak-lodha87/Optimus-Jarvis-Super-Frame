import time
import random

class SatelliteNetwork:
    def __init__(self):
        self.satellites_online = 24 # GPS/GLONASS Constellation
        self.signal_strength = "Excellent"

    def phase_2621(self):
        print("\033[1;36m>> INITIATING: [SYSTEM_ROOT_2621] - Satellite Uplink\033[0m")
        print("[LOG] Handshaking with Orbital Data Nodes...")
        time.sleep(1.2)
        # Unique Logic: Latency simulation
        latency = random.randint(15, 45)
        print(f"[ACT] Synchronizing orbital clock. Latency: {latency}ms")
        time.sleep(1.5)
        print(f"[RES] Uplink Established. Connected to {self.satellites_online} orbital units.")

    def phase_2622(self):
        print("\n\033[1;33m>> INITIATING: [SYSTEM_ROOT_2622] - Global Surveillance\033[0m")
        print("[LOG] Accessing Thermal and Visual Feeds")
        target_coords = "23.5257° N, 75.0455° E" # Ratlam Coordinates
        time.sleep(1)
        print(f"[ACT] Calibrating high-resolution lenses for: {target_coords}")
        time.sleep(1.2)
        print("[RES] Live feed integrated. Jarvis can now monitor global events in real-time.")
        print("\033[1;32m>> STATUS: GLOBAL VISION ACTIVE\033[0m")

if __name__ == "__main__":
    sat = SatelliteNetwork()
    sat.phase_2621()
    sat.phase_2622()
