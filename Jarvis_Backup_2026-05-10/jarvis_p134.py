import os

def aerodynamics_logic():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 134: AERODYNAMICS SIMULATOR    |")
    print("="*50)

    # Physics Constants
    print("[SYSTEM]: Calculating Air Resistance (Drag)...")
    
    speed_mach = float(input("\n[COMMAND]: Enter Target Speed (Mach 1-5): "))
    
    if speed_mach >= 1 and speed_mach < 5:
        result = "Supersonic Flight - Requires Titanium Heat Shielding."
    elif speed_mach >= 5:
        result = "Hypersonic Flight - Requires Carbon-Carbon Composites."
    else:
        result = "Subsonic Flight - Standard Aluminum Frame."

    print(f"\n[JARVIS ANALYSIS]: For Mach {speed_mach}, status is: {result}")
    os.system(f"termux-tts-speak 'Commander, for Mach {speed_mach}, we need {result}'")

    print("\n[LOG]: Phase 134 Complete. Engineering data saved.")

if __name__ == "__main__":
    aerodynamics_logic()
