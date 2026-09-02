import time
import sys
import random

def stream_data(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class OptimusJarvisMaster:
    def __init__(self):
        self.total_phases = 2001
        self.version = "9.2.0"
        self.status = "ACTIVE"

    def boot_sequence(self):
        print("\033[1;32m") # Terminal text Green color mein badalne ke liye
        stream_data(">>> INITIALIZING OPTIMUS JARVIS SUPER-FRAME CORE...")
        time.sleep(1)
        
        print("\n--- LOADING HISTORICAL PHASE DATA ---")
        for i in range(0, 2001, 200): # 200 ke gap mein phases load hote dikhenge
            time.sleep(0.3)
            print(f"[LOADED] Phase {i} to {i+199}... OK")

        print("\n--- SYSTEM DIAGNOSTICS ---")
        metrics = {
            "Neural Expansion": "98.4%",
            "Quantum Stability": "Optimal",
            "Security Shield": "Encrypted (256-bit)",
            "Flight Logic": "Phase 2001 Synchronized"
        }
        
        for key, value in metrics.items():
            stream_data(f"Checking {key}: {value}")
            time.sleep(0.5)

        print("\n--- LIVE DATA STREAM ---")
        try:
            for _ in range(15): # Live data ka simulation
                cpu_load = random.randint(10, 45)
                mem_usage = random.uniform(1.2, 2.5)
                packet = random.choice(["SYNC_OK", "DATA_RCVD", "LOG_UPDATED"])
                print(f"ID: {random.randint(100,999)} | CPU: {cpu_load}% | MEM: {mem_usage:.2f}GB | STATUS: {packet}")
                time.sleep(0.4)
        except KeyboardInterrupt:
            pass

        print("\n\033[1;34mMASTER CONTROL INTERFACE READY.\033[0m")
        print(f"Current Phase: {self.total_phases} | System Health: 100%")

if __name__ == "__main__":
    jarvis = OptimusJarvisMaster()
    jarvis.boot_sequence()
