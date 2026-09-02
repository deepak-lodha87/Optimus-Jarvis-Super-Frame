import os
import time

def flight_stress_test():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 145: FLIGHT STRESS INTEGRATION |")
    print("="*50)

    print("\n[SYSTEM]: Connecting to Jet's Flight Control Computer...")
    time.sleep(1.5)
    
    # Simulating High-G Turn Logic
    g_force = float(input("\n[COMMAND]: Enter Target G-Force for Maneuver: "))
    
    print(f"\n[JARVIS]: Analyzing structural integrity for {g_force}G...")
    time.sleep(2)
    
    if g_force > 9.0:
        status = "CRITICAL: Structural failure imminent. Redesigning wings."
    else:
        status = "STABLE: Flight logic synchronized with hardware actuators."

    print(f"\n[RESULT]: {status}")
    os.system(f"termux-tts-speak '{status}'")

    print("\n[LOG]: Hardware-Software handshake complete.")
    print("="*50)

if __name__ == "__main__":
    flight_stress_test()
