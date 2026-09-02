import os
import time

class RealJarvis:
    def __init__(self):
        self.name = "Optimus Jarvis"

    def speak(self, text):
        # Jarvis will now speak through your phone's speaker
        os.system(f'termux-tts-speak "{text}"')

    def hardware_feedback(self):
        print("\033[1;36m[SYSTEM]\033[0m Activating Physical Feedback...")
        # Phone will vibrate to let you know it's working
        os.system('termux-vibrate -d 500')
        time.sleep(0.5)
        # Flashlight test
        print("\033[1;33m[TEST]\033[0m Testing Optical Output (Torch)...")
        os.system('termux-torch on')
        time.sleep(2)
        os.system('termux-torch off')

    def check_battery(self):
        # Real battery status instead of simulated logic
        import json
        battery_data = os.popen('termux-battery-status').read()
        data = json.loads(battery_data)
        percentage = data['percentage']
        status = data['status']
        
        response = f"Deepak sir, battery is at {percentage} percent and it is currently {status}."
        print(f"\033[1;32m[BATTERY]\033[0m {response}")
        self.speak(response)

if __name__ == "__main__":
    jarvis = RealJarvis()
    jarvis.speak("System online. Good evening, Deepak sir.")
    jarvis.hardware_feedback()
    jarvis.check_battery()
