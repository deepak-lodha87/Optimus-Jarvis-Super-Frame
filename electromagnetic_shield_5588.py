import time, secrets, gc, cmath

class ElectromagneticShieldGrid:
    def __init__(self):
        self.esg_id = f"ESG-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5584, "Faraday-Cage", "ISOLATING INTERNAL CIRCUITRY..."),
            (5585, "Ionic-Damping", "NEUTRALIZING EXTERNAL INTERFERENCE..."),
            (5586, "Flux-Mapping", "CALCULATING MAGNETIC DENSITY FIELDS..."),
            (5587, "Signal-Camouflage", "ENCRYPTING EMISSION SIGNATURES..."),
            (5588, "Logic v330", "ESG-CORE: ELECTROMAGNETIC SHIELD ACTIVE.")
        ]

    def calculate_impedance(self, frequency):
        # Unique logic: Complex math for wave resistance
        # Z = R + jX (Real + Imaginary impedance)
        z = cmath.rect(1.0, math.radians(frequency))
        return z

    def activate_shield(self):
        print(f"\033[1;37m--- ELECTROMAGNETIC-SHIELDING-GRID ONLINE (ID: {self.esg_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            freq = secrets.randbelow(5000) # Simulated MHz
            imp = self.calculate_impedance(freq)
            print(f"\033[1;{colors[i]}m[IMP:{imp.real:.2f}Ω | FREQ:{freq}MHz] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mESG STATUS: HARDWARE PROTECTED AGAINST EXTERNAL EMP ATTACKS.\033[0m")

import math
if __name__ == "__main__":
    esg = ElectromagneticShieldGrid()
    esg.activate_shield()
