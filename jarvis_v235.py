import os
import time

def command_intent_parser():
    print("\n" + "="*40)
    print("      JARVIS ADVANCED INTENT PARSER")
    print("="*40)
    
    msg_init = "Commander Deepak, standing by for complex command analysis."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    raw_input = input("\n[VOICE/TEXT INPUT]: ").lower()
    
    # कीवर्ड आधारित इंटेंट एनालिसिस
    intents = {
        "security": ["lockdown", "secure", "firewall", "block"],
        "academic": ["study", "quiz", "exam", "notes"],
        "system": ["status", "storage", "vitality", "health"],
        "personal": ["budget", "expense", "motivation", "mood"]
    }
    
    found_intent = "General Inquiry"
    for intent, keywords in intents.items():
        if any(word in raw_input for word in keywords):
            found_intent = intent
            break
            
    processing_msg = f"Intent identified as: {found_intent.upper()}. Routing to relevant core..."
    print(f"\n[ANALYSIS]: {processing_msg}")
    os.system(f"termux-tts-speak '{processing_msg}'")
    
    time.sleep(1)
    
    success = f"Command parsed successfully. Executing {found_intent} protocols."
    print(f"[STATUS]: {success}")
    os.system(f"termux-tts-speak '{success}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    command_intent_parser()
