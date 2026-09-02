import time
import os
import subprocess

def check_battery_status():
    print("\n[SYSTEM]: Analyzing Power Matrix...")
    try:
        # Termux API के जरिए बैटरी स्टेटस लेना
        output = subprocess.check_output(["termux-battery-status"]).decode("utf-8")
        import json
        data = json.loads(output)
        percentage = data['percentage']
        status = data['status']
        
        msg = f"Commander Deepak, Battery is at {percentage} percent. Status: {status}."
        print(f"[JARVIS]: {msg}")
        os.system(f"termux-tts-speak '{msg}'")
        
        if percentage < 20 and status != "CHARGING":
            alert = "Warning! Power levels are critical. Please connect the charger."
            print(f"[ALERT]: {alert}")
            os.system(f"termux-tts-speak '{alert}'")
    except:
        print("[ERROR]: Termux API not found. Please install termux-api package.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 185: POWER MONITOR        |")
    print("="*50)
    time.sleep(1)
    
    check_battery_status()
    
    print("\n[SYSTEM]: Optimus Jarvis Super-Frame is active.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
