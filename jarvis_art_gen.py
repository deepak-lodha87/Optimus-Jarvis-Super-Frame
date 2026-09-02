import os
import time

def draw_blueprint():
    frames = [
        "      .---.      ",
        "     /     \     ",
        "    |  (O)  |    ",
        "     \     /     ",
        "      '---'      "
    ]
    
    colors = ["\033[1;36m", "\033[1;32m", "\033[1;35m", "\033[1;34m"]
    
    print("\n\033[1;33m[GENERATING ADVANCED VISUAL]\033[0m Rendering Starhawk Core...")
    time.sleep(1.5)
    
    for _ in range(5): # एनीमेशन लूप
        for i, frame in enumerate(frames):
            os.system('clear')
            print(f"\n\n\n{colors[i%4]}")
            print("        OPTIMUS JARVIS SUPER-FRAME")
            print("        ==========================")
            print(f"             {frame}")
            print(f"             {frame[::-1]}") # रिफ्लेक्शन
            print("\033[0m\n        CORE STABILITY: 100%")
            time.sleep(0.2)

    msg = "Deepak sir, the unique neural blueprint has been rendered in Termux. This is the visual soul of your machine."
    os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    draw_blueprint()
