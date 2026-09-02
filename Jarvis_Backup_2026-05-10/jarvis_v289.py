import time, random, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def starhawk_telemetry():
    print(f"\n{C['B']}[SYSTEM]: Initializing Starhawk Live Telemetry...{C['W']}")
    time.sleep(1)
    
    try:
        altitude = 0
        velocity = 0
        while altitude < 5000:
            os.system('clear')
            altitude += random.randint(100, 300)
            velocity += random.randint(50, 150)
            pitch = random.uniform(5.0, 15.0)
            
            print(f"{C['B']}╔" + "═"*44 + "╗")
            print(f"║ {C['BOLD']}{'STARHAWK FLIGHT TELEMETRY (LIVE)':^42} {C['B']}║")
            print(f"╚" + "═"*44 + f"╝{C['W']}")
            
            print(f"\n {C['W']}ALTITUDE  : {C['G']}{altitude} m")
            print(f" {C['W']}VELOCITY  : {C['G']}{velocity} km/h")
            print(f" {C['W']}PITCH

cat << 'EOF' > jarvis_v289.py
import time, random, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def starhawk_telemetry():
    print(f"\n{C['B']}[SYSTEM]: Initializing Starhawk Live Telemetry...{C['W']}")
    time.sleep(1)
    
    try:
        altitude = 0
        velocity = 0
        while altitude < 5000:
            os.system('clear')
            altitude += random.randint(100, 300)
            velocity += random.randint(50, 150)
            pitch = random.uniform(5.0, 15.0)
            
            print(f"{C['B']}╔" + "═"*44 + "╗")
            print(f"║ {C['BOLD']}{'STARHAWK FLIGHT TELEMETRY (LIVE)':^42} {C['B']}║")
            print(f"╚" + "═"*44 + f"╝{C['W']}")
            
            print(f"\n {C['W']}ALTITUDE  : {C['G']}{altitude} m")
            print(f" {C['W']}VELOCITY  : {C['G']}{velocity} km/h")
            print(f" {C['W']}PITCH/YAW : {C['Y']}{pitch:.2f}°")
            print(f" {C['W']}FUEL CELL : {C['G']}98.2%")
            
            print(f"\n{C['B']}[HUD]: Climbing to target altitude...{C['W']}")
            time.sleep(0.5)
            
        print(f"\n{C['G']}[SUCCESS]: Target Altitude Reached. Leveling off.{C['W']}")
    except KeyboardInterrupt:
        print(f"\n{C['R']}[ALERT]: Telemetry Feed Disconnected.{C['W']}")

if __name__ == "__main__":
    starhawk_telemetry()
