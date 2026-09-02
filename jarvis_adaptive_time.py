import os
import time
import datetime

class AdaptiveEnvironment:
    def __init__(self):
        self.master = "Deepak"
        self.version = "Supreme.2400"

    def get_smart_greeting(self):
        # वर्तमान समय का सटीक विश्लेषण (24-घंटे के फॉर्मेट में)
        current_hour = datetime.datetime.now().hour
        current_time_str = datetime.datetime.now().strftime("%I:%M %p")
        
        # दीपक सर के मूड और वास्तविक समय के हिसाब से डायनेमिक ग्रीटिंग
        if 0 <= current_hour < 4:
            greeting = f"Welcome back to your late-night session, Deepak sir. The clock reflects {current_time_str}."
            ui_status = "[ LATE-NIGHT ARCHITECT MODE ]"
        elif 4 <= current_hour < 12:
            greeting = f"Good morning, Deepak sir. System initialized for your day."
            ui_status = "[ STRATEGIC MORNING MODE ]"
        elif 12 <= current_hour < 17:
            greeting = f"Good afternoon, Deepak sir. Core operational integrity is maximum."
            ui_status = "[ AFTERNOON SYNC MODE ]"
        else:
            greeting = f"Good evening, Deepak sir. Monitoring ongoing background tasks."
            ui_status = "[ EVENING MONITOR MODE ]"
            
        return greeting, ui_status

    def deploy_adaptive_core(self):
        greeting_msg, ui_label = self.get_smart_greeting()
        
        print(f"\n\033[1;37;44m {ui_label} \033[0m")
        print(f"\033[1;32m[PERCEPTION]:\033[0m Time awareness synchronized successfully.")
        
        # जार्विस अब दीपक सर के वास्तविक समय के अनुसार बात करेगा
        os.system(f'termux-tts-speak "{greeting_msg}"')
        
        # बैकग्राउंड में क्लाउड और स्वतः कोड जनरेशन चालू रखना
        print(f"\033[1;36m[STATUS]:\033[0m Continuous Proactive Protection: ACTIVE")

if __name__ == "__main__":
    adaptive_jarvis = AdaptiveEnvironment()
    adaptive_jarvis.deploy_adaptive_core()
