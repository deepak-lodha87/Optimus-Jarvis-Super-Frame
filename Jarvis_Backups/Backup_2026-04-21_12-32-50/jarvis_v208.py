import os
import time

def fitness_tracker():
    print("\n" + "="*40)
    print("      JARVIS FITNESS TRACKER CORE")
    print("="*40)
    
    msg_ask = "Commander Deepak, please enter the total steps you walked today."
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    try:
        steps = int(input("\n[INPUT]: Steps walked: "))
        
        if steps >= 10000:
            feedback = f"Outstanding performance! {steps} steps is a target achieved."
        elif steps >= 5000:
            feedback = f"Good job! You have reached {steps} steps. Keep moving."
        else:
            feedback = f"Only {steps} steps today? We should increase the activity, Commander."
            
        print(f"\n[JARVIS]: {feedback}")
        os.system(f"termux-tts-speak '{feedback}'")
        
        # डेटा को एक फाइल में सेव करना
        with open("fitness_log.txt", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d')}: {steps} steps\n")
            
    except ValueError:
        error = "Commander, please provide a valid number for steps."
        print(f"\n[ERROR]: {error}")
        os.system(f"termux-tts-speak '{error}'")

    print("="*40)

if __name__ == "__main__":
    fitness_tracker()
