import os
import time

def smart_home_protocol():
    print("\n" + "="*40)
    print("      JARVIS SMART HOME INTERFACE")
    print("="*40)
    
    devices = {
        "1": "Living Room Lights",
        "2": "Air Conditioning (AC)",
        "3": "Main Gate Security Lock",
        "4": "Kitchen Ventilation"
    }
    
    msg_ask = "Commander Deepak, smart devices are online. Select a device to toggle."
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    for key, name in devices.items():
        print(f"[{key}] {name}")
        
    choice = input("\n[INPUT]: Select Device (1-4): ")
    
    if choice in devices:
        device_name = devices[choice]
        state = input(f"[INPUT]: Command for {device_name} (ON/OFF): ").upper()
        
        if state in ['ON', 'OFF']:
            action_msg = f"Commander, switching {device_name} to {state} mode."
            print(f"\n[JARVIS]: {action_msg}")
            os.system(f"termux-tts-speak '{action_msg}'")
            
            # सिमुलेशन डिले
            time.sleep(1)
            
            success = f"Protocol executed. {device_name} is now {state}."
            print(f"[STATUS]: {success}")
            os.system(f"termux-tts-speak '{success}'")
        else:
            print("[ERROR]: Invalid state command.")
    else:
        print("[ERROR]: Device not recognized in the smart grid.")

    print("\n" + "="*40)

if __name__ == "__main__":
    smart_home_protocol()
