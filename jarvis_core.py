import os
import sys
import platform

class OptimusJarvis:
    def __init__(self):
        self.name = "Optimus Jarvis Super-Frame"
        self.version = "1.0.0 (Mobile Core)"
        self.status = "Active"
    
    def start_system(self):
        print("="*50)
        print(f"[{self.name}] Initialized")
        print(f"Version: {self.version}")
        print(f"Environment: Termux Terminal Engine")
        print("="*50)
        print("Jarvis is online and ready for operational commands.")
        print("Type 'help' for commands or 'exit' to turn off.\n")

    def run_diagnostics(self):
        print("\n--- [SYSTEM DIAGNOSTICS] ---")
        print(f"OS Platform : {platform.system()}")
        print(f"Python Ver  : {sys.version.split()[0]}")
        print(f"Core Engine : Operational")
        print("----------------------------\n")

    def run_command_loop(self):
        while True:
            cmd = input("Jarvis > ").strip().lower()
            if cmd == 'exit':
                print("Shutting down Jarvis core... Goodbye!")
                break
            elif cmd in ['hello', 'hi']:
                print("Hello! Systems are fully operational.")
            elif cmd == 'status':
                print(f"System: {self.name}\nStatus: {self.status}\nVersion: {self.version}")
            elif cmd == 'diag':
                self.run_diagnostics()
            elif cmd == 'help':
                print("\nAvailable Commands:")
                print(" status - Check system version and state")
                print(" diag   - Run internal system diagnostics")
                print(" clear  - Clear terminal screen")
                print(" exit   - Shut down system\n")
            elif cmd == 'clear':
                os.system('clear')
            elif cmd != '':
                print(f"Command '{cmd}' received. Processing logic...")

if __name__ == "__main__":
    jarvis = OptimusJarvis()
    jarvis.start_system()
    jarvis.run_command_loop()
