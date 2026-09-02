import time, secrets, gc, math

class SubZeroBatteryPreheat:
    def __init__(self):
        self.sbp_id = f"SBP-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5674, "Viscosity-Check", "ANALYZING ELECTROLYTE FLOW DENSITY..."),
            (5675, "Self-Heating", "ACTIVATING INTERNAL RESISTANCE COILS..."),
            (5676, "Voltage-Boost", "STABILIZING LOW-TEMP CURRENT FLOW..."),
            (5677, "Thermal-Lock", "ENGAGING COMPONENT INSULATION..."),
            (5678, "Logic v348", "SBP-CORE: BATTERY PREHEAT SEQUENCE ACTIVE.")
        ]

    def estimate_battery_efficiency(self, temp_c):
        # Unique logic: Arrhenius-inspired efficiency drop model
        # Efficiency falls exponentially as temperature drops below 25°C
        if temp_c >= 25: return 100.0
        return round(100 * math.exp(0.05 * (temp_c - 25)), 2)

    def start_preheat(self):
        print(f"\033[1;37m--- SUB-ZERO-BATTERY-PREHEAT ONLINE (ID: {self.sbp_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        current_temp = -15 # Simulated extreme cold (-15°C)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            eff = self.estimate_battery_efficiency(current_temp)
            print(f"\033[1;{colors[i]}m[TEMP:{current_temp}°C | EFF:{eff}%] Phase {p_id}: {title} >> {status}\033[0m")
            current_temp += 8 # Simulating heating progress
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mSBP STATUS: OPTIMAL THERMAL OPERATING RANGE REACHED.\033[0m")

if __name__ == "__main__":
    sbp = SubZeroBatteryPreheat()
    sbp.start_preheat()
