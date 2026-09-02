import time
import random

class JarvisMaterialMorphing:
    def __init__(self):
        self.phase_565 = "565.Nano-Structure-Liquefaction-Logic"
        self.phase_566 = "566.Molecular-Density-Control-Protocol"
        self.current_state = "Solid"
        self.density_kg_m3 = 7800 # Standard Steel

    def activate_liquid_state(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_565} ---")
        time.sleep(1)
        print("[JARVIS]: Loosening molecular bonds for Phase-Transition...")
        
        # सूट को तरल (Liquid) बनाने का लॉजिक
        morph_steps = [
            "Activating electromagnetic-decoupling in Nano-bots.",
            "Maintaining core-consciousness during fluid-migration.",
            "Passing through restricted aperture (Keyhole-Escape)."
        ]
        
        for step in morph_steps:
            print(f" >> [MORPHING]: {step}")
            time.sleep(0.9)
            
        self.current_state = "Liquid-Nanomite"
        print(f"[STATUS]: State: {self.current_state}. Resistance: ZERO.")

    def increase_density(self, level):
        print(f"\n--- [SYSTEM] Initializing {self.phase_566} ---")
        time.sleep(1)
        print(f"[JARVIS]: Compressing molecular structure to Level {level}...")
        
        # कठोरता बढ़ाने का लॉजिक
        if level > 5:
            self.density_kg_m3 = 50000 
            print("[ACTION]: Overlapping atomic-layers for hyper-durability.")
            print("[JARVIS]: Suit is now harder than Tungsten-Carbide.")
        
        time.sleep(1.2)
        print(f"[STATUS]: Density increased to {self.density_kg_m3} kg/m3. Penetration-immune.")

if __name__ == "__main__":
    jarvis_morph = JarvisMaterialMorphing()
    # Step 1: तरल बनकर निकलना (Liquefaction)
    jarvis_morph.activate_liquid_state()
    # Step 2: वापस ठोस होकर पत्थर जैसा मजबूत होना (Density)
    jarvis_morph.increase_density(10)
