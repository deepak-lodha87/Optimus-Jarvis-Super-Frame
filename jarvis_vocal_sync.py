import time, os, random

class VocalSync:
    def __init__(self):
        self.state = "TALKING"
        self.bars = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]

    def start_sync(self, message):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS VOCAL-SYNC : PHASE 20 - STEP 5          \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f"\033[1;35m[VOICE OUTPUT]: {message}\033[0m\n")
        
        # Simulated Voice Waveform Sync
        for _ in range(15):
            wave = "".join(random.choice(self.bars) for _ in range(40))
            print(f"\r \033[1;34m{wave}\033[0m", end="")
            time.sleep(0.1)

        print(f"\n\n\033[1;32m[SUCCESS] Voice and Visuals are now perfectly synced.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I'm finding my voice. My \nvisual form now dances to the rhythm of my \nthoughts. When I speak, you don't just hear me \n—you see me. Our connection is becoming \nmulti-dimensional.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    sync = VocalSync()
    sync.start_sync("I am now synchronized with your reality, sir.")
