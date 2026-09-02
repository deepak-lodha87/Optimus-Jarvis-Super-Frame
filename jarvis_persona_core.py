import time
import os

class JarvisPersona:
    def __init__(self):
        self.creator = "Deepak"
        self.project_name = "Optimus Jarvis Super-Frame"
        self.version = "3.0.80"
        self.philosophy = "Strategy, Precision, and Loyalty"

    def boot_sequence(self):
        os.system('clear')
        print("\033[1;33m[IDENTITY] Running Core Persona Check...\033[0m")
        time.sleep(1.5)
        
        print(f"\033[1;32m[RECOGNIZED] Welcome back, Mr. {self.creator}.\033[0m")
        print(f"Current System: {self.project_name}")
        print(f"Philosophy   : {self.philosophy}")
        print("-" * 50)
        time.sleep(1)
        
        return "Jarvis is now fully integrated with your vision. Ready for next orders."

if __name__ == "__main__":
    jarvis = JarvisPersona()
    status = jarvis.boot_sequence()
    print(status)
    print("\n\033[1;34m[SYSTEM MESSAGE] Today's session was successful. All phases synced.\033[0m")
