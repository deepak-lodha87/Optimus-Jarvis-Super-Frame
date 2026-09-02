import time, secrets, gc

class NeuralSpaceComm:
    def __init__(self):
        self.ndscl_id = f"NDSCL-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5949, "Signal-Comp", "BOOSTING SIGNAL AMPLITUDE FOR LONG-RANGE TRANSMISSION..."),
            (5950, "Time-Sync", "SYNCHRONIZING LIGHT-SPEED DELAY COMPENSATION..."),
            (5951, "Freq-Hopping", "SHIFITING CARRIER FREQUENCIES FOR SECURITY..."),
            (5952, "Noise-Filter", "ELIMINATING COSMIC BACKGROUND INTERFERENCE..."),
            (5953, "Logic v403", "NDSCL-CORE: DEEP SPACE LINK ESTABLISHED.")
        ]

    def calculate_delay(self, distance_km):
        # Unique logic: Signal travels at speed of light (~300,000 km/s)
        speed_of_light = 300000
        delay_seconds = distance_km / speed_of_light
        return round(delay_seconds, 2)

    def run_comm_test(self):
        print(f"\033[1;37m--- NEURAL-DEEP-SPACE-COMM-LINK ONLINE (ID: {self.ndscl_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        # Simulated distance to Mars (~225 million km)
        distance = 225000000
        delay = self.calculate_delay(distance)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[DISTANCE:{distance/1e6}M km | DELAY:{delay}s] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;36mTRANSMISSION: MESSAGE RECEIVED FROM MARS BASE IN {delay} SECONDS.\033[0m")
        print("\033[1;32mSTATUS: OPTIMUS JARVIS IS NOW COMMUNICATING ACROSS THE SOLAR SYSTEM.\033[0m")

if __name__ == "__main__":
    comm = NeuralSpaceComm()
    comm.run_comm_test()
