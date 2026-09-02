import subprocess
import time

class JarvisSpeaker:
    def __init__(self):
        self.voice_profile = "Synthetic-Neural-01"

    def speak(self, text):
        print(f"\n[JARVIS]: {text}")
        # Termux API command to speak the text
        try:
            subprocess.run(['termux-tts-speak', text])
        except Exception as e:
            print(f"[ERROR]: Could not access TTS engine. {e}")

    def boot_sequence(self):
        self.speak("Systems are online, Deepak. Optimus Jarvis Super-Frame is at your service.")
        time.sleep(1)
        self.speak("All modules, including Alien Engineering and Strategic Planning, are ready for execution.")

if __name__ == "__main__":
    jarvis_voice = JarvisSpeaker()
    jarvis_voice.boot_sequence()
    
    # Custom interaction
    msg = input("\nType a message for Jarvis to say: ")
    jarvis_voice.speak(msg)
