import time, secrets, gc

class NeuralAsteroidDefense:
    def __init__(self):
        self.naid_id = f"NAID-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5944, "Object-Scan", "SCANNING NEAR-EARTH OBJECTS (NEO) VELOCITY..."),
            (5945, "Impact-Matrix", "CALCULATING COLLISION PROBABILITY VECTORS..."),
            (5946, "Deflection-Sync", "SYNCHRONIZING KINETIC DEFLECTION ANGLES..."),
            (5947, "Impact-Sim", "SIMULATING MOMENTUM TRANSFER..."),
            (5948, "Logic v402", "NAID-CORE: PLANETARY DEFENSE PROTOCOLS ACTIVE.")
        ]

    def check_impact_risk(self, distance, velocity):
        # Unique logic: Risk increases as distance decreases and velocity increases
        risk_score = (velocity / distance) * 100
        return round(min(risk_score, 100.0), 2)

    def run_defense_drill(self):
        print(f"\033[1;37m--- NEURAL-ASTEROID-IMPACT-DEFENSE ONLINE (ID: {self.naid_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        # Simulated Asteroid at 50,000 km traveling at 25,000 km/h
        risk = self.check_impact_risk(50000, 25000)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[RISK:{risk}% | STATUS:ARMED] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        if risk > 40:
            print("\033[1;31mCRITICAL ALERT: IMPACT LIKELY. INITIATING EVASIVE MANEUVERS.\033[0m")
        else:
            print("\033[1;32mSTATUS: CLEAR PATH. NO IMMEDIATE THREAT DETECTED.\033[0m")

if __name__ == "__main__":
    naid = NeuralAsteroidDefense()
    naid.run_defense_drill()
