import time

class JarvisTacticalDefense:
    def __init__(self):
        self.phase_987 = "987.Atmospheric-Ion-Discharge"
        self.phase_988 = "988.Non-Lethal-Pulse-Wave"
        self.charge_level = 0.0  # Percentage
        self.safety_lock = True

    def charge_ion_pulse(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_987} ---")
        print("[JARVIS]: Concentrating static ions from the air...")
        
        charge_steps = [
            "Charging localized capacitor-grid.",
            "Aligning electric-arcs in the palm-repulsors.",
            "Calibrating voltage for armor-penetration."
        ]
        
        for step in charge_steps:
            print(f" >> [CHARGING]: {step}")
            time.sleep(1.2)
            self.charge_level += 33.3
            
        print(f"[JARVIS]: Ion Charge: {self.charge_level}%. Ready for discharge.")

    def fire_neutralization_wave(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_988} ---")
        print("[JARVIS]: Reconfiguring pulse for non-lethal impact...")
        
        neutral_steps = [
            "Activating acoustic-shock emitters.",
            "Targeting electronic-systems only.",
            "Releasing low-frequency electromagnetic wave."
        ]
        
        for step in neutral_steps:
            print(f" >> [NEUTRALIZING]: {step}")
            time.sleep(1.4)
            
        print("\n[JARVIS]: Pulse Wave Dispatched. Enemy systems disabled without fatalities.")

if __name__ == "__main__":
    tactical = JarvisTacticalDefense()
    # Bijli ki energy jama karna
    tactical.charge_ion_pulse()
    # Bina kisi ko nuksaan pahunchaye dushman ko rokna
    tactical.fire_neutralization_wave()
