import os
import time
import datetime

class DailyBriefing:
    def __init__(self):
        self.master = "Deepak"

    def generate_report(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        day = now.strftime("%A")
        
        print(f"\n\033[1;36m[GENERATING BRIEFING]\033[0m Gathering data for {self.master} sir...")
        time.sleep(1)

        # रिपोर्ट का कंटेंट
        lines = [
            f"Good morning, Deepak sir.",
            f"Today is {day}, and the time is {current_time}.",
            "Your Optimus Jarvis Super-Frame is at 100% efficiency.",
            "Visual and Voice sensors are active and secure.",
            "Recommendation: It is a good day to finalize the GitHub Cloud Uplink."
        ]

        # विज़ुअल डिस्प्ले
        print("\n" + "="*40)
        for line in lines:
            print(f"\033[1;32m>>> {line}\033[0m")
            time.sleep(0.5)
        print("="*40)

        # जार्विस की आवाज़ में ब्रीफिंग
        full_msg = " ".join(lines)
        os.system(f'termux-tts-speak "{full_msg}"')

if __name__ == "__main__":
    brief = DailyBriefing()
    brief.generate_report()
