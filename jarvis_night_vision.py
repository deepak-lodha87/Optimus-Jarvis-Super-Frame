import os
import time
import random

def activate_night_vision():
    # नाइट विजन के लिए ग्रीन शेड्स
    green_shades = ["\033[1;32m", "\033[0;32m", "\033[1;30m"]
    chars = ["▓", "▒", "░", " "]
    
    print("\n\033[1;32m[INITIATING NIGHT VISION]\033[0m Adjusting ISO Gain...")
    time.sleep(1.5)

    try:
        for _ in range(40): # एनीमेशन लूप
            os.system('clear')
            print("\033[1;32m        JARVIS NVG MODE | LOW-LIGHT OPTIMIZATION")
            print("        ========================================\033[0m\n")
            
            for y in range(12):
                line = "                "
                for x in range(35):
                    # नाइट विजन "Noise" और ऑब्जेक्ट डिटेक्शन सिमुलेशन
                    pixel = random.choice(chars)
                    color = random.choice(green_shades)
                    line += f"{color}{pixel}"
                print(line)
            
            print(f"\n\033[1;32m[STATUS]:\033[0m Amplification: +{random.randint(15, 30)}dB | Tracking Active")
            time.sleep(0.08)

        msg = "Deepak sir, Night Vision is calibrated. I can now see structural defects even in zero-light conditions. Shadows will no longer hide the truth."
        os.system(f'termux-tts-speak "{msg}"')
        
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    activate_night_vision()
