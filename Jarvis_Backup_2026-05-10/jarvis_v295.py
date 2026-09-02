import os, time, random

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def render_hud(alt, vel, fuel):
    os.system('clear')
    print(f"{C['B']}╔" + "═"*50 + "╗")
    print(f"║{C['BOLD']}{' STARHAWK TACTICAL HUD - MK II ':^50}{C['W']}{C['B']}║")
    print(f"╠" + "═"*50 + "╣")
    
    # Altitude and Velocity Bar
    alt_bar = "█" * int(alt/500)
    print(f"║ ALTITUDE : {C['G']}{alt:<6} m{C['W']} |{C['Y']}{alt_bar:<10}{C['B']}║")
    
    vel_bar = "█" * int(vel/150)
    print(f"║ VELOCITY : {C['G']}{vel:<6} km/h{C['W']}|{C['Y']}{vel_bar:<10}{C['B']}║")
    
    print(f"╠" + "═"*50 + "╣")
    print(f"║ FUEL CELL: {C['Y']}{fuel}%{C['W']} | STATUS: {C['G']}STABLE{C['B']:>13} ║")
    print(f"╚" + "═"*50 + f"╝{C['W']}")
    print(f"\n{C['B']}[JARVIS]: Scanning Sector for anomalies...{C['W']}")

def start_flight():
    altitude = 0
    velocity = 0
    fuel = 100
    try:
        while altitude < 5000:
            render_hud(altitude, velocity, fuel)
            altitude += random.randint(200, 400)
            velocity += random.randint(100, 200)
            fuel -= 1
            time.sleep(0.4)
        print(f"\n{C['G']}[SUCCESS]: Target Altitude Reached.{C['W']}")
    except KeyboardInterrupt:
        print(f"\n{C['R']}[ABORT]: Flight HUD Terminated.{C['W']}")

if __name__ == "__main__":
    start_flight()
