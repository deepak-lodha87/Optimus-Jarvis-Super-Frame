import time

class JarvisGravityCore:
    def __init__(self):
        self.phase_969 = "969.Graviton-Field-Generator"
        self.phase_960 = "970.Zero-G-Kinetic-Stabilizer"
        self.gravity_status = "Normal"
        self.stabilization_active = False

    def manipulate_gravity(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_969} ---")
        print("[JARVIS]: Adjusting localized graviton density...")
        
        grav_steps = [
            "Activating circular particle accelerator in the base.",
            "Creating an artificial weight-pocket for heavy lifting.",
            "Neutralizing external G-force during sharp turns."
        ]
        
        for step in grav_steps:
            print(f" >> [GRAVITY]: {step}")
            time.sleep(1.2)
            
        self.gravity_status = "Modified"
        print(f"[JARVIS]: Gravity Field: {self.gravity_status}. User can now lift heavy objects effortlessly.")

    def engage_zero_g_mode(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_970} ---")
        print("[JARVIS]: Detecting weightless environment...")
        
        zero_g_steps = [
            "Deploying micro-thrusters for attitude control.",
            "Syncing magnetic boots with the Super-Frame floor.",
            "Stabilizing internal fluid-pressure for the user."
        ]
        
        for step in zero_g_steps:
            print(f" >> [ZERO-G]: {step}")
            time.sleep(1.4)
            
        self.stabilization_active = True
        print("\n[JARVIS]: Zero-G Stabilization Active. Movement is now precise in space.")

if __name__ == "__main__":
    gravity = JarvisGravityCore()
    # Gurutvakarshan ko kam ya zyada karna
    gravity.manipulate_gravity()
    # Bina vajan wali jagah par control pana
    gravity.engage_zero_g_mode()
