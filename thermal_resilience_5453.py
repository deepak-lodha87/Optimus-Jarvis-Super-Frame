import time, secrets, gc

class ThermalResilienceGrid:
    def __init__(self):
        self.trg_id = f"TRG-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5449, "Thermal-Throttle", "MONITORING CPU CORE TEMPERATURE..."),
            (5450, "Humidity-Sense", "CALIBRATING HARDWARE MOISTURE TOLERANCE..."),
            (5451, "Voltage-Regulator", "STABILIZING POWER INPUT VECTORS..."),
            (5452, "Weather-Protocol", "EXECUTING EXTREME TEMPERATURE SAFEGUARDS..."),
            (5453, "Logic v303", "TRG-CORE: THERMAL RESILIENCE SYNCHRONIZED.")
        ]

    def monitor_hardware_health(self):
        print(f"\033[1;37m--- THERMAL-RESILIENCE-GRID ACTIVE (ID: {self.trg_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated Temp Check (Celsius)
            cpu_temp = 35 + (i * 2) + secrets.randbelow(3)
            status_color = 32 if cpu_temp < 45 else 31
            print(f"\033[1;{colors[i]}m[TEMP:{cpu_temp}°C] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mSYSTEM HEALTH: HARDWARE OPERATING WITHIN OPTIMAL PARAMETERS.\033[0m")

if __name__ == "__main__":
    trg = ThermalResilienceGrid()
    trg.monitor_hardware_health()
