import os
import time
import random

def monitor_core_temp():
    print("\n[SYSTEM]: Accessing CPU Thermal Sensors...")
    time.sleep(1.2)
    # सिम्युलेटेड टेम्परेचर डेटा
    temp = random.randint(35, 65)
    print(f"[STATUS]: Core Temperature at {temp}°C.")
    
    if temp > 60:
        alert = "Commander Deepak, system core is overheating. Suggesting immediate cooling protocols."
        print(f"!!! WARNING: {alert} !!!")
        os.system(f"termux-tts-speak '{alert}'")
    else:
        print("[JARVIS]: Thermal levels are optimal. Systems running cool.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 191: THERMAL CORE MONITOR    |")
    print("="*50)
    
    monitor_core_temp()
    
    print("\n[SYSTEM]: Monitoring continues in background.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
