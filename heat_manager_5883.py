import time, secrets, gc

class NeuralHeatManager:
    def __init__(self):
        self.nphm_id = f"NPHM-{secrets.token_hex(4).upper()}"
        self.temp_threshold = 85.0 # Max safe temperature in Celsius
        self.nodes = [
            (5879, "Thermal-Sync", "SYNCHRONIZING CORE THERMAL SENSORS..."),
            (5880, "Coolant-Flow", "INJECTING LIQUID COOLANT INTO PROPULSION CHANNELS..."),
            (5881, "Heat-Sink", "OPENING EXTERNAL VENTILATION FLAPS..."),
            (5882, "Thermal-Throttle", "INITIATING POWER REDUCTION TO PREVENT MELTDOWN..."),
            (5883, "Logic v389", "NPHM-CORE: THERMAL DEFENSES ARE OPTIMAL.")
        ]

    def manage_heat(self, current_temp):
        # Unique logic: Triggering cooling if temp exceeds threshold
        if current_temp > self.temp_threshold:
            return f"OVERHEAT! Temp: {current_temp}°C. REDUCING POWER."
        return f"STABLE. Temp: {current_temp}°C. ENGINES NOMINAL."

    def run_thermal_audit(self):
        print(f"\033[1;37m--- NEURAL-PROPULSION-HEAT-MANAGEMENT ONLINE (ID: {self.nphm_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        # Simulated propulsion heat (e.g., during high-speed flight)
        live_temp = 92.4 
        thermal_status = self.manage_heat(live_temp)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[CORE_TEMP:{live_temp}°C | STATUS:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;31mTHERMAL ALERT: {thermal_status}\033[0m")
        print("\033[1;32mNPHM STATUS: SYSTEM STABILIZED AT 78.5°C AFTER COOLING.\033[0m")

if __name__ == "__main__":
    nphm = NeuralHeatManager()
    nphm.run_thermal_audit()
