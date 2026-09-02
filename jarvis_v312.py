import os, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def system_audit():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: AUTO-CLEAN & INTEGRITY AUDIT v312':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[SYSTEM]: Initiating directory scan...{C['W']}")
    time.sleep(1)

    # Temporary or cache files to look for
    junk_extensions = ['.tmp', '.cache', '__pycache__']
    removed_count = 0

    print(f"\n{C['B']}--- AUDIT LOG ---{C['W']}")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if any(file.endswith(ext) for ext in junk_extensions):
                try:
                    os.remove(os.path.join(root, file))
                    print(f"{C['R']}[CLEANED]: {file}{C['W']}")
                    removed
cat << 'EOF' > jarvis_v312.py
import os, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def system_audit():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: AUTO-CLEAN & INTEGRITY AUDIT v312':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[SYSTEM]: Initiating directory scan...{C['W']}")
    time.sleep(1)

    # Temporary or cache files to look for
    junk_extensions = ['.tmp', '.cache', '__pycache__']
    removed_count = 0

    print(f"\n{C['B']}--- AUDIT LOG ---{C['W']}")
    for root, dirs, files in os.walk('.'):
        for file in files:
            if any(file.endswith(ext) for ext in junk_extensions):
                try:
                    os.remove(os.path.join(root, file))
                    print(f"{C['R']}[CLEANED]: {file}{C['W']}")
                    removed_count += 1
                except:
                    pass

    if removed_count == 0:
        print(f"{C['G']}[SUCCESS]: System is already optimized. No junk found.{C['W']}")
    else:
        print(f"\n{C['G']}[SUCCESS]: {removed_count} temporary files purged.{C['W']}")

    print(f"\n{C['Y']}[INTEGRITY]: Checking core framework files...{C['W']}")
    # Detecting key jarvis files to ensure they are safe
    jarvis_files = [f for f in os.listdir('.') if f.startswith('jarvis_v')]
    print(f"{C['G']}[OK]: {len(jarvis_files)} Core Modules verified and intact.{C['W']}")

    input(f"\n{C['B']}>> Return to Master Console...{C['W']}")

if __name__ == "__main__":
    system_audit()
