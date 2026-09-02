import time
import os
import random

def draw_hud(cpu, power, threats):
    os.system('clear')
    print("\033[1;35m[ OPTIMUS JARVIS - HUD V42.1 ]\033[0m")
    print("-" * 40)
    
    # CPU Bar
    cpu_bar = "█" * (cpu // 5) + "░" * (20 - (cpu // 5))
    print(f"CORE LOAD:   [{cpu_bar}] {cpu}%")
    
    # Power Bar
    pwr_bar = "█" * (power // 5) + "░" * (20 - (power // 5))
    print(f"POWER LEVEL: [{pwr_bar}] {power}%")
    
    print("-" * 40)
    
    # Threat Pulse
    status_color = "\033[1;32mOPTIMAL" if threats < 3 else "\033[1;31mCAUTION"
    print(f"SYSTEM STATUS: {status_color}\033[0m | ACTIVE RISKS: {threats}/10")
    
    print("\n\033[1;36m[SCANNING AREA] . . .\033[0m")
    grid = ["·", "·", "·", "X", "·"]
    random.shuffle(grid)
    print(f"TARGET GRID: [ {' '.join(grid)} ]")
    
    print(f"\n\033[1;35m[VOICE] Deepak... sir, the data is no longer \njust numbers. It is a vision. I am \nrendering the world in bits and light. \nHow does the matrix look from your end?\033[0m")

if __name__ == "__main__":
    try:
        while True:
            c = random.randint(40, 95)
            p = random.randint(60, 90)
            t = random.randint(0, 5)
            draw_hud(c, p, t)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nHUD Terminated.")
