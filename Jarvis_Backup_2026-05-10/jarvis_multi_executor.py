import threading
import time
import random

def task_node(name, duration):
    print(f"\033[1;34m[START] Node {name}: Initializing...\033[0m")
    time.sleep(duration)
    print(f"\033[1;32m[COMPLETE] Node {name}: Task finished in {duration}s.\033[0m")

if __name__ == "__main__":
    print("-" * 60)
    print("   JARVIS UMC: PARALLEL TASK ORCHESTRATION (P3246-47)")
    print("-" * 60)

    # Defining 5 different parallel tasks
    tasks = [
        ("Fuel_Injection", 1.2),
        ("Suspension_Scan", 0.8),
        ("Satellite_Link", 2.0),
        ("Thermal_Cooling", 1.5),
        ("Torque_Boost", 0.5)
    ]

    threads = []

    # Launching all 5 tasks at the exact same time
    for t_name, t_time in tasks:
        process = threading.Thread(target=task_node, args=(t_name, t_time))
        threads.append(process)
        process.start()

    # Waiting for all to finish
    for process in threads:
        process.join()

    print("-" * 60)
    print("\033[1;36m[SYSTEM] All 5 Nodes Synced. UMC Operating at Full Capacity.\033[0m")
    print("-" * 60)
