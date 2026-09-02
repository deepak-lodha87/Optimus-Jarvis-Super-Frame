import os
import time

def system_overdrive():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 141: SYSTEM OVERDRIVE ENGINE   |")
    print("="*50)

    item = input("\n[COMMAND]: Enter System/Machine to Upgrade: ").upper().strip()
    
    print(f"\n[JARVIS]: Analyzing {item} architecture...")
    time.sleep(1.5)
    
    print("[LOG]: Finding optimization gaps...")
    time.sleep(1)

    # Upgrade Logic
    upgrade_path = {
        "ENGINE": "Install High-Flow Injectors & AI Fuel Mapping. Speed +40%.",
        "PROCESSOR": "Redirecting unused background power. Efficiency +25%.",
        "BATTERY": "Optimizing chemical discharge cycles. Life +50%.",
        "FRAME": "Adding Carbon-Fiber reinforcement points. Weight -15%."
    }

    if item in upgrade_path:
        solution = upgrade_path[item]
        status_msg = f"Upgrade found! {solution}"
        print(f"\n[STATUS]: OPTIMIZATION READY")
        print(f"[JARVIS]: {status_msg}")
        os.system(f"termux-tts-speak '{status_msg}'")
    else:
        status_msg = f"Commander, I am creating a custom upgrade for {item}."
        print(f"\n[STATUS]: CALCULATING CUSTOM PATH")
        print(f"[JARVIS]: {status_msg}")
        os.system(f"termux-tts-speak '{status_msg}'")

    print("\n[RESULT]: System is now running in 2X Efficiency Mode.")
    print("="*50)

if __name__ == "__main__":
    system_overdrive()
