import os
import requests

# DEEPAK SIR: Is line mein apna asli IP daalein (Example: "192.168.1.10")
TV_IP = "ASLI_IP_YAHAN_LIKHO" 

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def connect_to_hardware():
    url = f"http://{TV_IP}:8001/api/v2/"
    print(f"\033[1;36m[ATTEMPTING]\033[0m Handshake with Samsung TV at {TV_IP}...")
    
    try:
        # Asli internet request for hardware link
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("\033[1;32m[SUCCESS]\033[0m Reality Bridge established!")
            speak("Deepak sir, I am now inside the TV system. Physical control is active.")
        else:
            print("\033[1;33m[PENDING]\033[0m Found TV! Press ALLOW on your screen now.")
            speak("Sir, please authorize the connection on your TV screen.")
    except:
        print("\033[1;31m[FAILED]\033[0m Still cannot find TV. Please check your IP and Wi-Fi.")

if __name__ == "__main__":
    if "ASLI_IP" in TV_IP:
        print("\033[1;31m[ERROR]\033[0m Deepak sir, pehle IP badaliye!")
    else:
        connect_to_hardware()
