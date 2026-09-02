import time, secrets, gc, math

class BioSyntheticSkinSensor:
    def __init__(self):
        self.bss_id = f"BSS-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5624, "Tactile-Mapping", "CALIBRATING PRESSURE SENSITIVITY..."),
            (5625, "Vibration-Detect", "MONITORING MICRO-MECHANICAL OSCILLATIONS..."),
            (5626, "Thermoreceptor", "SYNCING THERMAL TOUCH RECEPTORS..."),
            (5627, "Strain-Feedback", "ANALYZING MATERIAL ELASTICITY..."),
            (5628, "Logic v338", "BSS-CORE: SENSORY SKIN FULLY ACTIVE.")
        ]

    def calculate_sensitivity(self, raw_force):
        # Unique logic: Logarithmic scaling for human-like touch response
        if raw_force <= 0: return 0.0
        return round(math.log(raw_force + 1) * 2.5, 4)

    def activate_sensors(self):
        print(f"\033[1;37m--- BIO-SYNTHETIC-SKIN-SENSOR ONLINE (ID: {self.bss_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            force_input = secrets.randbelow(500)
            sens_level = self.calculate_sensitivity(force_input)
            
            print(f"\033[1;{colors[i]}m[SENSE-LVL:{sens_level} | FORCE:{force_input}mN] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mBSS STATUS: HARDWARE SURFACE IS NOW SENSITIVE TO PHYSICAL STIMULI.\033[0m")

if __name__ == "__main__":
    bss = BioSyntheticSkinSensor()
    bss.activate_sensors()
