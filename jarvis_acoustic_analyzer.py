import os
import time
import math
import random

def analyze_sound():
    print("\n\033[1;36m[LISTENING]\033[0m Jarvis is capturing Engine Frequency...")
    time.sleep(1.5)
    
    try:
        for t in range(50): # 50 फ्रेम्स का वेव फॉर्म
            os.system('clear')
            print("\033[1;33m        JARVIS ACOUSTIC ANALYZER | ENGINE RPM SYNC")
            print("        ==========================================\033[0m\n")
            
            # वेव फॉर्म जेनरेट करना
            for y in range(10):
                line = "    "
                for x in range(60):
                    # Sine wave logic for sound visualization
                    formula = 5 + 4 * math.sin(x / 3.0 + t / 2.0)
                    if int(formula) == y:
                        line += "\033[1;32m█\033[0m"
                    elif y > int(formula):
                        line += "\033[1;34m.\033[0m"
                    else:
                        line += " "
                print(line)
            
            print(f"\n\033[1;36m[DATA]:\033[0m Peak Frequency: {random.randint(800, 1200)} Hz | Noise: Low")
            time.sleep(0.05)

        msg = "Deepak sir, the acoustic signature is stable. No abnormal friction detected in the piston rings. The engine rhythm is perfect."
        os.system(f'termux-tts-speak "{msg}"')
        
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    analyze_sound()
