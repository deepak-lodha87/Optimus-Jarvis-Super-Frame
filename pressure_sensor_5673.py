import time, secrets, gc, math

class AtmosphericPressureSensor:
    def __init__(self):
        self.aps_id = f"APS-{secrets.token_hex(4).upper()}"
        self.sea_level_p = 1013.25 # hPa
        self.nodes = [
            (5669, "Barometric-Sync", "SYNCING ALTITUDE VIA PRESSURE GRADIENT..."),
            (5670, "Weather-Predict", "ANALYZING ISOBARIC TRENDS..."),
            (5671, "Oxygen-Alert", "MONITORING O2 SATURATION THRESHOLDS..."),
            (5672, "Fluid-Density", "CALIBRATING THRUST FOR AIR THICKNESS..."),
            (5673, "Logic v347", "APS-CORE: ATMOSPHERIC SENSING ACTIVE.")
        ]

    def calculate_altitude(self, current_p):
        # Hypsometric Formula: Altitude based on pressure
        return round(44330 * (1 - math.pow(current_p / self.sea_level_p, 1/5.255)), 2)

    def start_sensing(self):
        print(f"\033[1;37m--- ATMOSPHERIC-PRESSURE-SENSOR ONLINE (ID: {self.aps_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            sim_p = 1013.25 - (i * 150) # Simulated pressure drop
            alt = self.calculate_altitude(sim_p)
            print(f"\033[1;{colors[i]}m[ALTITUDE:{alt}m | P:{sim_p}hPa] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mAPS STATUS: ENVIRONMENTAL DATA ACQUISITION STABLE.\033[0m")

if __name__ == "__main__":
    aps = AtmosphericPressureSensor()
    aps.start_sensing()
