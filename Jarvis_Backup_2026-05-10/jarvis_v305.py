import time, os, sys

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def security_vault():
    os.system('clear')
    print(f"{C['R']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: SECURE ENCRYPTION VAULT v305':^46} {C['R']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    # Security Configuration
    MASTER_PASS = "STARK7" 
    
    print(f"\n{C['Y']}[WARNING]: Restricted Area. Unauthorized access is logged.{C['W']}")
    attempt = input(f"\n{C['G']}>> ENTER MASTER ACCESS KEY: {C['W']}")

    if attempt == MASTER_PASS:
        print(f"\n{C['B']}[SYSTEM]: Identity Verified. Welcome, Commander Deepak.{C['W']}")
        time.sleep(1)
        print(f"{C['G']}Status: ALL ENCRYPTED FILES ARE NOW ACCESSIBLE.{C['W']}")
        print(f"\n{C['BOLD']}1. View Encrypted Project Logs")
        print("2. Decrypt Starhawk Blueprints")
        print("3. Return to Supreme Console")
        input(f"\n{C['Y']}>> Select Directive: {C['W']}")
    else:
        print(f"\n{C['R']}[CRITICAL]: INCORRECT KEY! INITIALIZING LOCKDOWN...{C['W']}")
        for i in range(3, 0, -1):
            print(f"Locking system in {i}...")
            time.sleep(1)
        print(f"{C['BOLD']}{C['R']}ACCESS DENIED. EXITING SYSTEM.{C['W']}")
        sys.exit()

if __name__ == "__main__":
    security_vault()
