import os

def blueprint_engine():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 132: OFFLINE BLUEPRINT ENGINE    |")
    print("="*50)

    # 1. Engineering Database (Offline)
    blueprints = {
        "FIGHTER JET": "Model: Mach-X, Engine: Scramjet, Capability: Hypersonic Stealth.",
        "IRON SUIT": "Armor: Gold-Titanium Alloy, Power: Arc Core (Theoretical Logic).",
        "PLANET DATA": "Kepler-186f: Earth-size planet in habitable zone (580 LY away).",
        "MANUFACTURING": "Protocol: Wireless CNC/3D Link, Status: Ready to Fabricate."
    }

    print("\n[JARVIS]: Offline Blueprints Loaded Successfully.")
    query = input("\n[COMMAND]: Commander, which blueprint data do you need? ").upper().strip()

    if query in blueprints:
        result = blueprints[query]
        print(f"\n[DATA FOUND]: {result}")
        os.system(f"termux-tts-speak '{query} specifications retrieved.'")
    else:
        print("\n[ERROR]: This blueprint is not in my local database yet.")
        os.system("termux-tts-speak 'I do not have that data yet, Commander.'")

if __name__ == "__main__":
    blueprint_engine()
