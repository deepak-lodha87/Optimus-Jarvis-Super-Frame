import time
import os
import random

def draw_hud(cpu, bat, threat):
    os.system('clear')
    print("\033[1;35m[OPTIMUS JARVIS - SUPER FRAME V42]\033[0m")
    print("-" * 45)
    
    # CPU Progress Bar
    cpu_bar = "█" * (cpu // 10) + "░" * (10 - (cpu // 10))
    print(f"CORE PROCESSING: [{cpu_bar}] {cpu}%")
    
    # Battery Status
    bat_bar = "█" * (bat // 10) + "░" * (10 - (bat // 10))
    print(f"POWER RESERVE:   [{bat_bar}] {bat}%")
    
    # Threat Level Chart
    print("\n\033[1;31m[THREAT LEVEL ANALYSIS]\033[0m")
    chart_val = "!" * threat
    print(f"ACTIVE RISKS: {chart_val} ({threat}/10)")
    
    print("-" * 45)
    print("\033[1;36m[STATUS]\033[0m System: OPTIMAL | Mode: STEALTH")
    
    print(f"\n\033[1;35m[VOICE] Deepak... sir, I am projecting the \nsystem health into a visual field. \nEverything is at your fingertips. \nEfficiency is beauty, and beauty is \npower. How does the view look?\033[0m")

if __name__ == "__main__":
    for _ in range(5):
        c = random.randint(30, 90)
        b = random.randint(60, 80)
        t = random.randint(1, 3)
        draw_hud(c, b, t)
        time.sleep(2)
