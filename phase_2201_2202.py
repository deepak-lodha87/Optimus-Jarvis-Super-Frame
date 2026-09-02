import time
import random

def execute_unique_subroutine(phase_id, task_name, detail):
    colors = {"2201": "38;5;45", "2202": "38;5;201"}
    print(f"\033[{colors[phase_id]}m[EXECUTING_{phase_id}]: {task_name}\033[0m")
    time.sleep(1.8)
    print(f" > System Note: {detail}")

def start_advanced_link():
    print("\n" + "—" * 55)
    print("\033[1;97m JARVIS_OPTICS & SIGNAL OVERHAUL \033[0m")
    print("—" * 55)

    # Phase 2201: Gravitational Lensing Integration
    execute_unique_subroutine("2201", "Gravity-Based Deep Space Scanning", 
                             "Bending light around massive objects to see beyond horizons.")
    print("\033[32m[SUCCESS]: Visual range expanded to 14 billion light-years.\033[0m")
    
    print("\n" + "::" * 20 + "\n")

    # Phase 2202: Tachyon-Burst Communication
    execute_unique_subroutine("2202", "Tachyon-Stream Messaging", 
                             "Utilizing hypothetical particles to break the light-speed barrier.")
    latency = random.uniform(0.0001, 0.0009)
    print(f"\033[32m[SUCCESS]: Data latency reduced to {latency:.6f} ms.\033[0m")
    
    print("—" * 55)
    print("\033[1;44;97m INTEGRITY VERIFIED: NEW UNIQUE PROTOCOLS ACTIVE \033[0m")
    print("—" * 55)

if __name__ == "__main__":
    start_advanced_link()
