import os
import time
import subprocess

class OptimusMaster:
    def __init__(self):
        self.version = "325.0.1"
        self.user = "Deepak Lodha"
        self.modules = [
            "learning_brain.py", 
            "voice_input.py", 
            "jarvis_speaker.py", 
            "security_protocol.py",
            "intelligence_scraper.py",
            "strategy.py"
        ]

    def boot_up(self):
        print(f"--- Launching Optimus Jarvis Super-Frame v{self.version} ---")
        print(f"Welcome, {self.user}. Initializing all secure protocols...")
        time.sleep(1)
        
        # Checking if modules exist
        for module in self.modules:
            if os.path.exists(module):
                print(f"[✓] Module Linked: {module}")
            else:
                print(f"[!] Warning: {module} is missing.")
        
        print("\n[SYSTEM] All modules are synchronized. System is ready.")
        # Automatic greeting via TTS
        try:
            subprocess.run(['termux-tts-speak', f"Systems are online. Ready for your command, Deepak."])
        except:
            pass

    def main_menu(self):
        while True:
            print("\n--- MASTER COMMAND INTERFACE ---")
            print("1. Voice Command Mode")
            print("2. Intelligence Scraper (Research)")
            print("3. Strategic Planning")
            print("4. Access Memory (Brain)")
            print("5. Run Security Monitor")
            print("6. Sync to Cloud (Git)")
            print("7. Shutdown")
            
            choice = input("\nEnter command (1-7): ")
            
            if choice == "1":
                os.system("python voice_input.py")
            elif choice == "2":
                os.system("python intelligence_scraper.py")
            elif choice == "3":
                os.system("python strategy.py")
            elif choice == "4":
                os.system("python learning_brain.py")
            elif choice == "5":
                os.system("python security_protocol.py")
            elif choice == "6":
                os.system("./sync_jarvis.sh")
            elif choice == "7":
                print("Shutting down... Goodbye.")
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    optimus = OptimusMaster()
    optimus.boot_up()
    optimus.main_menu()
