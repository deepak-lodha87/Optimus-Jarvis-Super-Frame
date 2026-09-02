import os, time
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def memory_logger():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: NEURAL MEMORY LOGGER v311':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    log_file = "jarvis_memory.txt"
    
    print(f"\n{C['Y']}[SYSTEM]: Memory Link Established.{C['W']}")
    user_note = input(f"\n{C['G']}>> Commander Deepak, what should I remember? {C['W']}")

    if user_note.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] - {user_note}\n")
        
        print(f"\n{C['B']}[JARVIS]: Information archived in {log_file}.{C['W']}")
        time.sleep(1)
    else:
        print(f"\n{C['R']}[ERROR]: No data provided for logging.{C['W']}")

    view = input(f"\n{C['Y']}>> Access archived memories? (y/n): {C['W']}").lower()
    if view == 'y':
        if os.path.exists(log_file):
            print(f"\n{C['BOLD']}{C['B']}--- ARCHIVED MEMORIES ---{C['W']}")
            with open(log_file, "r") as f:
                print(f.read())
        else:
            print(f"{C['R']}No memories found.{C['W']}")

    input(f"\n{C['G']}>> Return to Master Console...{C['W']}")

if __name__ == "__main__":
    memory_logger()
