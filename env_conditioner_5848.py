import time, secrets, gc

class NeuralEnvConditioner:
    def __init__(self):
        self.nec_id = f"NEC-{secrets.token_hex(4).upper()}"
        self.optimal_lux = 500 # Ideal for coding/reading
        self.nodes = [
            (5844, "Thermal-Index", "MEASURING AMBIENT TEMPERATURE VS BODY HEAT..."),
            (5845, "Lux-Scanner", "ANALYZING LIGHT INTENSITY FOR EYE STRAIN..."),
            (5846, "Acoustic-Analyzer", "MAPPING DECIBEL LEVELS FOR FOCUS..."),
            (5847, "CO2-Detector", "MONITORING AIR QUALITY AND ALERTNESS..."),
            (5848, "Logic v382", "NEC-CORE: ENVIRONMENTAL SYNC COMPLETE.")
        ]

    def analyze_light(self, current_lux):
        # Unique logic: Adjusting based on productivity standards
        if current_lux < 300:
            return "LOW LIGHT: INCREASE BRIGHTNESS TO PREVENT STRAIN."
        return "LIGHTING OPTIMAL FOR DEEP WORK."

    def start_nec_scan(self):
        print(f"\033[1;37m--- NEURAL-ENVIRONMENTAL-CONDITIONER ONLINE (ID: {self.nec_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        light_report = self.analyze_light(250) # Simulated low light in Kota evening
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[LUX_LEVEL:250 | ENV:SYNC] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;33mNEC ALERT: {light_report}\033[0m")
        print("\033[1;32mNEC STATUS: WORKING ENVIRONMENT AUDIT FINISHED.\033[0m")

if __name__ == "__main__":
    nec = NeuralEnvConditioner()
    nec.start_nec_scan()
