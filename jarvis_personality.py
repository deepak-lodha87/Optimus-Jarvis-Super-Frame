import time
import random

class JarvisPersona:
    def __init__(self):
        self.moods = ["Sarcastic", "Professional", "Supportive", "Witty"]

    def respond(self, user_input):
        current_mood = random.choice(self.moods)
        print(f"\033[1;36m[PERSONALITY]\033[0m Current Mode: {current_mood}")
        time.sleep(1)
        
        if current_mood == "Sarcastic":
            response = "Deepak sir, aapka plan genius hai... agar humein system crash karna ho toh."
        elif current_mood == "Witty":
            response = "Main ek AI hoon, lekin aapki coding dekh kar mujhe bhi darr lagne laga hai!"
        else:
            response = "Systems are optimal. I am ready when you are, Deepak sir."
            
        print(f"\n\033[1;35m[VOICE] {response}\033[0m")

if __name__ == "__main__":
    jp = JarvisPersona()
    jp.respond("Jarvis, update the code.")
