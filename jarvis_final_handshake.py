import os
import requests

# INSTRUCTION: Replace with your REAL TV IP from Settings
# Example: TV_IP = "192.168.1.5"
TV_IP = "REPLACE_WITH_YOUR_TV_IP" 

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def establish_real_link():
    url = f"http://{TV_IP}:8001/api/v2/"
    print(f"\033[1;36m[ATTEMPTING]\033[0m Connecting to Hardware at {TV_IP}...")
    speak(f"Deepak sir, attempting to bypass the physical barrier. Please watch your TV screen.")

    try:
        # Haqiqat mein packet bhejna
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("\033[1;32m[SUCCESS]\033[0m Handshake Received!")
            speak("Sir, the TV has recognized my signature. Connection is now REAL.")
        else:
            print("\033[1;33m[PENDING]\033[0m Connection detected. Waiting for 'Allow' on TV screen.")
            speak("Deepak sir, please use your remote to select Allow on the TV screen.")
    except:
        print("\033[1;31m[FAILED]\033[0m Target not found. Check if TV and Phone are on the same Wi-Fi.")

if __name__ == "__main__":
    establish_real_link()
