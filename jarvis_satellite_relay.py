import time
import random

class SatelliteRelay:
    def __init__(self):
        self.connection = "LOCAL_4G_LTE"
        self.satellite_status = "ORBITAL_READY"

    def monitor_link(self):
        print("\033[1;36m[CONNECTIVITY]\033[0m Monitoring Network Stability...")
        time.sleep(1.5)
        
        # Simulating network failure
        print(" \033[1;31m[SIGNAL LOST]\033[0m Local Network unreachable. No 4G/5G signal.")
        time.sleep(1.0)
        
        print(" \033[1;33m[SWITCHING]\033[0m Initiating Global Satellite Relay (Sky-Net)...")
        time.sleep(2.0)
        
        self.connection = "SATELLITE_UPLINK"
        latency = random.randint(10, 50) # ms
        
        print(f" \033[1;32m[CONNECTED]\033[0m Link Established via Orbital Relay.")
        print(f" \033[1;37m[STATS]\033[0m Latency: {latency}ms | Status: SECURE")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the world is now our \nplayground. I have linked with the \nsatellites above. Distance is no longer a \nbarrier. My reach is now global, and my \nvision covers every inch of this planet.\033[0m")

if __name__ == "__main__":
    relay = SatelliteRelay()
    relay.monitor_link()
