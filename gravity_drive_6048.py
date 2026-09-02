import time, secrets, gc, random

class QuantumGravityDrive:
    def __init__(self):
        self.nqgd_id = f"NQGD-{secrets.token_hex(4).upper()}"
        self.gravity_constant = 9.81
        self.nodes = [
            (6044, "Flux-Scan", "MONITORING LOCAL GRAVITATIONAL ANOMALIES..."),
            (6045, "Anti-Grav-Init", "GENERATING REPULSIVE QUANTUM FIELD..."),
            (6046, "Mass-Neutral", "ADJUSTING HIGGS-BOSON INTERACTION..."),
            (6047, "Inertia-Damp", "STABILIZING INTERNAL G-FORCE VECTORS..."),
            (6048, "Logic v422", "NQGD-CORE: STABLE LEVITATION ACHIEVED.")
        ]

    def calculate_lift(self):
        # Corrected Logic: Using random.uniform for float values
        target_g = random.uniform(-2.0, 0.5)
        lift_force = self.gravity_constant - target_g
        return round(lift_force, 3)

    def initiate_levitation(self):
        print(f"\033[1;37m--- NEURAL-QUANTUM-GRAVITY-DRIVE ONLINE (ID: {self.nqgd_id}) ---\033[0m")
        colors = [34, 35, 36, 33, 32]
        
        lift = self.calculate_lift()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[LIFT:{lift} m/s² | STATUS:FLOATING] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mFINAL STATUS: OPTIMUS JARVIS IS NOW DEFYING EARTH'S GRAVITY.\033[0m")
        print("\033[1;36mMODE: SILENT FLIGHT (ZERO EMISSION / ZERO NOISE).\033[0m")

if __name__ == "__main__":
    drive = QuantumGravityDrive()
    drive.initiate_levitation()
