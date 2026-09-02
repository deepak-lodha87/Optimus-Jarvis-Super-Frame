import os, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def deep_repair():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'SYSTEM DEEP REPAIR PROTOCOL ACTIVATED':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")
    
    tasks = [
        "Scanning internal logic paths...",
        "Optimizing memory allocation...",
        "Re-indexing modular protocols...",
        "Flushing temporary cache...",
        "Syncing Starhawk HUD telemetry..."
    ]
    
    for i, task in enumerate(tasks):
        print(f"\n{C['Y']}[STEP {i+1}/5]: {task}{C['W']}")
        for _ in range(10):
            print("█", end="", flush=True)
            time.sleep(0.2)
        print(f" {C['G']}[DONE]{C['W']}")
    
    print(f"\n{C['G']}{C['BOLD']}[SUCCESS]: System logic is now 100% optimized.{C['W']}")

if __name__ == "__main__":
    deep_repair()
