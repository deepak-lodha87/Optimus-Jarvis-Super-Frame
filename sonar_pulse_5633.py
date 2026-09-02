import time, secrets, gc, math

class OmniDirectionalSonar:
    def __init__(self):
        self.osp_id = f"OSP-{secrets.token_hex(4).upper()}"
        self.sound_speed = 343  # m/s in air
        self.nodes = [
            (5629, "Ping-Emission", "SENDING ULTRASONIC PULSE TRAIN..."),
            (5630, "Echo-Location", "PROCESSING REFLECTION VECTORS..."),
            (5631, "Doppler-Shift", "ANALYZING OBJECT RELATIVE VELOCITY..."),
            (5632, "Density-Scan", "PROFILING TARGET MATERIAL COMPOSITION..."),
            (5633, "Logic v339", "OSP-CORE: SONAR NAVIGATION ACTIVE.")
        ]

    def calculate_distance(self, travel_time):
        # Unique logic: Distance = (Speed * Time) / 2 (for echo)
        return round((self.sound_speed * travel_time) / 2, 3)

    def ping_environment(self):
        print(f"\033[1;37m--- OMNI-DIRECTIONAL-SONAR-PULSE ONLINE (ID: {self.osp_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated micro-time for echo return
            t_start = time.perf_counter()
            time.sleep(0.05) # Simulated delay
            t_end = time.perf_counter()
            
            dist = self.calculate_distance(t_end - t_start)
            print(f"\033[1;{colors[i]}m[RANGE:{dist}m | SYNC:OK] Phase {p_id}: {title} >> {status}\033[0m")
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mOSP STATUS: 360° ENVIRONMENT MAPPING COMPLETE.\033[0m")

if __name__ == "__main__":
    osp = OmniDirectionalSonar()
    osp.ping_environment()
