import os
import datetime

class JarvisIdentity:
    def __init__(self):
        self.name = "Optimus Jarvis Super-Frame"
        self.master = "Deepak"
        self.version = "1.5.0"

    def boot_sequence(self):
        hour = int(datetime.datetime.now().hour)
        greeting = ""
        
        if 0 <= hour < 12:
            greeting = "Good Morning"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        print(f"\n\033[1;32m[SYSTEM BOOT SUCCESS]\033[0m")
        print(f"\033[1;36mNAME    :\033[0m {self.name}")
        print(f"\033[1;36mVERSION :\033[0m {self.version}")
        print(f"\033[1;36mMASTER  :\033[0m {self.master}")
        
        msg = f"{greeting} Deepak sir. {self.name} version {self.version} is now online and at your service."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    jarvis = JarvisIdentity()
    jarvis.boot_sequence()
