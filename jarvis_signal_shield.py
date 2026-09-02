import time
import random

class SignalJammer:
    def __init__(self):
        self.jamming_active = False

    def neutralize_interference(self):
        print("\033[1;31m[DETECTION] External Radio Interference Detected!\033[0m")
        time.sleep(1)
        print("\033[1;34m[JAMMING] Emitting White-Noise on Hostile Frequency...\033[0m")
        time.sleep(1.5)
        self.jamming_active = True
        return "\033[1;32m[SUCCESS] Hostile Signal Neutralized. Perimeter Secure.\033[0m"

class ECCM_Protocol:
    def frequency_hop(self):
        print("\033[1;35m[ECCM] Initiating Rapid Frequency Hopping Pattern...\033[0m")
        time.sleep(1.2)
        new_freq = f"{random.uniform(2.4, 5.8):.2f} GHz"
        print(f"  • Secure Channel Re-established at: {new_freq}")
        return "\033[1;32m[STABLE] Connection locked. Jamming bypassed.\033[0m"

if __name__ == "__main__":
    jammer = SignalJammer()
    shield = ECCM_Protocol()
    
    print("-" * 50)
    print("   JARVIS SIGNAL SHIELD & COUNTERMEASURES (P3153-54)")
    print("-" * 50)
    
    print(jammer.neutralize_interference())
    print("\n" + shield.frequency_hop())
    print("-" * 50)
