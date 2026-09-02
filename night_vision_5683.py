import time, secrets, gc, math

class MultiSpectrumNightVision:
    def __init__(self):
        self.msn_id = f"MSN-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5679, "Photon-Boost", "AMPLIFYING LOW-LIGHT PARTICLES..."),
            (5680, "Thermal-Mapping", "SCANNING HEAT SIGNATURES (37°C)..."),
            (5681, "IR-Illumination", "ENGAGING INFRARED FLOODLIGHTS..."),
            (5682, "Fusion-Overlay", "MERGING THERMAL & OPTICAL DATA..."),
            (5683, "Logic v349", "MSN-CORE: NIGHT VISION OPERATIONAL.")
        ]

    def calculate_contrast_gain(self, lux_level):
        # Unique logic: Higher gain for lower lux levels
        if lux_level <= 0: lux_level = 0.0001
        return round(math.sqrt(1 / lux_level) * 10, 2)

    def activate_optics(self):
        print(f"\033[1;37m--- MULTI-SPECTRUM-NIGHT-VISION ONLINE (ID: {self.msn_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            lux = 0.5 - (i * 0.1) # Simulating decreasing light
            gain = self.calculate_contrast_gain(max(lux, 0.01))
            print(f"\033[1;{colors[i]}m[LUX:{round(lux, 2)} | GAIN:x{gain}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mMSN STATUS: FULL SPECTRUM VISUALIZATION ACTIVE.\033[0m")

if __name__ == "__main__":
    msn = MultiSpectrumNightVision()
    msn.activate_optics()
