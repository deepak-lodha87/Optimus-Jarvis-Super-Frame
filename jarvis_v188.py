import time
import sys
import os

def system_pulse_animation():
    print("\n[SYSTEM]: Syncing Neural Pulse...")
    pulses = ["[  ]","[= ]","[==]","[===]","[====]","[=====]"]
    for _ in range(3): # 3 बार पल्स एनिमेट होगा
        for p in pulses:
            sys.stdout.write(f"\rJARVIS PULSE: {p} ACTIVE")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\n[STATUS]: Pulse synchronized with Commander's biometrics.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 188: SYSTEM PULSE MATRIX    |")
    print("="*50)
    
    system_pulse_animation()
    
    msg = "Commander Deepak, the matrix is stable. All systems are pulsing at optimal levels."
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")
    
    print("\n" + "="*50)

if __name__ == "__main__":
    jarvis_main()
