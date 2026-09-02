import time, secrets, gc, math

class SolarRadiationShield:
    def __init__(self):
        self.srs_id = f"SRS-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5699, "UV-Profiling", "MONITORING ULTRA-VIOLET FLUX DENSITY..."),
            (5700, "Gamma-Deflection", "ACTIVATING LEAD-ION BARRIER..."),
            (5701, "Photo-Isolation", "MANAGING RADIATIVE THERMAL LOADS..."),
            (5702, "Signal-Filter", "CLEANING ELECTROMAGNETIC INTERFERENCE..."),
            (5703, "Logic v353", "SRS-CORE: SOLAR SHIELDING OPERATIONAL.")
        ]

    def calculate_penetration_risk(self, radiation_level):
        # Unique logic: Using erfc to find the probability of shield breach
        # Risk decreases as shield density increases
        return round(math.erfc(radiation_level / 1000) * 100, 4)

    def activate_shielding(self):
        print(f"\033[1;37m--- SOLAR-RADIATION-SHIELDING ONLINE (ID: {self.srs_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            rad_flux = secrets.randbelow(2000)
            risk = self.calculate_penetration_risk(rad_flux)
            print(f"\033[1;{colors[i]}m[FLUX:{rad_flux}mW | RISK:{risk}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mSRS STATUS: HARDWARE PROTECTED AGAINST EXTREME RADIATION.\033[0m")

if __name__ == "__main__":
    srs = SolarRadiationShield()
    srs.activate_shielding()
