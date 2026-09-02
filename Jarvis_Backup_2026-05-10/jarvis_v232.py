import os
import time

def adaptive_personality_engine():
    print("\n" + "="*40)
    print("      JARVIS ADAPTIVE PERSONALITY CORE")
    print("="*40)
    
    msg_init = "Commander Deepak, system personality core is active. How are you feeling today?"
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    print("\n[MODES]: 1. Focused | 2. Tired | 3. Excited | 4. Critical")
    mood = input("\n[INPUT]: Current State (1-4): ")
    
    responses = {
        "1": {
            "text": "Excellent. Efficiency is our top priority. Standing by for complex tasks.",
            "voice": "Excellent. Efficiency is our top priority."
        },
        "2": {
            "text": "I suggest a 15-minute recharge, Commander. I will monitor the perimeter while you rest.",
            "voice": "I suggest a 15 minute recharge, Commander."
        },
        "3": {
            "text": "Energy levels are optimal! Let's push the boundaries of the Super-Frame today.",
            "voice": "Energy levels are optimal! Let's push the boundaries today."
        },
        "4": {
            "text": "Protocol red active. All non-essential systems are on standby. Specify target.",
            "voice": "Protocol red active. Specify target."
        }
    }
    
    if mood in responses:
        selected = responses[mood]
        print(f"\n[JARVIS]: {selected['text']}")
        os.system(f"termux-tts-speak '{selected['voice']}'")
    else:
        print("[ERROR]: Mood signature not recognized.")

    print("\n" + "="*40)

if __name__ == "__main__":
    adaptive_personality_engine()
