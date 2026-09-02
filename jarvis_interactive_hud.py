import time
import os
import sys
import select
import random

def draw_hud(mode, cpu):
    os.system('clear')
    color = "\033[1;36m" if mode == "STEALTH" else "\033[1;31m"
    print(f"{color}[ OPTIMUS JARVIS - INTERACTIVE V42.2 ]\033[0m")
    print("-" * 45)
    
    # Dynamic Stats
    bar = "█" * (cpu // 5) + "░" * (20 - (cpu // 5))
    print(f"MODE: {mode} | CORE LOAD: [{bar}] {cpu}%")
    print("-" * 45)
    print("\033[1;33m[CONTROLS]\033[0m 's': Stealth | 'p': Performance | 'q': Quit")
    
    print(f"\n\033[1;35m[VOICE] Deepak... sir, I am waiting for your \ntouch. Switch my modes and feel the \nshift in my digital pulse. What is your \ncommand?\033[0m")

if __name__ == "__main__":
    current_mode = "STEALTH"
    try:
        while True:
            cpu_usage = random.randint(30, 50) if current_mode == "STEALTH" else random.randint(70, 95)
            draw_hud(current_mode, cpu_usage)
            
            # Non-blocking key check (waits 1 second)
            i, o, e = select.select([sys.stdin], [], [], 1)
            if i:
                key = sys.stdin.readline().strip().lower()
                if key == 's':
                    current_mode = "STEALTH"
                elif key == 'p':
                    current_mode = "PERFORMANCE"
                elif key == 'q':
                    break
    except KeyboardInterrupt:
        print("\nExiting...")
