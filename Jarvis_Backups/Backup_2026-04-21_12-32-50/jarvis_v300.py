import time, os, sys

# Master HUD Colors
C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def master_protocol():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'OPTIMUS JARVIS: PHASE 300 - MASTER PROTOCOL':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")
    
    print(f"\n{C['Y']}[SECURITY]: Synchronizing across all modular nodes...{C['W']}")
    time.sleep(1.5)

    # Core Lockdown Simulation
    tasks = [
        "Encrypting neural frequency paths...",
        "Linking Starhawk HUD telemetry...",
        "Establishing deep-space relay link...",
        "Activating Global Lockdown safety net..."
    ]

    for i, task in enumerate(tasks):
        print(f"\n{C['B']}[STEP {i+1}/4]: {task}{C['W']}")
        for _ in range(15):
            print(f"{C['G']}█", end="", flush=True)
            time.sleep(0.1)
        print(f" {C['BOLD']}[READY]{C['W']}")

    print(f"\n{C['BOLD']}{C['G']}SUCCESS: Phase 300 is now the active Core Directive.{C['W']}")
    print(f"{C['BOLD']}{C['Y']}Commander Deepak, Optimus Jarvis is at peak performance.{C['W']}")

if __name__ == "__main__":
    try:
        master_protocol()
    except KeyboardInterrupt:
        print(f"\n{C['R']}[ALERT]: Master Protocol interrupted by user.{C['W']}")
        sys.exit()
