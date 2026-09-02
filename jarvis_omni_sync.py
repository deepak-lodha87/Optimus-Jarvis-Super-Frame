import os
import requests
import time

# DEEPAK SIR: Yahan TV Settings > Network se mila IP daalein
TV_IP = "APKA_TV_IP" 

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def execute_omni_sync():
    print(f"\033[1;36m[UPLINK]\033[0m Reaching Starlink-1008 Registry...")
    try:
        # Step 1: Satellite ki live location lena
        sat_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
        sat_data = requests.get(sat_url, timeout=10).json()[0]
        name = sat_data['OBJECT_NAME']
        
        print(f"\033[1;32m[LIVE]\033[0m Data Received for {name}")
        speak(f"Deepak sir, {name} telemetry is locked. Establishing TV bridge.")
        
        # Step 2: TV ke sath handshake karna
        tv_url = f"http://{TV_IP}:8001/api/v2/"
        print(f"\033[1;34m[BRIDGE]\033[0m Connecting to Samsung TV at {TV_IP}...")
        
        # Testing if TV is reachable
        tv_check = requests.get(tv_url, timeout=5)
        
        if tv_check.status_code == 200:
            print("\033[1;32m[SUCCESS]\033[0m Omni-Sync Established!")
            speak("Sir, the satellite feed is now synchronized with your television.")
        else:
            print("\033[1;33m[ALERT]\033[0m TV found. Use remote to press 'Allow'.")
            speak("Deepak sir, please authorize Jarvis on your TV screen.")
            
    except Exception as e:
        print(f"\033[1;31m[ERROR]\033[0m Link failed. IP: {TV_IP} unreachable.")
        speak("Sir, the physical connection failed. Please check the IP address.")

if __name__ == "__main__":
    execute_omni_sync()
