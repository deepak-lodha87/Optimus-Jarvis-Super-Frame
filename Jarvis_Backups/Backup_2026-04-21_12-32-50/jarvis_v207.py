import os
import time

def app_usage_alert():
    print("\n" + "="*40)
    print("      JARVIS APP-USAGE MONITOR")
    print("="*40)
    
    app_name = input("\n[INPUT]: Which app are you monitoring? ")
    limit_min = int(input("[INPUT]: Set alert limit (in minutes): "))
    
    msg_start = f"Monitoring {app_name} for {limit_min} minutes, Commander."
    print(f"\n[JARVIS]: {msg_start}")
    os.system(f"termux-tts-speak '{msg_start}'")
    
    # समय का इंतजार (मिनट को सेकंड में बदलकर)
    time.sleep(limit_min * 60)
    
    alert_msg = f"Commander Deepak, time limit for {app_name} has been reached. Please check your schedule."
    print(f"\n[!!! ALERT !!!]: {alert_msg}")
    os.system(f"termux-tts-speak '{alert_msg}'")
    print("="*40)

if __name__ == "__main__":
    app_usage_alert()
