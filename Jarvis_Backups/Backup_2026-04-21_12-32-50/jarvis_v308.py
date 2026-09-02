import time, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def emergency_protocol():
    os.system('clear')
    print(f"{C['R']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'CRITICAL ALERT: EMERGENCY DISTRESS SIGNAL':^46} {C['R']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[SYSTEM]: Initiating Rapid Response...{C['W']}")
    time.sleep(1)

    # Emergency Actions
    actions = [
        "Transmitting GPS Coordinates to Rescue Satellite",
        "Engaging Auxiliary Power to Shield Emitters",
        "Broadcasting SOS on Encrypted Frequency",
        "Locking down sensitive Project Blueprints"
    ]

    for action in actions:
        print(f"{C['R']}>> {C['W']}{action}... {C['G']}[DONE]{C['W']}")
        time.sleep(0.6)

    print(f"\n{C['BOLD']}{C['Y']}--- STATUS REPORT ---{C['W']}")
    print(f"Distress Signal : {C['G']}ACTIVE{C['W']}")
    print(f"System State    : {C['R']}STAY-SAFE MODE{C['W']}")
    
    print(f"\n{C['BOLD']}{C['B']}[JARVIS]: Commander Deepak, emergency protocols are in place. Standing by for further instructions.{C['W']}")

    input(f"\n{C['G']}>> Deactivate Alert and Return...{C['W']}")

if __name__ == "__main__":
    emergency_protocol()
