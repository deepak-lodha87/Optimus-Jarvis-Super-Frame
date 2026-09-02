import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def behavior_analytics_engine():
    os.system('clear')
    print("\033[1;36m" + "📈"*30)
    print("      OPTIMUS NEURAL SYSTEMS : BEHAVIOR ANALYTICS (P368)")
    print("📈"*30 + "\033[0m")
    
    optimus_speak("Initiating behavior analytics. Mapping user activity cycles.")
    
    # Simulated Usage Data (Hour of the day: Activity Level %)
    usage_data = {
        "08:00 AM": 20, "12:00 PM": 85, "04:00 PM": 95, 
        "08:00 PM": 70, "12:00 AM": 10
    }
    
    print("\n\033[1;33m[ANALYZING]: Activity Distribution Over 24 Hours...\033[0m")
    time.sleep(1.2)
    
    peak_hour = ""
    max_val = 0
    
    print("-" * 45)
    print(f"{'TIME CYCLE':<15} | {'ACTIVITY LEVEL (%)':<20}")
    print("-" * 45)
    
    for t, val in usage_data.items():
        bar = '█' * (val // 10)
        print(f"{t:<15} | \033[1;32m{bar:<10}\033[0m {val}%")
        if val > max_val:
            max_val = val
            peak_hour = t
        time.sleep(0.3)
    
    print("-" * 45)
    
    optimus_speak(f"Peak activity detected at {peak_hour}. Optimizing CPU allocation for high performance.")
    print(f"\n\033[1;36m[INSIGHT]: System will enter 'Performance Mode' at {peak_hour}.\033[0m")

if __name__ == "__main__":
    behavior_analytics_engine()
