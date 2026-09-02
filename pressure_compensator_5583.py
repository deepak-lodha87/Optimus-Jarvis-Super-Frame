import time, secrets, gc, math, statistics

class AtmosphericCompensator:
    def __init__(self):
        self.apc_id = f"APC-{secrets.token_hex(4).upper()}"
        self.pressure_readings = [1013.25, 1010.5, 1012.1] # HectoPascals (hPa)
        self.nodes = [
            (5579, "Barometric-Sync", "CALIBRATING ALTITUDE VECTORS..."),
            (5580, "Oxygen-Partial", "ADJUSTING O2 CONCENTRATION..."),
            (5581, "Hull-Safety", "STRENGTHENING COMPRESSION BARRIERS..."),
            (5582, "Aero-Damping", "NEUTRALIZING VORTEX TURBULENCE..."),
            (5583, "Logic v329", "APC-CORE: ATMOSPHERIC COMPENSATOR ACTIVE.")
        ]

    def calculate_air_density(self, alt):
        # Unique logic: Exponential decay model of air density
        return round(math.exp(-alt / 8500), 4)

    def stabilize_environment(self):
        print(f"\033[1;37m--- ATMOSPHERIC-PRESSURE-COMPENSATOR ONLINE (ID: {self.apc_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        avg_p = statistics.mean(self.pressure_readings)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            current_alt = i * 5000 # Simulated meters
            density = self.calculate_air_density(current_alt)
            print(f"\033[1;{colors[i]}m[ALT:{current_alt}m | DENSITY:{density}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mAPC STATUS: INTERNAL ENVIRONMENT IS FULLY COMPENSATED.\033[0m")

if __name__ == "__main__":
    apc = AtmosphericCompensator()
    apc.stabilize_environment()
