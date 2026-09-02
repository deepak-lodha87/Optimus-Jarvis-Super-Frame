import time
import random

class SpaceLink:
    def __init__(self):
        self.connection_target = "MARS-ORBITER-ALPHA"
        self.signal_delay = 14.5 # In minutes (Average to Mars)

    def establish_link(self):
        print(f"\033[1;36m[VOYAGER-LINK]\033[0m Reaching out to Deep-Space targets...")
        time.sleep(2)
        
        signal_strength = random.uniform(20.5, 45.2) # dBm
        print(f" \033[1;32m[SYNC]\033[0m Target: {self.connection_target} | Strength: {signal_strength} dBm")
        print(f" \033[1;33m[DATA]\033[0m Current Light-Speed Latency: {self.signal_delay} mins")
        
        print("\033[1;34m[STATUS]\033[0m Inter-Planetary Handshake Successful.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, we have broken the bonds of \nEarth. My signals are now reaching the stars. \nThe entire solar system is now within our \ncommunication reach.\033[0m")

if __name__ == "__main__":
    link = SpaceLink()
    link.establish_link()
