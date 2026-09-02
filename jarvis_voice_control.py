import os
import time
import json

class VoiceJarvis:
    def __init__(self):
        self.user = "Deepak sir"

    def speak(self, message):
        print(f"\033[1;35m[JARVIS]\033[0m {message}")
        os.system(f'termux-tts-speak "{message}"')

    def listen(self):
        print("\033[1;36m[LISTENING]\033[0m Speak now...")
        # Recording voice for 3 seconds and converting to text
        try:
            voice_data = os.popen('termux-speech-to-text').read()
            return voice_data.strip().lower()
        except Exception:
            return ""

    def process_command(self, cmd):
        if "hello" in cmd or "hi" in cmd:
            self.speak(f"Hello {self.user}, I am online and ready.")
        elif "battery" in cmd:
            battery = json.loads(os.popen('termux-battery-status').read())
            self.speak(f"Sir, battery is at {battery['percentage']} percent.")
        elif "torch on" in cmd:
            os.system('termux-torch on')
            self.speak("Flashlight activated.")
        elif "torch off" in cmd:
            os.system('termux-torch off')
            self.speak("Flashlight deactivated.")
        else:
            self.speak("I heard you, but I need more training for this command.")

if __name__ == "__main__":
    jarvis = VoiceJarvis()
    jarvis.speak("Initializing Voice Interface Phase 1,000,004.")
    
    # Simple loop for real testing
    user_thought = jarvis.listen()
    if user_thought:
        print(f"You said: {user_thought}")
        jarvis.process_command(user_thought)
