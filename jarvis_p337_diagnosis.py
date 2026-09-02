import time
import subprocess
import os

def jarvis_speak(text):
    print(f"\033[1;34m[JARVIS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

# Diagnosis Knowledge Base
knowledge_base = {
    "not starting": {
        "check": ["Battery voltage", "Spark plug condition", "Fuel level"],
        "solution": "Ensure the kill switch is ON and battery has at least 12V."
    },
    "overheating": {
        "check": ["Engine oil level", "Cooling fins", "Air intake"],
        "solution": "Clean the cooling fins and check for oil leaks."
    },
    "drone drift": {
        "check": ["IMU Calibration", "Propeller balance", "GPS lock"],
        "solution": "Recalibrate the accelerometer in Mission Planner."
    }
}

def self_diagnosis():
    os.system('clear')
    print("\033[1;35m" + "="*50)
    print("      OPTIMUS JARVIS : SELF-DIAGNOSIS CORE")
    print("="*50 + "\033[0m")
    
    jarvis_speak("I am ready for system diagnosis. What is the issue?")
    issue = input("\033[1;33m[INPUT]: Describe the problem: \033[0m").lower()

    found = False
    for key in knowledge_base:
        if key in issue:
            data = knowledge_base[key]
            jarvis_speak(f"Analyzing {key} issue. Please follow these steps.")
            print(f"\n\033[1;32m[DIAGNOSIS REPORT]\033[0m")
            print("-" * 30)
            for step in data["check"]:
                print(f"[ ] SCANNING: {step}...")
                time.sleep(1)
            print("-" * 30)
            print(f"\033[1;36m[SUGGESTION]:\033[0m {data['solution']}")
            jarvis_speak(data["solution"])
            found = True
            break
    
    if not found:
        jarvis_speak("I couldn't find a direct match. Scanning global repair manuals.")
        print("\033[1;31m[RETRY]: Try keywords like 'starting' or 'overheating'.\033[0m")

if __name__ == "__main__":
    self_diagnosis()
