import os, time, secrets

class JarvisVoice:
    def __init__(self):
        self.voice_id = f"VOX-{secrets.token_hex(2).upper()}"

    def speak(self, text, speed=1.0):
        print(f"\n\033[1;35m[VOICE OUTPUT] ID: {self.voice_id}\033[0m")
        print(f"\033[1;37m' {text} '\033[0m")
        
        # Simulating the command to trigger mobile OS text-to-speech
        # Actual command: termux-tts-speak "text"
        os.system(f"termux-tts-speak '{text}'") 
        time.sleep(1)

    def intro_sequence(self):
        print("\033[1;32m[SYSTEM] Initializing Vocal Cords...\033[0m")
        time.sleep(0.5)
        self.speak("Hello Deepak. Optimus Jarvis Super-Frame is now fully vocal and ready for your command.")

if __name__ == "__main__":
    vox = JarvisVoice()
    vox.intro_sequence()
