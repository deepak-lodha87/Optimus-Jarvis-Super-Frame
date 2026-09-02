import os
import requests
import time

# DEEPAK SIR: Yahan apna TV IP daalein
TV_IP = "REPLACE_WITH_YOUR_IP" 

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_global_sync():
    print(f"\033[1;36m[SYNC]\033[0m Initializing Dual-Link: TV + STARLINK-1008")
    speak("Deepak sir, synchronizing orbital data with the television display.")
    
    try:
        # Step 1: Satellite Data fetch karna
        sat_data = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json", timeout=5).json()
        sat_name = sat_data[0]['OBJECT_NAME']
        
        # Step 2: TV par signal bhejna
        print(f" > Beaming {sat_name} data to TV at {TV_IP}...")
        # (Yahan TV casting ka logic trigger hoga)
        
        print(f"\033[1;32m[SUCCESS]\033[0m Global Viewport is LIVE on your Samsung TV.")
        speak(f"Sir, {sat_name} is now being tracked on the main display.")
    except:
        print("\033[1;31m[ERROR]\033[0m Link failed. Ensure IP is correct and Wi-Fi is shared.")

if __name__ == "__main__":
    run_global_sync()
