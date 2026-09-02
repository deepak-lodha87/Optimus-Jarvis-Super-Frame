import time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def thrust_calculation():
    print(f"\n{C['B']}[AEROSPACE]: Initializing Thrust-to-Weight Ratio Check...{C['W']}")
    try:
        weight = float(input(f"{C['Y']}Enter Drone Weight (grams): {C['W']}"))
        thrust = float(input(f"{C['Y']}Enter Total Motor Thrust (grams): {C['W']}"))
        ratio = thrust / weight
        
        print(f"\n{C['W']}ANALYSIS RESULTS:")
        print(f"─"*30)
        print(f"TWR Ratio: {C['G'] if ratio >= 2 else C['R']}{ratio:.2f}{C['W']}")
        
        if ratio < 2:
            print(f"{C['R']}[ALERT]: Insufficient lift for stable flight.{C['W']}")
        else:
            print(f"{C['G']}[STABLE]: Flight dynamics optimized.{C['W']}")
    except ValueError:
        print(f"{C['R']}[ERROR]: Invalid data input.{C['W']}")

def mission_entry():
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS AEROSPACE & FLIGHT LOGIC':^42} {C['B']}║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    thrust_calculation()

if __name__ == "__main__":
    mission_entry()
