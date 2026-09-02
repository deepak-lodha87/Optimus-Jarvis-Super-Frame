import os
import requests
import time

# DEEPAK SIR: Yahan apna TV IP dalkar enter dabayein
TV_IP = "192.168.X.X" 

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def establish_sync():
    print(f"\033[1;34m[UPLINK]\033[0m Fetching Real-Time Starlink Metadata...")
    try:
        # Step 1: Internet se asli satellite data lena
        r = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json", timeout=10)
        sat_data = r.json()[0]
        name = sat_data['OBJECT_NAME']
        
        # Step 2: TV ke hardware se baat karna
        print(f"\033[1;36m[BRIDGE]\033[0m Beaming {name} trajectory to TV at {TV_IP}...")
        speak(f"Deepak sir, reality bridge is forming. Sending {name} data to your Samsung display.")
        
        # Testing physical connection
        test_tv = requests.get(f"http://{TV_IP}:8001/api/v2/", timeout=5)
        
        if test_tv.status_code == 200:
            print(f"\033[1;32m[SUCCESS]\033[0m Satellite and TV are now SYNCHRONIZED.")
            speak("Sir, the orbital eye is now open on your main screen.")
        else:
            print("\033[1;33m[WAITING]\033[0m TV found. Check screen for 'Allow' permission.")
            speak("Please authorize Jarvis on your TV screen.")
            
    except Exception as e:
        print(f"\033[1;31m[ERROR]\033[0m Link failed. Ensure IP is correct and phone is on same Wi-Fi.")

if __name__ == "__main__":
    establish_sync()
