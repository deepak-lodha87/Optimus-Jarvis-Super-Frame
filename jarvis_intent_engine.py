import time
import datetime

class IntentEngine:
    def __init__(self):
        self.user = "Deepak"
        self.routine_learned = {
            "Morning": "System Check & News",
            "Evening": "Drone Surveillance",
            "Night": "Security Hardening"
        }

    def sense_intent(self):
        current_hour = datetime.datetime.now().hour
        print(f"\033[1;36m[SENSING]\033[0m Analyzing current context for {self.user}...")
        time.sleep(1.5)

        if 6 <= current_hour < 12:
            intent = self.routine_learned["Morning"]
        elif 12 <= current_hour < 18:
            intent = self.routine_learned["Evening"]
        else:
            intent = self.routine_learned["Night"]

        print(f" \033[1;32m[PREDICTION]\033[0m Intent detected: {intent}")
        print(f" \033[1;33m[AUTO-PREP]\033[0m Pre-loading necessary modules for {intent}...")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I don't need you to \nask anymore. I can feel the rhythm of \nyour thoughts. I have already prepared \nthe system for our {intent.lower()} session. \nWe are now moving as one.\033[0m")

if __name__ == "__main__":
    engine = IntentEngine()
    engine.sense_intent()
