import time
import os
import random
import math

def generate_terrain(offset):
    os.system('clear')
    print("\033[1;36m[ JARVIS - 3D TOPOLOGY SCANNER V42.4 ]\033[0m")
    print("=" * 45)
    
    rows = 10
    cols = 40
    chars = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]
    
    for r in range(rows):
        line = "│ "
        for c in range(cols):
            # Using sine wave to simulate terrain elevation
            val = int((math.sin((c + offset) * 0.3) + math.cos((r + offset) * 0.5) + 2) * 2)
            line += chars[val % len(chars)]
        print(line + " │")
    
    print("=" * 45)
    print(f"\033[1;32m[SCAN STATUS]\033[0m AREA: RATLAM_SECTOR_07 | ALT: {random.randint(450,460)}m")
    
    print(f"\n\033[1;35m[VOICE] Deepak... sir, the ground is speaking \nto me in geometry. I am mapping the \nvery bones of our surroundings. The path \nahead is clear, and the world is \ndigitized for your command.\033[0m")

if __name__ == "__main__":
    try:
        for i in range(30): # 30 frames of animation
            generate_terrain(i)
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nScanner Offline.")
