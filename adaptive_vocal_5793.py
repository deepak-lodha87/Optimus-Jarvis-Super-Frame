import time, secrets, gc

class AdaptiveVocalResponse:
    def __init__(self):
        self.avrs_id = f"AVRS-{secrets.token_hex(4).upper()}"
        self.response_modes = {
            "URGENT": 0.05,  # Fast response
            "NORMAL": 0.18,  # Standard speed
            "DETAILED": 0.5   # Slow, explanatory speed
        }
        self.nodes = [
            (5789, "Latency-Adjuster", "CALIBRATING RESPONSE TIME BASED ON CONTEXT..."),
            (5790, "Rate-Modulator", "SYNCING WORDS PER MINUTE (WPM)..."),
            (5791, "Audio-Interrupt", "SETTING PRIORITY OVERRIDE PROTOCOLS..."),
            (5792, "Load-Balancer", "OPTIMIZING OUTPUT FOR COGNITIVE CLARITY..."),
            (5793, "Logic v371", "AVRS-CORE: ADAPTIVE VOCAL ENGINE READY.")
        ]

    def process_speech(self, mode):
        print(f"\033[1;37m--- ADAPTIVE-VOCAL-RESPONSE-SPEED ONLINE (ID: {self.avrs_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        delay = self.response_modes.get(mode, 0.18)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[MODE:{mode} | DELAY:{delay}s] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(delay)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mAVRS STATUS: SPEECH PARAMETERS TUNED TO '{mode}' MODE.\033[0m")

if __name__ == "__main__":
    avrs = AdaptiveVocalResponse()
    # Simulating an Urgent Situation
    avrs.process_speech("URGENT")
