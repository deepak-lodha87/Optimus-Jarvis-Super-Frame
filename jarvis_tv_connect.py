import os
import requests
import json

# DEEPAK SIR: Yahan apni TV ka asli IP address daalein
TV_IP = "192.168.1.XX" # Apne TV settings se dekh kar badlein

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def send_tv_command():
    url = f"http://{TV_IP}:8001/api/v2/"
    print(f"\033[1;36m[UPLINK]\033[0m Sending handshake to Samsung TV at {TV_IP}...")
    
    try:
        # TV ki info fetch karne ki koshish
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("\033[1;32m[CONNECTED]\033[0m TV has acknowledged Jarvis.")
            speak("Deepak sir, physical connection established. Please check your TV screen for authorization.")
        else:
            print("\033[1;31m[REJECTED]\033[0m TV is on the network but connection was refused.")
    except Exception as e:
        print(f"\033[1;31m[ERROR]\033[0m Could not find TV. Are you on the same Wi-Fi?")

if __name__ == "__main__":
    send_tv_command()
