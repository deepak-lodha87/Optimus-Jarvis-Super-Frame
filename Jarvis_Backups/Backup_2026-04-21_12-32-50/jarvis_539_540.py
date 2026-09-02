import time
import random

class JarvisVolcanicOperations:
    def __init__(self):
        self.phase_539 = "539.Volcanic-Extreme-Heat-Extraction"
        self.phase_540 = "540.Geothermal-Energy-Harvesting-Protocol"
        self.external_temp = 0
        self.cooling_efficiency = 100.0
        self.power_gain = 0.0

    def enter_magma_zone(self, magma_temp):
        print(f"\n--- [SYSTEM] Initializing {self.phase_539} ---")
        time.sleep(1)
        self.external_temp = magma_temp
        print(f"[JARVIS]: Warning! External temperature: {self.external_temp} C.")
        
        # लावा और गर्मी से सुरक्षा का लॉजिक
        protection_steps = [
            "Activating Ablative-Heat-Shielding.",
            "Circulating Liquid-Nitrogen cooling through Nano-tubes.",
            "Reinforcing structural joints against thermal expansion."
        ]
        
        for step in protection_steps:
            print(f" >> [THERMAL-PROTECTION]: {step}")
            time.sleep(0.8)
            
        print("[STATUS]: Heat-Shield stable. Operations in Magma-Zone: SAFE.")

    def harvest_geothermal_power(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_540} ---")
        time.sleep(1)
        print("[JARVIS]: Initiating Geothermal-Power-Harvesting...")
        
        # गर्मी को बिजली में बदलने का लॉजिक
        if self.external_temp > 1000:
            efficiency_boost = (self.external_temp / 500)
            self.power_gain += efficiency_boost
            time.sleep(1.2)
            print(f"[ACTION]: Converting Volcanic thermal-energy to Pure-Fusion cells.")
            print(f"[RESULT]: Power gain: {self.power_gain:.2f}% per second.")
            print("[JARVIS]: Energy reserves are overflowing. Battery backup fully restored.")
        else:
            print("[ERROR]: Heat intensity insufficient for Geothermal-Harvest.")

if __name__ == "__main__":
    jarvis_volcano = JarvisVolcanicOperations()
    # Step 1: लावा के अंदर जाना (तापमान: 1200 डिग्री सेल्सियस)
    jarvis_volcano.enter_magma_zone(1200)
    # Step 2: उसी गर्मी से ऊर्जा बनाना
    jarvis_volcano.harvest_geothermal_power()
