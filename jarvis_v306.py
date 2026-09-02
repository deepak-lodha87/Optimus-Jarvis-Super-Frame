import time, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def task_automation():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: GLOBAL TASK & DATA AUTOMATION':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    # Project Milestones
    goals = [
        "Complete Starhawk Suit MK-I Fabrication",
        "Integrate Real-time GPS Telemetry",
        "Expand Neural Voice Vocabulary"
    ]

    print(f"\n{C['Y']}[CURRENT MISSION GOALS]:{C['W']}")
    for i, goal in enumerate(goals, 1):
        print(f"{C['G']}{i}. {C['W']}{goal}")
        time.sleep(0.4)

    print(f"\n{C['BOLD']}{C['B']}--- AUTOMATION TOOLS ---{C['W']}")
    print("1. Add New Project Task")
    print("2. Run Global Integrity Audit")
    print("3. Return to Supreme Console")

    choice = input(f"\n{C['G']}>> SELECT COMMAND: {C['W']}")

    if choice == '2':
        print(f"\n{C['Y']}Running Global Audit...{C['W']}")
        for i in range(1, 101, 25):
            print(f"Checking Framework v300-305... {i}%")
            time.sleep(0.5)
        print(f"{C['BOLD']}{C['G']}AUDIT SUCCESS: All systems synchronized.{C['W']}")
    
    else:
        print("Returning...")

if __name__ == "__main__":
    task_automation()
