import os
import time
import random

def environmental_awareness():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 162: ENVIRONMENTAL INTELLIGENCE |")
    print("="*50)

    print("\n[SYSTEM]: Accessing onboard mobile sensors...")
    time.sleep(1.2)
    
    # Simulating sensor data (Temperature, Light, Battery)
    temp = random.randint(28, 35)
    light_level = random.randint(100, 800) # in Lux
    battery = random.randint(10, 100)
    
    print(f"[DATA]: Ambient Temperature: {temp}°C")
    print(f"[DATA]: Light Intensity: {light_level} Lux")
    print(f"[DATA]: Power Source Stability: {battery}%")

    if temp > 40:
        advice = "Commander, ambient heat is high. Cooling protocols recommended for hardware."
    elif battery < 20:
        advice = "Alert: Power levels are critical. Entering energy-saving mode."
    else:
        advice = "Environmental conditions are optimal. All systems nominal."

    print(f"\n[JARVIS]: {advice}")
    os.system(f"termux-tts-speak '{advice}'")

    print("\n[LOG]: Environmental scan complete. Monitoring active.")
    print("="*50)

if __name__ == "__main__":
    environmental_awareness()
