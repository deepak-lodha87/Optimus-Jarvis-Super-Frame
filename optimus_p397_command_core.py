import os
import time
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def command_core_init():
    os.system('clear')
    print("\033[1;31m" + "⚔️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : COMMAND CORE (P397)")
    print("⚔️"*30 + "\033[0m")
    
    optimus_speak("Establishing Neural Command Core. Prioritizing administrator directives.")
    
    # Priority Logic Simulation
    priority_levels = {
        "CRITICAL": "Emergency Protocols",
        "HIGH": "Strategic Tactical Analysis",
        "MEDIUM": "User Interface Updates",
        "LOW": "Background Telemetry"
    }
    
    for level, task in priority_levels.items():
        print(f"Setting Priority [{level:.<10}] for {task:.<25} [ \033[1;32mSET\033[0m ]")
        time.sleep(0.5)
    
    print("-" * 55)
    optimus_speak("Command core is operational. All directives are now prioritized.")
    print("\033[1;31m[CORE]: PRIORITY LOGIC ACTIVE\033[0m")

if __name__ == "__main__":
    command_core_init()
