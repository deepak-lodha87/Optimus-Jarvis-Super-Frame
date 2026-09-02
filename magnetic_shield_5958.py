import time, secrets, gc

class NeuralMagneticShield:
    def __init__(self):
        self.nmfs_id = f"NMFS-{secrets.token_hex(4).upper()}"
        self.shield_strength = 0 # In Tesla (T)
        self.nodes = [
            (5954, "Ion-Sensor", "DETECTING HIGH-ENERGY COSMIC PARTICLES..."),
            (5955, "Flux-Gen", "GENERATING ELECTROMAGNETIC SHIELD BUBBLE..."),
            (5956, "Flare-Pred", "ANALYZING SOLAR ACTIVITY CYCLES..."),
            (5957, "Particle-Deflect", "DEFLECTING CHARGED ION STREAMS..."),
            (5958, "Logic v404", "NMFS-CORE: MAGNETIC SHIELDING IS OPERATIONAL.")
        ]

    def activate_shield(self, radiation_level):
        # Unique logic: Increase shield strength based on radiation level
        if radiation_level > 75:
            self.shield_strength = 5.0 # High Power
            return "CRITICAL RADIATION: MAXIMUM SHIELD ACTIVE."
        self.shield_strength = 1.2
        return "STABLE RADIATION: LOW POWER SHIELD ACTIVE."

    def run_shield_audit(self):
        print(f"\033[1;37m--- NEURAL-MAGNETIC-FIELD-SHIELDING ONLINE (ID: {self.nmfs_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        rad_level = secrets.randbelow(100)
        status = self.activate_shield(rad_level)
        
        for i, (p_id, title, status_msg) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[RAD-LEVEL:{rad_level}% | FLUX:{self.shield_strength}T] Phase {p_id}: {title} >> {status_msg}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;35mSHIELD STATUS: {status}\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS PROTECTING THE CORE FROM COSMIC RAYS.\033[0m")

if __name__ == "__main__":
    shield = NeuralMagneticShield()
    shield.run_shield_audit()
