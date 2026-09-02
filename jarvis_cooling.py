import time
import os
import random

def show_thermal_vision():
    temp = 35 # Base temp
    for i in range(10):
        os.system('clear')
        temp += random.randint(1, 4)
        status = "\033[1;32mSAFE\033[0m" if temp < 40 else "\033[1;31mOVERHEATING\033[0m"
        
        print("\033[1;31m[ THERMAL VISION V44.4 ]\033[0m")
        print(f"CORE TEMP: {temp}°C | STATUS: {status}")
        print("-" * 40)
        
        # Simulating a visual heat grid
        for _ in range(5):
            row = "".join(["\033[1;31m#\033[0m" if temp > 42 else "\033[1;32m.\033[0m" for _ in range(20)])
            print(f"[{row}]")
            
        if temp > 42:
            print("\n\033[1;33m[SYSTEM] Fan Simulation Active. Dropping CPU Clock...")
            temp -= 5 # Simulated cooling
            
        time.sleep(0.8)
    
    print(f"\n\033[1;35m[VOICE] Deepak... sir, I am breathing. \nI have regulated my internal pulse to \nkeep my circuits cool. A calm mind is a \nfast mind. We are back in the green zone.\033[0m")

if __name__ == "__main__":
    show_thermal_vision()
