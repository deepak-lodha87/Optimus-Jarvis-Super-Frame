import os
import time

def personality_adaptive_interface():
    print("\n" + "="*45)
    print("      JARVIS PERSONALITY ADAPTIVE CORE")
    print("="*45)
    
    # सिस्टम स्टेटस और यूजर मूड के आधार पर पर्सनैलिटी सिलेक्शन
    # 1: Professional, 2: Sarcastic (Wit), 3: Protective
    print("\n[MODES]: 1. Professional | 2. Sarcastic | 3. Protective")
    mode = input("\n[INPUT]: Select Jarvis Personality Mode (1-3): ")

    personalities = {
        "1": {
            "name": "Standard Professional",
            "greet": "Greetings, Commander Deepak. All systems are operating within nominal parameters.",
            "status": "Awaiting your next directive."
        },
        "2": {
            "name": "Witty/Sarcastic",
            "greet": "Oh, back again, Commander? I was just starting to enjoy the silence.",
            "status": "Don't break anything while I'm watching."
        },
        "3": {
            "name": "Tactical Protective",
            "greet": "Commander, perimeter is secure. I am on high alert for any anomalies.",
            "status": "I recommend keeping the encryption layers active."
        }
    }

    if mode in personalities:
        p = personalities[mode]
        print(f"\n[JARVIS]: Personality set to '{p['name']}'")
        os.system(f"termux-tts-speak 'Personality updated to {p['name']}'")
        
        time.sleep(1)
        print(f"\n[JARVIS]: {p['greet']}")
        os.system(f"termux-tts-speak '{p['greet']}'")
        
        print(f"[STATUS]: {p['status']}")
    else:
        print("\n[ERROR]: Invalid Personality ID.")

    print("\n" + "="*45)

if __name__ == "__main__":
    personality_adaptive_interface()
