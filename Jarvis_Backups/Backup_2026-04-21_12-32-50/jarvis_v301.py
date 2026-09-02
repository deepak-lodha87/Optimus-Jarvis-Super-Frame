import time, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def drone_control():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'DRONE & MANUFACTURING INTERFACE v301':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[SYSTEM]: Initializing Flight Controller Data...{C['W']}")
    time.sleep(1)

    # Manufacturing & Flight Parameters
    specs = {
        "Propulsion": "Quad-Engine Brushless",
        "Navigation": "GPS + LiDAR Scanning",
        "Payload": "Tactical Recon Camera",
        "Material": "Carbon Fiber Reinforcement"
    }

    for key, value in specs.items():
        print(f"{C['G']}[OK] {key}: {C['W']}{value}")
        time.sleep(0.3)

    print(f"\n{C['BOLD']}{C['Y']}--- TACTICAL COMMANDS ---{C['W']}")
    print("1. Launch Drone (Flight Prep)")
    print("2. Start Prototype Manufacturing")
    print("3. Return to Master Console")

    choice = input(f"\n{C['G']}>> ENTER COMMAND: {C['W']}")

    if choice == '1':
        print(f"\n{C['R']}[ALERT]: Calibrating ESC and Rotors...{C['W']}")
        for i in range(1, 6):
            print(f"Propeller Rpm Test {i*20}%... {C['G']}STABLE{C['W']}")
            time.sleep(0.5)
        print(f"{C['BOLD']}{C['G']}READY FOR LIFT-OFF!{C['W']}")
        
    elif choice == '2':
        print(f"\n{C['B']}[INFO]: Loading Blueprint: Iron-Man Suit MK-I Component...{C['W']}")
        time.sleep(1.5)
        print(f"{C['Y']}Status: 3D Printing sequence initialized...{C['W']}")
        
    else:
        print("Returning...")

if __name__ == "__main__":
    drone_control()
