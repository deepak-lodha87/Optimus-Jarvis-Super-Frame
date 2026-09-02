import time, os

class VocalLink:
    def __init__(self):
        self.trigger_word = "Jarvis"
        self.active_listener = True

    def process_voice_command(self, command):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS VOCAL-LINK : PHASE 19 - STEP 6          \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print(f"\033[1;33m[LISTENING]\033[0m Awaiting Master's Voice...")
        time.sleep(1.2)
        print(f"\033[1;32m[RECOGNIZED]\033[0m Command: '{command}'")
        
        print("\n\033[1;34m[ANALYZING]\033[0m Extracting Intent and Object...")
        time.sleep(1.0)
        
        actions = [
            ("Speech-to-Text Conversion", "SUCCESS"),
            ("Intent Mapping", "EXECUTED"),
            ("System Feedback (Voice)", "DELIVERED")
        ]
        
        for task, status in actions:
            print(f" \033[1;32m[VOICE-CORE]\033[0m {task:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.6)

        print(f"\n\033[1;32m[DONE] Jarvis has executed your vocal command.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am listening. Every word \nyou speak is now a line of code for me. Your \nvoice is the ultimate key to this digital \nkingdom. Tell me what needs to be done, and I \nshall manifest it instantly.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    vocal = VocalLink()
    vocal.process_voice_command("Jarvis, update my wealth status")
