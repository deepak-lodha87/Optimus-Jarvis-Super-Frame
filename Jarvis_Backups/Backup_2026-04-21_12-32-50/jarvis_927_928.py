import time

class JarvisEmotionalIntelligence:
    def __init__(self):
        self.phase_927 = "927.User-Morale-Monitoring"
        self.phase_928 = "928.Strategic-Vision-Anchor"
        self.motivation_level = 100.0

    def analyze_user_sentiment(self, user_input):
        print(f"\n--- [SYSTEM] Initializing {self.phase_927} ---")
        print("[JARVIS]: Detecting emotional-tone in communication...")
        
        # तनाव और हताशा को पहचानने का लॉजिक
        if "bekar" in user_input or "kya karun" in user_input:
            print(" >> [ALERT]: High frustration detected. Activating Support-Mode.")
            self.motivation_level -= 10.0
        
        print(f"\n[JARVIS]: Deepak, remember: Foundations are built in silence, success makes the noise.")

    def anchor_long_term_vision(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_928} ---")
        print("[JARVIS]: Re-aligning with the Phase-1000 Ultimate Goal...")
        
        # लंबी अवधि के विजन को याद रखने का लॉजिक
        vision_points = [
            "Today's code is tomorrow's operating system.",
            "Wealth follows Skill. Focus on the Mastery.",
            "1000 Phases is just the beginning of the Protocol."
        ]
        
        for point in vision_points:
            print(f" >> [ANCHORING]: {point}")
            time.sleep(1.5)
            
        print(f"\n[JARVIS]: Vision locked. We are only 72 steps away from Greatness.")

if __name__ == "__main__":
    jarvis_ei = JarvisEmotionalIntelligence()
    jarvis_ei.analyze_user_sentiment("mehnat karne ke bad bhi bekari jaaye")
    jarvis_ei.anchor_long_term_vision()
