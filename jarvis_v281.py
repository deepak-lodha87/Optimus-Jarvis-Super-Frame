import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "W": "\033[0m", "BOLD": "\033[1m"}

def save_log(entry):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    with open("project_logs.txt", "a") as f:
        f.write(f"[{timestamp}] {entry}\n")
    print(f"\n{C['G']}[SUCCESS]: Entry secured in project_logs.txt{C['W']}")

def mission_entry():
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS PROJECT LOG INTERFACE':^42} {C['B']}║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    
    note = input(f"\n{C['Y']}ENTER LOG ENTRY:{C['W']} ")
    if note:
        save_log(note)
    else:
        print("Log cancelled. Empty entry.")

if __name__ == "__main__":
    mission_entry()
