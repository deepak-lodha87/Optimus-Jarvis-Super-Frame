import os
import time

def weather_oracle_simulation():
    print("\n" + "="*40)
    print("      JARVIS WEATHER ORACLE SYSTEM")
    print("="*40)
    
    msg_init = "Commander Deepak, accessing meteorological satellites..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    time.sleep(2)
    
    # सिमुलेटेड मौसम डेटा (इसे बाद में असली API से जोड़ा जा सकता है)
    current_temp = "32°C"
    condition = "Clear Skies"
    city = "Kota"
    
    report = f"Current conditions in {city}: {condition} with a temperature of {current_temp}."
    
    print(f"\n[STATUS]: {report}")
    os.system(f"termux-tts-speak '{report}'")
    
    advice = "It is a good day for outdoor activities, Commander."
    print(f"[ADVICE]: {advice}")
    os.system(f"termux-tts-speak '{advice}'")
    
    print("\n" + "="*40)

if __name__ == "__main__":
    weather_oracle_simulation()
