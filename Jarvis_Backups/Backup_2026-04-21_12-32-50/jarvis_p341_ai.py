import os
import subprocess

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def ai_interaction():
    os.system('clear')
    print("\033[1;36m" + "="*50)
    print("      OPTIMUS JARVIS : AI INTELLIGENCE CORE")
    print("="*50 + "\033[0m")
    
    jarvis_speak("AI Core is active. I can now reason and assist with complex tasks.")
    
    while True:
        user_input = input("\033[1;33m[DEEPAK]: \033[0m").lower()
        
        if "exit" in user_input or "stop" in user_input:
            jarvis_speak("Closing AI session.")
            break
            
        # Simulation of AI Reasoning
        jarvis_speak("Processing your request through my neural network.")
        print(f"\033[1;32m[JARVIS]:\033[0m I am analyzing your request regarding '{user_input}'.")
        # Yahan hum future mein real API connect karenge

if __name__ == "__main__":
    ai_interaction()
