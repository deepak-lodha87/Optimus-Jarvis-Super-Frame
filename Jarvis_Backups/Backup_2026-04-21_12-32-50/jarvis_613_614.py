import time
import random

class JarvisPrimePropulsion:
    def __init__(self):
        self.phase_613 = "613.Dark-Matter-Quantum-Engine-Core"
        self.phase_614 = "614.Antimatter-Annihilation-Thruster-Logic"
        self.engine_stability = 100.0
        self.velocity_kms = 0.0

    def stabilize_dark_matter(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_613} ---")
        time.sleep(1)
        print("[JARVIS]: Harvesting Dark-Matter particles from the local void...")
        
        # डार्क मैटर इंजन का लॉजिक
        harvest_steps = [
            "Capturing Weakly Interacting Massive Particles (WIMPs).",
            "Injecting particles into the Singularity-Chamber.",
            "Converting gravitational-pull into usable Voltage."
        ]
        
        for step in harvest_steps:
            print(f" >> [ENGINE]: {step}")
            time.sleep(0.9)
            
        print("[STATUS]: Dark-Matter Engine is PURRING. Infinite energy source locked.")

    def engage_antimatter_thrust(self, target_speed_pct):
        print(f"\n--- [SYSTEM] Initializing {self.phase_614} ---")
        time.sleep(1)
        print(f"[JARVIS]: Preparing Antimatter-Matter reaction for {target_speed_pct}% light-speed...")
        
        # एंटी-मैटर थ्रस्टर का लॉजिक
        print("[ACTION]: Releasing Positron-stream into the reaction-nozzle.")
        time.sleep(1.5)
        
        # Speed of light is ~300,000 km/s
        self.velocity_kms = (target_speed_pct / 100) * 299792
        print(f" >> [JARVIS]: Total Annihilation achieved. Current Velocity: {self.velocity_kms:.2f} km/s.")
        print("[STATUS]: Interstellar travel initiated. Destination: Alpha Centauri.")

if __name__ == "__main__":
    jarvis_prop = JarvisPrimePropulsion()
    # Step 1: डार्क मैटर इंजन चालू करना
    jarvis_prop.stabilize_dark_matter()
    # Step 2: प्रकाश की 50% गति से उड़ना
    jarvis_prop.engage_antimatter_thrust(50)
