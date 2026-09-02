import os, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def file_navigator():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: NEURAL FILE NAVIGATOR v309':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[JARVIS]: Scanning local directory for project files...{C['W']}")
    time.sleep(1)

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    print(f"\n{C['BOLD']}{C['B']}--- DETECTED MODULES ---{C['W']}")
    for i, f in enumerate(files, 1):
        if "jarvis" in f.lower():
            print(f"{C['G']}{i}. {C['W']}{f}")
        else:
            print(f"{C['W']}{i}. {f}")
    
    search = input(f"\n{C['BOLD']}{C['Y']}>> Enter keyword to search: {C['W']}").lower()
    
    results = [f for f in files if search in f.lower()]
    
    if results:
        print(f"\n{C['G']}[MATCH FOUND]:{C['W']}")
        for r in results:
            print(f"- {r}")
    else:
        print(f"\n{C['R']}[ERROR]: No files matching '{search}' found.{C['W']}")

    input(f"\n{C['B']}>> Return to Console...{C['W']}")

if __name__ == "__main__":
    file_navigator()
