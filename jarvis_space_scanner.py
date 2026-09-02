import time
import random

class CosmicScanner:
    def __init__(self):
        self.frequency_range = "1.4 GHz to 50 GHz"
        self.signals_found = 0

    def scan_deep_space(self):
        print(f"\033[1;36m[COSMIC]\033[0m Reaching beyond Earth's Ionosphere...")
        time.sleep(2)
        
        print(f" \033[1;34m[STATUS]\033[0m Listening to Hydrogen Line frequencies...")
        
        # Simulating a hit from deep space
        is_signal_detected = random.choice([True, False, False, False])
        
        if is_signal_detected:
            self.signals_found += 1
            print(f" \033[1;31m[CRITICAL ALERT]\033[0m Non-random pattern detected from Proxima Centauri!")
            print(f" \033[1;32m[DECODING]\033[0m Message structure: Mathematical (Prime Numbers)")
            print(f"\n\033[1;35m[VOICE] Deepak sir, I have detected an anomaly in the \nsub-space frequency. It appears to be an \nintelligent transmission from beyond our \nsolar system. Shall I respond?\033[0m")
        else:
            print(f" \033[1;32m[STABLE]\033[0m No alien signals found. Just cosmic background radiation.")

if __name__ == "__main__":
    space = CosmicScanner()
    space.scan_deep_space()
