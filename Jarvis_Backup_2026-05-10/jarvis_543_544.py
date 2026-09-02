import time
import random

class JarvisOrbitalCommand:
    def __init__(self):
        self.phase_543 = "543.Cosmic-Solar-Radiation-Shielding"
        self.phase_544 = "544.Orbital-Atmospheric-Re-entry-Protocol"
        self.radiation_level = 0.0  # mSv (millisieverts)
        self.hull_temp = 25.0

    def engage_radiation_shield(self, solar_activity):
        print(f"\n--- [SYSTEM] Initializing {self.phase_543} ---")
        time.sleep(1)
        print(f"[JARVIS]: Detecting Solar Flare activity: {solar_activity}...")
        
        # रेडिएशन से बचने के लिए 'Magnetic Bubble' का लॉजिक
        if solar_activity == "High":
            print("[ALERT]: High-energy Gamma and X-rays detected.")
            print("[ACTION]: Generating Lead-infused Nano-Electromagnetic Field.")
            self.radiation_level = 0.01
            time.sleep(1.2)
            print(f"[STATUS]: Radiation exposure minimized to {self.radiation_level} mSv. Pilot safe.")
        else:
            print("[STATUS]: Cosmic radiation within background limits.")

    def start_reentry_sequence(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_544} ---")
        time.sleep(1)
        print("[JARVIS]: Entering Earth's upper atmosphere... Velocity: Mach 25.")
        
        # वायुमंडल में प्रवेश करते समय जलने से बचने का लॉजिक
        reentry_steps = [
            "Deploying Ablative Carbon-Composite Heat Shield.",
            "Activating Active-Liquid-Cooling (ALC) across the chassis.",
            "Adjusting Angle of Attack (AoA) to dissipate plasma friction."
        ]
        
        for step in reentry_steps:
            self.hull_temp += 500
            print(f" >> [RE-ENTRY]: {step} | Hull Temp: {self.hull_temp} C")
            time.sleep(1)
            
        print("\n[JARVIS]: Plasma blackout cleared. Speed dropping to subsonic.")
        print("[STATUS]: Re-entry successful. Touchdown coordinates locked.")

if __name__ == "__main__":
    jarvis_space = JarvisOrbitalCommand()
    # Step 1: सौर विकिरण से सुरक्षा
    jarvis_space.engage_radiation_shield("High")
    # Step 2: अंतरिक्ष से जमीन पर वापस आना (Re-entry)
    jarvis_space.start_reentry_sequence()
