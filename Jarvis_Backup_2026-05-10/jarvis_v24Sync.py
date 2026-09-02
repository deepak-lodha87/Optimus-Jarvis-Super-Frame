import os
import json
import subprocess

def get_real_battery():
    # Termux API से असली बैटरी डेटा प्राप्त करना
    try:
        output = subprocess.check_output(['termux-battery-status'])
        data = json.loads(output)
        return data['percentage'], data['status'], data['temperature']
    except:
        return "Error", "Unknown", 0.0

def sync_dashboard():
    print("\n" + "="*45)
    print("      JARVIS REAL-TIME HARDWARE SYNC")
    print("="*45)
    
    pct, status, temp = get_real_battery()
    
    if pct == "Error":
        msg = "Commander, Termux API is not responding. Please install termux-api."
    else:
        msg = f"Commander Deepak, real-time battery is at {pct} percent. Thermal level is {temp} degrees."
    
    print(f"\n[REAL-DATA]:")
    print(f"  --> Battery: [{pct}%]")
    print(f"  --> Status:  [{status}]")
    print(f"  --> Temperature: [{temp}°C]")
    
    # विजुअल प्रोग्रेस बार (असली प्रतिशत के आधार पर)
    if isinstance(pct, int):
        bar = "█" * (pct // 5) + "-" * (20 - (pct // 5))
        print(f"\n[ENERGY CORE]: |{bar}| {pct}%")
    
    os.system(f"termux-tts-speak '{msg}'")
    print("\n" + "="*45)

if __name__ == "__main__":
    sync_dashboard()
