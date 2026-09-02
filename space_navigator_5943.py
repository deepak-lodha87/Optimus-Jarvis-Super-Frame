import time, secrets, gc, math

class NeuralSpaceNavigator:
    def __init__(self):
        self.nsto_id = f"NSTO-{secrets.token_hex(4).upper()}"
        self.G = 6.67430e-11 # Universal Gravitational Constant
        self.M = 5.972e24    # Mass of Earth (kg)
        self.R = 6371000     # Earth Radius (m)
        self.nodes = [
            (5939, "Orbital-Sim", "CALCULATING GRAVITATIONAL PULL VECTORS..."),
            (5940, "Vacuum-Sync", "ADJUSTING COLD-GAS THRUSTER OUTPUT..."),
            (5941, "Rad-Shield", "MONITORING COSMIC IONIZATION LEVELS..."),
            (5942, "Inter-Planetary", "MAPPING ASTRO-COORDINATE LATTICE..."),
            (5943, "Logic v401", "NSTO-CORE: SPACE TRAJECTORY OPTIMIZED.")
        ]

    def calculate_orbital_velocity(self, altitude):
        # Unique logic: Calculating Velocity needed to stay in orbit
        r = self.R + altitude
        velocity = math.sqrt((self.G * self.M) / r)
        return round(velocity, 2)

    def run_space_mission(self):
        print(f"\033[1;37m--- NEURAL-SPACE-TRAJECTORY-OPTIMIZER ONLINE (ID: {self.nsto_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        alt = 400000 # ISS Altitude (400km)
        v = self.calculate_orbital_velocity(alt)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[SPACE:READY | ALT:{alt/1000}km] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mORBITAL VELOCITY REQUIRED: {v} m/s\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS NOW OPERATIONAL BEYOND THE ATMOSPHERE.\033[0m")

if __name__ == "__main__":
    nav = NeuralSpaceNavigator()
    nav.run_space_mission()
