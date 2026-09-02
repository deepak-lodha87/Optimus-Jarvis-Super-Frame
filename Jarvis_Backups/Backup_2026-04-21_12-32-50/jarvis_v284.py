import time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def gravity_sim():
    planets = {"Earth": 9.8, "Mars": 3.7, "Moon": 1.6}
    print(f"\n{C['B']}[AEROSPACE]: Gravity & Lift Simulation Active...{C['W']}")
    
    try:
        mass = float(input(f"{C['Y']}Enter Starhawk Mass (kg): {C['W']}"))
        print(f"\n{C['W']}Required Lift Force (Newtons):")
        print(f"─"*35)
        
        for name, g in planets.items():
            force = mass * g
            print(f"{name:<10}: {C['G']}{force:.2f} N{C['W']}")
            
    except ValueError:
        print(f"{C['R']}[ERROR]: Invalid mass input.{C['W']}")

def mission_entry():
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'STARHAWK GRAVITY & LIFT SIMULATOR':^42} {C['B']}║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    gravity_sim()

if __name__ == "__main__":
    mission_entry()
