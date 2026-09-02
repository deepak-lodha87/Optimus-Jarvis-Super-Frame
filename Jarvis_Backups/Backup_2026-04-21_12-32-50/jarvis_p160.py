import os
import time

def visual_avatar_init():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 160: AI AVATAR INTERFACE      |")
    print("="*50)

    print("\n[SYSTEM]: Loading Visual Core Assets...")
    time.sleep(1.2)
    
    # Simulating the UI pulses
    frames = ["(  o  )", "( <o> )", "(==o==)", "( <o> )", "(  o  )"]
    
    print("[LOG]: Calibrating Avatar Eye/Core...")
    for _ in range(2):
        for frame in frames:
            print(f"\r[AVATAR]: {frame} Status: Synchronizing...", end="")
            time.sleep(0.3)
    
    print("\n\n[STATUS]: Interface Online.")
    
    msg = "Commander, I have established a visual presence. You can now see my core status in real-time."
    
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    print("\n" + "-"*20 + " UI ACTIVE " + "-"*20)
    print("      [  OPTIMUS JARVIS SUPER-FRAME  ]      ")
    print("="*50)

if __name__ == "__main__":
    visual_avatar_init()
