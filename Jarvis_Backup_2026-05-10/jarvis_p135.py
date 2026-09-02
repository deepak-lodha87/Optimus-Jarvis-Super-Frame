import os

def materials_science():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 135: MATERIALS & METALLURGY    |")
    print("="*50)

    materials = {
        "TITANIUM": "Strong, light, heat resistant. Used in Jet Engines.",
        "CARBON FIBER": "Ultra-light, high strength. Used in Wings/Body.",
        "GRAPHENE": "Future material. 200x stronger than steel.",
        "ALUMINUM 7075": "Standard aircraft grade. Cheap but strong."
    }

    print("\n[SYSTEM]: Analyzing materials for high-speed flight...")
    
    choice = input("\n[COMMAND]: Enter Material Name (Titanium/Carbon/Graphene): ").upper().strip()
    
    if choice in materials:
        data = materials[choice]
        print(f"\n[DATA]: {data}")
        os.system(f"termux-tts-speak 'Commander, {choice} is an excellent choice for our project.'")
    else:
        print("\n[ERROR]: Material not in offline database.")

if __name__ == "__main__":
    materials_science()
