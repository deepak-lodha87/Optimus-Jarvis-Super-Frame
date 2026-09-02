import os, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def check_integrity():
    print(f"\n{C['B']}[SYSTEM]: Running Integrity Check...{C['W']}")
    time.sleep(1.5)
    
    required_files = [
        "jarvis_v273.py", "jarvis_v274.py", "jarvis_v275.py", "jarvis_v276.py",
        "jarvis_v278.py", "jarvis_v280.py", "jarvis_v281.py", "jarvis_v283.py",
        "jarvis_v284.py", "jarvis_v286.py", "jarvis_v287.py", "jarvis_v289.py",
        "jarvis_v291.py"
    ]
    
    missing = []
    for f in required_files:
        if os.path.exists(f):
            print(f"{C['G']}[FOUND]: {f}{C['W']}")
        else:
            print(f"{C['R']}[MISSING]: {f}{C['W']}")
            missing.append(f)
            
    if not missing:
        print(f"\n{C['BOLD']}{C['G']}INTEGRITY STATUS: 100% OPTIMAL{C['W']}")
    else:
        print(f"\n{C['R']}ALERT: {len(missing)} Modules missing. System unstable.{C['W']}")

if __name__ == "__main__":
    check_integrity()
