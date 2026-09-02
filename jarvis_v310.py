import os, sys, time

# Terminal Colors for Elite Interface
C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def main_launcher():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'OPTIMUS JARVIS: SUPREME CONSOLE v310':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    # Step 1: Automatically find all your legacy files
    # It scans your directory for any file starting with 'jarvis'
    legacy_files = sorted([f for f in os.listdir('.') if f.startswith('jarvis_v') and f.endswith('.py')])

    if not legacy_files:
        print(f"{C['R']}[ALERT]: No legacy jarvis files detected in directory!{C['W']}")
        return

    print(f"\n{C['Y']}LEGACY PROTOCOLS PRESERVED (v273 to v309):{C['W']}")
    for i, file_name in enumerate(legacy_files, 1):
        # Highlighting the specific module name
        print(f"{C['BOLD']}{i:02d}{C['W']} - {file_name}")

    print(f"\n{C['R']}99 - System Standby (Exit){C['W']}")
    
    try:
        cmd = input(f"\n{C['G']}>> INITIALIZE DIRECTIVE: {C['W']}")
        
        if cmd == '99':
            print(f"{C['R']}Shutting down... All legacy data remains intact.{C['W']}")
            sys.exit()
            
        idx = int(cmd) - 1
        if 0 <= idx < len(legacy_files):
            target = legacy_files[idx]
            print(f"\n{C['B']}[JARVIS]: Launching {target}...{C['W']}")
            time.sleep(1)
            os.system(f'python {target}')
        else:
            print(f"{C['R']}Directive ID out of range.{C['W']}")
            time.sleep(1)
    except ValueError:
        print(f"{C['R']}Invalid command format.{C['W']}")
        time.sleep(1)

if __name__ == "__main__":
    while True:
        main_launcher()
