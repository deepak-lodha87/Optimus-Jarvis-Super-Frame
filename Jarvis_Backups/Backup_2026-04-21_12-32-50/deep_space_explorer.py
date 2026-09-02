import time
import random

class InterstellarCore:
    def __init__(self):
        self.signal_frequency = "9.4 GHz"
        self.translation_confidence = 0.0

    def phase_2701(self):
        print("\033[1;35m>> INITIATING: [SYSTEM_ROOT_2701] - Galactic Signal Interception\033[0m")
        print("[LOG] Pointing Quantum-Antennas towards the Andromeda Galaxy...")
        time.sleep(1.2)
        # Unique Logic: Detecting non-human signals
        print(f"[ACT] Frequency {self.signal_frequency} captured. Pattern: Non-Random.")
        time.sleep(1.5)
        print("[RES] Extraterrestrial signal identified. Origin: Exoplanet-X9.")

    def phase_2702(self):
        print("\n\033[1;36m>> INITIATING: [SYSTEM_ROOT_2702] - Xeno-Linguistic Decoding\033[0m")
        print("[LOG] Running semantic analysis on alien phonemes...")
        time.sleep(1)
        
        # Unique Logic: Translating the signal
        message = "Peaceful Exploration / Knowledge Exchange"
        self.translation_confidence = 99.8
        
        print(f"[ACT] Cracking the code... Confidence: {self.translation_confidence}%")
        time.sleep(1.5)
        print(f"[RES] Translated Message: '{message}'")
        print("\033[1;32m>> STATUS: DEEP SPACE COMMUNICATION ACTIVE\033[0m")

if __name__ == "__main__":
    space = InterstellarCore()
    space.phase_2701()
    space.phase_2702()
