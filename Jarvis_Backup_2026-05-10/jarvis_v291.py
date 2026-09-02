import os, time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def analyze_logs():
    print(f"\n{C['B']}[SYSTEM]: Analyzing Engineering Logs...{C['W']}")
    time.sleep(1.5)
    
    log_file = "project_logs.txt"
    if not os.path.exists(log_file):
        print(f"{C['R']}[ERROR]: No log history found.{C['W']}")
        return

    with open(log_file, "r") as f:
        logs = f.readlines()
        
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS SYSTEM ANALYTICS':^42} {C['B']}║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    
    print(f"\n{C['W']}TOTAL ENTRIES : {C['G']}{len(logs)}")
    print(f"{C['W']}LAST ACTIVITY : {C['Y']}{logs[-1].strip() if logs else 'None'}")
    print(f"\n{C['G']}[SUCCESS]: Analysis complete.{C['W']}")

if __name__ == "__main__":
    analyze_logs()
