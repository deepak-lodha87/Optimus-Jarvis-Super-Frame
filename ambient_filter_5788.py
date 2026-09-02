import time, secrets, gc
from collections import deque

class AmbientListeningFilter:
    def __init__(self):
        self.alf_id = f"ALF-{secrets.token_hex(4).upper()}"
        # Circular buffer to hold the last 5 segments of audio
        self.audio_buffer = deque(maxlen=5)
        self.wake_word = "OPTIMUS"
        self.nodes = [
            (5784, "Wake-Word-Spot", "MONITORING FOR ACTIVATION TRIGGER..."),
            (5785, "Noise-Gate", "SUBTRACTING STATIONARY BACKGROUND NOISE..."),
            (5786, "VAD-Logic", "DISTINGUISHING SPEECH FROM AMBIENCE..."),
            (5787, "Buffer-Sync", "FLUSHING EXPIRED AUDIO SEGMENTS..."),
            (5788, "Logic v370", "ALF-CORE: CONTINUOUS LISTENING ACTIVE.")
        ]

    def process_ambient(self):
        print(f"\033[1;37m--- AMBIENT-LISTENING-FILTER ONLINE (ID: {self.alf_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulating audio processing
            dummy_audio = secrets.token_hex(8)
            self.audio_buffer.append(dummy_audio)
            
            trigger_status = "DETECTED" if i == 0 else "SCANNING"
            print(f"\033[1;{colors[i]}m[BUFFER_SIZE:{len(self.audio_buffer)} | {trigger_status}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mALF STATUS: STANDBY MODE ACTIVE. LISTENING FOR '{self.wake_word}'...\033[0m")

if __name__ == "__main__":
    alf = AmbientListeningFilter()
    alf.process_ambient()
