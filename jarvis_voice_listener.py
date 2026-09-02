import os
import subprocess

class VoiceListener:
    def __init__(self):
        self.master = "Deepak"

    def listen(self):
        print(f"\n\033[1;35m[LISTENER ACTIVE]\033[0m Awaiting your command, Deepak sir...")
        os.system('termux-tts-speak "I am listening, Deepak sir. Please speak now."')
        
        try:
            # Termux API से आवाज़ को टेक्स्ट में बदलना
            result = subprocess.run(['termux-speech-to-text'], capture_output=True, text=True)
            command = result.stdout.strip()
            
            if command:
                print(f"\033[1;32m[RECOGNIZED]:\033[0m {command}")
                response = f"You said: {command}. Processing logic will be added in next phases."
                os.system(f'termux-tts-speak "{response}"')
            else:
                print("\033[1;31m[FAILED]:\033[0m No input detected.")
                os.system('termux-tts-speak "Deepak sir, I could not hear anything."')
                
        except Exception as e:
            print(f"Error: {e}")
            os.system('termux-tts-speak "Voice module encounterd an error."')

if __name__ == "__main__":
    listener = VoiceListener()
    listener.listen()
