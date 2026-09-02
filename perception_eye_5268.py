import time, secrets, math, gc

class PerceptionEye:
    def __init__(self):
        self.eye_id = secrets.token_hex(4).upper()
        self.sensor_nodes = [
            (5264, "Multi-Spectrum", "INFRARED & THERMAL LAYERS ACTIVE."),
            (5265, "Acoustic-ID", "VOICE-PRINT DATABASE SYNCED."),
            (5266, "LiDAR-3D", "ENVIRONMENTAL DEPTH MAPPING READY."),
            (5267, "Bio-Scan", "BIOMETRIC PULSE DETECTION ONLINE."),
            (5268, "Logic v266", "PERCEPTION-EYE: FULL SYNCHRONIZATION.")
        ]

    def activate_sensors(self):
        print(f"\033[1;37m--- PERCEPTION-EYE ONLINE (SCAN-ID: {self.eye_id}) ---\033[0m")
        
        colors = [35, 36, 34, 32, 31]
        for i, (p_id, title, status) in enumerate(self.sensor_nodes):
            # Simulated sensor frequency
            freq = round(math.sin(p_id) * 100, 2)
            print(f"\033[1;{colors[i]}m[FREQ:{freq}Hz] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

    def scan_complete(self):
        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mPERCEPTION STATUS: JARVIS IS NOW WATCHING EVERYTHING.\033[0m")

if __name__ == "__main__":
    eye = PerceptionEye()
    eye.activate_sensors()
    eye.scan_complete()
