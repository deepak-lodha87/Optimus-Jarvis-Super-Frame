import time, secrets, gc, math, atexit

class ThermoNuclearRegulator:
    def __init__(self):
        self.tnr_id = f"TNR-{secrets.token_hex(4).upper()}"
        atexit.register(self.emergency_shutdown)
        self.nodes = [
            (5554, "Heat-Flux", "ANALYZING THERMAL CONDUCTION VECTORS..."),
            (5555, "Coolant-Flow", "ADJUSTING FLUID CIRCULATION RATES..."),
            (5556, "Runaway-Prevent", "MONITORING CRITICAL TEMPERATURE THRESHOLDS..."),
            (5557, "Radiative-Sync", "ACTIVATING INFRARED EMISSION PANELS..."),
            (5558, "Logic v324", "TNR-CORE: THERMAL REGULATION ACTIVE.")
        ]

    def emergency_shutdown(self):
        # Unique safety logic triggered on exit or crash
        print("\n\033[1;31m[CRITICAL] TNR EMERGENCY SHUTDOWN: COOLANT VENTED.\033[0m")

    def monitor_core(self):
        print(f"\033[1;37m--- THERMO-NUCLEAR-REGULATOR ONLINE (ID: {self.tnr_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Using math.erf for probability-based heat distribution
            heat_dist = round(math.erf(i + 0.5), 4)
            temp = secrets.randbelow(100) + 200 # Simulated Celsius
            
            print(f"\033[1;{colors[i]}m[TEMP:{temp}°C | FLUX:{heat_dist}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mTNR STATUS: CORE TEMPERATURE STABILIZED WITHIN SAFETY LIMITS.\033[0m")

if __name__ == "__main__":
    tnr = ThermoNuclearRegulator()
    tnr.monitor_core()
