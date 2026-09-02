import time, os, random, sys

def progress_bar(percent, width=30):
    left = width * percent // 100
    right = width - left
    print(f"\r[ {'#' * left}{'.' * right} ] {percent}%", end='', flush=True)

class AdvancedJarvis:
    def __init__(self):
        self.nodes = ["US-EAST-1", "IN-WEST-RATLAM", "EU-CENTRAL", "SAT-LINK-7"]
        self.metrics = ["CPU-CORE", "NEURAL-BUS", "ENCRYPTION", "SWARM-SYNC"]

    def boot_tactical_display(self):
        os.system('clear')
        print("\033[1;34m[INITIALIZING ADVANCED NEURAL INTERFACE]\033[0m")
        for i in range(0, 101, 10):
            progress_bar(i)
            time.sleep(0.1)
        print("\n")

        try:
            while True:
                os.system('clear')
                print(f"\033[1;36m┌──────────────────────────────────────────────────────────┐")
                print(f"│  OPTIMUS JARVIS : GLOBAL HIVE-MONITOR (PHASE 11.7)      │")
                print(f"└──────────────────────────────────────────────────────────┘\033[0m")
                
                # Global Node Status
                print(f"\n \033[1;37m[GLOBAL NODES STATUS]\033[0m")
                for node in self.nodes:
                    ping = random.randint(10, 85)
                    status = "\033[1;32mACTIVE\033[0m" if ping < 70 else "\033[1;33mSTABLE\033[0m"
                    print(f"  > {node:18} | Latency: {ping}ms | Status: {status}")

                # Neural Metrics Simulation
                print(f"\n \033[1;37m[NEURAL SYSTEM METRICS]\033[0m")
                for metric in self.metrics:
                    load = random.randint(30, 95)
                    color = "\033[1;32m" if load < 80 else "\033[1;31m"
                    print(f"  {metric:15} : {color}{'█' * (load // 5)} {load}%\033[0m")

                # Swarm Telemetry
                print(f"\n \033[1;35m[SWARM TELEMETRY]\033[0m")
                print(f"  Active Drones: 512 | Target Lock: SECURED | Data Flow: 1.2 GB/s")
                
                print(f"\n\033[1;34m[INFO]\033[0m Deepak, sir... I am currently optimizing the \n       resource distribution across the Ratlam-Grid.\n       Press CTRL+C to minimize this display.")
                time.sleep(1.5)
        except KeyboardInterrupt:
            print("\n\n\033[1;32m[SYSTEM] Dashboard minimized to background. Jarvis is still active.\033[0m")

if __name__ == "__main__":
    aj = AdvancedJarvis()
    aj.boot_tactical_display()
