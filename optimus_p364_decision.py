import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def logic_override_engine():
    os.system('clear')
    print("\033[1;34m" + "⚖️"*30)
    print("      OPTIMUS NEURAL SYSTEMS : DECISION ENGINE (P364)")
    print("⚖️"*30 + "\033[0m")
    
    optimus_speak("Neural decision engine online. Evaluating environmental safety constraints.")
    
    # Input Command
    command = input("\n\033[1;33m[INPUT]: Enter Mission Command (e.g., Launch Drone): \033[0m").lower()
    
    # Environmental Sensors (Simulated)
    weather_condition = "Rainy"  # Simulated from Phase 342
    battery_level = 15           # Simulated from Phase 349
    
    print(f"\n\033[1;36m[ANALYZING]: Validating Logistics for: '{command.upper()}'\033[0m")
    time.sleep(1.5)
    
    # Logic Decision Tree
    if "drone" in command or "launch" in command:
        if weather_condition == "Rainy":
            print("\033[1;31m[DENIED]: Adverse weather detected. Precipitation risk: HIGH.\033[0m")
            optimus_speak("Negative. Mission aborted due to heavy rain. Protecting hardware integrity.")
        elif battery_level < 20:
            print("\033[1;31m[DENIED]: Critical battery levels. Energy reserve: LOW.\033[0m")
            optimus_speak("Insufficient power for safe flight. Charge mobile device.")
        else:
            print("\033[1;32m[APPROVED]: All safety parameters met. Proceeding to launch.\033[0m")
            optimus_speak("Clear for takeoff. Initializing flight telemetry.")
    else:
        print("\033[1;32m[EXECUTING]: Standard protocol initiated.\033[0m")
        optimus_speak("Command accepted and processing.")

if __name__ == "__main__":
    logic_override_engine()
