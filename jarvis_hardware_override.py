import os
import requests

TV_IP = os.getenv('TV_IP')

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def execute_reality_link():
    url = f"http://{TV_IP}:8001/api/v2/"
    print(f"\033[1;36m[TARGET]\033[0m Initializing link to {TV_IP}...")
    
    try:
        # Asli hardware request
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("\033[1;32m[SUCCESS]\033[0m Reality Bridge established!")
            speak("Deepak sir, the connection is now tangible. I am inside the hardware.")
        else:
            print("\033[1;33m[PENDING]\033[0m Hardware found. Deepak sir, press ALLOW on your TV screen now!")
            speak("Sir, please authorize my access on the physical screen.")
    except:
        print("\033[1;31m[FAILED]\033[0m Physical target not found. Check IP and Wi-Fi.")

if __name__ == "__main__":
    execute_reality_link()
