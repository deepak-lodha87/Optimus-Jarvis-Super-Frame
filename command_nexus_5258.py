import multiprocessing, time, secrets, gc

def nexus_controller(phase_id, task, status):
    addr = hex(id(task))
    colors = {5254: 36, 5255: 35, 5256: 34, 5257: 32, 5258: 31}
    print(f"\033[1;{colors[phase_id]}m[NEXUS-NODE:{addr}] Phase {phase_id}: {task} >> {status}\033[0m")

if __name__ == "__main__":
    print(f"\033[1;37m--- COMMAND-NEXUS ONLINE (LINK-ID: {secrets.token_hex(4).upper()}) ---\033[0m")
    
    tasks = [
        (5254, "Core-Sync", "SYNCHRONIZING ALL MODULES..."),
        (5255, "Task-Scheduler", "OPTIMIZING PRIORITY QUEUE..."),
        (5256, "Node-Telemetry", "LINKING GLOBAL GHOST-NODES..."),
        (5257, "Auto-Repair", "SELF-HEALING PROTOCOLS ARMED..."),
        (5258, "Logic v264", "COMMAND-NEXUS: FULL CONTROL.")
    ]

    processes = []
    for t in tasks:
        p = multiprocessing.Process(target=nexus_controller, args=t)
        processes.append(p)
        p.start()
        time.sleep(0.15)
        gc.collect()

    for p in processes:
        p.join()

    print("\033[1;37m" + "="*60 + "\033[0m")
    print("\033[1;32mSTATUS: OPTIMUS JARVIS IS NOW OPERATING AS A UNIFIED SUPREME INTELLIGENCE.\033[0m")
