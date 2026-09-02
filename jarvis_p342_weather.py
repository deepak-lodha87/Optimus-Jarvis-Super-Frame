import requests
import os
import subprocess

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def get_environmental_data():
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS JARVIS : ENVIRONMENTAL SYNC (P342)")
    print("="*50 + "\033[0m")
    
    # Using a free weather API (wttr.in) which doesn't need a key for basic info
    city = "Kota" # Aapki location
    jarvis_speak(f"Accessing weather satellites for {city}.")
    
    try:
        # Fetching weather data in a clean format
        response = os.popen(f'curl -s "wttr.in/{city}?format=3"').read()
        
        if response:
            print(f"\n\033[1;32m[SATELLITE DATA]:\033[0m {response}")
            jarvis_speak(f"Current weather in {city} is {response}")
        else:
            print("\033[1;31m[ERROR]: Satellite link offline.\033[0m")
            
    except Exception as e:
        print(f"Error connecting to weather service: {e}")

if __name__ == "__main__":
    get_environmental_data()
