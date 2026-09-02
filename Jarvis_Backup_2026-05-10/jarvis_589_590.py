import time
import random

class JarvisPlanetaryInsight:
    def __init__(self):
        self.phase_589 = "589.Deep-Core-Planetary-Scanning-Logic"
        self.phase_590 = "590.Artificial-Gravity-Field-Generator"
        self.gravity_strength = 9.81 # Earth Gravity (m/s^2)
        self.scan_depth_km = 0

    def scan_planet_interior(self, planet_name):
        print(f"\n--- [SYSTEM] Initializing {self.phase_589} ---")
        time.sleep(1)
        print(f"[JARVIS]: Sending Neutrino-Pulses through {planet_name}...")
        
        # ग्रह के अंदर देखने का लॉजिक
        layers = ["Crust", "Upper-Mantle", "Outer-Core", "Inner-Core"]
        for layer in layers:
            self.scan_depth_km += 1500
            print(f" >> [SCANNING]: Penetrating {layer}... Depth: {self.scan_depth_km} km")
            time.sleep(0.8)
            
        resources = ["Molten-Iron", "Diamond-Cores", "Magma-Chambers"]
        found = random.choice(resources)
        print(f"\n[JARVIS]: Scan complete. Detected {found} at the center of {planet_name}.")

    def generate_gravity_field(self, target_g):
        print(f"\n--- [SYSTEM] Initializing {self.phase_590} ---")
        time.sleep(1)
        print(f"[JARVIS]: Adjusting Graviton-Emitter to {target_g}G...")
        
        # खुद की ग्रेविटी बनाने का लॉजिक
        if target_g == 0:
            print("[ACTION]: Weightlessness mode activated. Zero-G environment.")
        else:
            print(f"[ACTION]: Creating localized gravity anchor. Stability: 100%.")
            
        self.gravity_strength = target_g * 9.81
        time.sleep(1.2)
        print(f"[STATUS]: Gravity Field locked at {self.gravity_strength:.2f} m/s^2.")

if __name__ == "__main__":
    jarvis_geo = JarvisPlanetaryInsight()
    # Step 1: किसी ग्रह के आर-पार देखना
    jarvis_geo.scan_planet_interior("Mars-Prime")
    # Step 2: 2G ग्रेविटी पैदा करना (ताकि पैरों के नीचे ज़मीन जैसा महसूस हो)
    jarvis_geo.generate_gravity_field(2.0)
