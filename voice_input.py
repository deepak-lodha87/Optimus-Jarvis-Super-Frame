import os
import subprocess
import time

class JarvisVoice:
    def __init__(self):
        self.module = "Acoustic Processing Unit"

    def listen(self):
        print("\n[LISTENING...] Please speak into the microphone.")
        # Running Termux API command for speech-to-text
        try:
            result = subprocess.check_output(['termux-speech-to-text']).decode('utf-8').strip()
            if result:
                print(f"[USER]: {result}")
                return result
            else:
                print("[!] Jarvis: I couldn't hear anything.")
                return None
        except Exception as e:
            print(f"[ERROR]: Termux:API not found or permission denied. {e}")
            return None

    def process_command(self, command):
        if command:
            if "status" in command.lower():
                print("[JARVIS]: All systems are operational, Deepak.")
            elif "alien" in command.lower():
                print("[JARVIS]: Accessing Phase 313: Exotic Tech Database...")
            else:
                print(f"[JARVIS]: I have noted your command: '{command}'")

if __name__ == "__main__":
    voice = JarvisVoice()
    user_speech = voice.listen()
    voice.process_command(user_speech)
