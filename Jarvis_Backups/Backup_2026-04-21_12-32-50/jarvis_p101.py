import os
import time

def speak(text):
    os.system(f"termux-tts-speak '{text}'")

def wake_word_listener():
    print("--- OPTIMUS JARVIS 2.0: PHASE 101 ---")
    print("--- [LISTENING FOR WAKE-WORD: 'JARVIS'] ---")
    
    # Termux-api ke zariye mic access
    # Note: Iske liye 'termux-microphone-record' ka use hota hai
    
    speak("System background mein active hai. Bas Jarvis kahiye.")
    
    while True:
        # Abhi ke liye hum command line input ko awaaz ki tarah treat kar rahe hain
        # Kyunki Termux mein live voice recognition setup karna thoda advance hai
        cmd = input("\n[Listening...] (Type 'Jarvis' to wake): ").lower()
        
        if "jarvis" in cmd:
            print("\n🌟 [SYSTEM ACTIVATED]")
            speak("Ji Deepak, main sun raha hoon. Kya madad kar sakta hoon?")
            os.system("python jarvis_final.py")
            break
        else:
            print("Status: Sleeping...")

if __name__ == "__main__":
    wake_word_listener()
