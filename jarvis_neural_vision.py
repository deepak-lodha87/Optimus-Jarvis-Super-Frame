import os
import time
import math

def render_vision():
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    scale = 0
    
    print("\033[1;36m[BOOTING NEURAL VISION...]\033[0m")
    time.sleep(1)

    try:
        for _ in range(50): # 50 फ्रेम्स का एनीमेशन
            os.system('clear')
            scale += 0.2
            output = ""
            
            for y in range(-10, 11):
                line = "        "
                for x in range(-20, 21):
                    # Space-Time Curve Logic
                    formula = math.sin(math.sqrt(x*x + y*y) - scale)
                    index = int((formula + 1) * 5)
                    line += chars[index]
                output += line + "\n"
            
            print("\033[1;32m       OPTIMUS JARVIS: ADVANCED BLUEPRINT")
            print("       ==================================\033[0m")
            print(output)
            print("\033[1;34m       [CORE STATUS]: DISTORTING SPACE-TIME\033[0m")
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        pass

    msg = "Deepak sir, the neural vision is active. This is how I see the world—not as objects, but as a flow of data and energy."
    os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    render_vision()
