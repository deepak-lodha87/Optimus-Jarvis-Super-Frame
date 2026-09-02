import time
import os
import subprocess
import random

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_resource_balancer():
    os.system('clear')
    print("\033[1;32m" + "⚖️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : RESOURCE BALANCER (P379)")
    print("⚖️"*30 + "\033[0m")
    
    optimus_speak("Initiating resource balancing. Distributing CPU load across neural cores.")
    
    # Active Modules and their simulated CPU usage
    active_modules = {
        "Neural Firewall (P369)": random.randint(5, 15),
        "Decision Engine (P364)": random.randint(10, 25),
        "Log Archive (P365)": random.randint(2, 8),
        "Mesh Network (P376)": random.randint(20, 45)
    }
    
    total_load = sum(active_modules.values())
    print(f"\n\033[1;33m[TOTAL SYSTEM LOAD]: {total_load}%\033[0m")
    print("-" * 55)
    
    for module, load in active_modules.items():
        status = "\033[1;32mOPTIMAL\033[0m"
        if load > 30:
            status = "\033[1;31mHEAVY - THROTTLING\033[0m"
            optimus_speak(f"High load detected in {module}. Reducing clock speed.")
        
        bar = '■' * (load // 2)
        print(f"{module:<25} | {bar:<20} | {load}% | {status}")
        time.sleep(0.5)
    
    print("-" * 55)
    
    if total_load > 80:
        optimus_speak("Warning. Total system load is critical. Switching to energy-efficient mode.")
    else:
        optimus_speak("Resource allocation is balanced. System thermal levels are stable.")

if __name__ == "__main__":
    neural_resource_balancer()
