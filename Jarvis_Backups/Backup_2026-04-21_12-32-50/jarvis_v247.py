import os
import time

def tactical_home_command():
    print("\n" + "="*45)
    print("      JARVIS TACTICAL HOME-COMMAND")
    print("="*45)
    
    msg_init = "Commander Deepak, home-automation sub-routine is active."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    devices = {
        "1": "Main Perimeter Gate",
        "2": "Laboratory Lights",
        "3": "Climate Control (AC)",
        "4": "Surveillance Drones"
    }
    
    print("\n[ACTIVE DEVICES]:")
    for key, name in devices.items():
        print(f"{key}. {name}")
    
    choice = input("\n[INPUT]: Select Device ID to toggle: ")
    
    if choice in devices:
        action = "Activating" if choice != "1" else "Securing"
        msg = f"{action} {devices[choice]}. Protocol initiated."
        print(f"\n[PROCESS]: {msg}")
        os.system(f"termux-tts-speak '{msg}'")
        
        # सिमुलेटेड हार्डवेयर रिस्पॉन्स
        time.sleep(1.5)
        print(f"[STATUS]: {devices[choice]} is now operational/secured.")
    else:
        print("\n[ERROR]: Device not recognized.")

    print("\n" + "="*45)

if __name__ == "__main__":
    tactical_home_command()
