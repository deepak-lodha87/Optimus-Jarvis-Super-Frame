import os

def energy_core():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 136: PROPULSION & ENERGY CORE  |")
    print("="*50)

    fuel_types = {
        "HYDROGEN": "Zero emission, high efficiency. Great for space.",
        "ION DRIVE": "Electrical propulsion for long-distance space travel.",
        "SOLID FUEL": "High thrust, used in missile and rocket boosters.",
        "ARC REACTOR": "Theoretical High-density energy source (Iron Man Style)."
    }

    print("\n[SYSTEM]: Analyzing energy efficiency...")
    
    choice = input("\n[COMMAND]: Select Fuel/Power (Hydrogen/Ion/Solid/Arc): ").upper().strip()
    
    if choice in fuel_types:
        spec = fuel_types[choice]
        print(f"\n[ENERGY DATA]: {spec}")
        os.system(f"termux-tts-speak 'Power source confirmed: {choice}. Output optimized.'")
    else:
        print("\n[ERROR]: Unknown energy source. Need more research.")

if __name__ == "__main__":
    energy_core()
