import time
import os

class ChronosProtocol:
    def __init__(self):
        self.master = "Deepak"
        # आपके कार्यों की लिस्ट (समय और कार्य)
        self.schedule = {
            "19:00": "Deepak sir, it is time to review the Jarvis Core Phase updates.",
            "21:00": "Sir, time for your dinner and a quick break.",
            "22:30": "System reminder: Time to sync the day's progress."
        }

    def monitor_tasks(self):
        print(f"\n\033[1;34m[CHRONOS PROTOCOL ACTIVE]\033[0m Monitoring your schedule...")
        
        while True:
            current_time = time.strftime("%H:%M")
            if current_time in self.schedule:
                task = self.schedule[current_time]
                print(f"\033[1;32m[TASK ALERT]:\033[0m {task}")
                os.system(f'termux-tts-speak "{task}"')
                # एक मिनट रुकना ताकि बार-बार अलर्ट न आए
                time.sleep(61)
            
            # हर 30 सेकंड में चेक करना
            time.sleep(30)

if __name__ == "__main__":
    chronos = ChronosProtocol()
    # इसे आप बैकग्राउंड में चला सकते हैं
    chronos.monitor_tasks()
