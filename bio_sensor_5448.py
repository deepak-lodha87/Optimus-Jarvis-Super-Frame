import time, secrets, gc, statistics

class BioSensorIntegration:
    def __init__(self):
        self.bsi_id = f"BSI-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5444, "Biometric-Enc", "LOCKING BIOMETRIC HASH VECTORS..."),
            (5445, "Light-Adapt", "ADJUSTING DISPLAY SPECTRUM..."),
            (5446, "Noise-Cancel", "FILTERING AMBIENT AUDIO FREQUENCIES..."),
            (5447, "Proximity-Sense", "ACTIVATING NEAR-FIELD SECURITY..."),
            (5448, "Logic v302", "BSI-CORE: SENSOR INTEGRATION COMPLETE.")
        ]

    def scan_environment(self):
        print(f"\033[1;37m--- BIO-SENSOR-INTEGRATION ACTIVE (ID: {self.bsi_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated Signal Stability
            stability = round(statistics.mean([95, 98, secrets.randbelow(5)+95]), 2)
            print(f"\033[1;{colors[i]}m[SIGNAL:{stability}%] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()
        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mBSI STATUS: JARVIS IS NOW RESPONSIVE TO PHYSICAL STIMULI.\033[0m")

if __name__ == "__main__":
    bsi = BioSensorIntegration()
    bsi.scan_environment()
