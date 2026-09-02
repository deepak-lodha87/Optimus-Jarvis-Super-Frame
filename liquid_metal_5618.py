import time, secrets, gc, math, struct

class LiquidMetalCooling:
    def __init__(self):
        self.lmc_id = f"LMC-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5614, "Gallium-Flow", "INITIATING LIQUID METAL CIRCULATION..."),
            (5615, "EM-Pumping", "ACTIVATING ELECTROMAGNETIC PUMP COILS..."),
            (5616, "Oxidation-Shield", "STABILIZING CHEMICAL BARRIERS..."),
            (5617, "Heat-Sinking", "MAXIMIZING THERMAL DISSIPATION FLUX..."),
            (5618, "Logic v336", "LMC-CORE: LIQUID METAL CYCLE ACTIVE.")
        ]

    def process_binary_temp(self, temp_val):
        # Unique logic: Using struct to handle binary thermal packets
        packed = struct.pack('f', temp_val)
        return struct.unpack('f', packed)[0]

    def activate_cooling(self):
        print(f"\033[1;37m--- LIQUID-METAL-COOLING-CYCLE ONLINE (ID: {self.lmc_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            raw_temp = 75.5 + (i * 12.2) # Simulated thermal load
            safe_temp = self.process_binary_temp(raw_temp)
            print(f"\033[1;{colors[i]}m[CORE-TEMP:{safe_temp}°C] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mLMC STATUS: THERMAL OVERLOAD PREVENTED VIA LIQUID METAL EXCHANGE.\033[0m")

if __name__ == "__main__":
    lmc = LiquidMetalCooling()
    lmc.activate_cooling()
