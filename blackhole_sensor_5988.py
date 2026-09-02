import time, secrets, gc, math

class BlackHoleSensor:
    def __init__(self):
        self.nbehs_id = f"NBEHS-{secrets.token_hex(4).upper()}"
        self.c = 299792458  # Speed of light (m/s)
        self.nodes = [
            (5984, "Photon-Sphere", "LOCATING ORBITAL LIGHT BENDING RADIUS..."),
            (5985, "Time-Sync", "ADJUSTING FOR RELATIVISTIC TIME DILATION..."),
            (5986, "Stretch-Alert", "MONITORING TIDAL FORCES (SPAGHETTIFICATION)..."),
            (5987, "Horizon-Map", "TRIANGULATING EVENT HORIZON BOUNDARY..."),
            (5988, "Logic v410", "NBEHS-CORE: STABLE ORBIT AROUND SINGULARITY.")
        ]

    def calculate_time_dilation(self, r, rs):
        # Logic: Gravitational time dilation formula
        if r <= rs: return float('inf')
        dilation_factor = math.sqrt(1 - (rs / r))
        return round(dilation_factor, 4)

    def run_horizon_scan(self):
        print(f"\033[1;37m--- NEURAL-BLACK-HOLE-EVENT-HORIZON-SENSOR ONLINE (ID: {self.nbehs_id}) ---\033[0m")
        colors = [34, 35, 31, 36, 32]
        
        # Simulated: Distance from center vs Schwarzschild Radius
        rs = 10.0  # Event Horizon Radius
        r = 15.0   # Current position
        t_factor = self.calculate_time_dilation(r, rs)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[GRAVITY:EXTREME | TIME_FACTOR:{t_factor}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;31mALERT: 1 MINUTE HERE = {round(1/t_factor, 2)} MINUTES ON EARTH.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS MAINTAINING SAFE RADIUS.\033[0m")

if __name__ == "__main__":
    sensor = BlackHoleSensor()
    sensor.run_horizon_scan()
