import time, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def system_intelligence():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'INTERNAL SYSTEM MONITORING v304':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[JARVIS]: Scanning local hardware nodes...{C['W']}")
    time.sleep(1)

    # Simulating Real-time System Fetch
    try:
        # Fetching battery via termux-battery-status (if available)
        print(f"{C['B']}Power Source: {C['G']}INTERNAL FUEL CELL (BATTERY){C['W']}")
        print(f"{C['B']}Integrity: {C['G']}STABLE{C['W']}")
        
        # Simulated Diagnostics for Starhawk Suit
        print(f"\n{C['BOLD']}{C['Y']}--- HARDWARE DIAGNOSTICS ---{C['W']}")
        modules = ["CPU Core Link", "RAM Allocation", "Thermal Sensors", "Neural Buffer"]
        
        for mod in modules:
            print(f"{mod.ljust(20)}: {C['G']}[ONLINE]{C['W']}")
            time.sleep(0.4)
            
        print(f"\n{C['BOLD']}{C['B']}[JARVIS]: Commander Deepak, all hardware is within optimal range.{C['W']}")

    except Exception as e:
        print(f"{C['R']}Diagnostic Error: {e}{C['W']}")

    print(f"\n{C['BOLD']}{C['Y']}1. Return to Supreme Console{C['W']}")
    input(f"\n{C['G']}>> Press Enter to Acknowledge...{C['W']}")

if __name__ == "__main__":
    system_intelligence()
