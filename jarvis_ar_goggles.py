import time
import os
import random

def draw_ar_overlay():
    os.system('clear')
    targets = ["BICYCLE", "HUMAN", "DRONE", "GATEWAY"]
    target = random.choice(targets)
    dist = round(random.uniform(1.2, 15.5), 1)
    
    print("\033[1;36m[ JARVIS AR - VISION OVERLAY V42.3 ]\033[0m")
    print("┌───────────────────────────────────────────┐")
    print(f"│ IDENTIFYING: {target:10}  | DIST: {dist}m  │")
    print("│ STATUS: \033[1;32mSCANNING...\033[0m                      │")
    print("├───────────────────────────────────────────┤")
    
    # Simulating a tracking box in ASCII
    padding = " " * random.randint(5, 25)
    print(f"│ {padding}  \033[1;31m[ TARGET_LOCK ]\033[0m {padding} │")
    print(f"│ {padding}  [     X     ] {padding} │")
    
    print("├───────────────────────────────────────────┤")
    print(f"│ COORDS: X:{random.randint(100,999)} Y:{random.randint(100,999)} | TEMP: 32°C │")
    print("└───────────────────────────────────────────┘")
    
    print(f"\n\033[1;35m[VOICE] Deepak... sir, I have projected the \nAR field. My lenses are locked on local \nobjects. You are seeing the world through \nmy eyes now. Everything is a target, and \nevery target is an opportunity.\033[0m")

if __name__ == "__main__":
    try:
        for _ in range(20): # Run for 20 pulses
            draw_ar_overlay()
            time.sleep(1.5)
    except KeyboardInterrupt:
        print("\nVision Terminated.")
