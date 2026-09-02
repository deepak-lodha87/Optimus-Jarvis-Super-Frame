import time
import random

class SignalDefender:
    def __init__(self):
        self.current_freq = 2.4 # GHz
        self.mode = "PROTECTED"

    def scan_for_jamming(self):
        print(f"\033[1;36m[SCAN]\033[0m Monitoring signal integrity on {self.current_freq} GHz...")
        time.sleep(1.5)
        
        # Simulating interference detection
        interference = random.randint(0, 100)
        
        if interference > 70:
            print("\033[1;31m[!] WARNING: Signal Jammer Detected. Interference High.\033[0m")
            self.hop_frequency()
        else:
            print("\033[1;32m[SAFE]\033[0m Clear Spectrum. Signal Strength: 100%")

    def hop_frequency(self):
        new_freq = round(random.uniform(1.0, 6.0), 2)
        print(f"\033[1;33m[ACTION]\033[0m Initiating Frequency Hopping to {new_freq} GHz...")
        time.sleep(1)
        self.current_freq = new_freq
        print(f" \033[1;32m[SUCCESS]\033[0m Link Restored on Ghost Frequency. We are invisible.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, the jammer has been neutralized. \nI am now rotating through ten thousand \nfrequencies per second. Our link is now \ncompletely unshakeable.\033[0m")

if __name__ == "__main__":
    defender = SignalDefender()
    defender.scan_for_jamming()
