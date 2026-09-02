import os

class JarvisBrain:
    def __init__(self):
        self.master = "Deepak"

    def start_system(self):
        print("\n\033[1;32m[SYSTEM BOOT SUCCESS]\033[0m Optimus Jarvis is ready.")
        os.system('termux-tts-speak "Welcome back, Deepak sir. All modules integrated."')
        
        while True:
            cmd = input("\n\033[1;36mListening Deepak sir:\033[0m ").lower()
            
            if "news" in cmd:
                os.system("python jarvis_news_radar.py")
            elif "battery" in cmd:
                os.system("python jarvis_power_guardian.py")
            elif "clean" in cmd:
                os.system("python jarvis_file_architect.py")
            elif "lock" in cmd:
                os.system("python jarvis_security_lock.py")
            elif "exit" in cmd:
                os.system('termux-tts-speak "Shutting down systems. Goodbye, sir."')
                break
            else:
                print("\033[1;31m[ERROR]:\033[0m Command not recognized in Core.")

if __name__ == "__main__":
    brain = JarvisBrain()
    brain.start_system()
