import os
import time
import random

def thermal_scan():
    # थर्मल कलर्स (Blue = Cold, Red = Hot)
    colors = ["\033[1;34m", "\033[1;36m", "\033[1;33m", "\033[1;31m"]
    chars = ["░", "▒", "▓", "█"]
    
    print("\n\033[1;35m[INITIATING THERMAL SCAN]\033[0m Scanning for Heat Signatures...")
    time.sleep(1.5)

    try:
        for _ in range(30): # 30 फ्रेम का स्कैन
            os.system('clear')
            print("\033[1;37m        JARVIS THERMAL VISION | ENGINE DIAGNOSTIC")
            print("        =========================================\033[0m\n")
            
            for y in range(15):
                line = "                "
                for x in range(30):
                    # रैंडम हीट सिग्नेचर सिमुलेशन
                    intensity = random.randint(0, 3)
                    line += f"{colors[intensity]}{chars[intensity]}"
                print(line)
            
            print("\n\033[1;32m[SCAN STATUS]:\033[0m Detecting Component Temperatures...")
            time.sleep(0.1)

        msg = "Deepak sir, thermal scan complete. I have detected a minor heat leak in the secondary coolant line. No manual intervention needed, I am adjusting the flow."
        os.system(f'termux-tts-speak "{msg}"')
        
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    thermal_scan()
