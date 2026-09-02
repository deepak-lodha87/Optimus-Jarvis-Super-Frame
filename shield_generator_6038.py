import time, secrets, gc

class PlanetaryShieldGenerator:
    def __init__(self):
        self.npsg_id = f"NPSG-{secrets.token_hex(4).upper()}"
        self.shield_integrity = 100 # Percentage (%)
        self.plasma_temp = 12000 # Celsius
        self.nodes = [
            (6034, "Mag-Harmonics", "GENERATING HIGH-FREQUENCY MAGNETIC BUBBLE..."),
            (6035, "Plasma-Stabilize", "IONIZING GAS PARTICLES FOR THERMAL DEFENSE..."),
            (6036, "Kinetic-Absorb", "REDISTRIBUTING IMPACT ENERGY TO BATTERY..."),
            (6037, "Layer-Deflect", "STACKING MULTI-PHASE DEFLECTION BARRIERS..."),
            (6038, "Logic v420", "NPSG-CORE: SHIELD FREQUENCY SYNCHRONIZED.")
        ]

    def intercept_threat(self):
        # Unique logic: Simulating an incoming asteroid or beam
        impact_force = secrets.randbelow(50)
        self.shield_integrity -= (impact_force // 5)
        return impact_force

    def activate_defense(self):
        print(f"\033[1;37m--- NEURAL-PLANETARY-SHIELD-GENERATOR ONLINE (ID: {self.npsg_id}) ---\033[0m")
        colors = [34, 35, 36, 31, 32]
        
        force = self.intercept_threat()
        print(f"\033[1;31mWARNING: Incoming Threat! Impact Force: {force}kN\033[0m")
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[SHIELD:ACTIVE | INTEGRITY:{self.shield_integrity}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mDEFENSE STATUS: THREAT NEUTRALIZED. SHIELD RECHARGING...\033[0m")
        print("\033[1;33mADVICE: OPTIMUS JARVIS HAS CREATED A 360-DEGREE SAFETY BUBBLE.\033[0m")

if __name__ == "__main__":
    shield = PlanetaryShieldGenerator()
    shield.activate_defense()
