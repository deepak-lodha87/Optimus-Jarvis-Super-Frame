import time, secrets, gc

class NeuralLifeSupport:
    def __init__(self):
        self.nlsb_id = f"NLSB-{secrets.token_hex(4).upper()}"
        self.oxygen_level = 21.0 # Percentage (%)
        self.pressure = 101.3    # kPa (Earth Standard)
        self.nodes = [
            (5969, "Pressure-Reg", "STABILIZING INTERNAL ATMOSPHERIC PRESSURE..."),
            (5970, "O2-Scrubber", "RECYCLING CO2 INTO BREATHABLE OXYGEN..."),
            (5971, "Humidity-Sync", "ADJUSTING DEHUMIDIFIER ARRAY..."),
            (5972, "Leak-Defense", "MONITORING HULL INTEGRITY FOR LEAKS..."),
            (5973, "Logic v407", "NLSB-CORE: CABIN ENVIRONMENT STABILIZED.")
        ]

    def check_vitals(self):
        # Logic: If O2 drops below 19%, trigger alert
        self.oxygen_level -= secrets.choice([0.1, 0.2, -0.3])
        status = "NOMINAL" if self.oxygen_level > 19.5 else "CRITICAL"
        return round(self.oxygen_level, 2), status

    def run_support_sim(self):
        print(f"\033[1;37m--- NEURAL-LIFE-SUPPORT-BIO-LINK ONLINE (ID: {self.nlsb_id}) ---\033[0m")
        colors = [34, 32, 36, 35, 31]
        
        o2, health = self.check_vitals()
        
        for i, (p_id, title, status_msg) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[O2:{o2}% | PRESS:{self.pressure}kPa] Phase {p_id}: {title} >> {status_msg}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        if health == "CRITICAL":
            print("\033[1;31m[!] DANGER: OXYGEN LEVELS DROPPING. ACTIVATING EMERGENCY TANKS.\033[0m")
        else:
            print("\033[1;32m[+] STATUS: ALL BIO-SYSTEMS OPERATIONAL. BREATHING IS STEADY.\033[0m")

if __name__ == "__main__":
    nlsb = NeuralLifeSupport()
    nlsb.run_support_sim()
