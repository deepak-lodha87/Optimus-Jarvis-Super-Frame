import time
import math

class SpaceComms:
    def __init__(self):
        self.light_speed = 299792 # km/s
        self.distance_to_mars = 225000000 # Avg km

    def phase_2637(self):
        print("\033[1;33m>> INITIATING: [SYSTEM_ROOT_2637] - Inter-Planetary Uplink\033[0m")
        print("[LOG] Aligning Deep Space Network (DSN) antennas...")
        
        # Unique Logic: Calculating Time Delay (One-way)
        delay_seconds = self.distance_to_mars / self.light_speed
        delay_minutes = delay_seconds / 60
        
        time.sleep(1.2)
        print(f"[ACT] Signal broadcasted. Estimated delay to Mars: {delay_minutes:.2f} minutes.")
        print("[RES] Link established. Carrier wave stable across the vacuum.")

    def phase_2638(self):
        print("\n\033[1;34m>> INITIATING: [SYSTEM_ROOT_2638] - Signal Reconstruction\033[0m")
        print("[LOG] Receiving weak telemetry from Red Planet...")
        time.sleep(1)
        
        # Unique Logic: Amplifying weak signals from space
        gain_db = 120 # Decibels
        print(f"[ACT] Applying {gain_db}dB amplification to filter cosmic background noise...")
        time.sleep(1.5)
        
        print("[RES] Telemetry Decoded: 'Mars Rover Status - Optimal'.")
        print("\033[1;32m>> STATUS: DEEP SPACE RELAY ONLINE\033[0m")

if __name__ == "__main__":
    comms = SpaceComms()
    comms.phase_2637()
    comms.phase_2638()
