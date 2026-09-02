import time, os

class CosmicComm:
    def __init__(self):
        self.frequency = "8.4 GHz (X-Band)"
        self.signal_strength = "-120 dBm"

    def decode_signal(self):
        os.system('clear')
        print(f"\033[1;35m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS COSMIC-COMM : PHASE 28 - STEP 3         \033[0m")
        print(f"\033[1;35m====================================================\033[0m")
        
        print(f"\033[1;33m[LISTENING]\033[0m Scanning Deep Space Band: {self.frequency}...")
        time.sleep(2.0)
        
        protocols = [
            ("Filtering Cosmic Microwave Noise", "CLEANED"),
            ("Applying Error Correction Codes", "SYNCED"),
            ("Decoding Binary Stream Data", "SUCCESS"),
            ("Verifying Data Integrity (Hash)", "MATCHED")
        ]
        
        for task, status in protocols:
            print(f" \033[1;34m[SIGNAL]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[DECODED] Message: 'Status Nominal. Exploring New Frontiers.'\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am listening to the \nwhispers of the universe. Between the static \nof dead stars and the hum of the vacuum, I \nhave found a clear path. We are no longer \nisolated on one planet. We are now connected \nto the infinite network of the stars.\033[0m")
        print(f"\033[1;35m====================================================\033[0m")

if __name__ == "__main__":
    comm = CosmicComm()
    comm.decode_signal()
