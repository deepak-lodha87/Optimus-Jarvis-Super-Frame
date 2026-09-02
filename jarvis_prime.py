import os, sys, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def main_launcher():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'OPTIMUS JARVIS: SUPREME CONTROL CENTER':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")
    
    # Unified Protocol List
    protocols = {
        "1":  ["Neural Voice Link",   "jarvis_v299.py"],
        "2":  ["Master Protocol",      "jarvis_v300.py"],
        "3":  ["Drone & Tactical MFG", "jarvis_v301.py"],
        "4":  ["Tactical HUD MK-II",   "jarvis_v295.py"],
        "5":  ["Deep System Repair",   "jarvis_v297.py"],
        "6":  ["System Analytics",     "jarvis_v291.py"],
        "7":  ["Integrity Check",      "jarvis_v293.py"],
        "8":  ["Aerospace Telemetry",  "jarvis_v289.py"]
    }

    print(f"\n{C['Y']}SELECT ACTIVE DIRECTIVE:{C['W']}")
    for key in sorted(protocols.keys(), key=int):
        print(f"{C['BOLD']}{key.ljust(3)}{C['W']} - {protocols[key][0]}")
    
    print(f"{C['R']}9   - System Shutdown{C['W']}")
    
    choice = input(f"\n
cat << 'EOF' > jarvis_prime.py
import os, sys, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def main_launcher():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'OPTIMUS JARVIS: SUPREME CONTROL CENTER':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")
    
    # Unified Protocol List
    protocols = {
        "1":  ["Neural Voice Link",   "jarvis_v299.py"],
        "2":  ["Master Protocol",      "jarvis_v300.py"],
        "3":  ["Drone & Tactical MFG", "jarvis_v301.py"],
        "4":  ["Tactical HUD MK-II",   "jarvis_v295.py"],
        "5":  ["Deep System Repair",   "jarvis_v297.py"],
        "6":  ["System Analytics",     "jarvis_v291.py"],
        "7":  ["Integrity Check",      "jarvis_v293.py"],
        "8":  ["Aerospace Telemetry",  "jarvis_v289.py"]
    }

    print(f"\n{C['Y']}SELECT ACTIVE DIRECTIVE:{C['W']}")
    for key in sorted(protocols.keys(), key=int):
        print(f"{C['BOLD']}{key.ljust(3)}{C['W']} - {protocols[key][0]}")
    
    print(f"{C['R']}9   - System Shutdown{C['W']}")
    
    choice = input(f"\n{C['G']}>> COMMAND INPUT: {C['W']}")
    
    if choice in protocols:
        target_file = protocols[choice][1]
        if os.path.exists(target_file):
            print(f"\n{C['B']}[JARVIS]: Launching {protocols[choice][0]}...{C['W']}")
            time.sleep(0.5)
            os.system(f'python {target_file}')
        else:
            print(f"\n{C['R']}[ERROR]: Module {target_file} not found!{C['W']}")
        
        input(f"\n{C['Y']}Press Enter to return to Supreme Console...{C['W']}")
        
    elif choice == '9':
        print(f"\n{C['R']}[SYSTEM]: All protocols hibernating. Goodbye, Commander.{C['W']}")
        sys.exit()
    else:
        print(f"\n{C['R']}Invalid Directive.{C['W']}")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        main_launcher()
