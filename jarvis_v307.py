import time, os, random

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def atmospheric_analysis():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS: ATMOSPHERIC & WEATHER UPLINK':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")

    print(f"\n{C['Y']}[JARVIS]: Establishing Satellite Link...{C['W']}")
    time.sleep(1.5)

    # Simulated Environmental Data
    temp = random.randint(25, 42)
    wind_speed = random.randint(5, 25)
    visibility = random.choice(["EXCELLENT", "MODERATE", "LOW (FOG)"])

    print(f"\n{C['BOLD']}{C['B']}--- CURRENT EXTERNAL CONDITIONS ---{C['W']}")
    print(f"{C['W']}Temperature     : {C['Y']}{temp}°C")
    print(f"Wind Velocity   : {C['Y']}{wind_speed} km/h")
    print(f"Visual Range    : {C['G'] if visibility == 'EXCELLENT' else C['R']}{visibility}{C['W']}")
    
    print(f"\n{C['BOLD']}{C['B']}--- FLIGHT SAFETY ADVISORY ---{C['W']}")
    if wind_speed > 20:
        print(f"{C['R']}[ALERT]: High wind speeds detected. Drone flight not recommended.{C['W']}")
    else:
        print(f"{C['G']}[SUCCESS]: Conditions optimal for Starhawk deployment.{C['W']}")

    input(f"\n{C['G']}>> Acknowledge and Return...{C['W']}")

if __name__ == "__main__":
    atmospheric_analysis()
