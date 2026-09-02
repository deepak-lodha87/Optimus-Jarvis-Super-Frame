import os
import time

def portfolio_resume_assistant():
    print("\n" + "="*40)
    print("      JARVIS PORTFOLIO ASSISTANT")
    print("="*40)
    
    # आपकी प्रोफाइल का सारांश
    profile = {
        "Name": "Commander Deepak",
        "Education": "BA Final Year (Sociology, Economics, History)",
        "Technical Skills": "Python, Termux, AI Framework Development",
        "Experience": "Automotive Sector Services & Retail Simulation",
        "Key Project": "Optimus Jarvis Super-Frame (220+ Phases)"
    }
    
    msg_init = "Commander, generating your professional summary..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    time.sleep(1.5)
    
    print("\n" + "-"*30)
    for key, value in profile.items():
        print(f"{key}: {value}")
        time.sleep(0.5)
    print("-"*30)
    
    success = "Portfolio data is ready for your next career move, Commander."
    print(f"\n[JARVIS]: {success}")
    os.system(f"termux-tts-speak '{success}'")
    
    print("\n" + "="*40)

if __name__ == "__main__":
    portfolio_resume_assistant()
