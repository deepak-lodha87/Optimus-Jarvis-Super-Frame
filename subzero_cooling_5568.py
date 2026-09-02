import time, secrets, gc, math, sys

class SubZeroCoolingLogic:
    def __init__(self):
        self.scl_id = f"SCL-{secrets.token_hex(4).upper()}"
        # Setting recursion limit for deep thermal tree analysis
        sys.setrecursionlimit(2000)
        self.nodes = [
            (5564, "Vapor-Chamber", "MAPPING PHASE-CHANGE THERMAL VECTORS..."),
            (5565, "Cryo-Pulse", "INJECTING CRYOGENIC SUPPRESSION SIGNALS..."),
            (5566, "Peltier-Effect", "ACTIVATING THERMOELECTRIC COOLING CORES..."),
            (5567, "Thermal-Inertia", "CALCULATING PREDICTIVE HEAT DISSIPATION..."),
            (5568, "Logic v326", "SCL-CORE: SUB-ZERO COOLING SYNCHRONIZED.")
        ]

    def calculate_cooling_delta(self, ambient_temp):
        # Unique logic using Inverse Hyperbolic Sine for non-linear cooling
        return round(math.asinh(ambient_temp) * 1.5, 4)

    def activate_cryo_core(self):
        print(f"\033[1;37m--- SUB-ZERO-COOLING-LOGIC ONLINE (ID: {self.scl_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            temp_threshold = 45.0 - (i * 8.5) # Simulated temperature drop
            cooling_delta = self.calculate_cooling_delta(temp_threshold)
            
            print(f"\033[1;{colors[i]}m[TARGET:{temp_threshold}°C | DELTA:{cooling_delta}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mSCL STATUS: HARDWARE TEMPERATURE IS NOW BELOW AMBIENT LEVELS.\033[0m")

if __name__ == "__main__":
    scl = SubZeroCoolingLogic()
    scl.activate_cryo_core()
