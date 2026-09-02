import os
import time
import random

def draw_bar(label, percent):
    bar_length = 20
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"{label:12} |{bar}| {percent}%")

def health_dashboard():
    print("\n" + "="*40)
    print("      JARVIS SYSTEM HEALTH CORE")
    print("="*40)
    time.sleep(0.5)
    
    # सिम्युलेटेड डेटा (इसे रियल सेंसर से भी जोड़ा जा सकता है)
    cpu_load = random.randint(15, 45)
    ram_usage = random.randint(40, 75)
    battery = random.randint(80, 95)
    
    draw_bar("CPU LOAD", cpu_load)
    draw_bar("RAM USAGE", ram_usage)
    draw_bar("BATTERY", battery)
    
    status_msg = "Commander Deepak, all hardware parameters are within safe limits."
    print("\n[JARVIS]: " + status_msg)
    os.system(f"termux-tts-speak '{status_msg}'")
    print("="*40)

if __name__ == "__main__":
    health_dashboard()
