import os
import time
import shutil
import json

def get_battery():
    status = os.popen("termux-battery-status").read()
    return json.loads(status)['percentage']

def get_storage():
    total, used, free = shutil.disk_usage("/sdcard")
    return int((used / total) * 100)

def draw_bar(percent, label):
    bar_length = 20
    filled_length = int(bar_length * percent // 100)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    print(f"{label}: [{bar}] {percent}%")

def phase_76_dashboard():
    os.system("clear")
    print("==========================================")
    print("      JARVIS SYSTEM HEALTH DASHBOARD      ")
    print("==========================================")
    time.sleep(1)
    
    battery = get_battery()
    storage = get_storage()
    
    draw_bar(battery, "🔋 BATTERY")
    draw_bar(storage, "💾 STORAGE")
    
    print("==========================================")
    print("STATUS: ALL SYSTEMS NOMINAL")
    print("==========================================")
    
    os.system("termux-tts-speak 'दीपक, सिस्टम हेल्थ डैशबोर्ड अपडेट कर दिया गया है।'")

if __name__ == "__main__":
    phase_76_dashboard()
