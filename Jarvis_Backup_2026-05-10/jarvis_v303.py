import time, os

# Advanced UI Colors
C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def advanced_mfg():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'ADVANCED MANUFACTURING & DRONE LAB':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[JARVIS]: Accessing Manufacturing Blueprints...{C['W']}")
    time.sleep(1)

    menu = {
        "1": "Fabricate MK-I Suit Component (Titanium-Gold Alloy)",
        "2": "Drone Reconnaissance - Flight Test Mode",
        "3": "Satellite Uplink - Drone GPS Calibration",
        "4": "Return to Supreme Console"
    }

    for k, v in menu.items():
        print(f"{C['G']}{k}. {C['W']}{v}")

    choice = input(f"\n{C['BOLD']}{C['B']}Commander Deepak, enter directive: {C['W']}")

    if choice == "1":
        print(f"\n{C['
cat << 'EOF' > jarvis_v303.py
import time, os

# Advanced UI Colors
C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def advanced_mfg():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'ADVANCED MANUFACTURING & DRONE LAB':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[JARVIS]: Accessing Manufacturing Blueprints...{C['W']}")
    time.sleep(1)

    menu = {
        "1": "Fabricate MK-I Suit Component (Titanium-Gold Alloy)",
        "2": "Drone Reconnaissance - Flight Test Mode",
        "3": "Satellite Uplink - Drone GPS Calibration",
        "4": "Return to Supreme Console"
    }

    for k, v in menu.items():
        print(f"{C['G']}{k}. {C['W']}{v}")

    choice = input(f"\n{C['BOLD']}{C['B']}Commander Deepak, enter directive: {C['W']}")

    if choice == "1":
        print(f"\n{C['Y']}[PRINTING]: Starting 3D fabrication sequence...{C['W']}")
        for i in range(0, 101, 20):
            print(f"Laying Layer {i}%... {C['G']}STABLE{C['W']}")
            time.sleep(0.6)
        print(f"\n{C['BOLD']}{C['G']}SUCCESS: Component Fabricated.{C['W']}")
    
    elif choice == "2":
        print(f"\n{C['R']}[PRE-FLIGHT]: Checking Drone Rotors...{C['W']}")
        time.sleep(1)
        print(f"{C['B']}Checking LiDAR Scanning... {C['G']}[ACTIVE]{C['W']}")
        print(f"{C['B']}Battery Level: 98%... {C['G']}[OPTIMAL]{C['W']}")
        print(f"\n{C['BOLD']}{C['Y']}JARVIS: Drone is cleared for take-off.{C['W']}")

    elif choice == "4":
        return

if __name__ == "__main__":
    advanced_mfg()
