import time
import os
import subprocess
import random

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def voice_pattern_recognition():
    os.system('clear')
    print("\033[1;34m" + "🎙️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : VOICE ID VERIFICATION (P381)")
    print("🎙️"*30 + "\033[0m")
    
    optimus_speak("Initiating neural voice recognition. Please speak the authorization phrase.")
    
    print("\n\033[1;33m[ACTION]: Say 'Optimus Alpha Secure' clearly.\033[0m")
    time.sleep(1) # Simulating waiting for microphone input
    
    print("\n\033[1;36m[CAPTURING]: Recording Audio Stream...\033[0m")
    time.sleep(2)
    
    # Simulated Frequency Matching Logic
    match_percentage = random.randint(85, 99)
    
    print("\033[1;33m[ANALYZING]: Matching Frequency Patterns...\033[0m")
    time.sleep(1.5)
    
    print(f"\n\033[1;37m- Sample Rate: 44.1 kHz")
    print(f"- Frequency Match: {match_percentage}%")
    print(f"- Pitch Variance: 0.04 Hz\033[0m")
    
    if match_percentage > 90:
        print(f"\n\033[1;32m[SUCCESS]: Voice Signature Confirmed. Welcome, Administrator.\033[0m")
        optimus_speak("Identity verified. All neural cores are now at your command.")
    else:
        print(f"\n\033[1;31m[FAILED]: Voice Mismatch. Security Perimeter Maintained.\033[0m")
        optimus_speak("Voice pattern does not match the authorized profile. Access denied.")

if __name__ == "__main__":
    voice_pattern_recognition()
