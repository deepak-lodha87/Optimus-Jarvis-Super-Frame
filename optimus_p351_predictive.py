import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def predictive_analysis():
    os.system('clear')
    print("\033[1;33m" + "▲"*60)
    print("      OPTIMUS NEURAL SYSTEMS : PREDICTIVE MAINTENANCE (P351)")
    print("▲"*60 + "\033[0m")
    
    optimus_speak("Initiating predictive forecasting. Analyzing wear and tear patterns.")
    
    # Asset Health Data
    assets = {
        "hunter 350": [
            {"part": "Engine Oil", "usage": "2800km", "limit": "3000km", "risk": "HIGH"},
            {"part": "Brake Pads", "usage": "60%", "limit": "90%", "risk": "MEDIUM"},
            {"part": "Chain Tension", "usage": "Normal", "limit": "Adjust soon", "risk": "LOW"}
        ],
        "uav drone": [
            {"part": "Motor Bearings", "usage": "45 hrs", "limit": "50 hrs", "risk": "HIGH"},
            {"part": "Propeller Integrity", "usage": "Minor Scratches", "limit": "Replace", "risk": "MEDIUM"},
            {"part": "Battery Cycles", "usage": "120", "limit": "150", "risk": "LOW"}
        ]
    }
    
    target = input("\n\033[1;32m[INPUT]: Select Asset for Forecasting (Hunter 350 / UAV Drone): \033[0m").lower()
    
    if target in assets:
        optimus_speak(f"Forecasting results for {target} are ready.")
        print(f"\n\033[1;36m[REPORT]: {target.upper()} HEALTH ANALYSIS\033[0m")
        print("-" * 55)
        print(f"{'PART':<20} | {'STATUS/USAGE':<15} | {'RISK LEVEL'}")
        print("-" * 55)
        for item in assets[target]:
            color = "\033[1;31m" if item["risk"] == "HIGH" else "\033[1;33m"
            print(f"{item['part']:<20} | {item['usage']:<15} | {color}{item['risk']}\033[0m")
            time.sleep(0.5)
        print("-" * 55)
    else:
        optimus_speak("Target asset not found in maintenance logs.")

if __name__ == "__main__":
    predictive_analysis()
